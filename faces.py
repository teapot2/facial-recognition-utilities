import os
import cv2
from deepface import DeepFace
import logging


def extract_faces_from_database(db_path):
    """
    Extract faces from images in a database and save them.

    Parameters:
    - db_path (str): Path to the database containing images.

    Returns:
    None
    """
    # Iterate through each file in the database path
    for filename in os.listdir(db_path):
        if filename.lower().endswith((".jpg", ".png")):
            img_path = os.path.join(db_path, filename)

            # Read the image using OpenCV
            frame = cv2.imread(img_path)

            logging.info(f"Processing image: {filename}")

            # Extract faces from the image using DeepFace
            face_objs = DeepFace.extract_faces(
                img_path=frame,
                target_size=(224, 224),
                detector_backend="opencv",
                enforce_detection=False,
            )

            # Check if any faces are detected in the image
            if not face_objs:
                logging.warning(f"No faces detected in {filename}")
                continue

            # Iterate through each detected face in the image
            for idx, obj in enumerate(face_objs):
                face = cv2.cvtColor(obj["face"], cv2.COLOR_BGR2RGB)

                logging.info(f"Detected face {idx + 1} in {filename}")

                # Construct the output path for the saved face
                output_path = f"data/db/{os.path.splitext(filename)[0]}_face_{idx}.jpg"

                # Save the face to the specified output path
                cv2.imwrite(output_path, face * 255)
                logging.info(f"Saved face to {output_path}")

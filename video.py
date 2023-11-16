import cv2
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import datetime
import time
import os
import logging


def capture_video_stream(url, output_folder="."):
    """
    Capture a video stream from the specified URL and save frames as images.

    Parameters:
    - url (str): The URL for the video stream.
    - output_folder (str): The folder where captured frames will be saved (default: current directory).

    Returns:
    None
    """
    try:
        # Camera Setup
        cap = cv2.VideoCapture(url)

        # Set frame width and height
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1080)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

        # Set bitrate
        cap.set(cv2.CAP_PROP_BITRATE, 4000)

        while True:
            ret, frame = cap.read()

            frame = cv2.resize(frame, (1080, 720))
            frame = cv2.flip(frame, 0)
            frame = cv2.flip(frame, 1)

            if not ret:
                logging.error("Failed to read frame.")
                break

            cv2.imshow("URL Stream", frame)

            timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")[:-3]

            filename = os.path.join(output_folder, f"frame_{timestamp}.jpg")

            time.sleep(0.01)

            cv2.imwrite(filename, frame)

            logging.info(f"Frame saved: {filename}")

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

    finally:
        cap.release()
        cv2.destroyAllWindows()

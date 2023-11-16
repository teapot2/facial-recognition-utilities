from PIL import Image
import os
import logging


def compress_images_in_directory(
    directory_path, compression_ratio=1, compression_quality=85, output_directory="."
):
    """
    Compress images in the specified directory.

    Parameters:
    - directory_path (str): The path to the directory containing images.
    - compression_ratio (float): The compression ratio for resizing images (default: 1).
    - compression_quality (int): The compression quality for saving images (default: 85).
    - output_directory (str): The directory to save the compressed images (default: current directory).

    Returns:
    None
    """
    try:
        image_count = len(os.listdir(directory_path))
        logging.info(f"Found {image_count} images in {directory_path}")

        for i, image_path in enumerate(os.listdir(directory_path)):
            logging.info(f"Processing image {i + 1} of {image_count}")
            compress_image(
                image_path, compression_ratio, compression_quality, directory_path
            )

    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")


def compress_image(
    image_path, compression_ratio=1, compression_quality=85, output_directory="."
):
    """
    Compress a single image.

    Parameters:
    - image_path (str): The path to the image file.
    - compression_ratio (float): The compression ratio for resizing the image (default: 1).
    - compression_quality (int): The compression quality for saving the image (default: 85).
    - output_directory (str): The directory to save the compressed image (default: current directory).

    Returns:
    None
    """
    try:
        image = Image.open(os.path.join(output_directory, image_path))

        logging.info(f"Compressing {image_path}")
        width, height = image.size
        new_size = (int(width * compression_ratio), int(height * compression_ratio))
        resized_image = image.resize(new_size, Image.Resampling.LANCZOS)

        # Construct the output path for the compressed image
        output_path = os.path.join(output_directory, f"compressed_{image_path}")

        resized_image.save(output_path, optimize=True, quality=compression_quality)
        logging.info(f"Compressed image saved to {output_path}")

    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

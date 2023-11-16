import requests
from bs4 import BeautifulSoup
import os
import logging
import time


def download_real_madrid_images(url, save_folder):
    """
    Download Real Madrid squad images from the specified URL and save them to the specified folder.

    Last working URL: https://www.realmadrid.com/en/football/squad

    Parameters:
    - url (str): The URL of the page containing the images.
    - save_folder (str): The folder where images will be saved.

    Returns:
    None
    """
    try:
        if not os.path.exists(save_folder):
            os.makedirs(save_folder)

        # Send a request to the URL and parse the HTML
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        image_divs = soup.find_all("img", class_="nfj-listado_position_imagen")

        for idx, img_div in enumerate(image_divs):
            img_url = img_div["src"]
            img_name = f"real_image_{idx}.jpg"
            img_data = requests.get(f"https://www.realmadrid.com{img_url}").content

            with open(os.path.join(save_folder, img_name), "wb") as handler:
                handler.write(img_data)

        logging.info("Images saved successfully.")

    except requests.RequestException as e:
        logging.error(f"An error occurred during the request: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")


def download_newcastle_images(url, save_folder):
    """
    Download Newcastle United first team images from the specified URL and save them to the specified folder.

    Last working URL: https://www.nufc.co.uk/teams/first-team/

    Parameters:
    - url (str): The URL of the page containing the images.
    - save_folder (str): The folder where images will be saved.

    Returns:
    None
    """
    try:
        if not os.path.exists(save_folder):
            os.makedirs(save_folder)

        # Send a request to the URL and parse the HTML
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        image_divs = soup.find_all("img", class_="image lazyload u-blur-up")

        for idx, img_div in enumerate(image_divs):
            img_url = img_div["src"]
            img_name = f"newcastle_image_{idx}.jpg"
            img_data = requests.get(img_url).content

            with open(os.path.join(save_folder, img_name), "wb") as handler:
                handler.write(img_data)

            time.sleep(0.5)  # Add a delay to avoid overloading the server

        logging.info("Images saved successfully.")

    except requests.RequestException as e:
        logging.error(f"An error occurred during the request: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

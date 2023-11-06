import os
import requests
from urllib.parse import urlparse
from dotenv import load_dotenv
load_dotenv()
import argparse


def shorten_link(token, url):
    header = {
        "Authorization": f"Bearer {token}",
    }

    body = {"long_url": url}

    url_to_shorten = "https://api-ssl.bitly.com/v4/bitlinks"

    response = requests.post(
        url_to_shorten,
        headers=header,
        json=body
    )
    response.raise_for_status()

    return response.json().get("link")


def count_clicks(token, url):

    url_attributes = urlparse(url)
    url = f"{url_attributes.netloc}{url_attributes.path}"

    header = {
        "Authorization": f"Bearer {token}",
    }

    body = {
        "units": "-1",
        "unit": "day",
    }

    clicks_url = f"https://api-ssl.bitly.com/v4/bitlinks/{url}/clicks/summary"

    response = requests.get(
        clicks_url,
        headers=header,
        params=body,
    )
    response.raise_for_status()

    total_clicks = response.json().get("total_clicks")
    return total_clicks


def is_bitlink(token, url):

    url_attributes = urlparse(url)
    url = f"{url_attributes.netloc}{url_attributes.path}"

    header = {
        "Authorization": f"Bearer {token}",
    }

    bitlink_checker_url = f"https://api-ssl.bitly.com/v4/bitlinks/{url}"

    response = requests.get(
        bitlink_checker_url,
        headers=header,
    )

    return response.ok


def main():
    bitly_token = os.environ['BITLY_TOKEN']

    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='URL input')
    args = parser.parse_args()

    url = args.url

    try:
        if is_bitlink(bitly_token, url):
            print(f"Number of clicks on link {url}:",
                  f"{count_clicks(bitly_token, url)}")
        else:

            bitlink = shorten_link(
                bitly_token,
                url,
            )
            print(f"Shortened link: {bitlink}")

    except (
        requests.exceptions.HTTPError,
        requests.exceptions.ConnectionError,
        requests.exceptions.MissingSchema,
    ):
        print(f"Error in URL: {url}")


if __name__ == "__main__":
    main()

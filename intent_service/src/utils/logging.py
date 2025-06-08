from config import config
import requests
import warnings


def log_info(info: dict) -> None:
   response = requests.post(config.logging.endpoint, json=info)
   if response.status_code != 200:
     warnings.warn(response.text)

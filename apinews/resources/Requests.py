from requests import request as req
from dotenv import find_dotenv, dotenv_values
from json import loads

environments = dotenv_values(dotenv_path=find_dotenv())


def request_apinews(query: str):
    params = {"q": query, "apiKey": environments["KEY_API_NEWS"]}
    response = req("GET", url=environments["APINEWS_URL"], params=params)
    return loads(response.text)
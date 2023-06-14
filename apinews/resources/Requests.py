from requests import request as req
from dotenv import find_dotenv, dotenv_values
from json import loads
import math

environments = dotenv_values(dotenv_path=find_dotenv())


def request_apinews(query: str, first_page_only=True, page=1):
    params = {"q": query, "page": f"{page}", "apiKey": environments["KEY_API_NEWS"]}
    response = req("GET", url=environments["APINEWS_URL"], params=params)
    data = loads(response.text)
    if first_page_only is False:
        return _many_pages(results=data["totalResults"], query=query)
    return loads(response.text)

def _many_pages(results: int, query: str):
    data_list = {"articles": []}
    pages = int(math.ceil(results/100))
    for page in range(1, pages+1):
        params = {"q": query, "page": f"{page}", "apiKey": environments["KEY_API_NEWS"]}
        response = req("GET", url=environments["APINEWS_URL"], params=params)
        data = loads(response.text)
        data_list["articles"].extend(data["articles"])
    return data_list

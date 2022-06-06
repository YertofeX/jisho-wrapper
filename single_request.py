import json
import requests

base_url = "https://jisho.org/api/v1/search/words?keyword="

jlpt_level = 5
page = 1
search_string = f"%23jlpt-n{jlpt_level}&page={page}"

data = requests.get(base_url + search_string).json()['data']

with open("single_data.json", "wb") as fp:
    fp.write(json.dumps(data, ensure_ascii=False).encode("utf8"))

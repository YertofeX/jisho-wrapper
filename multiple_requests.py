import json
import requests

base_url = "https://jisho.org/api/v1/search/words?keyword="

# jlpt level : page count
search_dict = {
    # 5: 33,
    # 4: 29,
    3: 89,
    2: 91,
    1: 172
}
for level in search_dict:
    jlpt_level = level
    page_count = search_dict[level]
    print(f"N{jlpt_level}")
    with open(f"words/n{jlpt_level}.json", "ab") as fp:
        for page in range(1, page_count + 1):
            print(f"\tPAGE {page}")
            search_string = f"%23jlpt-n{jlpt_level}&page={page}"
            data = requests.get(base_url + search_string).json()['data']
            fp.write(json.dumps(data, ensure_ascii=False).encode("utf8"))
        fp.close()

print("FINISHED")

import sys
import json
from urllib.request import urlopen
from urllib.error import HTTPError


def extract_from_content_data(content_data):
    result = []
    for item in content_data["data"]["children"]:
        question = item['data']['title'].replace("\n", "")
        answer = item["data"]["selftext"].replace("\n", "")
        joke = {"P": question, "R": answer}
        result.append(joke)
    return result


def save_to_json(jokes):
    with open("jokes.json", "w") as fp:
        json.dump(jokes, fp)


def main(args):
    url = args[1]
    try:
        content = urlopen(url).read()
    except HTTPError as e:
        raise e
    else:
        data = json.loads(content)
        jokes = extract_from_content_data(data)
        save_to_json(jokes)
        print("arquivo salvo")


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        main(sys.argv)
    elif len(sys.argv) == 1:
        print("deve informar a URL")
    else:
        print("erro inesperado")

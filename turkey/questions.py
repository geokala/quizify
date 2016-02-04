from bs4 import BeautifulSoup
import random
from urllib.request import urlopen

MAX_ID = 10000
QUESTIONS = 5
URL = r'http://www.quizballs.com/quizbynumberA.php?qid={id}'


def get_next_package():
    while True:
        while True:
            q_id = random.randint(1, MAX_ID)
            print(q_id)
            url = URL.format(id=q_id)
            html = urlopen(url).read()
            soup = BeautifulSoup(html)
            paragraphs = soup.find_all('p')
            if len(paragraphs) > 3 and paragraphs[2].text and paragraphs[3].text:
                break
        yield paragraphs[2].text, paragraphs[3].text


gen = get_next_package()


def get_package():
    package = [next(gen) for _ in range(QUESTIONS)]
    correct_id = random.randint(0, QUESTIONS - 1)
    return {
        'question': package[correct_id][0],
        'answers': [x[1] for x in package],
        'correct_answer': correct_id
    }


# Example usage
# print(get_package())

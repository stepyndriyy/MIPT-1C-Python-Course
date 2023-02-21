import contextlib

import requests as api
from bs4 import BeautifulSoup


def example():
    with api.get('https://journal.tinkoff.ru/p50-review/') as tj:
        tj.encoding = 'utf-8'
        content = BeautifulSoup(tj.text, 'lxml')
        print(content.find('h1', {'class': 'article-header__title'}).text)


@contextlib.contextmanager
def my_context_manager(name):
    print('Start context manager')
    yield f'Hello {name}!'
    print('Finish context manager')


def try_my():
    with my_context_manager('Big man') as hello:
        print(hello)

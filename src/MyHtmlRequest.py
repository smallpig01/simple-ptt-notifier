from urllib.request import Request, urlopen
from urllib.parse import quote
from bs4 import BeautifulSoup
import os


class MyHttpRequest:
    url: str
    headers: str = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36', 'cookie': 'over18=1;'}
    req: Request
    page: urlopen
    soup: BeautifulSoup

    def HttpRequest(self, url):
        self.url = quote(url, safe='/:?=')
        self.req = Request(self.url, headers=self.headers)
        self.page = urlopen(self.req)
        self.soup = BeautifulSoup(self.page, 'html.parser')

    def PrintSoup(self):
        print(self.soup)

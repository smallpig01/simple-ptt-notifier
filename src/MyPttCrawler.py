from MyHtmlRequest import *
import re


class PttItem:
    index: int
    title: str
    url: str


class MyPttCrawler:
    # url sample : https://www.ptt.cc/bbs/Gossiping/index.html
    url_root = "https://www.ptt.cc"
    url1 = "https://www.ptt.cc/bbs/"
    url2 = "/index.html"
    board_name = ""
    keyword = ""
    url: str
    latest_title_index: int = 0
    latest_title_url: str
    latest_title_text: str
    my_html_request: MyHttpRequest
    page_content_list = []
    new_content_list = []

    def CrawlPageAsList(self, board_name):
        page_content_list = []
        latest_index = 0

        # prepare data
        self.board_name = board_name
        self.url = self.url1 + self.board_name + self.url2
        # print(self.url)

        # request html
        self.my_html_request = MyHttpRequest()
        self.my_html_request.HttpRequest(self.url)
        # self.my_html_request.PrintSoup()

        # find 'r-ent' in all for capture tiles
        all_rents = self.my_html_request.soup.find_all('div', attrs="r-ent")

        #
        for rent in all_rents:
            title = rent.find('div', attrs="title").find('a')

            if(title == None):
                continue

            href = title.get('href')
            item = PttItem()
            item.index = int(href.split('M.')[1].split('.A')[0])
            item.title = title.contents[0]
            item.url = self.url_root + href

            if(item.index < latest_index):
                continue

            latest_index = item.index
            page_content_list.append(item)
            # print(item.index)
            # print(item.title)
            # print(item.url)

        return page_content_list

    def Crawl(self, board_name, keyword):
        self.new_content_list.clear()
        self.page_content_list.clear()
        self.page_content_list = self.CrawlPageAsList(board_name)

        x: PttItem
        for x in self.page_content_list:
            if(x.index <= self.latest_title_index):
                continue

            # print(x.index)
            # print(x.title)
            # print(x.url)

            self.latest_title_index = x.index

            if(x.title.find(keyword) != -1):
                self.new_content_list.append(x)

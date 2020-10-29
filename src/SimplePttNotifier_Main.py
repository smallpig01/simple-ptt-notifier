from MyTelepot import *
from MyHtmlRequest import *
from MyPttCrawler import *
import time

#prepare argument
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("bot_id", help="telegram bot id",type=str)
parser.add_argument("chat_id", help="telegram chat id",type=str)
parser.add_argument("board_name", help="ptt board name",type=str)
parser.add_argument("keyword", help="keyword", type=str)
parser.add_argument("--delay_s", help="delay time in secend", type=int)
args = parser.parse_args()

bot_token = args.bot_id
chat_id = args.chat_id
board_name = args.board_name
keyword = args.keyword
wait_time = 10
if(args.delay_s):
    wait_time = args.delay_s

mypot = MyTelepot(bot_token, chat_id)

my_ptt_crawler = MyPttCrawler()
my_ptt_crawler.Crawl(board_name, keyword)

latest_item: PttItem
num_items = len(my_ptt_crawler.new_content_list)
if(num_items > 0):
    latest_item = my_ptt_crawler.new_content_list[num_items-1]
    print("目前版面最新文章")
    print("index: " + str(latest_item.index))
    print("title: " + str(latest_item.title))
    print("url  : " + str(latest_item.url))
    print("")


# send bot start msg
msg = "bot啟動, 新文章偵測參數如下\n" + \
      "board_name:" + board_name + "\n" + \
      "keyword   :" + keyword + "\n"
print("bot發送開始訊息")
print(msg)
mypot.PotSendMsg(msg)

# scraw while loop
while(1):
    time.sleep(wait_time)
    my_ptt_crawler.Crawl(board_name, keyword)
    print("爬文中: " + time.ctime(time.time()))

    new_items: PttItem
    for new_items in my_ptt_crawler.new_content_list:
        msg = new_items.title + "\n" + \
            new_items.url
        print("***發現新文章, 發送bot訊息")
        print(msg)
        mypot.PotSendMsg(msg)
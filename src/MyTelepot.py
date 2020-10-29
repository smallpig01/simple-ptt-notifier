import telepot


class MyTelepot:
    pot: telepot
    bot_token: str
    chat_id: str

    def __init__(self, bot_token, chat_id):
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.pot = telepot.Bot(self.bot_token)

    def PotSendMsg(self, msg):
        self.pot.sendMessage(self.chat_id, msg)

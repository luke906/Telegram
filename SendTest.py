import os
import telegram

bot = telegram.Bot(token='453642591:AAFwBdO7CaZ4XpfYi1ud3b6nURjYisHgs-s')

updates = bot.getUpdates()  #업데이트 내역을 받아옵니다.

for u in updates:
    # 내역중 메세지를 출력합니다.
    print(u.message)

chat_id = bot.getUpdates()[-1].message.chat.id


bot.sendMessage(chat_id='468017156', text='News COMMING!!')


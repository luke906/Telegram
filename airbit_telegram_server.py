from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import os
import random

# 로그 처리
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

def help(bot, update):
    bot.sendMessage(update.message.chat_id, text='Help!')

def iam(bot, update):
    chat_id = update.message.chat_id
    msg = "my chat_id is %d" % (chat_id)
    bot.sendMessage(update.message.chat_id, text=msg)

def start(bot, update):
    chat_id = update.message.chat_id
    user = update.message.from_user
    msg = "안녕하세요, %s %s! 에어비트클럽 공지방에 오신걸 환영 합니다." %(user.first_name, user.last_name)
    bot.sendMessage(update.message.chat_id, text=msg)

def query(msg):
    return msg

def response(bot, update):
    chat_id = update.message.chat_id
    user = update.message.from_user
    user_name = "%s%s" %(user.first_name, user.last_name)

    r_msg = query(update.message.text)
    bot.sendMessage(chat_id, text=r_msg)
    bot.sendMessage(chat_id, text=user_name)

def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))

def main():

    # 봇에게 토큰 전달
    token = "453642591:AAFwBdO7CaZ4XpfYi1ud3b6nURjYisHgs-s"
    updater = Updater(token)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("iam", iam))

    dp.add_handler(MessageHandler([Filters.text], response))

    dp.add_error_handler(error)

    #  봇 시작
    updater.start_polling()

    # Ctrl-C 도는 프로세스가 SIGINT, SIGTERM, SIGABRT 수신 전까지 계속 작동
    updater.idle()


if __name__ == '__main__':
    main()






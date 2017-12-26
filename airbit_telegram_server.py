from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import telegram
import os
import random

# 봇이 응답할 명령어
CMD_START     = '/start'
CMD_STOP      = '/stop'
CMD_HELP      = '/help'
CMD_BROADCAST = '/broadcast'

# 커스텀 키보드
CUSTOM_KEYBOARD = [
        [CMD_START],
        [CMD_STOP],
        [CMD_HELP],
        ]

# 로그 처리
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

def help(bot, update):
    bot.sendMessage(update.message.chat_id, text='Help!')

def iam(bot, update):
    chat_id = update.message.chat_id
    msg = "my chat_id is %d" % (chat_id)
    bot.sendMessage(update.message.chat_id, text=msg)

def remove_custom_keyboard(bot, update):
    reply_markup = telegram.ReplyKeyboardRemove()
    bot.send_message(update.message.chat_id, text="I'm back.", reply_markup=reply_markup)

def start(bot, update):

    kb = [[telegram.KeyboardButton('전체 계좌 금액 합산')],
          [telegram.KeyboardButton('전체 계좌 이체 실행')],
          [telegram.KeyboardButton('command3')],
          [telegram.KeyboardButton('command4')],
          [telegram.KeyboardButton('command5')]]
    kb_markup = telegram.ReplyKeyboardMarkup(kb)

    user = update.message.from_user
    msg = "안녕하세요, %s %s! 에어비트클럽 공지방에 오신걸 환영 합니다." %(user.first_name, user.last_name)
    bot.sendMessage(update.message.chat_id, text=msg, reply_markup=kb_markup)


def query(msg):
    return msg

def response(bot, update):
    chat_id = update.message.chat_id
    user = update.message.from_user
    user_name = "%s%s" %(user.first_name, user.last_name)

    r_msg = query(update.message.text)
    bot.sendMessage(chat_id, text=r_msg)
    bot.sendMessage(chat_id, text=user_name)
    bot.sendMessage(chat_id, text=chat_id)

def error(update, error):
    logger.warning('Update "%s" caused error "%s"' % (update, error))

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






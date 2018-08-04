#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
# from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import logging
import tkn

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def start(bot, update):
    print(update.message.text)
    update.message.reply_text('Hi! ')

def new_member(bot, update):
    print(update.message.text)
    update.message.reply_sticker(sticker='CAADAgADaQADk5h-FwzA5kpuP7CvAg')


def help(bot, update):
    update.message.reply_text('Help! | ' + str(update.message.chat_id))


def mem(bot, update, args):
    print(update.message.text)
    if not args:
        bot.send_message(chat_id=update.message.chat_id,
                        text='Мемы:\n'
                        '/mem дуранчоусы  — <i>Вы шо дуранчоусы?</i>\n'
                        '/mem борис  — <i>Похотливый Борис</i>', parse_mode='HTML')
    for s in args:
        if s.lower() == 'дуранчоусы':
            bot.send_chat_action(chat_id=update.message.chat_id, action='record_video_note')
            bot.send_video_note(chat_id=update.message.chat_id, video_note='DQADAgADVQIAAnNbMUv23rJ7tb5U0QI')
            # bot.send_video_note(chat_id=update.message.chat_id, video_note=open('files/duranchousi.mp4', 'rb'), duration=1)
        elif s.lower() == 'борис':
            bot.send_chat_action(chat_id=update.message.chat_id, action='record_video_note')
            bot.send_video_note(chat_id=update.message.chat_id, video_note='DQADAgADWwIAAoCFUUqPv5dxuJnYcAI')


def mem_btn(bot, update):
    q = update.callback_query
    # bot.edit_message_text(text='Selected: {}'.format(q.data),
    #                       chat_id=q.message.chat_id,
    #                       message_id=q.message.message_id)
    if q.data == 'дуранчоусы':
        bot.send_chat_action(chat_id=q.message.chat_id, action='record_video_note')
        bot.delete_message(chat_id=q.message.chat_id, message_id=q.message.message_id)
        # bot.edit_message_text(text='/meme {}'.format(q.data),
        #                                             chat_id=q.message.chat_id,
        #                                             message_id=q.message.message_id)
        bot.send_video_note(chat_id=q.message.chat_id, video_note=open('files/duranchousi.mp4', 'rb'), \
                        length='352', duration=1)


def getchatid(bot, update):
    update.message.reply_text(str(update.message.chat_id))


def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    updater = Updater(tkn.BOT_TKN)
    dp = updater.dispatcher
    dp.add_handler(CallbackQueryHandler(mem_btn))
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("mem", mem, pass_args=True))
    # dp.add_handler(CommandHandler("getchatid", getchatid))
    dp.add_handler(CommandHandler("getchatid", getchatid, filters=Filters.user(user_id=144149077)))
    dp.add_handler(CommandHandler("help", help, filters=Filters.user(user_id=144149077) | \
                                                        Filters.user(user_id=4044957411)| \
                                                        Filters.chat(chat_id=-1001289154724)))

    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, new_member))
    # dp.add_handler(MessageHandler(Filters.chat(-144149077) & Filters.text, echo))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

# -*- coding: utf-8 -*-
#!/usr/local/bin/python
import json
import telebot
import requests
from datetime import datetime
from decouple import config

API_TOKEN = config('API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)

_logger = telebot.logger

@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, u"""\
Hi! I am the non-official Telegram bot for the Python Brasil '12
Write /help for more help
""")

@bot.message_handler(commands=['help'])
def send_help(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, u"""\
/start  Send welcome message
/help   Show this help message
/invite_link Displays invite link
/where  Show location
... (TODO)
Please contribute: https://github.com/citec/pybrtelegrambot
""")

@bot.message_handler(commands=['invite_link', 'link'])
def send_invite_link(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, u"""\
https://telegram.me/pythonbr
""")


@bot.message_handler(commands=['where'])
def send_where(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, u'The #pybr12 will take place in Florianópolis')

bot.polling()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

import random
import telebot

from telebot import types

bot = telebot.TeleBot("5291023081:AAHW6QkCRr9nsNDUkwflmRetKl_xEpk02ko")


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id,"Hello my friend!")


@bot.message_handler(commands=["planet"])
def planet(message):
    bot.send_photo(message.chat.id,"https://www.pnp.ru/upload/entities/2021/04/19/18/article/detailPicture/7e/66/9f/55/23c871532e2289d5791561c8adda1a1a.jpg")


@bot.message_handler(content_types=["text"])
def echo(message):
    bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True, interval=0)

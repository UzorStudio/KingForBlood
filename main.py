import telebot as telebot
from telebot import types
import base
import KIngdom
import random

bot = telebot.TeleBot('5006967059:AAElAfnRXBqTD_G_bFOrYEuM_506KJ0ULic')
bd = base.Base("localhost")

king = KIngdom.Kingdom()


@bot.message_handler(commands=['start'])
def start(message):
    if bd.getUsrById(message.chat.id) is None:
        bd.postUser(usrName=message.from_user.username,
                    usrId=message.chat.id,
                    KingdomName="",
                    kingdom=king.Generate_kingdom_location(),
                    gold=0)
        bot.send_message(message.chat.id, "Введи имя своего королевства")
        bot.register_next_step_handler(message, regKingdom)
    else:
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add(types.KeyboardButton(text="Управление королевством"))
        keyboard.add(types.KeyboardButton(text="Доклад о королевстве"))
        keyboard.add(types.KeyboardButton(text="Рынок"))
        keyboard.add(types.KeyboardButton(text="Купить участок"))
        keyboard.add(types.KeyboardButton(text="Купить крепостного"))
        bot.send_message(message.chat.id, "Да Да, Сэр", reply_markup=keyboard)


def regKingdom(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    keyboard.add(types.KeyboardButton(text="Управление королевством"))
    keyboard.add(types.KeyboardButton(text="Доклад о королевстве"))
    keyboard.add(types.KeyboardButton(text="Рынок"))
    keyboard.add(types.KeyboardButton(text="Купить участок"))
    keyboard.add(types.KeyboardButton(text="Купить крепостного"))

    text = """
        Приветсвую тебя, дорогой Друг, тебе надо купить землю для развития своего королевства, стоит оно 200trx"""

    bd.setNameOfKingdom(message.chat.id,message.text)
    bot.send_message(message.chat.id, text, reply_markup=keyboard)

@bot.message_handler(content_types="text")
def Menu(message):
    if message.text == "Доклад о королевстве":
        kingdom = bd.getUsrById(message.chat.id)
        terr = kingdom["kingdom"]
        text = "Название: "+kingdom["KingdomName"]+"\n"+\
               "Количество жителей: "+str(kingdom["liver"])+"\n"+\
               "Количесвто еды: "+str(kingdom["food"])+"\n"+\
               "Войнов: "+str(kingdom["warriors"])+"\n"+\
               "Рабочих: "+str(kingdom["workers"])+"\n"+\
               "Строители: "+str(kingdom["bilders"])+"\n"+\
               "Золото: "+str(kingdom["gold"])+"\n"+\
               "================================\n"+\
               "Леса: "+str(terr["forest"])+"\n"+\
               "Пустые равнины: "+str(terr["terra"])+"\n"+\
               "Дома: "+str(terr["home"])+"\n"+\
               "Скалы: "+str(terr["stoneBlock"])+"\n"+\
               "Железные руды: "+str(terr["ore"])+"\n"+\
               "Фермы: "+str(terr["ferm"])+"\n"+\
               "Рынок: "+str(terr["market"])+"\n"+\
               "Каменоломня: "+str(terr["stonequarry"])+"\n"+\
               "Рудовая шахта: "+str(terr["orequarry"])+"\n"+\
               "Лесоповалы: "+str(terr["woodcutter"])+"\n"+\
               "Кузни: "+str(terr["forge"])+"\n"
        bot.send_message(message.chat.id,text)


bot.polling(none_stop=True)

import telebot
from langdetect import detect
import random

uni_list = [u"\u2061", u"\u2062", u"\u2063", u"\u2064"]

bot = telebot.TeleBot("5844926586:AAFmCC21LaNpcMUB9Tg90V9v8w_AGyH5Uks")

id_sticker = "CAACAgIAAxkBAAEGlkVjhKdcurpQwMm9redbmkBGG1uUEwACKgwAArn2kUnBfIbAyJ91rCsE"

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    language_message = detect(message.text)
    print(language_message)
    s_2 = []
    s_3 = []
    s_4 = []
    if "/t" in message.text:
        if language_message == "ne":
            for i in message.text:
                if i == "ी" or i == "्" or i == "ो" or i == "ा" or i =="ि" or i =="े" or i == "़":
                    s_3.append(i)
                else:
                    s_3 += random.choice(uni_list)
                    s_3.append(i)
            del s_3[0:5]
            bot.send_message(message.chat.id, "".join(map(str, s_3)),
                             reply_to_message_id=message.message_id)
        elif language_message == "hi":
            for i in message.text:
                if i == "ी" or i == "्" or i == "ो" \
                        or i == "ा" or i == "ि" or i == "े" or i == "़" or i == "ै" or i == "ं":
                    s_4.append(i)
                else:
                    s_4 += random.choice(uni_list)
                    s_4.append(i)
            del s_4[0:5]
            bot.send_message(message.chat.id, "".join(map(str, s_4)),
                             reply_to_message_id=message.message_id)
            print(language_message)
        else:
            for i in message.text:
                s_2.append(i)
                s_2 += random.choice(uni_list)

        del s_2[0:4]
        bot.send_message(message.chat.id, "".join(map(str, s_2)),
                         reply_to_message_id=message.message_id)
    if message.text == '/hohol':
        bot.send_sticker(message.chat.id, id_sticker, reply_to_message_id=message.message_id)


if __name__ == '__main__':
    bot.infinity_polling()



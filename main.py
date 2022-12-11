import telebot

bot = telebot.TeleBot("5844926586:AAFmCC21LaNpcMUB9Tg90V9v8w_AGyH5Uks")

id_sticker = "CAACAgIAAxkBAAEGlkVjhKdcurpQwMm9redbmkBGG1uUEwACKgwAArn2kUnBfIbAyJ91rCsE"

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    s_2 = []
    if "/t" in message.text:
        for i in message.text:
            s_2.append(i)
            s_2 += u"\u2061"
            final_str = "".join(s_2)
        bot.send_message(message.chat.id, final_str.replace('t', '', 1).replace('/', '', 1),
                         reply_to_message_id=message.message_id)
    if message.text == '/hohol':
        bot.send_sticker(message.chat.id, id_sticker, reply_to_message_id=message.message_id)

if __name__ == '__main__':
    bot.infinity_polling()

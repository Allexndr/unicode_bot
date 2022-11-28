import telebot

import telebot

bot = telebot.TeleBot("5844926586:AAFmCC21LaNpcMUB9Tg90V9v8w_AGyH5Uks")


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    s_2 = []

    if "/t" in message.text:
        # message.text.translate({ord('/t'): None})
        for i in message.text:
            if i == '/':
                continue
            s_2.append(i)
            s_2[0] = "\u2061"
            s_2 += u"\u2061"
            # s_2[0] = ""
            print(s_2)
            # s_2[1] = ""
            final_str = "".join(s_2)

        # bot.send_message(message.chat.id, final_str.translate({ord('/'): None}),final_str.translate({ord('t'): None}), reply_to_message_id=message.message_id)
        # bot.send_message(message.chat.id, final_str.translate(str.maketrans('', '', chars)),reply_to_message_id=message.message_id)
        bot.send_message(message.chat.id, final_str, reply_to_message_id=message.message_id)
        # bot.send_message(message.chat.id, final_str_2.replace('/t',''),reply_to_message_id=message.message_id)

        # bot.send_message(message.chat.id, 'text')


if __name__ == '__main__':
    bot.infinity_polling()

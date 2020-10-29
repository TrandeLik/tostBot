import telebot
import numpy as np
from random import randint
import pickle


def getResult():
    with open('bag_of_words.pickle', 'rb') as f:
        bag_of_words = pickle.load(f)
    with open('words_dict.pickle', 'rb') as f:
        words_dict = pickle.load(f)

    stop_word = bag_of_words[len(bag_of_words) - 1]
    first_word = np.random.choice(bag_of_words)
    while first_word == stop_word:
        first_word = np.random.choice(bag_of_words)

    chain = [first_word]
    n_words = randint(10, 51)

    for i in range(n_words):
        if chain[-1] != stop_word:
            chain.append(np.random.choice(words_dict[chain[-1]]))
        else:
            break
    chain[0] = chain[0][0].upper() + chain[0][1::]

    return 'А сейчас будет унивирсальный тост для 4 часов ночи! \n\n' + ' '.join(chain) + '! Давайте выпьем!🥂'


bot = telebot.TeleBot("")
keyboard = telebot.types.ReplyKeyboardMarkup()
keyboard.row('🥂🥂🥂')


@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    bot.send_message(message.chat.id,
                     'А сейчас ты скажешь тост... Ой, не скажешь, ты же не знаешь, что говорить.... Ну, жми на кнопку, так уж и быть, помогу',
                     reply_markup=keyboard
    )


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    bot.send_message(message.from_user.id, getResult(), reply_markup=keyboard)


bot.polling(none_stop=True, interval=0)

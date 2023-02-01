# MS REAL CRUSADE 4 DON'T ASK ME WHY, WRITTEN BY BERSENRAR GITHUB PROFILE STOP READING THIS PLEAS... I'M VERY TURBIROVANIY
# Clear Ukrainian code| ruzzia is China colony red sun in the sun the best track ever
import time

import telebot
from telebot import types
import os
from dotenv import load_dotenv


load_dotenv(".env.template")

bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))


@bot.message_handler(commands=["start"])
def menu(message):
    '''
    Головне меню яке з'являється при запуску бота
    :param message: обьект класса message детальніше дивіться у документації pytelegrambotapi
    :return:
    '''

    # button_1 = types.KeyboardButton('Хто такі Chinese Tiger?')
    # button_2 = types.KeyboardButton('Все про замовлення')
    # button_3 = types.KeyboardButton('Телеграм канал з ідеями товарів')
    # button_4 = types.KeyboardButton('Наш сайт')
    # button_5 = types.KeyboardButton('Наші соц. мережі, де ви знайдете ще більше інформації')
    # button_6 = types.KeyboardButton('Написати менеджеру')
    buttons_list = [types.KeyboardButton('Хто такі Chinese Tiger?'), types.KeyboardButton('Все про замовлення'), types.KeyboardButton('Телеграм канал з ідеями товарів'),
                    types.KeyboardButton('Наш сайт'), types.KeyboardButton('Наші соц. мережі, де ви знайдете ще більше інформації'), types.KeyboardButton('Написати менеджеру')]
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # markup.add([[button_1, button_2, button_3], [button_4, button_5, button_6]])
    # markup.add(button_1)
    # markup.add(button_2)
    # markup.add(button_3)
    # markup.add(button_4)
    # markup.add(button_5)
    # markup.add(button_6)
    for button in buttons_list:
        markup.add(button)

    bot.send_message(

        chat_id=message.from_user.id,
        text=f'Доброго дня, {message.from_user.first_name}.'
             f'\nЩоб дізнатися більше про замовлення з Chinese Tiger, тисніть на потрібну кнопку👇🏻.',
        reply_markup=markup
    )


@bot.message_handler(
                        func=lambda message: message.text == 'Хто такі Chinese Tiger?'
                         or message.text == 'Все про замовлення'
                         or message.text == 'Телеграм канал з ідеями товарів'
                         or message.text == 'Наш сайт'
                         or message.text == 'Наші соц. мережі, де ви знайдете ще більше інформації'
                         or message.text == 'Написати менеджеру'
)
def message_dealer(call):
    '''
    Функція для обробки натискань на кнопки від користувача
    :param call: обьект message
    :return: None
    '''
    user_chat_id = call.from_user.id

    if call.text == "Хто такі Chinese Tiger?":
        info_message(user_chat_id)

    elif call.text == 'Все про замовлення':
        send_pdf_file(user_chat_id)
    elif call.text == "Телеграм канал з ідеями товарів":
        send_tg(user_chat_id)
    elif call.text == "Наш сайт":
        send_site(user_chat_id)
    elif call.text == "Наші соц. мережі, де ви знайдете ще більше інформації":
        send_social_network(user_chat_id)
    elif call.text == "Написати менеджеру":
        send_manager(user_chat_id)


def info_message(user_id):
    '''
    Надсилає інформаційне повідомлення користувачу
    :param user_id: id користувача за яким можно звернутись до нього
    :return:
    '''
    bot.send_message(chat_id=user_id, text='''▪️Компанія по замовленням з Китаю, де кожен з працівників знає китайську мову та має всі знання потрібні для встановлення бізнес відносин з китайською стороною.

▪️Ми замовляємо будь-які товари оптом. 

Також замовляємо на Амазон. 

Надаємо додаткові послуги: пошук постачальника і передача контактів клієнту, переклад з китайської, інспекція товару в Китаї, замовлення семплів.

▪️На зв‘язку 24/7. 

Завжди готові надати безкоштовну консультацію по замовленню товарів з Китаю🤝''')


def send_pdf_file(user_id):
    with open("check_list.pdf", "rb") as file:
        bot.send_document(chat_id=user_id, document=file)


def send_tg(user_id):
    '''
    Функція яка надсилає повідомлення з посиланням на телеграм канал
    :param user_id:
    :return:
    '''
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text="Канал", url="https://t.me/chinesespy")
    markup.add(button)
    bot.send_message(chat_id=user_id, text="Натискай для переходу у телеграм канал👇🏻", reply_markup=markup)


def send_site(user_id):
    '''
    Функція яка надсилає повідомлення з кнопкой з посиланнням на сайт
    :param user_id:
    :return:
    '''
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text="Сайт", url="https://chinesetiger.com.ua")
    markup.add(button)
    bot.send_message(chat_id=user_id, text="Натискай для переходу на сайт👇🏻", reply_markup=markup)


def send_social_network(user_id):
    '''
    Функція яка надсилає повідомлення з кнопками для переходу на соц.мережі
    :param user_id:
    :return:
    '''
    markup = types.InlineKeyboardMarkup()
    button_insta = types.InlineKeyboardButton(text="Instagram", url="https://instagram.com/chinese_tiger_?igshid=YmMyMTA2M2Y=")
    button_facebook = types.InlineKeyboardButton(text="Facebook", url="https://www.facebook.com/Chinese.tiger1/? ref=pages_you_manage")
    button_whats_up = types.InlineKeyboardButton(text="What’s app", url="https://wa.me/+380997024198")
    # markup.add(button_insta, button_facebook, button_whats_up)
    markup.add(button_insta)
    markup.add(button_facebook)
    markup.add(button_whats_up)
    bot.send_message(chat_id=user_id, text="Тут наші соц.мережі👇🏻", reply_markup=markup)


def send_manager(user_id):
    '''
    Функція яка надсилає контакт менеджера
    :param user_id:
    :return:
    '''
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text="Наш менеджер", url="https://t.me/vasiutayevheniia")
    markup.add(button)
    bot.send_message(chat_id=user_id, text="Натискай щоб зв'язатись з нами👇🏻", reply_markup=markup)


def non_stop():
    try:
        bot.polling(none_stop=True)
    except Exception as err:
        print(f'Something happened {err}')
        time.sleep(1)
        non_stop()


if __name__ == "__main__":

    non_stop()
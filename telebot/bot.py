import os
import telebot
from telebot import types

import config

bot = telebot.TeleBot(config.TOKEN)

products = [
    {
        "name": "Strawberry banana",
        "emoji": "🍓🍌",
        "price": 1500,
        "photo": "Strawberry_banana.webp",
        "nicotine": 5,
        "quantity": 1
    },
    {
        "name": "Spearmint",
        "emoji": "🍃",
        "price": 1500,
        "photo": "Spearmint.webp",
        "nicotine": 5,
        "quantity": 1
    },
    {
        "name": "Neon rain",
        "emoji": "🍬",
        "price": 1500,
        "photo": "neon_rain.webp",
        "nicotine": 5,
        "quantity": 1
    },
    {
        "name": "Coconut melon",
        "emoji": "🥥🍈",
        "price": 1500,
        "photo": "Coconut_melon.webp",
        "nicotine": 5,
        "quantity": 1
    },
    {
        "name": "Mangо",
        "emoji": "🥭",
        "photo": "mango.webp",
        "price": 1500,
        "nicotine": 5,
        "quantity": 1
    },
    {
        "name": "Blue razz lemonade",
        "emoji": "🥤",
        "photo": "blue_razz.webp",
        "price": 1500,
        "nicotine": 5,
        "quantity": 1
    },
    {
        "name": "Pink lemonade",
        "emoji": "🥤",
        "photo": "pink_lemonade.webp",
        "price": 1500,
        "nicotine": 5,
        "quantity": 1
    },
    {
        "name": "Watermelon",
        "emoji": "🍉",
        "photo": "watermelon.webp",
        "price": 1500,
        "nicotine": 5,
        "quantity": 1
    },
    {
        "name": "Blueberry",
        "emoji": "🫐",
        "photo": "blueberry.webp",
        "price": 1500,
        "nicotine": 5,
        "quantity": 1
    },
    {
        "name": "Banana milk",
        "emoji": "🍌🍼",
        "photo": "Banana_milk.webp",
        "price": 1500,
        "nicotine": 5,
        "quantity": 1
    },
    {
        "name": "Cola",
        "emoji": "🥤",
        "photo": "cola.webp",
        "price": 1500,
        "nicotine": 5,
        "quantity": 1
    },
    {
        "name": "Pineapple peach mango",
        "emoji": "🍍🥭🍑",
        "photo": "pineapple_peach_mango.webp",
        "price": 1500,
        "nicotine": 5,
        "quantity": 1
    },
    {
        "name": "Kiwi passion fruit guava",
        "emoji": "🥝",
        "photo": "Kiwi_passion_fruit_guava.webp",
        "price": 1500,
        "nicotine": 5,
        "quantity": 1
    },
]


def get_menu_markup():
    # Ответ на Просмотреть товар кнопками
    markup = types.InlineKeyboardMarkup(row_width=1)

    for index, product in enumerate(products):
        product_name = f"{product['emoji']}{product['price']}|{product['name']}"
        button = types.InlineKeyboardButton(product_name, callback_data=f"product_{index}")
        markup.add(button)

    return markup


def edit_message(call, text, markup):
    if text:
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=text,
                              parse_mode='html')
    if markup:
        bot.edit_message_reply_markup(call.from_user.id, call.message.message_id, reply_markup=markup)
    pass


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(
        types.KeyboardButton("🔮Просмотреть товар"),
        types.KeyboardButton("💎Купить ELF BAR"),
        types.KeyboardButton("💸Цена и описание"),
        types.KeyboardButton("🎁Скидочная система"),
        types.KeyboardButton("🔍Наш канал"),
        types.KeyboardButton("🔋Вкусы недели"))
    bot.send_message(message.chat.id,
                     "👋Здравствуйте, {0.first_name}!\nЯ - официальный бот канала <b>ELf Bar | Prague💫</b>\n\nЧем могу "
                     "Вам помочь?".format(
                         message.from_user, bot.get_me()
                     ),
                     parse_mode='html', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    print(call)

    if call.data == 'buy_product':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton(text='👨Александр', url='https://t.me/alxnlvk', callback_data='left'),
                   types.InlineKeyboardButton(text="👨Егор", url="https://t.me/egornegativ", callback_data='right'))
        edit_message(call=call, text="<b>Выберете человека у которого будете заказывать товар:</b>", markup=markup)

    elif 'product' in call.data:
        product_index = call.data.split('_')[1]

        product = products[int(product_index)]

        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(types.InlineKeyboardButton('Выбрать', callback_data="buy_product"),
                   types.InlineKeyboardButton("Назад", callback_data='main_menu'))

        directory = os.path.abspath(os.getcwd())
        image_path = os.path.join(directory, 'static', product['photo'])

        sticker = open(image_path, 'rb')

        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_sticker(call.message.chat.id, sticker)
        bot.send_message(call.message.chat.id,
                         f"Ваш выбор: <b>{product['emoji']}{product['price']}|{product['name']}.</b>\nКоличество "
                         f"никотина:<b> {product['nicotine']}% </b>",
                         parse_mode='html', reply_markup=markup)

    elif call.data == "main_menu":
        menu_markup = get_menu_markup()
        edit_message(call=call, text="<b>Список доступных товаров:</b>", markup=menu_markup)

    elif call.data == "back_2":
        bot.delete_message(call.message.chat.id, call.message.id)

    elif call.data == "description":
        bot.delete_message(call.message.chat.id, call.message.id)
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton("➡Назад", callback_data='back_2'))
        bot.send_message(call.message.chat.id,
                         '⚠️<b>Скидки в нашей группе распространяются только тогда, когды Вы на нее подписаны.</b>\n\n '
                         '🔹Если я приглашу 10 человек в группу, это значит что я получу 100% скидки?\n- Нет, '
                         'скидка будет засчитана как за 1 приглашенного человека на весь заказ.\n\n🔹<b>Можно ли '
                         'получить '
                         'скидку на следующий заказ, если я опять приглашу человека?</b>\n -Да, можно✅\n\n'
                         '🔹<b>Если я напишу 10 коментариев, я получу 50% скидки?</b>\n - Нет, одного коментария будет '
                         'вполне достаточно☺.\n\n<b>С уважением ELF BAR PRAGUE💫</b>',
                         parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def quest_1(message):
    if message.chat.type == 'private':
        # Просмотреть товар кнопка
        if message.text == '🔮Просмотреть товар':
            menu_markup = get_menu_markup()

            # Ответ на Просмотреть товар в строчке
            bot.send_message(message.chat.id, "<b>Список доступных товаров:</b>", parse_mode='html',
                             reply_markup=menu_markup)

        elif message.text == "💎Купить ELF BAR":

            markup = types.InlineKeyboardMarkup(row_width=1)
            people_sasha = types.InlineKeyboardButton(text='👨Александр', url='https://t.me/alxnlvk',
                                                      callback_data='left')
            people_danya = types.InlineKeyboardButton(text="👨Егор", url="https://t.me/egornegativ",
                                                      callback_data='right')
            markup.add(people_sasha, people_danya)
            bot.send_message(message.chat.id,
                             "👤Выберете человека, который поможет Вам оформить заказ.",
                             parse_mode='html', reply_markup=markup)

        elif message.text == '💸Цена и описание':
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(types.InlineKeyboardButton("➡Назад", callback_data='back_2'))
            bot.send_message(message.chat.id,
                             '💎Цена на весь предоставленый нами продукт составляет <b>300 CZK</b> вне акций. На '
                             'данный момент вся продукция исключительно на <b>1500 тяг и 5% никотина.</b>\n\nВ случае '
                             'заводского брака, купленый Вами продукт полностью возмещается деньгами потраченными на '
                             'покупку либо же заменной на иной <b>(выбор зависит исключительно от Вас)</b>.\n\n<b>С '
                             'уважением ELF BAR PRAGUE💫</b>',
                             parse_mode='html', reply_markup=markup)

        elif message.text == '🎁Скидочная система':
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(types.InlineKeyboardButton("🔎Подробнее...", callback_data='description'))
            bot.send_message(message.chat.id,
                             '<b>В нашей группе действует система скидок💸</b>\n🧐Что нужно сделать, чтобы получить '
                             'скидку?\n\n◦ Привести друга и получить <b>10% скидки (просто пригласить в '
                             'группу)✉</b>\n◦ Написать объективный  комментарий и получить <b>5% скидки📝</b>\n◦ '
                             'Покупаешь от 3 и более единиц товара — ещё <b>5% скидки  на каждый из '
                             'них📦</b>\n❗Акция «ВКУСЫ НЕДЕЛИ»\n<ins>(на них скидочная система не '
                             'распространяется).</ins>\n\n<b>С уважением ELF BAR PRAGUE💫</b>',
                             parse_mode='html', reply_markup=markup)

        elif message.text == '🔋Вкусы недели':
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(types.InlineKeyboardButton('➡Назад', callback_data='back_2'))
            bot.send_message(message.chat.id, '<b>Вкусы недели🌟</b>\nС 28.10 по 04.11🗓.\n\n◦Pink '
                                              'lemonade🥤\n◦Strawberry banana🍓🍌 '
                                              '\n◦Spearmint🍃\nНа данные продукты действует\n скидка: вместо '
                                              '<b>300 CZK — 250 CZK🏷</b>\n\n<b>С уважением ELF BAR PRAGUE💫</b>',
                             parse_mode='html', reply_markup=markup)

        elif message.text == '🔍Наш канал':
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(types.InlineKeyboardButton('➡Назад', callback_data='back_2'))
            bot.send_message(message.chat.id,
                             "<a href='https://t.me/praguelfbar'>Elfbar | Prague</a>, онлайн магазин по продаже "
                             "электронных сигарет продукции Elf Bar и мы готовы предоставить вам:\n\n• качественный, "
                             "гарантировано оригинальный товар💎\n• Разнообразный выбор вкусов продукции💫\n• "
                             "Активная служба поддержки👥\n• Самая быстрая доставка по Праге📦📌\n\nБолее детальная "
                             "информация в нашем телеграм канале.",
                             parse_mode='html', reply_markup=markup)
        else:
            bot.send_message(message.chat.id,
                             'Я не знаю как ответить на данный запрос 😔\n\n<b>Воспользуйтесь кнопками которые '
                             'находятся ниже.</b>\n\n• Если бот завис либо же не отвечает на запросы - напишите '
                             'команду: <b>/start</b>.\n\n\n⚠Если бот вовсе никак не реагирует на Ваши запросы, '
                             'пожалуйста, напишите в службу поддержки. Она в кротчайшие сроки свяжется с Вами.',
                             parse_mode='html')


bot.polling(none_stop=True)

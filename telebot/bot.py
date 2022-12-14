import os
import telebot
from telebot import types

import config

bot = telebot.TeleBot(config.TOKEN)

products = [
    {
        "name": "Strawberry banana",
        "emoji": "ππ",
        "price": 1500,
        "photo": "Strawberry_banana.webp",
        "nicotine": 5,
        "quantity": 1
    },
    {
        "name": "Spearmint",
        "emoji": "π",
        "price": 1500,
        "photo": "Spearmint.webp",
        "nicotine": 5,
        "quantity": 1
    },
    {
        "name": "Neon rain",
        "emoji": "π¬",
        "price": 1500,
        "photo": "neon_rain.webp",
        "nicotine": 5,
        "quantity": 1
    },
    {
        "name": "Coconut melon",
        "emoji": "π₯₯π",
        "price": 1500,
        "photo": "Coconut_melon.webp",
        "nicotine": 5,
        "quantity": 1
    },
    {
        "name": "MangΠΎ",
        "emoji": "π₯­",
        "photo": "mango.webp",
        "price": 1500,
        "nicotine": 5,
        "quantity": 1
    },
    {
        "name": "Blue razz lemonade",
        "emoji": "π₯€",
        "photo": "blue_razz.webp",
        "price": 1500,
        "nicotine": 5,
        "quantity": 1
    },
    {
        "name": "Pink lemonade",
        "emoji": "π₯€",
        "photo": "pink_lemonade.webp",
        "price": 1500,
        "nicotine": 5,
        "quantity": 1
    },
    {
        "name": "Watermelon",
        "emoji": "π",
        "photo": "watermelon.webp",
        "price": 1500,
        "nicotine": 5,
        "quantity": 1
    },
    {
        "name": "Blueberry",
        "emoji": "π«",
        "photo": "blueberry.webp",
        "price": 1500,
        "nicotine": 5,
        "quantity": 1
    },
    {
        "name": "Banana milk",
        "emoji": "ππΌ",
        "photo": "Banana_milk.webp",
        "price": 1500,
        "nicotine": 5,
        "quantity": 1
    },
    {
        "name": "Cola",
        "emoji": "π₯€",
        "photo": "cola.webp",
        "price": 1500,
        "nicotine": 5,
        "quantity": 1
    },
    {
        "name": "Pineapple peach mango",
        "emoji": "ππ₯­π",
        "photo": "pineapple_peach_mango.webp",
        "price": 1500,
        "nicotine": 5,
        "quantity": 1
    },
    {
        "name": "Kiwi passion fruit guava",
        "emoji": "π₯",
        "photo": "Kiwi_passion_fruit_guava.webp",
        "price": 1500,
        "nicotine": 5,
        "quantity": 1
    },
]


def get_menu_markup():
    # ΠΡΠ²Π΅Ρ Π½Π° ΠΡΠΎΡΠΌΠΎΡΡΠ΅ΡΡ ΡΠΎΠ²Π°Ρ ΠΊΠ½ΠΎΠΏΠΊΠ°ΠΌΠΈ
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
        types.KeyboardButton("π?ΠΡΠΎΡΠΌΠΎΡΡΠ΅ΡΡ ΡΠΎΠ²Π°Ρ"),
        types.KeyboardButton("πΠΡΠΏΠΈΡΡ ELF BAR"),
        types.KeyboardButton("πΈΠ¦Π΅Π½Π° ΠΈ ΠΎΠΏΠΈΡΠ°Π½ΠΈΠ΅"),
        types.KeyboardButton("πΠ‘ΠΊΠΈΠ΄ΠΎΡΠ½Π°Ρ ΡΠΈΡΡΠ΅ΠΌΠ°"),
        types.KeyboardButton("πΠΠ°Ρ ΠΊΠ°Π½Π°Π»"),
        types.KeyboardButton("πΠΠΊΡΡΡ Π½Π΅Π΄Π΅Π»ΠΈ"))
    bot.send_message(message.chat.id,
                     "πΠΠ΄ΡΠ°Π²ΡΡΠ²ΡΠΉΡΠ΅, {0.first_name}!\nΠ― - ΠΎΡΠΈΡΠΈΠ°Π»ΡΠ½ΡΠΉ Π±ΠΎΡ ΠΊΠ°Π½Π°Π»Π° <b>ELf Bar | Pragueπ«</b>\n\nΠ§Π΅ΠΌ ΠΌΠΎΠ³Ρ "
                     "ΠΠ°ΠΌ ΠΏΠΎΠΌΠΎΡΡ?".format(
                         message.from_user, bot.get_me()
                     ),
                     parse_mode='html', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    print(call)

    if call.data == 'buy_product':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton(text='π¨ΠΠ»Π΅ΠΊΡΠ°Π½Π΄Ρ', url='https://t.me/alxnlvk', callback_data='left'),
                   types.InlineKeyboardButton(text="π¨ΠΠ³ΠΎΡ", url="https://t.me/egornegativ", callback_data='right'))
        edit_message(call=call, text="<b>ΠΡΠ±Π΅ΡΠ΅ΡΠ΅ ΡΠ΅Π»ΠΎΠ²Π΅ΠΊΠ° Ρ ΠΊΠΎΡΠΎΡΠΎΠ³ΠΎ Π±ΡΠ΄Π΅ΡΠ΅ Π·Π°ΠΊΠ°Π·ΡΠ²Π°ΡΡ ΡΠΎΠ²Π°Ρ:</b>", markup=markup)

    elif 'product' in call.data:
        product_index = call.data.split('_')[1]

        product = products[int(product_index)]

        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(types.InlineKeyboardButton('ΠΡΠ±ΡΠ°ΡΡ', callback_data="buy_product"),
                   types.InlineKeyboardButton("ΠΠ°Π·Π°Π΄", callback_data='main_menu'))

        directory = os.path.abspath(os.getcwd())
        image_path = os.path.join(directory, 'static', product['photo'])

        sticker = open(image_path, 'rb')

        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_sticker(call.message.chat.id, sticker)
        bot.send_message(call.message.chat.id,
                         f"ΠΠ°Ρ Π²ΡΠ±ΠΎΡ: <b>{product['emoji']}{product['price']}|{product['name']}.</b>\nΠΠΎΠ»ΠΈΡΠ΅ΡΡΠ²ΠΎ "
                         f"Π½ΠΈΠΊΠΎΡΠΈΠ½Π°:<b> {product['nicotine']}% </b>",
                         parse_mode='html', reply_markup=markup)

    elif call.data == "main_menu":
        menu_markup = get_menu_markup()
        edit_message(call=call, text="<b>Π‘ΠΏΠΈΡΠΎΠΊ Π΄ΠΎΡΡΡΠΏΠ½ΡΡ ΡΠΎΠ²Π°ΡΠΎΠ²:</b>", markup=menu_markup)

    elif call.data == "back_2":
        bot.delete_message(call.message.chat.id, call.message.id)

    elif call.data == "description":
        bot.delete_message(call.message.chat.id, call.message.id)
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton("β‘ΠΠ°Π·Π°Π΄", callback_data='back_2'))
        bot.send_message(call.message.chat.id,
                         'β οΈ<b>Π‘ΠΊΠΈΠ΄ΠΊΠΈ Π² Π½Π°ΡΠ΅ΠΉ Π³ΡΡΠΏΠΏΠ΅ ΡΠ°ΡΠΏΡΠΎΡΡΡΠ°Π½ΡΡΡΡΡ ΡΠΎΠ»ΡΠΊΠΎ ΡΠΎΠ³Π΄Π°, ΠΊΠΎΠ³Π΄Ρ ΠΡ Π½Π° Π½Π΅Π΅ ΠΏΠΎΠ΄ΠΏΠΈΡΠ°Π½Ρ.</b>\n\n '
                         'πΉΠΡΠ»ΠΈ Ρ ΠΏΡΠΈΠ³Π»Π°ΡΡ 10 ΡΠ΅Π»ΠΎΠ²Π΅ΠΊ Π² Π³ΡΡΠΏΠΏΡ, ΡΡΠΎ Π·Π½Π°ΡΠΈΡ ΡΡΠΎ Ρ ΠΏΠΎΠ»ΡΡΡ 100% ΡΠΊΠΈΠ΄ΠΊΠΈ?\n- ΠΠ΅Ρ, '
                         'ΡΠΊΠΈΠ΄ΠΊΠ° Π±ΡΠ΄Π΅Ρ Π·Π°ΡΡΠΈΡΠ°Π½Π° ΠΊΠ°ΠΊ Π·Π° 1 ΠΏΡΠΈΠ³Π»Π°ΡΠ΅Π½Π½ΠΎΠ³ΠΎ ΡΠ΅Π»ΠΎΠ²Π΅ΠΊΠ° Π½Π° Π²Π΅ΡΡ Π·Π°ΠΊΠ°Π·.\n\nπΉ<b>ΠΠΎΠΆΠ½ΠΎ Π»ΠΈ '
                         'ΠΏΠΎΠ»ΡΡΠΈΡΡ '
                         'ΡΠΊΠΈΠ΄ΠΊΡ Π½Π° ΡΠ»Π΅Π΄ΡΡΡΠΈΠΉ Π·Π°ΠΊΠ°Π·, Π΅ΡΠ»ΠΈ Ρ ΠΎΠΏΡΡΡ ΠΏΡΠΈΠ³Π»Π°ΡΡ ΡΠ΅Π»ΠΎΠ²Π΅ΠΊΠ°?</b>\n -ΠΠ°, ΠΌΠΎΠΆΠ½ΠΎβ\n\n'
                         'πΉ<b>ΠΡΠ»ΠΈ Ρ Π½Π°ΠΏΠΈΡΡ 10 ΠΊΠΎΠΌΠ΅Π½ΡΠ°ΡΠΈΠ΅Π², Ρ ΠΏΠΎΠ»ΡΡΡ 50% ΡΠΊΠΈΠ΄ΠΊΠΈ?</b>\n - ΠΠ΅Ρ, ΠΎΠ΄Π½ΠΎΠ³ΠΎ ΠΊΠΎΠΌΠ΅Π½ΡΠ°ΡΠΈΡ Π±ΡΠ΄Π΅Ρ '
                         'Π²ΠΏΠΎΠ»Π½Π΅ Π΄ΠΎΡΡΠ°ΡΠΎΡΠ½ΠΎβΊ.\n\n<b>Π‘ ΡΠ²Π°ΠΆΠ΅Π½ΠΈΠ΅ΠΌ ELF BAR PRAGUEπ«</b>',
                         parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def quest_1(message):
    if message.chat.type == 'private':
        # ΠΡΠΎΡΠΌΠΎΡΡΠ΅ΡΡ ΡΠΎΠ²Π°Ρ ΠΊΠ½ΠΎΠΏΠΊΠ°
        if message.text == 'π?ΠΡΠΎΡΠΌΠΎΡΡΠ΅ΡΡ ΡΠΎΠ²Π°Ρ':
            menu_markup = get_menu_markup()

            # ΠΡΠ²Π΅Ρ Π½Π° ΠΡΠΎΡΠΌΠΎΡΡΠ΅ΡΡ ΡΠΎΠ²Π°Ρ Π² ΡΡΡΠΎΡΠΊΠ΅
            bot.send_message(message.chat.id, "<b>Π‘ΠΏΠΈΡΠΎΠΊ Π΄ΠΎΡΡΡΠΏΠ½ΡΡ ΡΠΎΠ²Π°ΡΠΎΠ²:</b>", parse_mode='html',
                             reply_markup=menu_markup)

        elif message.text == "πΠΡΠΏΠΈΡΡ ELF BAR":

            markup = types.InlineKeyboardMarkup(row_width=1)
            people_sasha = types.InlineKeyboardButton(text='π¨ΠΠ»Π΅ΠΊΡΠ°Π½Π΄Ρ', url='https://t.me/alxnlvk',
                                                      callback_data='left')
            people_danya = types.InlineKeyboardButton(text="π¨ΠΠ³ΠΎΡ", url="https://t.me/egornegativ",
                                                      callback_data='right')
            markup.add(people_sasha, people_danya)
            bot.send_message(message.chat.id,
                             "π€ΠΡΠ±Π΅ΡΠ΅ΡΠ΅ ΡΠ΅Π»ΠΎΠ²Π΅ΠΊΠ°, ΠΊΠΎΡΠΎΡΡΠΉ ΠΏΠΎΠΌΠΎΠΆΠ΅Ρ ΠΠ°ΠΌ ΠΎΡΠΎΡΠΌΠΈΡΡ Π·Π°ΠΊΠ°Π·.",
                             parse_mode='html', reply_markup=markup)

        elif message.text == 'πΈΠ¦Π΅Π½Π° ΠΈ ΠΎΠΏΠΈΡΠ°Π½ΠΈΠ΅':
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(types.InlineKeyboardButton("β‘ΠΠ°Π·Π°Π΄", callback_data='back_2'))
            bot.send_message(message.chat.id,
                             'πΠ¦Π΅Π½Π° Π½Π° Π²Π΅ΡΡ ΠΏΡΠ΅Π΄ΠΎΡΡΠ°Π²Π»Π΅Π½ΡΠΉ Π½Π°ΠΌΠΈ ΠΏΡΠΎΠ΄ΡΠΊΡ ΡΠΎΡΡΠ°Π²Π»ΡΠ΅Ρ <b>300 CZK</b> Π²Π½Π΅ Π°ΠΊΡΠΈΠΉ. ΠΠ° '
                             'Π΄Π°Π½Π½ΡΠΉ ΠΌΠΎΠΌΠ΅Π½Ρ Π²ΡΡ ΠΏΡΠΎΠ΄ΡΠΊΡΠΈΡ ΠΈΡΠΊΠ»ΡΡΠΈΡΠ΅Π»ΡΠ½ΠΎ Π½Π° <b>1500 ΡΡΠ³ ΠΈ 5% Π½ΠΈΠΊΠΎΡΠΈΠ½Π°.</b>\n\nΠ ΡΠ»ΡΡΠ°Π΅ '
                             'Π·Π°Π²ΠΎΠ΄ΡΠΊΠΎΠ³ΠΎ Π±ΡΠ°ΠΊΠ°, ΠΊΡΠΏΠ»Π΅Π½ΡΠΉ ΠΠ°ΠΌΠΈ ΠΏΡΠΎΠ΄ΡΠΊΡ ΠΏΠΎΠ»Π½ΠΎΡΡΡΡ Π²ΠΎΠ·ΠΌΠ΅ΡΠ°Π΅ΡΡΡ Π΄Π΅Π½ΡΠ³Π°ΠΌΠΈ ΠΏΠΎΡΡΠ°ΡΠ΅Π½Π½ΡΠΌΠΈ Π½Π° '
                             'ΠΏΠΎΠΊΡΠΏΠΊΡ Π»ΠΈΠ±ΠΎ ΠΆΠ΅ Π·Π°ΠΌΠ΅Π½Π½ΠΎΠΉ Π½Π° ΠΈΠ½ΠΎΠΉ <b>(Π²ΡΠ±ΠΎΡ Π·Π°Π²ΠΈΡΠΈΡ ΠΈΡΠΊΠ»ΡΡΠΈΡΠ΅Π»ΡΠ½ΠΎ ΠΎΡ ΠΠ°Ρ)</b>.\n\n<b>Π‘ '
                             'ΡΠ²Π°ΠΆΠ΅Π½ΠΈΠ΅ΠΌ ELF BAR PRAGUEπ«</b>',
                             parse_mode='html', reply_markup=markup)

        elif message.text == 'πΠ‘ΠΊΠΈΠ΄ΠΎΡΠ½Π°Ρ ΡΠΈΡΡΠ΅ΠΌΠ°':
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(types.InlineKeyboardButton("πΠΠΎΠ΄ΡΠΎΠ±Π½Π΅Π΅...", callback_data='description'))
            bot.send_message(message.chat.id,
                             '<b>Π Π½Π°ΡΠ΅ΠΉ Π³ΡΡΠΏΠΏΠ΅ Π΄Π΅ΠΉΡΡΠ²ΡΠ΅Ρ ΡΠΈΡΡΠ΅ΠΌΠ° ΡΠΊΠΈΠ΄ΠΎΠΊπΈ</b>\nπ§Π§ΡΠΎ Π½ΡΠΆΠ½ΠΎ ΡΠ΄Π΅Π»Π°ΡΡ, ΡΡΠΎΠ±Ρ ΠΏΠΎΠ»ΡΡΠΈΡΡ '
                             'ΡΠΊΠΈΠ΄ΠΊΡ?\n\nβ¦ ΠΡΠΈΠ²Π΅ΡΡΠΈ Π΄ΡΡΠ³Π° ΠΈ ΠΏΠΎΠ»ΡΡΠΈΡΡ <b>10% ΡΠΊΠΈΠ΄ΠΊΠΈ (ΠΏΡΠΎΡΡΠΎ ΠΏΡΠΈΠ³Π»Π°ΡΠΈΡΡ Π² '
                             'Π³ΡΡΠΏΠΏΡ)β</b>\nβ¦ ΠΠ°ΠΏΠΈΡΠ°ΡΡ ΠΎΠ±ΡΠ΅ΠΊΡΠΈΠ²Π½ΡΠΉ  ΠΊΠΎΠΌΠΌΠ΅Π½ΡΠ°ΡΠΈΠΉ ΠΈ ΠΏΠΎΠ»ΡΡΠΈΡΡ <b>5% ΡΠΊΠΈΠ΄ΠΊΠΈπ</b>\nβ¦ '
                             'ΠΠΎΠΊΡΠΏΠ°Π΅ΡΡ ΠΎΡ 3 ΠΈ Π±ΠΎΠ»Π΅Π΅ Π΅Π΄ΠΈΠ½ΠΈΡ ΡΠΎΠ²Π°ΡΠ° β Π΅ΡΡ <b>5% ΡΠΊΠΈΠ΄ΠΊΠΈ  Π½Π° ΠΊΠ°ΠΆΠ΄ΡΠΉ ΠΈΠ· '
                             'Π½ΠΈΡπ¦</b>\nβΠΠΊΡΠΈΡ Β«ΠΠΠ£Π‘Π« ΠΠΠΠΠΠΒ»\n<ins>(Π½Π° Π½ΠΈΡ ΡΠΊΠΈΠ΄ΠΎΡΠ½Π°Ρ ΡΠΈΡΡΠ΅ΠΌΠ° Π½Π΅ '
                             'ΡΠ°ΡΠΏΡΠΎΡΡΡΠ°Π½ΡΠ΅ΡΡΡ).</ins>\n\n<b>Π‘ ΡΠ²Π°ΠΆΠ΅Π½ΠΈΠ΅ΠΌ ELF BAR PRAGUEπ«</b>',
                             parse_mode='html', reply_markup=markup)

        elif message.text == 'πΠΠΊΡΡΡ Π½Π΅Π΄Π΅Π»ΠΈ':
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(types.InlineKeyboardButton('β‘ΠΠ°Π·Π°Π΄', callback_data='back_2'))
            bot.send_message(message.chat.id, '<b>ΠΠΊΡΡΡ Π½Π΅Π΄Π΅Π»ΠΈπ</b>\nΠ‘ 28.10 ΠΏΠΎ 04.11π.\n\nβ¦Pink '
                                              'lemonadeπ₯€\nβ¦Strawberry bananaππ '
                                              '\nβ¦Spearmintπ\nΠΠ° Π΄Π°Π½Π½ΡΠ΅ ΠΏΡΠΎΠ΄ΡΠΊΡΡ Π΄Π΅ΠΉΡΡΠ²ΡΠ΅Ρ\n ΡΠΊΠΈΠ΄ΠΊΠ°: Π²ΠΌΠ΅ΡΡΠΎ '
                                              '<b>300 CZK β 250 CZKπ·</b>\n\n<b>Π‘ ΡΠ²Π°ΠΆΠ΅Π½ΠΈΠ΅ΠΌ ELF BAR PRAGUEπ«</b>',
                             parse_mode='html', reply_markup=markup)

        elif message.text == 'πΠΠ°Ρ ΠΊΠ°Π½Π°Π»':
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(types.InlineKeyboardButton('β‘ΠΠ°Π·Π°Π΄', callback_data='back_2'))
            bot.send_message(message.chat.id,
                             "<a href='https://t.me/praguelfbar'>Elfbar | Prague</a>, ΠΎΠ½Π»Π°ΠΉΠ½ ΠΌΠ°Π³Π°Π·ΠΈΠ½ ΠΏΠΎ ΠΏΡΠΎΠ΄Π°ΠΆΠ΅ "
                             "ΡΠ»Π΅ΠΊΡΡΠΎΠ½Π½ΡΡ ΡΠΈΠ³Π°ΡΠ΅Ρ ΠΏΡΠΎΠ΄ΡΠΊΡΠΈΠΈ Elf Bar ΠΈ ΠΌΡ Π³ΠΎΡΠΎΠ²Ρ ΠΏΡΠ΅Π΄ΠΎΡΡΠ°Π²ΠΈΡΡ Π²Π°ΠΌ:\n\nβ’ ΠΊΠ°ΡΠ΅ΡΡΠ²Π΅Π½Π½ΡΠΉ, "
                             "Π³Π°ΡΠ°Π½ΡΠΈΡΠΎΠ²Π°Π½ΠΎ ΠΎΡΠΈΠ³ΠΈΠ½Π°Π»ΡΠ½ΡΠΉ ΡΠΎΠ²Π°Ρπ\nβ’ Π Π°Π·Π½ΠΎΠΎΠ±ΡΠ°Π·Π½ΡΠΉ Π²ΡΠ±ΠΎΡ Π²ΠΊΡΡΠΎΠ² ΠΏΡΠΎΠ΄ΡΠΊΡΠΈΠΈπ«\nβ’ "
                             "ΠΠΊΡΠΈΠ²Π½Π°Ρ ΡΠ»ΡΠΆΠ±Π° ΠΏΠΎΠ΄Π΄Π΅ΡΠΆΠΊΠΈπ₯\nβ’ Π‘Π°ΠΌΠ°Ρ Π±ΡΡΡΡΠ°Ρ Π΄ΠΎΡΡΠ°Π²ΠΊΠ° ΠΏΠΎ ΠΡΠ°Π³Π΅π¦π\n\nΠΠΎΠ»Π΅Π΅ Π΄Π΅ΡΠ°Π»ΡΠ½Π°Ρ "
                             "ΠΈΠ½ΡΠΎΡΠΌΠ°ΡΠΈΡ Π² Π½Π°ΡΠ΅ΠΌ ΡΠ΅Π»Π΅Π³ΡΠ°ΠΌ ΠΊΠ°Π½Π°Π»Π΅.",
                             parse_mode='html', reply_markup=markup)
        else:
            bot.send_message(message.chat.id,
                             'Π― Π½Π΅ Π·Π½Π°Ρ ΠΊΠ°ΠΊ ΠΎΡΠ²Π΅ΡΠΈΡΡ Π½Π° Π΄Π°Π½Π½ΡΠΉ Π·Π°ΠΏΡΠΎΡ π\n\n<b>ΠΠΎΡΠΏΠΎΠ»ΡΠ·ΡΠΉΡΠ΅ΡΡ ΠΊΠ½ΠΎΠΏΠΊΠ°ΠΌΠΈ ΠΊΠΎΡΠΎΡΡΠ΅ '
                             'Π½Π°ΡΠΎΠ΄ΡΡΡΡ Π½ΠΈΠΆΠ΅.</b>\n\nβ’ ΠΡΠ»ΠΈ Π±ΠΎΡ Π·Π°Π²ΠΈΡ Π»ΠΈΠ±ΠΎ ΠΆΠ΅ Π½Π΅ ΠΎΡΠ²Π΅ΡΠ°Π΅Ρ Π½Π° Π·Π°ΠΏΡΠΎΡΡ - Π½Π°ΠΏΠΈΡΠΈΡΠ΅ '
                             'ΠΊΠΎΠΌΠ°Π½Π΄Ρ: <b>/start</b>.\n\n\nβ ΠΡΠ»ΠΈ Π±ΠΎΡ Π²ΠΎΠ²ΡΠ΅ Π½ΠΈΠΊΠ°ΠΊ Π½Π΅ ΡΠ΅Π°Π³ΠΈΡΡΠ΅Ρ Π½Π° ΠΠ°ΡΠΈ Π·Π°ΠΏΡΠΎΡΡ, '
                             'ΠΏΠΎΠΆΠ°Π»ΡΠΉΡΡΠ°, Π½Π°ΠΏΠΈΡΠΈΡΠ΅ Π² ΡΠ»ΡΠΆΠ±Ρ ΠΏΠΎΠ΄Π΄Π΅ΡΠΆΠΊΠΈ. ΠΠ½Π° Π² ΠΊΡΠΎΡΡΠ°ΠΉΡΠΈΠ΅ ΡΡΠΎΠΊΠΈ ΡΠ²ΡΠΆΠ΅ΡΡΡ Ρ ΠΠ°ΠΌΠΈ.',
                             parse_mode='html')


bot.polling(none_stop=True)

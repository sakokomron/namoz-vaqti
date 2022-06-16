import telebot
from telebot import types
TOKEN = '5569902565:AAH52CKf17aGp_gRUevytzPEl3B-dTJm4nw'

bot = telebot.TeleBot(TOKEN)


def listener(message):
	markup = types.ReplyKeyboardMarkup()
	for m in message:
		chatid = m.chat.id
		if m.content_type == 'text':
			text = m.text
			if(text == '/start'):
				bot.send_message(chatid, 'Assalomu alekum')
			if(text == 'text'):
				markup.add('toshkentadagi namoz vaqti', 'juma muborak', 'boshqa viloyatlardagi namoz vaqti')
				bot.send_message(chatid, '<b>salom</b>', parse_mode="HTML", reply_markup=markup)
			elif (text == 'boshqa viloyatlardagi namoz vaqti'):
				markup.add('toshkentdagi namoz vaqti', 'juma muborak', 'boshqa viloyatlardagi namoz vaqti')
				bot.send_photo(chatid, 'https://t.me/namoz/22284')
			elif (text == 'toshkentadagi namoz vaqti'):
			    markup.add('toshkentdagi namoz vaqti', 'juma muborak', 'boshqa viloyatlardagi namoz vaqti')
			    bot.send_photo(chatid, 'https://t.me/KDUZB/82424', reply_markup=markup)
			elif text == 'juma muborak':
				markup.add('toshkentadagi namoz vaqti', 'juma muborak', 'boshqa viloyatlardagi namoz vaqti')
				bot.send_photo(chatid, 'https://t.me/suralar_duolar_qurondan_maruzala/714', reply_markup=markup)
		elif m.content_type == 'photo':
			bot.send_message(chatid, "salom")

bot.set_update_listener(listener)

bot.polling()
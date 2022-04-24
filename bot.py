#библиотеки, которые загружаем из вне
import telebot
TOKEN = 'ВСТАВЬТЕ ВАШ ТОКЕН'

from telebot import types

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('AnimatedSticker.tgs', 'rb')
	bot.send_sticker(message.chat.id, sti)

	#клавиатура
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("😻 GitHub")
	item2 = types.KeyboardButton("😼 Telegram")
	item3 = types.KeyboardButton("😺 Погоняем?")
	markup.add(item1, item2, item3)

	bot.send_message(message.chat.id, "Привет 😺, я рад знакомству, {0.first_name}!".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

#назначаем действие для клавиатуры
@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == '😻 GitHub':
			bot.send_message(message.chat.id, 'https://github.com/AntonSadkov')
		elif message.text == '😼 Telegram':
			bot.send_message(message.chat.id, 'https://t.me/AntonSadkov')
		elif message.text == '😺 Погоняем?':
			bot.send_message(message.chat.id, 'https://prizes.gamee.com/game-bot/Q8PWil-49dfe04bb912b525fdea9d0f61635e451e53310b#tgShareScoreUrl=tg%3A%2F%2Fshare_game_score%3Fhash%3DcRUbpkRbiKL3FpnNSRXYuYM9rALC-BN3FbA2F0bFmjkpVJISFQ9iI1S9M8fAr-Kl')
		else:
			bot.send_message(message.chat.id, 'Не знаю что ответить😢')


bot.polling(none_stop=True)









#https://core.telegram.org/bots/api#available-methods

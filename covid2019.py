import COVID19Py
import telebot

covid2019 = COVID19Py.COVID19()
bot=telebot.TeleBot('place for your token')

@bot.message_handler(commands=['start'])
def start(message):
    send_message='Привет , этот бот поможет тебе узнать последнию информацию о ситуации с короновирусом. \n Напишите название страны из этого списка, что бы получить данные(Кыргызстан, Казахстан, Россия)'

    bot.send_message(message.chat.id, send_message)

@bot.message_handler(content_types=['text'])
def start(message):
    info_message=''
    get_message_bot=message.text.strip().lower()
    if get_message_bot=='кыргызстан':
        info=covid2019.getLocationByCountryCode('KG')
    elif get_message_bot=='россия':
        info=covid2019.getLocationByCountryCode('RU')
    elif get_message_bot=='казахстан':
        info=covid2019.getLocationByCountryCode('KZ')
    else:
        info = covid2019.getLatest()
        info_message="Количество заболошевших в мире: {} , \n Количество умерших{}".format(info['confirmed'], info['deaths'])
    if info_message=='':
        info_message = 'Количество заболевших в стране {} : \n Количество умерших: {} \n Дата обновления: {}'.format(info[0]['latest']['confirmed'], info[0]['latest']['deaths'],info[0]['last_updated'])

    bot.send_message(message.chat.id, info_message)


bot.polling(none_stop=True)

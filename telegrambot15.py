import telebot

token = '1094865183:AAGH3s7ND6P0iH6oIWDsu4I9-QgW3SeChf4'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello , '
                                      'I will help you find lessons in ocs')
    bot.send_message(message.chat.id, 'What do you need?')
    bot.send_message(message.chat.id, '1 /english')
    bot.send_message(message.chat.id, '2 /ecology')
    bot.send_message(message.chat.id, '3 /python')
    bot.send_message(message.chat.id, '4 /intro2eng')
    bot.send_message(message.chat.id, '5 /physics')
    bot.send_message(message.chat.id, '6 /calculus')
    bot.send_message(message.chat.id, '7 /russian')
    bot.send_message(message.chat.id, '8 /turkish')
    bot.send_message(message.chat.id, '9 /physicalculture')


@bot.message_handler(commands=['settings'])
def start_message(message):
    bot.send_message(message.chat.id, 'There is no problem here\n'
                                      'Click on /help')


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'If you want to start the program,\n'
                                      'press the /start command!\n\n'
                                      'If you need help with python,\n'
                                      'press to /python_language command!\n\n'
                                      'If you need help with HTML,\n'
                                      'press to /html_language command!\n\n'
                                      'If you want to create '
                                      'a telegram bot like me,\n'
                                      'press to /create_a_bot command!')


@bot.message_handler(commands=['entertainment'])
def start_message(message):
    bot.send_message(message.chat.id, 'WHAT DO YOU PREFER?')
    bot.send_message(message.chat.id, '1) /football')
    bot.send_message(message.chat.id, '2) /news')
    bot.send_message(message.chat.id, '3) /nat_geo_wild')
    bot.send_message(message.chat.id, '4) /films')
    bot.send_message(message.chat.id, '5) /gamers')


@bot.message_handler(commands=['football'])
def start_message(message):
    bot.send_message(message.chat.id, 'Football:'
                                      'https://www.'
                                      'youtube.com/c/TARAFTARKANALIHD/videos')
    bot.send_message(message.chat.id, 'https://www.youtube.com/channel/'
                                      'UCO8qj5u80Ga7N_tP3BZWWhQ/videos')
    bot.send_message(message.chat.id, 'https://www.'
                                      'youtube.com/c/AllFootball28/videos')
    bot.send_message(message.chat.id, 'https://www.'
                                      'youtube.com/c/Score90/videos')


@bot.message_handler(commands=['news'])
def start_message(message):
    bot.send_message(message.chat.id, 'News: '
                                      'https://www.'
                                      'youtube.com/c/NBCNews/videos')
    bot.send_message(message.chat.id, 'https://www.youtube.com/c/'
                                      'BBCNews/videos')
    bot.send_message(message.chat.id, 'https://www.'
                                      'youtube.com/c/globalnews/videos')
    bot.send_message(message.chat.id, 'https://www.'
                                      'youtube.com/c/ddnews/videos')


@bot.message_handler(commands=['nat_geo_wild'])
def start_message(message):
    bot.send_message(message.chat.id, 'Nat Geo Wild: '
                                      'https://www.youtube.com/channel'
                                      '/UChqjsr9DovXmAUtS_q_2V0w/videos')


@bot.message_handler(commands=['films'])
def start_message(message):
    bot.send_message(message.chat.id, 'Films'
                                      ':https://www.'
                                      'youtube.com/c/FilmsterRu/videos')
    bot.send_message(message.chat.id, 'https://www.youtube.'
                                      'com/c/RVisionChannel/videos')
    bot.send_message(message.chat.id, 'https://www.youtube.com/channel/'
                                      'UCK3AJaBVixx5BvCPLI2Ho9g/videos')


@bot.message_handler(commands=['gamers'])
def start_message(message):
    bot.send_message(message.chat.id, '1) Marmok:\n\n'
                                      'https://www.'
                                      'youtube.com/c/MrMarmok/videos')
    bot.send_message(message.chat.id, '2) Joe speen:\n\n'
                                      'https://www.'
                                      'youtube.com/c/JoeSpeen/videos')
    bot.send_message(message.chat.id, '3) Quantum:\n\n'
                                      'https://www.'
                                      'youtube.com/c/QuantumGames/videos')
    bot.send_message(message.chat.id, '4) Buster:\n\n'
                                      'https://www.youtube.'
                                      'com/c/%D0%91%D1%83%D1%81%'
                                      'D1%82%D0%B5%D1%80/videos')


@bot.message_handler(commands=['english'])
def start_message(message):
    bot.send_message(message.chat.id, 'English:\n'
                                      'https://classroom.'
                                      'google.com/c/MTU5MjczNzc1MDk1')
    bot.send_message(message.chat.id, 'Teacher: Sagyn Basnyat')
    bot.send_message(message.chat.id, 'Gmail: ')


@bot.message_handler(commands=['ecology'])
def start_message(message):
    bot.send_message(message.chat.id, 'Ecology:\n'
                                      'https://classroom.'
                                      'google.com/c/MTUzNjg2NTcxMTM5')
    bot.send_message(message.chat.id, 'Teacher: Turdukan Bekimbetova')
    bot.send_message(message.chat.id, 'Gmail: '
                                      'turdukan.bekimbetova@iaau.edu.kg')


@bot.message_handler(commands=['python'])
def start_message(message):
    bot.send_message(message.chat.id, 'Python:\n'
                                      'https://ocs.iaau.edu.kg/'
                                      'course/view.php?id=28')
    bot.send_message(message.chat.id, 'Teachers: '
                                      'Ruslan Isaev and Gulzada Esenalieva')
    bot.send_message(message.chat.id, 'Gmail: ruslan.isaev@alatoo.edu.kg')
    bot.send_message(message.chat.id, 'Gmail: ruslan.isaev@iaau.edu.kg')
    bot.send_message(message.chat.id, 'Gmail: gulzada.'
                                      'esenalieva@alatoo.edu.kg')


@bot.message_handler(commands=['intro2eng'])
def start_message(message):
    bot.send_message(message.chat.id, 'Intro2eng:\n'
                                      'https://ocs.iaau.edu.kg/'
                                      'course/view.php?id=2')
    bot.send_message(message.chat.id, 'Teacher: Burul Shambetova')
    bot.send_message(message.chat.id, 'Gmail: '
                                      'burul.shambetova@alatoo.edu.kg')


@bot.message_handler(commands=['physics'])
def start_message(message):
    bot.send_message(message.chat.id, 'Physics:\n'
                                      'https://ocs.iaau.edu.kg/'
                                      'course/view.php?id=135')
    bot.send_message(message.chat.id, 'Teacher: Tahir Aslan')
    bot.send_message(message.chat.id, 'Gmail: '
                                      't.aslan@alatoo.edu.kg')


@bot.message_handler(commands=['calculus'])
def start_message(message):
    bot.send_message(message.chat.id, 'Calculus:\n'
                                      'https://ocs.iaau.edu.kg/'
                                      'course/view.php?id=193')
    bot.send_message(message.chat.id, 'Teacher: Khalid Mohammad')
    bot.send_message(message.chat.id, 'Gmail: '
                                      'khalid.mohammad@alatoo.edu.kg')


@bot.message_handler(commands=['russian'])
def start_message(message):
    bot.send_message(message.chat.id, 'Russian:\n'
                                      'https://ocs.iaau.edu.kg/'
                                      'course/view.php?id=409')
    bot.send_message(message.chat.id, 'Teacher: Surakan Muzurbekovna')
    bot.send_message(message.chat.id, 'Gmail: '
                                      'surakan.alymbekova@iaau.edu.kg')


@bot.message_handler(commands=['turkish'])
def start_message(message):
    bot.send_message(message.chat.id, 'Turkish:\n'
                                      'https://ocs.iaau.edu.kg/'
                                      'course/view.php?id=1550')
    bot.send_message(message.chat.id, 'Teacher: Mr Mehmet')
    bot.send_message(message.chat.id, 'Gmail: ')


@bot.message_handler(commands=['physicalculture'])
def start_message(message):
    bot.send_message(message.chat.id, 'Physicalculture:\n'
                                      'https: //ocs.iaau.edu.kg/'
                                      'course/view.php?id=1217')
    bot.send_message(message.chat.id, 'Teacher: '
                                      'Irina Chalova')
    bot.send_message(message.chat.id, 'Gmail: '
                                      'irina.chalova@iaau.edu.kg')


@bot.message_handler(commands=['python_language'])
def start_message(message):
    bot.send_message(message.chat.id, 'Here you can learn to'
                                      ' python for free.')
    bot.send_message(message.chat.id, 'https://www.'
                                      'w3schools.com/python/')


@bot.message_handler(commands=['html_language'])
def start_message(message):
    bot.send_message(message.chat.id, 'Here you can learn to'
                                      ' html for free.')
    bot.send_message(message.chat.id, 'https://www.'
                                      'w3schools.com/html/default.asp')


@bot.message_handler(commands=['create_a_bot'])
def start_message(message):
    bot.send_message(message.chat.id, 'Here you can create a new bot.')
    bot.send_message(message.chat.id, 'https://t.me/BotFather')


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, 'I do not have such kind of command')
    bot.send_message(message.chat.id, 'If you get bored click on'
                                      ' /entertainment')
    bot.send_message(message.chat.id, 'if you need help click on /help')

bot.polling()


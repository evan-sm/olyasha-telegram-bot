def mem(bot, update, args):
    print(update.message.text)
    if not args:
        bot.send_message(chat_id=update.message.chat_id,
                        text='Мемы:\n'
                        '/mem дуранчоусы  — <i>Вы шо дуранчоусы?</i>\n'
                        '/mem борис  — <i>Похотливый Борис</i>', parse_mode='HTML')
    for s in args:
        if s.lower() == 'дуранчоусы':
            bot.send_chat_action(chat_id=update.message.chat_id, action='record_video_note')
            bot.send_video_note(chat_id=update.message.chat_id, video_note='DQADAgADVQIAAnNbMUv23rJ7tb5U0QI')
            # bot.send_video_note(chat_id=update.message.chat_id, video_note=open('files/duranchousi.mp4', 'rb'), duration=1)
        elif s.lower() == 'борис':
            bot.send_chat_action(chat_id=update.message.chat_id, action='record_video_note')
            bot.send_video_note(chat_id=update.message.chat_id, video_note='DQADAgADWwIAAoCFUUqPv5dxuJnYcAI')
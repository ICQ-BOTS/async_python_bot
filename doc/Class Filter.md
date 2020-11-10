# Class Filter
## message
Филтр сообщения
## command
Фильр команд
## file
Фильтр файлов
## image
Фильтр изображений
## video
Фильтр видео
## audio
Фильтр аудио
## voice
Фильтр голосовых сообщений
## media
Фильтр медиа файлов (image, video, audio, voice)
## sticker
Фильтр стикеров
## url
URL фильтр
## text_only
Фильтр текстовых сообщений, не (command, sticker, file, url)
## text(list)
Фильтр сообщения по тексту
```python
bot.dispatcher.add_handler(
    MessageHandler(
        callback=hello,
        filters=Filter.text(['Ghbdtn', 'Привет', 'Прив', 'Хай'])
    )
)
```

## regexp(regular)
Фильтр сообщения по тексту
Параметры:
* regular - регулярное выражение
```python
bot.dispatcher.add_handler(MessageHandler(
                            callback=hello, 
                            filters=Filter.regexp('(?i)^(привет|хай)')
                        )
                    )
```

## mention(user_id=None)
Упоминание пользователей
Параметры:
* user_id - id на который будет срабатывать

## forward
Фильтр пересылания сообщения

## reply
Фильтр ответа на сообщения

## callback_data(callback_data)
Фильтр кнопок
Параметры:
* callback_data - callbackData

## callback_data_regexp(regular)
Фильтр кнопок с регуляторным выражением
Параметры:
* regular - регулярное выражение

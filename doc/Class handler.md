# Class handler
## DefaultHandler(callback=func)
Обработчик по умолчанию
Параметры:
* callback - фукнцию которую вызывает хендлер

## NewChatMembersHandler(callback=None, filters=None, multiline=False, ignore=None)
Обработчик входа в чата
Параметры:
* callback - фукнцию которую вызывает хендлер.
* filters - Фильтр.
* multiline - Обработчик многострочных команд.На вход функция получит помимо (bot, event) объект user, через который можно ожидать следующий ответ пользователя.
* ignore - настройка приоритетов команд, на вход получает хендлер

## LeftChatMembersHandler(callback=None, filters=None, multiline=False, ignore=None)
Обработчик выхода из чата
Параметры:
* callback - фукнцию которую вызывает хендлер.
* filters - Фильтр.
* multiline - Обработчик многострочных команд.На вход функция получит помимо (bot, event) объект user, через который можно ожидать следующий ответ пользователя.
* ignore - настройка приоритетов команд, на вход получает хендлер

## PinnedMessageHandler(callback=None, filters=None, multiline=False, ignore=None)
Обработчик на закрепления сообщения
Параметры:
* callback - фукнцию которую вызывает хендлер.
* filters - Фильтр.
* multiline - Обработчик многострочных команд.На вход функция получит помимо (bot, event) объект user, через который можно ожидать следующий ответ пользователя.
* ignore - настройка приоритетов команд, на вход получает хендлер

## UnPinnedMessageHandler(callback=None, filters=None, multiline=False, ignore=None)
Обработчик открепления сообщения
Параметры:
* callback - фукнцию которую вызывает хендлер.
* filters - Фильтр.
* multiline - Обработчик многострочных команд.На вход функция получит помимо (bot, event) объект user, через который можно ожидать следующий ответ пользователя.
* ignore - настройка приоритетов команд, на вход получает хендлер

## MessageHandler(callback=None, filters=None, multiline=False, ignore=None)
Обработчик нового сообщения
Параметры:
* callback - фукнцию которую вызывает хендлер.
* filters - Фильтр.
* multiline - Обработчик многострочных команд.На вход функция получит помимо (bot, event) объект user, через который можно ожидать следующий ответ пользователя.
* ignore - настройка приоритетов команд, на вход получает хендлер

## EditedMessageHandler(callback=None, filters=None, multiline=False, ignore=None)
Обработчик редактирования сообщения
Параметры:
* callback - фукнцию которую вызывает хендлер.
* filters - Фильтр.
* multiline - Обработчик многострочных команд.На вход функция получит помимо (bot, event) объект user, через который можно ожидать следующий ответ пользователя.
* ignore - настройка приоритетов команд, на вход получает хендлер

## DeletedMessageHandler(callback=None, filters=None, multiline=False, ignore=None)
Обработчик удаление сообщений
Параметры:
* callback - фукнцию которую вызывает хендлер.
* filters - Фильтр.
* multiline - Обработчик многострочных команд.На вход функция получит помимо (bot, event) объект user, через который можно ожидать следующий ответ пользователя.
* ignore - настройка приоритетов команд, на вход получает хендлер

## CommandHandler(callback=None, command=None, multiline=False, ignore=None)
Обработчик команд
Параметры:
* callback - фукнцию которую вызывает хендлер.
* command - Команда.
* multiline - Обработчик многострочных команд.На вход функция получит помимо (bot, event) объект user, через который можно ожидать следующий ответ пользователя.
* ignore - настройка приоритетов команд, на вход получает хендлер.

## HelpCommandHandler(callback=None, command=None, multiline=False, ignore=None)
Обработчик команды /help
Параметры:
* callback - фукнцию которую вызывает хендлер.
* command - Команда.
* multiline - Обработчик многострочных команд.На вход функция получит помимо (bot, event) объект user, через который можно ожидать следующий ответ пользователя.
* ignore - настройка приоритетов команд, на вход получает хендлер.

## StartCommandHandler(callback=None, command=None, multiline=False, ignore=None)
Обработчик команды /start
Параметры:
* callback - фукнцию которую вызывает хендлер.
* command - Команда.
* multiline - Обработчик многострочных команд.На вход функция получит помимо (bot, event) объект user, через который можно ожидать следующий ответ пользователя.
* ignore - настройка приоритетов команд, на вход получает хендлер.

## UnknownCommandHandler(callback=None, multiline=False, ignore=None)
Обработчик неизвестной команды
Параметры:
* callback - фукнцию которую вызывает хендлер.
* command - Команда.
* multiline - Обработчик многострочных команд.На вход функция получит помимо (bot, event) объект user, через который можно ожидать следующий ответ пользователя.
* ignore - настройка приоритетов команд, на вход получает хендлер.

## BotButtonCommandHandler(callback=None, filters=None, multiline=False, ignore=None)
Обработчик кнопок
<details> 
  <summary>Параметры</summary>
   <ul>
    <li>callback - фукнцию которую вызывает хендлер.</li>
    <li>filters - Фильтр.</li>
     <li>multiline - Обработчик многострочных команд.На вход функция получит помимо (bot, event) объект user, через который можно ожидать следующий ответ пользователя.</li>
    <li>ignore - настройка приоритетов команд, на вход получает хендле</li>
    </ul>
</details>

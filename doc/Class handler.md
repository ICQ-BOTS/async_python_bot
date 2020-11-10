# Class handler
## DefaultHandler(callback=func)
Обработчик по умолчанию
<details> 
  <summary>Параметры</summary>
   <ul>
    <li>callback - фукнцию которую вызывает хендлер.</li>
    </ul>
</details>

## NewChatMembersHandler(callback=None, filters=None, multiline=False, ignore=None)
Обработчик входа в чата
<details> 
  <summary>Параметры</summary>
   <ul>
    <li>callback - фукнцию которую вызывает хендлер.</li>
    <li>filters - Фильтр.</li>
     <li>multiline - Обработчик многострочных команд.На вход функция получит помимо (bot, event) объект user, через который можно ожидать следующий ответ пользователя.</li>
    <li>ignore - настройка приоритетов команд, на вход получает хендле</li>
    </ul>
</details>

## LeftChatMembersHandler(callback=None, filters=None, multiline=False, ignore=None)
Обработчик выхода из чата
<details> 
  <summary>Параметры</summary>
   <ul>
    <li>callback - фукнцию которую вызывает хендлер.</li>
    <li>filters - Фильтр.</li>
     <li>multiline - Обработчик многострочных команд.На вход функция получит помимо (bot, event) объект user, через который можно ожидать следующий ответ пользователя.</li>
    <li>ignore - настройка приоритетов команд, на вход получает хендле</li>
    </ul>
</details>

## PinnedMessageHandler(callback=None, filters=None, multiline=False, ignore=None)
Обработчик на закрепления сообщения
<details> 
  <summary>Параметры</summary>
   <ul>
    <li>callback - фукнцию которую вызывает хендлер.</li>
    <li>filters - Фильтр.</li>
     <li>multiline - Обработчик многострочных команд.На вход функция получит помимо (bot, event) объект user, через который можно ожидать следующий ответ пользователя.</li>
    <li>ignore - настройка приоритетов команд, на вход получает хендле</li>
    </ul>
</details>

## UnPinnedMessageHandler(callback=None, filters=None, multiline=False, ignore=None)
Обработчик открепления сообщения
<details> 
  <summary>Параметры</summary>
   <ul>
    <li>callback - фукнцию которую вызывает хендлер.</li>
    <li>filters - Фильтр.</li>
     <li>multiline - Обработчик многострочных команд.На вход функция получит помимо (bot, event) объект user, через который можно ожидать следующий ответ пользователя.</li>
    <li>ignore - настройка приоритетов команд, на вход получает хендле</li>
    </ul>
</details>

## MessageHandler(callback=None, filters=None, multiline=False, ignore=None)
Обработчик нового сообщения
<details> 
  <summary>Параметры</summary>
   <ul>
    <li>callback - фукнцию которую вызывает хендлер.</li>
    <li>filters - Фильтр.</li>
     <li>multiline - Обработчик многострочных команд.На вход функция получит помимо (bot, event) объект user, через который можно ожидать следующий ответ пользователя.</li>
    <li>ignore - настройка приоритетов команд, на вход получает хендле</li>
    </ul>
</details>

## EditedMessageHandler(callback=None, filters=None, multiline=False, ignore=None)
Обработчик редактирования сообщения
<details> 
  <summary>Параметры</summary>
   <ul>
    <li>callback - фукнцию которую вызывает хендлер.</li>
    <li>filters - Фильтр.</li>
     <li>multiline - Обработчик многострочных команд.На вход функция получит помимо (bot, event) объект user, через который можно ожидать следующий ответ пользователя.</li>
    <li>ignore - настройка приоритетов команд, на вход получает хендле</li>
    </ul>
</details>

## DeletedMessageHandler(callback=None, filters=None, multiline=False, ignore=None)
Обработчик удаление сообщений
<details> 
  <summary>Параметры</summary>
   <ul>
    <li>callback - фукнцию которую вызывает хендлер.</li>
    <li>filters - Фильтр.</li>
     <li>multiline - Обработчик многострочных команд.На вход функция получит помимо (bot, event) объект user, через который можно ожидать следующий ответ пользователя.</li>
    <li>ignore - настройка приоритетов команд, на вход получает хендле</li>
    </ul>
</details>

## CommandHandler(callback=None, command=None, multiline=False, ignore=None)
Обработчик команд
<details> 
  <summary>Параметры</summary>
   <ul>
    <li>callback - фукнцию которую вызывает хендлер.</li>
    <li>command - Команда.</li>
     <li>multiline - Обработчик многострочных команд.На вход функция получит помимо (bot, event) объект user, через который можно ожидать следующий ответ пользователя.</li>
    <li>ignore - настройка приоритетов команд, на вход получает хендле</li>
    </ul>
</details>

## HelpCommandHandler(callback=None, command=None, multiline=False, ignore=None)
Обработчик команды /help
<details> 
  <summary>Параметры</summary>
   <ul>
    <li>callback - фукнцию которую вызывает хендлер.</li>
    <li>command - Команда.</li>
     <li>multiline - Обработчик многострочных команд.На вход функция получит помимо (bot, event) объект user, через который можно ожидать следующий ответ пользователя.</li>
    <li>ignore - настройка приоритетов команд, на вход получает хендле</li>
    </ul>
</details>

## StartCommandHandler(callback=None, command=None, multiline=False, ignore=None)
Обработчик команды /start
<details> 
  <summary>Параметры</summary>
   <ul>
    <li>callback - фукнцию которую вызывает хендлер.</li>
    <li>command - Команда.</li>
     <li>multiline - Обработчик многострочных команд.На вход функция получит помимо (bot, event) объект user, через который можно ожидать следующий ответ пользователя.</li>
    <li>ignore - настройка приоритетов команд, на вход получает хендле</li>
    </ul>
</details>

## UnknownCommandHandler(callback=None, multiline=False, ignore=None)
Обработчик неизвестной команды
<details> 
  <summary>Параметры</summary>
   <ul>
    <li>callback - фукнцию которую вызывает хендлер.</li>
     <li>multiline - Обработчик многострочных команд.На вход функция получит помимо (bot, event) объект user, через который можно ожидать следующий ответ пользователя.</li>
    <li>ignore - настройка приоритетов команд, на вход получает хендле</li>
    </ul>
</details>

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

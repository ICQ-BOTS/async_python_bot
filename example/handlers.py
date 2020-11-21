import json

async def hello_cb(bot, event, user):
    await bot.send_text(chat_id=event.message_author['userId'], text=f"1 ответ на {event.text}")
    response = await user.wait_response()
    await bot.send_text(chat_id=event.message_author['userId'], text=f"2 ответ на {response.text}")
    response = await user.wait_response()
    await bot.send_text(chat_id=event.message_author['userId'], text=f"3 ответ на {response.text}")


async def buttons_get_cb(bot, event):
    await bot.send_text(
        chat_id=event.message_author['userId'],
        text="Hello with buttons.",
        inline_keyboard_markup="[{}]".format(json.dumps([
            {"text": "Action 1", "url": "http://mail.ru"},
            {"text": "Action 2", "callbackData": "call_back_id_2"},
            {"text": "Action 3", "callbackData": "call_back_id_3"}
        ])))


async def buttons_answer_cb(bot, event):
    if event.data['callbackData'] == "call_back_id_2":
        await bot.answer_callback_query(
            query_id=event.data['queryId'],
            text="Hey! It's a working button 2.",
            show_alert=True
        )

    elif event.data['callbackData'] == "call_back_id_3":
        await bot.answer_callback_query(
            query_id=event.data['queryId'],
            text="Hey! It's a working button 3.",
            show_alert=False
        )


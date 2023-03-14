import logging
import os

from vkbottle import GroupEventType, GroupTypes, Keyboard, Callback
from vkbottle.bot import Bot, Message
from vkbottle.modules import json
from config import api

bot = Bot("TOKEN_BOTA")
logging.basicConfig(level=logging.INFO)

Keyboard = (
        Keyboard(one_time=False)
        .add(Callback("Сменить локацию", payload={"cmd": "change_location"}))
        .add(Callback("Инвентарь", payload={"cmd": "inventory"}))
        .row()
        .add(Callback("Арена", payload={"cmd": "arena"}))
        .add(Callback("Мини игры", payload={"cmd": "mini_games"}))
        .row()
        .add(Callback("Настройки", payload={"cmd": "settings"}))
    )

@bot.on.private_message(text="Начать")
async def gm(message: Message):
    await message.answer("Главное меню", keyboard=Keyboard)

@bot.on.raw_event(GroupEventType.MESSAGE_EVENT, dataclass=GroupTypes.MessageEvent)
async def event_gm(event: GroupTypes.MessageEvent):
    if event.object.payload["cmd"] == "change_location":
        await bot.api.messages.send_message_event_answer(
            event_id=event.object.event_id,
            user_id=event.object.user_id,
            peer_id=event.object.peer_id,
            event_data=json.dumps({"type": "show_snackbar", "text": "В разработке!"})
        )
    elif event.object.payload["cmd"] == "inventory":
         await bot.api.messages.send_message_event_answer(
            event_id=event.object.event_id,
            user_id=event.object.user_id,
            peer_id=event.object.peer_id,
            event_data=json.dumps({"type": "show_snackbar", "text": "В разработке!"})
        )
    elif event.object.payload["cmd"] == "arena":
        await bot.api.messages.send_message_event_answer(
            event_id=event.object.event_id,
            user_id=event.object.user_id,
            peer_id=event.object.peer_id,
            event_data=json.dumps({"type": "show_snackbar", "text": "В разработке!"})
        )
    elif event.object.payload["cmd"] == "mini_games":
        await bot.api.messages.send_message_event_answer(
            event_id=event.object.event_id,
            user_id=event.object.user_id,
            peer_id=event.object.peer_id,
            event_data=json.dumps({"type": "show_snackbar", "text": "В разработке!"})
        )
    else:
        await bot.api.messages.send_message_event_answer(
            event_id=event.object.event_id,
            user_id=event.object.user_id,
            peer_id=event.object.peer_id,
            event_data=json.dumps({"type": "show_snackbar", "text": "В разработке!"})
        )
bot.run_forever()

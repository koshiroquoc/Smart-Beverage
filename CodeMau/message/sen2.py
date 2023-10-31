import telegram
import asyncio

my_token = "6255771559:AAGVvLf8C6RwhYHK82NsuigFVon5p-lTH6Q"

async def send(msg, chat_id, token=my_token,typ=1):
    """
    Send a message to a telegram user or group specified on chatId
    chat_id must be a number!
    """
    bot = telegram.Bot(token=token)
    if typ==1:
        await bot.sendMessage(chat_id=chat_id, text=msg)
    else:
        await bot.sendPhoto(chat_id=chat_id, photo=open("total_drinks.png", "rb"), caption="Report")
    print('Message Sent!')


MessageString = 'Testing from virtual server'
print(MessageString)
asyncio.run(send(MessageString, 6212688305, my_token,2)) # Goes to Selection_Testing
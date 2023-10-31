
#bot.sendPhoto(chat_id="6212688305", photo = open("b.jpeg","rb"), caption = "Có súng, nguy hiêm!")
import asyncio
import telegram

async def main():
    my_token = "6255771559:AAGVvLf8C6RwhYHK82NsuigFVon5p-lTH6Q"

    # Tạo bot
    bot = telegram.Bot(token=my_token)
    # Gửi thử text message
    await bot.send_message(chat_id="6212688305", text="Gửi từ PyCharm")

asyncio.run(main())

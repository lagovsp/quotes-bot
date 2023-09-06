import telebot

from crawler import get_message
from token import token

bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def handle_start(message) -> None:
    bot.send_message(message.chat.id, "Hi, I am telling current time!")


@bot.message_handler(func=lambda m: True)
def handle_text(message) -> None:
    bot.send_message(
        message.chat.id,
        get_message(),
        parse_mode="HTML",
    )


if __name__ == "__main__":
    bot.infinity_polling()

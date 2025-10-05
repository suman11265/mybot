# bot.py
import os
import telebot
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

TOKEN = os.getenv("7606865104:AAGQkoSCcTqC7WzEo_0aiRGK1zAuoHF-qME")

if not TOKEN:
    logger.error("Token not found! Set TELEGRAM_BOT_TOKEN environment variable or token.txt file.")
    print("Options:")
    print("1) In CMD: set TELEGRAM_BOT_TOKEN=YOUR_TOKEN")
    print("2) Create token.txt in same folder containing token")
    exit(1)

bot = telebot.TeleBot(TOKEN)

# /start handler
@bot.message_handler(commands=['start'])
def start(message):
    logger.info("Received /start from %s", message.from_user.username)
    bot.reply_to(message, "hii")

# Hello/Hi/Hey handler
@bot.message_handler(func=lambda m: m.text and m.text.lower().strip() in ["hello", "hi", "hey"])
def reply_hello(message):
    logger.info("Received greeting from %s: %s", message.from_user.username, message.text)
    bot.reply_to(message, "hii")

# Default handler
@bot.message_handler(func=lambda m: True)
def fallback(message):
    pass  # do nothing for other messages

if __name__ == "__main__":
    logger.info("Bot starting...")
    try:
        bot.infinity_polling(timeout=60, long_polling_timeout=60)
    except KeyboardInterrupt:
        logger.info("Bot stopped by user")
    except Exception as e:
        logger.exception("Bot crashed: %s", e)

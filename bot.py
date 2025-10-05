# bot.py
import telebot
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

# ⚠️ Hard-coded token (local/demo use only)
TOKEN = "7606865104:AAGQkoSCcTqC7WzEo_0aiRGK1zAuoHF-qME"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    logger.info("Received /start from %s", message.from_user.username)
    bot.reply_to(message, "hii")

@bot.message_handler(func=lambda m: m.text and m.text.lower().strip() in ["hello","hi","hey"])
def reply_hello(message):
    logger.info("Received greeting from %s: %s", message.from_user.username, message.text)
    bot.reply_to(message, "hii")

@bot.message_handler(func=lambda m: True)
def fallback(message):
    pass

if __name__ == "__main__":
    logger.info("Bot running... (press CTRL+C to stop)")
    try:
        bot.infinity_polling(timeout=60, long_polling_timeout=60)
    except KeyboardInterrupt:
        logger.info("Bot stopped by user")
    except Exception as e:
        logger.exception("Bot crashed: %s", e)

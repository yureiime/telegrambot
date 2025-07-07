import logging
import os

from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, ContextTypes, CommandHandler
from dotenv import load_dotenv
from google import genai

from memory import get_user_memory, update_user_memory, add_conversation_history, get_recent_conversation_history

load_dotenv('.env')
TOKEN = os.getenv('TOKEN')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_memory = get_user_memory(user_id=user_id)
    name = user_memory.get('name', update.effective_user.first_name)
    await update.message.reply_text(f'Hello {name}! How can I help you with (use case)')
    # maybe implement pop up feature
    if 'name' not in user_memory:
        update_user_memory(user_id=user_id, key='name', value=update.effective_user.first_name)


def main():
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))

    application.run_polling()

if __name__ == "__main__":
    main()
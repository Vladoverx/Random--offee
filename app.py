import logging
from handlers.common_handlers import start
from handlers.coffee_handler import coffee, stop_poll, poll_answer_handler
from handlers.config_handler import get_token

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    PollAnswerHandler
)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

TOKEN = get_token()
               

def main() -> None:
    """Run the bot."""
    # Create the Application and pass it bot's token.
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("coffee", coffee))
    application.add_handler(CallbackQueryHandler(stop_poll, pattern='^stop_poll$'))
    application.add_handler(PollAnswerHandler(poll_answer_handler))
    
    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
    
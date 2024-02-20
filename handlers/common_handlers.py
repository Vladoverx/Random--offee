from telegram import Update
from telegram.ext import (
    ContextTypes,
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """"""

    message = """ Привіт! Це Random Coffee 😎
    
Я допоможу тобі знайомитися та організовувати зустрічі з цікавими людьми в твоєму чаті.
    
Для створення події використовуй команду /coffee разом з датою проведення.

Приклад: /coffee 30 липня

Необхідна кількість учасників для проведення Random Coffee від 4-х осіб.
Зупинити опитування може лише творець події.
            
Бажаю вдалого нетворкінгу!
    """

    await update.message.reply_text(message)

    
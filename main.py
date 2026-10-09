import os
import re
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.environ.get("8829356253:AAHwnkTRdVcKnDAjTkITm3M6irCZxWYBkp4")
AMAZON_TAG = os.environ.get("vikassmartdea-21")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("नमस्ते! मुझे कोई भी Amazon product link भेजें, मैं उसे आपके Affiliate Link में बदल दूंगा।")

async def convert_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    amazon_urls = re.findall(r'(https?://[^\s]+)', text)
    
    if not amazon_urls:
        return

    for url in amazon_urls:
        if "amazon" in url or "amzn" in url:
            # Simple Tag Injection
            if "?" in url:
                affiliate_url = f"{url}&tag={AMAZON_TAG}"
            else:
                affiliate_url = f"{url}?tag={AMAZON_TAG}"
            
            await update.message.reply_text(f"🛒 **आपका Affiliate Link:**\n{affiliate_url}")

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, convert_link))
    app.run_polling()


import os
import re
from threading import Thread
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Render के पोर्ट चेक के लिए Dummy Flask Server
app_express = Flask('')

@app_express.route('/')
def home():
    return "Bot is alive!"

def run():
    app_express.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

def keep_alive():
    t = Thread(target=run)
    t.start()

BOT_TOKEN = os.environ.get("BOT_TOKEN")
AMAZON_TAG = os.environ.get("AMAZON_TAG")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("नमस्ते! मुझे Amazon link भेजें, मैं इसे Affiliate Link में बदल दूंगा।")

async def convert_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    amazon_urls = re.findall(r'(https?://[^\s]+)', text)
    if not amazon_urls:
        return

    for url in amazon_urls:
        if "amazon" in url or "amzn" in url:
            affiliate_url = f"{url}&tag={AMAZON_TAG}" if "?" in url else f"{url}?tag={AMAZON_TAG}"
            await update.message.reply_text(f"🛒 **Affiliate Link:**\n{affiliate_url}")

if __name__ == '__main__':
    keep_alive()  # Web server स्टार्ट करें
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, convert_link))
    app.run_polling()
    

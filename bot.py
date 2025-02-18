# bot.py
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from downloader import download_video
from telegram import InputFile
import os
from config import BOT_TOKEN, DOWNLOAD_FOLDER

def start(update: Update, context):
    update.message.reply_text("Welcome to YouTube Video Downloader Bot! Send me a YouTube video link.")

def handle_message(update: Update, context):
    url = update.message.text
    if "youtube.com" in url:
        update.message.reply_text("Starting download...")
        
        # Download the video
        download_success = download_video(url, DOWNLOAD_FOLDER)
        
        if download_success:
            # Send the downloaded video to the user
            video_file = os.path.join(DOWNLOAD_FOLDER, url.split('=')[-1] + '.mp4')
            update.message.reply_text("Video downloaded! Uploading now...")
            with open(video_file, 'rb') as video:
                update.message.reply_video(video, caption="Here is your video!")
            # Optionally, delete the file after sending it
            os.remove(video_file)
        else:
            update.message.reply_text("Sorry, there was an error while downloading the video.")
    else:
        update.message.reply_text("Please send a valid YouTube link.")

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
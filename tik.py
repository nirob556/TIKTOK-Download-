import telebot
import yt_dlp
import os
import time
import random
import string
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = "7510635174:AAH5IS7L2RqVFvtagLZwkCUgB9v4QNUV7BU"
CHANNEL_USERNAME = "@SPEED_X_OFFICIAL"
OWNER_ID = 7224513731 # আপনার আইডি

# নতুন গ্রুপ আইডি এবং লিংক
LOG_CHANNEL_ID = -1002780174909
LOG_CHANNEL_LINK = "https://t.me/TIKTOK_7272272"

bot = telebot.TeleBot(BOT_TOKEN)
users = {} # সকল ব্যবহারকারীকে ট্র্যাক করতে
user_videos = {} # ব্যবহারকারীর ডাউনলোড হিস্টরি ট্র্যাক করতে

loading_texts = [
    "🚀 𝐋𝐎𝐀𝐃𝐈𝐍𝐆...\n[█▒▒▒▒▒▒▒▒▒▒] 10%",
    "🚀 𝐋𝐎𝐀𝐃𝐈𝐍𝐆...\n[███▒▒▒▒▒▒▒▒] 30%",
    "🚀 𝐋𝐎𝐀𝐃𝐈𝐍𝐆...\n[██████▒▒▒▒▒] 60%",
    "🚀 𝐋𝐎𝐀𝐃𝐈𝐍𝐆...\n[██████████▒] 90%",
    "🥹 𝗣𝗟𝗘𝗔𝗦𝗘 𝗪𝗔𝗜𝗧...........⏳"
]

def send_loading(chat_id, initial_message="🚀 𝐋𝐎𝐀𝐃𝐈𝐍𝐆..."):
    msg = bot.send_message(chat_id, initial_message, parse_mode="HTML")
    for text in loading_texts[1:]:
        time.sleep(1)
        try:
            bot.edit_message_text(text, chat_id, msg.message_id, parse_mode="HTML")
        except:
            break
    return msg

def download_tiktok(url, outtmpl='result.%(ext)s'):
    ydl_opts = {
        'outtmpl': outtmpl,
        'quiet': True,
        'noplaylist': True,
        'merge_output_format': 'mp4',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return info

def download_youtube_video(url, outtmpl='youtube_video.%(ext)s'):
    # ইউটিউব ডাউনলোডের জন্য অতিরিক্ত অপশন যোগ করা হয়েছে
    ydl_opts = {
        'outtmpl': outtmpl,
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'quiet': True,
        'noplaylist': True,
        'merge_output_format': 'mp4',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
        # নিচে YouTube এর বটের সমস্যা এড়ানোর জন্য কিছু অতিরিক্ত অপশন যোগ করা হলো:
        'no_check_certificate': True,
        'referer': 'https://www.youtube.com/',
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return info

def random_string(length=8):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

START_TEXT = """
👑 𝐖𝐄𝐋𝐂𝐎𝐌𝐄 𝐓𝐎 𝐒𝐏𝐄𝐄𝐃_𝐗 𝐕𝐈𝐏 𝐁𝐎𝐓 👑

🚀 𝐓𝐢𝐤𝐓𝐨𝐤 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 | 𝐄𝐱𝐭𝐫𝐚𝐜𝐭 𝐌𝐏𝟑 | 𝐘𝐨𝐮𝐓𝐮𝐛𝐞 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫

🔗 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬:

🎬 <b>/link TikTok_URL</b>  
  ➔ 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐓𝐢𝐤𝐓𝐨𝐤 𝐕𝐈𝐃𝐄𝐎/𝐏𝐇𝐎𝐓𝐎 (𝐇𝐃)

🎵 <b>/linkmp3 TikTok_URL</b>  
  ➔ 𝐄𝐱𝐭𝐫𝐚𝐜𝐭 𝐇𝐢𝐠𝐡 𝐐𝐮𝐚𝐥𝐢𝐭𝐲 𝐌𝐏𝟑

🎧 <b>/mp3 TikTok_URL</b>  
  ➔ 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐚𝐮𝐝𝐢𝐨 𝐚𝐧𝐝 𝐬𝐚𝐯𝐞 𝐰𝐢𝐭𝐡 𝐫𝐚𝐧𝐝𝐨𝐦 𝐧𝐚𝐦𝐞


⚡ 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲: SPEED_X  
📞 𝐂𝐨𝐧𝐭𝐚𝐜𝐭: @NIROB_BBZ

🚫 𝐉𝐨𝐢𝐧 𝐕𝐈𝐏 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐅𝐢𝐫𝐬𝐭!
"""

SAVE_GUIDE_TEXT = """
✅ 𝐇𝐎𝐖 𝐓𝐎 𝐒𝐀𝐕𝐄 𝐓𝐇𝐄 𝐅𝐈𝐋𝐄?

1️⃣ 𝐎𝐩𝐞𝐧 𝐭𝐡𝐞 𝐕𝐢𝐝𝐞𝐨/𝐏𝐡𝐨𝐭𝐨 𝐢𝐧 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦  
2️⃣ 𝐓𝐚𝐩 𝐭𝐡𝐞 𝐓𝐡𝐫𝐞𝐞 𝐃𝐨𝐭𝐬 (...)  
3️⃣ 𝐒𝐞𝐥𝐞𝐜𝐭 "𝐒𝐚𝐯𝐞 𝐭𝐨 𝐆𝐚𝐥𝐥𝐞𝐫𝐲"
"""

@bot.message_handler(commands=['start'])
def start(message):
    users[message.from_user.id] = message.from_user
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton("📢 𝐉𝐎𝐈𝐍 𝐕𝐈𝐏 𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=f"https://t.me/{CHANNEL_USERNAME.strip('@')}"),
        InlineKeyboardButton("✅ 𝐕𝐄𝐑𝐈𝐅𝐘 𝐀𝐂𝐂𝐄𝐒𝐒", callback_data="verify")
    )
    bot.send_message(message.chat.id, START_TEXT, reply_markup=markup, parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data == "verify")
def verify(call):
    try:
        member = bot.get_chat_member(CHANNEL_USERNAME, call.from_user.id)
        if member.status in ["member", "administrator", "creator"]:
            # ভেরিফাই সফল হলে সকল কমান্ডের তালিকা দেখানো হবে
            bot.edit_message_text(
                "✅ <b>𝐕𝐄𝐑𝐈𝐅𝐈𝐄𝐃!</b>\n" + START_TEXT, # START_TEXT যোগ করা হয়েছে
                call.message.chat.id,
                call.message.message_id,
                parse_mode="HTML"
            )
        else:
            bot.answer_callback_query(call.id, "❌ 𝐉𝐨𝐢𝐧 𝐕𝐈𝐏 𝐜𝐡𝐚𝐧𝐧𝐞𝐥 𝐟𝐢𝐫𝐬𝐭!", show_alert=True)
    except Exception as e:
        bot.answer_callback_query(call.id, f"❌ 𝐕𝐞𝐫𝐢𝐟𝐢𝐜𝐚𝐭𝐢𝐨𝐧 𝐅𝐚𝐢𝐥𝐞𝐝! {e}", show_alert=True)


@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id, START_TEXT, parse_mode="HTML")

@bot.message_handler(commands=['link'])
def link(message):
    user_id = message.from_user.id
    current_user = message.from_user
    users[user_id] = current_user

    try:
        url = message.text.split(" ", 1)[1].strip()
    except:
        bot.reply_to(message, "❌ <b>Usage:</b>\n/link TikTok_URL", parse_mode="HTML")
        return

    loading_msg = send_loading(message.chat.id)

    try:
        info = download_tiktok(url)
        ext = info.get('ext', 'mp4')
        file_name = f"result.{ext}"

        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("💾 𝐒𝐀𝐕𝐄 𝐓𝐎 𝐆𝐀𝐋𝐋𝐄𝐑𝐘", callback_data=f"save_{user_id}"))

        caption_text = f"🎬 <b>𝐕𝐈𝐏 𝐕𝐢𝐝𝐞𝐨 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐝</b>\n<b>𝐁𝐲 𝐒𝐏𝐄𝐄𝐃_𝐗</b>\n@NIROB_BBZ\n\n" \
                       f"👤 <b>𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐝 𝐁𝐲:</b> <a href='tg://user?id={current_user.id}'>{current_user.first_name}</a>\n" \
                       f"🆔 <b>𝐔𝐬𝐞𝐫 𝐈𝐃:</b> <code>{current_user.id}</code>\n" \
                       f"🔗 <b>𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞:</b> @{current_user.username if current_user.username else 'N/A'}"

        if info.get('duration', 0) <= 2 or info.get('_type') == 'image' or info.get('extractor_key') == 'TikTokImage':
            bot.send_photo(message.chat.id, open(file_name, 'rb'),
                caption="🖼️ <b>𝐕𝐈𝐏 𝐏𝐡𝐨𝐭𝐨 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐝</b>\n<b>𝐁𝐲 𝐒𝐏𝐄𝐄𝐃_𝐗</b>\n@NIROB_BBZ",
                reply_markup=markup,
                parse_mode="HTML")
            # গ্রুপে ফরোয়ার্ড
            bot.send_photo(LOG_CHANNEL_ID, open(file_name, 'rb'),
                           caption=caption_text, parse_mode="HTML") # disable_web_page_preview সরানো হয়েছে
        else:
            bot.send_video(message.chat.id, open(file_name, 'rb'),
                caption="🎬 <b>𝐕𝐈𝐏 𝐕𝐢𝐝𝐞𝐨 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐝</b>\n<b>𝐁𝐲 𝐒𝐏𝐄𝐄𝐃_𝐗</b>\n@NIROB_BBZ",
                reply_markup=markup,
                parse_mode="HTML")
            # গ্রুপে ফরোয়ার্ড
            bot.send_video(LOG_CHANNEL_ID, open(file_name, 'rb'),
                           caption=caption_text, parse_mode="HTML") # disable_web_page_preview সরানো হয়েছে

        user_videos.setdefault(user_id, []).append(url)
        os.remove(file_name)

    except Exception as e:
        bot.send_message(message.chat.id, f"❌ <b>𝐄𝐫𝐫𝐨𝐫:</b>\n{e}", parse_mode="HTML")

    try:
        bot.delete_message(message.chat.id, loading_msg.message_id)
    except:
        pass

@bot.message_handler(commands=['ytlink'])
def ytlink(message):
    user_id = message.from_user.id
    current_user = message.from_user
    users[user_id] = current_user

    try:
        url = message.text.split(" ", 1)[1].strip()
    except:
        bot.reply_to(message, "❌ <b>Usage:</b>\n/ytlink YouTube_URL", parse_mode="HTML")
        return

    initial_loading_message = "⏳ <b>𝐘𝐨𝐮𝐓𝐮𝐛𝐞 𝐕𝐢𝐝𝐞𝐨 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠 𝐒𝐭𝐚𝐫𝐭𝐞𝐝...</b>\n" \
                              "<i>𝐓𝐡𝐢𝐬 𝐦𝐚𝐲 𝐭𝐚𝐤𝐞 𝐬𝐨𝐦𝐞 𝐭𝐢𝐦𝐞 𝐝𝐞𝐩𝐞𝐧𝐝𝐢𝐧𝐠 𝐨𝐧 𝐯𝐢𝐝𝐞𝐨 𝐬𝐢𝐳𝐞 𝐚𝐧𝐝 𝐧𝐞𝐭𝐰𝐨𝐫𝐤 𝐬𝐩𝐞𝐞𝐝.</i>"
    loading_msg = send_loading(message.chat.id, initial_loading_message)

    try:
        file_name_prefix = "youtube_video"
        info = download_youtube_video(url, outtmpl=file_name_prefix)

        downloaded_file = None
        for f in os.listdir('.'):
            if f.startswith(file_name_prefix) and (f.endswith(".mp4") or f.endswith(".webm")):
                downloaded_file = f
                break

        if not downloaded_file:
            raise Exception("Downloaded file not found or unsupported format.")

        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("💾 𝐒𝐀𝐕𝐄 𝐓𝐎 𝐆𝐀𝐋𝐋𝐄𝐑𝐘", callback_data=f"save_{user_id}"))

        caption_text = f"▶️ <b>𝐘𝐨𝐮𝐓𝐮𝐛𝐞 𝐕𝐈𝐏 𝐕𝐢𝐝𝐞𝐨 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐝</b>\n<b>𝐁𝐲 𝐒𝐏𝐄𝐄𝐃_𝐗</b>\n@NIROB_BBZ\n\n" \
                       f"👤 <b>𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐝 𝐁𝐲:</b> <a href='tg://user?id={current_user.id}'>{current_user.first_name}</a>\n" \
                       f"🆔 <b>𝐔𝐬𝐞𝐫 𝐈𝐃:</b> <code>{current_user.id}</code>\n" \
                       f"🔗 <b>𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞:</b> @{current_user.username if current_user.username else 'N/A'}"

        bot.send_video(message.chat.id, open(downloaded_file, 'rb'),
                       caption=caption_text,
                       reply_markup=markup,
                       parse_mode="HTML")

        # গ্রুপে ফরোয়ার্ড করা
        bot.send_video(LOG_CHANNEL_ID, open(downloaded_file, 'rb'),
                       caption=caption_text,
                       parse_mode="HTML") # disable_web_page_preview সরানো হয়েছে

        user_videos.setdefault(user_id, []).append(url)
        os.remove(downloaded_file)

    except Exception as e:
        bot.send_message(message.chat.id, f"❌ <b>𝐄𝐫𝐫𝐨𝐫 𝐝𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠 𝐘𝐨𝐮𝐓𝐮𝐛𝐞 𝐯𝐢𝐝𝐞𝐨:</b>\n{e}", parse_mode="HTML")

    try:
        bot.delete_message(message.chat.id, loading_msg.message_id)
    except:
        pass


@bot.callback_query_handler(func=lambda call: call.data.startswith("save_"))
def save_gallery(call):
    bot.answer_callback_query(call.id, "✅ 𝐒𝐚𝐯𝐞 𝐆𝐮𝐢𝐝𝐞 𝐒𝐞𝐧𝐭!", show_alert=True)
    bot.send_message(call.message.chat.id, SAVE_GUIDE_TEXT, parse_mode="HTML")

@bot.message_handler(commands=['linkmp3'])
def linkmp3(message):
    user_id = message.from_user.id
    current_user = message.from_user
    users[user_id] = current_user

    try:
        url = message.text.split(" ", 1)[1].strip()
    except:
        bot.reply_to(message, "❌ <b>Usage:</b>\n/linkmp3 TikTok_URL", parse_mode="HTML")
        return

    loading_msg = send_loading(message.chat.id)

    try:
        ydl_opts = {
            'format': 'mp4',
            'outtmpl': 'result.%(ext)s',
            'quiet': True,
            'noplaylist': True,
            'merge_output_format': 'mp4',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        os.system("ffmpeg -i result.mp4 -vn -ab 192k -ar 44100 -y audio.mp3")

        caption_text = f"🎵 <b>𝐕𝐈𝐏 𝐌𝐏𝟑 𝐅𝐢𝐥𝐞</b>\n<b>𝐁𝐲 𝐒𝐏𝐄𝐄𝐃_𝐗</b>\n@NIROB_BBZ\n\n" \
                       f"👤 <b>𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐝 𝐁𝐲:</b> <a href='tg://user?id={current_user.id}'>{current_user.first_name}</a>\n" \
                       f"🆔 <b>𝐔𝐬𝐞𝐫 𝐈𝐃:</b> <code>{current_user.id}</code>\n" \
                       f"🔗 <b>𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞:</b> @{current_user.username if current_user.username else 'N/A'}"

        bot.send_document(message.chat.id, open('audio.mp3', 'rb'),
            caption="🎵 <b>𝐕𝐈𝐏 𝐌𝐏𝟑 𝐅𝐢𝐥𝐞</b>\n<b>𝐁𝐲 𝐒𝐏𝐄𝐄𝐃_𝐗</b>\n@NIROB_BBZ",
            parse_mode="HTML")
        # গ্রুপে ফরোয়ার্ড
        bot.send_document(LOG_CHANNEL_ID, open('audio.mp3', 'rb'),
                          caption=caption_text, parse_mode="HTML") # disable_web_page_preview সরানো হয়েছে

        os.remove('audio.mp3')
        os.remove('result.mp4')
        user_videos.setdefault(user_id, []).append(url)

    except Exception as e:
        bot.send_message(message.chat.id, f"❌ <b>𝐂𝐨𝐧𝐯𝐞𝐫𝐬𝐢𝐨𝐧 𝐄𝐫𝐫𝐨𝐫:</b>\n{e}", parse_mode="HTML")

    try:
        bot.delete_message(message.chat.id, loading_msg.message_id)
    except:
        pass

@bot.message_handler(commands=['mp3'])
def mp3_handler(message):
    user_id = message.from_user.id
    current_user = message.from_user
    users[user_id] = current_user

    try:
        url = message.text.split(" ", 1)[1].strip()
    except:
        bot.reply_to(message, "❌ <b>Usage:</b>\n/mp3 TikTok_URL", parse_mode="HTML")
        return

    loading_msg = send_loading(message.chat.id)

    random_name = random_string(10) + ".mp3"

    try:
        ydl_opts = {
            'format': 'mp4',
            'outtmpl': 'temp_video.%(ext)s',
            'quiet': True,
            'noplaylist': True,
            'merge_output_format': 'mp4',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        os.system(f"ffmpeg -i temp_video.mp4 -vn -ab 192k -ar 44100 -y {random_name}")

        caption_text = f"🎵 <b>𝐕𝐈𝐏 𝐌𝐏𝟑 𝐖𝐢𝐭𝐡 𝐑𝐚𝐧𝐝𝐨𝐦 𝐍𝐚𝐦𝐞</b>\n<b>𝐁𝐲 𝐒𝐏𝐄𝐄𝐃_𝐗</b>\n@NIROB_BBZ\n\n" \
                       f"👤 <b>𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐝 𝐁𝐲:</b> <a href='tg://user?id={current_user.id}'>{current_user.first_name}</a>\n" \
                       f"🆔 <b>𝐔𝐬𝐞𝐫 𝐈𝐃:</b> <code>{current_user.id}</code>\n" \
                       f"🔗 <b>𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞:</b> @{current_user.username if current_user.username else 'N/A'}"

        with open(random_name, 'rb') as audio_file:
            bot.send_document(message.chat.id, audio_file,
                caption=f"🎵 <b>𝐕𝐈𝐏 𝐌𝐏𝟑 𝐖𝐢𝐭𝐡 𝐑𝐚𝐧𝐝𝐨𝐦 𝐍𝐚𝐦𝐞</b>\n<b>𝐁𝐲 𝐒𝐏𝐄𝐄𝐃_𝐗</b>\n@NIROB_BBZ",
                parse_mode="HTML")
            # গ্রুপে ফরোয়ার্ড
            bot.send_document(LOG_CHANNEL_ID, open(random_name, 'rb'),
                              caption=caption_text, parse_mode="HTML") # disable_web_page_preview সরানো হয়েছে

        os.remove(random_name)
        os.remove('temp_video.mp4')
        user_videos.setdefault(user_id, []).append(url)

    except Exception as e:
        bot.send_message(message.chat.id, f"❌ <b>𝐂𝐨𝐧𝐯𝐞𝐫𝐬𝐢𝐨𝐧 𝐄𝐫𝐫𝐨𝐫:</b>\n{e}", parse_mode="HTML")

    try:
        bot.delete_message(message.chat.id, loading_msg.message_id)
    except:
        pass

@bot.message_handler(commands=['botuser'])
def botuser(message):
    if message.from_user.id != OWNER_ID:
        bot.reply_to(message, "❌ <b>𝐎𝐰𝐧𝐞𝐫 𝐎𝐧𝐥𝐲!</b>", parse_mode="HTML")
        return

    text = f"<b>👥 𝐓𝐨𝐭𝐚𝐥 𝐔𝐬𝐞𝐫𝐬:</b> {len(users)}\n\n"
    for user in users.values():
        text += f"""
<b>👤 𝐍𝐚𝐦𝐞:</b> {user.first_name}
<b>🆔 𝐈𝐃:</b> {user.id}
<b>🔗 𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞:</b> @{user.username if user.username else 'None'}
<b>🌐 𝐏𝐫𝐨𝐟𝐢𝐥𝐞:</b> <a href="tg://user?id={user.id}">𝐂𝐥𝐢𝐜𝐤</a>
------------------------------
"""
    bot.send_message(message.chat.id, text, parse_mode="HTML", disable_web_page_preview=True)

@bot.message_handler(commands=['bot_user_video'])
def user_video_list(message):
    if message.from_user.id != OWNER_ID:
        bot.reply_to(message, "❌ <b>𝐎𝐰𝐧𝐞𝐫 𝐎𝐧𝐥𝐲!</b>", parse_mode="HTML")
        return

    text = "<b>📥 𝐔𝐬𝐞𝐫 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐇𝐢𝐬𝐭𝐨𝐫𝐲:</b>\n\n"
    if not user_videos:
        text += "No download history available yet."
    else:
        for uid, links in user_videos.items():
            user_info = users.get(uid)
            if user_info:
                text += f"<b>👤 𝐔𝐬𝐞𝐫:</b> {user_info.first_name} (ID: <code>{uid}</code>)\n"
            else:
                text += f"<b>👤 𝐔𝐬𝐞𝐫 ID:</b> <code>{uid}</code> (Unknown User)\n"
            for i, link in enumerate(links):
                text += f"  {i+1}. 🔗 {link}\n"
            text += "--------------------------\n"

    bot.send_message(message.chat.id, text, parse_mode="HTML", disable_web_page_preview=True)


@bot.message_handler(commands=['n'])
def broadcast_message(message):
    if message.from_user.id != OWNER_ID:
        bot.reply_to(message, "❌ <b>𝐎𝐰𝐧𝐞𝐫 𝐎𝐧𝐥𝐲!</b>", parse_mode="HTML")
        return

    try:
        broadcast_text = message.text.split(" ", 1)[1].strip()
    except IndexError:
        bot.reply_to(message, "❌ <b>Usage:</b>\n/n Your message here", parse_mode="HTML")
        return

    sent_count = 0
    failed_count = 0
    for user_id in users:
        try:
            bot.send_message(user_id, broadcast_text, parse_mode="HTML")
            sent_count += 1
            time.sleep(0.1) # যাতে API লিমিট অতিক্রম না হয়
        except Exception as e:
            print(f"Failed to send message to user {user_id}: {e}")
            failed_count += 1
            # যদি ব্যবহারকারী বট ব্লক করে তাহলে তাকে users ডিকশনারি থেকে সরানো
            if "blocked" in str(e).lower() or "deactivated" in str(e).lower():
                if user_id in users:
                    del users[user_id]
                    if user_id in user_videos:
                        del user_videos[user_id]


    bot.reply_to(message, f"✅ <b>𝐁𝐫𝐨𝐚𝐝𝐜𝐚𝐬𝐭 𝐂𝐨𝐦𝐩𝐥𝐞𝐭𝐞𝐝!</b>\n"
                          f"<b>𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 𝐬𝐞𝐧𝐭 𝐭𝐨:</b> {sent_count} 𝐮𝐬𝐞𝐫𝐬.\n"
                          f"<b>𝐅𝐚𝐢𝐥𝐞𝐝 𝐭𝐨 𝐬𝐞𝐧𝐝 𝐭𝐨:</b> {failed_count} 𝐮𝐬𝐞𝐫𝐬.",
                          parse_mode="HTML")


# 🔥 এইখানে বট রান করানোর জন্য ফাইনাল লাইন 🔥
if __name__ == "__main__":
    print("🤖 SPEED_X VIP BOT STARTED...")
    bot.infinity_polling()

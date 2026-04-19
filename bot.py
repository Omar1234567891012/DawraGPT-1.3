import telebot
from openai import OpenAI

# 🔑 HIER DEINE TOKENS EINTRAGEN
TELEGRAM_TOKEN = "DEIN_TELEGRAM_TOKEN"
OPENAI_API_KEY = "DEIN_OPENAI_API_KEY"

bot = telebot.TeleBot(TELEGRAM_TOKEN)
client = OpenAI(api_key=OPENAI_API_KEY)

# 🕌 Start-Befehl
@bot.message_handler(commands=['start'])
def start(message):Hallo
    bot.reply_to(message, "🕌 Assalamu Alaikum! Ich bin dein Bot 🤖")

# 💬 Chat-Funktion
@bot.message_handler(func=lambda message: True)
def chat(message):
    user_text = message.text

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Du bist ein freundlicher islamischer Assistent. Antworte kurz, respektvoll und korrekt."},
            {"role": "user", "content": user_text}
        ]
    )

    bot.reply_to(message, response.choices[0].message.content)

print("Bot läuft...")
bot.polling()

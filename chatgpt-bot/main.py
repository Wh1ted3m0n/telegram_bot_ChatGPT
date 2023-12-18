import telebot
import openai

TOKEN = "" #api_keys
openai.api_key = ""

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.chat.id, "Привет я ChatGPT БОТ")

@bot.message_handler(content_types=['text'])
def main(message):
    reply = ''
    prompt = message.text
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        temperature=0.7,
        n=1,
        stop=None
    )
    if response and response.choices:
        reply = response.choices[0].text.strip()
    else:
        reply = "ой щось не так"
    bot.send_message(message.chat.id, reply)

bot.polling(none_stop=True)

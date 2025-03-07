from flask import Flask
import random
import string
import os
from telegram import Bot

app = Flask(__name__)

TOKEN = os.getenv("7860293663:AAF59dEj8t_p02f4gBctonWlIYwIzFudA_I")
ADMIN_ID = os.getenv("6680027477")
bot = Bot(token=TOKEN)

def generate_key():
    return "\n".join(["".join(random.choices(string.ascii_letters + string.digits, k=10)) for _ in range(10)])

@app.route("/generate-id")
def generate_id():
    user_id = str(random.randint(100000, 999999))  # Simulating user ID
    key = generate_key()
    
    # Send key to admin for approval
    bot.send_message(
        chat_id=ADMIN_ID,
        text=f"New key request:\nUser ID: {user_id}\nKey:\n{key}"
    )
    
    return user_id

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

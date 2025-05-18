import requests

TOKEN = "7506795414:AAG0hcynX6EbWT_X1LGu1fMmXTzM6MS1XNM"
WEBAPP_URL = "https://username.github.io/telegram-miniapp/index.html"

menu_data = {
    "menu_button": {
        "type": "web_app",
        "text": "Buka Mini App",
        "web_app": {
            "url": WEBAPP_URL
        }
    }
}

resp = requests.post(
    f"https://api.telegram.org/bot{TOKEN}/setChatMenuButton",
    json=menu_data
)

print(resp.json())


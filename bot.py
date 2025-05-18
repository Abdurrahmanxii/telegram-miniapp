import requests

TOKEN = "Your token bot"
WEBAPP_URL = "https://username.github.io/your bot/index.html"

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


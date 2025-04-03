
import time
import requests

def keep_alive():
    while True:
        try:
            requests.get("https://your-koyeb-app-url")
        except Exception as e:
            print("Ping failed:", e)
        time.sleep(60)  # Ping every 10 minutes

if __name__ == "__main__":
    keep_alive()

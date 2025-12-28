from flask import Flask
import os
import time

app = Flask(__name__)

@app.route('/')
def hello():
    return "Merhaba! Bu v2 versiyonu.", 200


print("Uygulama baslatiliyor... Konfigurasyonlar yukleniyor...")

print("KRITIK HATA: Veritabani baglantisi kurulamadi! (Timeout)")

raise Exception("FATAL ERROR: Database Connection Failed in deployment v2")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
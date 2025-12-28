from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    # Burası şu an düzgün çalışıyor
    return "Merhaba! EKS uzerinde Calisan v1 Uygulamasi. Her sey yolunda!", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
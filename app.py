from flask import Flask
import os

app = Flask(__name__)

@app.get("/")
def home():
    version = os.getenv("APP_VERSION", "1.0")
    return f"""
    <html>
      <head><title>My CI/CD Demo</title></head>
      <body style="font-family:Arial;max-width:650px;margin:60px auto;">
        <h1>Hello from my Ubuntu Docker server!</h1>
        <p>My first CI/CD pipeline is working.</p>
        <p>Application version: <strong>{version}</strong></p>
      </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

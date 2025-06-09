from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Hello from Cloud Run — Flask is working!"

if __name__ == "__main__":
    # Cloud Run provides PORT as env variable
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

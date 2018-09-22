import os
from flask import Flask

app = Flask(__name__)

@app.route("/.well-known/acme-challenge/5FeEE1UbWyWz9kUbsd640n7Ir9y1f8k2N6yxwAYbMnk")
def hello():
    return "5FeEE1UbWyWz9kUbsd640n7Ir9y1f8k2N6yxwAYbMnk.0PJTmSXcBn1hGck1NEMfzicOGKIdXuyTRMIJRzMzZIk"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

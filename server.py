import os
from flask import Flask

app = Flask(__name__)

@app.route("/zJAKRyrETz1k5CtjUjCsz59XshihdxkEZGKD_9owNw8")
# e.g. /.well-known/acme-challenge/lzrajCaq8vbw5Qz2o_XXXXXXXXXXXXXXXXX
def hello():
    return"zJAKRyrETz1k5CtjUjCsz59XshihdxkEZGKD_9owNw8.0PJTmSXcBn1hGck1NEMfzicOGKIdXuyTRMIJRzMzZIk"
    # e.g. return "lzrajCaq8vbw5Qz2o_XXXXXXXXXXXXXXXXXXz4RnfWtLKaIc6EdhsOsr4fb6RFZuUoabZW5dPW36cmc"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

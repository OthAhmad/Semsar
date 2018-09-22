import os
from flask import Flask

app = Flask(__name__)

@app.route("/.well-known/acme-challenge/6ghOsV23Vn_cfP8G9dOILam1gIGit_QifPB-HegvPQI")
# e.g. /.well-known/acme-challenge/lzrajCaq8vbw5Qz2o_XXXXXXXXXXXXXXXXX
def hello():
    return"6ghOsV23Vn_cfP8G9dOILam1gIGit_QifPB-HegvPQI.0PJTmSXcBn1hGck1NEMfzicOGKIdXuyTRMIJRzMzZIk"
    # e.g. return "lzrajCaq8vbw5Qz2o_XXXXXXXXXXXXXXXXXXz4RnfWtLKaIc6EdhsOsr4fb6RFZuUoabZW5dPW36cmc"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

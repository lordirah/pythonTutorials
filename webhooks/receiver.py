from flask import Flask, abort, request

app = Flask(__name__)


@app.route("/webhook", methods=["POST"])
def webhook():
    if request.method == "POST":
        print(request.json)
        return "success", 200
    else:
        abort(400)


if __name__ == "__main__":
    app.run()

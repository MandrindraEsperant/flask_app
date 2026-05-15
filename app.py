#!/usr/bin/env python3

from flask import Flask # type: ignore

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def hello_world():
    return {"message": "Hello World!"}, 200


@app.route("/hello/<string:username>")
def hello_user(username: str):
    return {"message": f"Hello {username}!"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
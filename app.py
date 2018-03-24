#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-24 20:35:34
# @Author  : andyhuzhill (andyhuzhill@gmail.com)
# @Link    : link
# @Version : 1.0.0

from flask import Flask, request

app = Flask(__name__)

from send_mail import *


@app.route("/", methods=["POST"])
def index_post():
    email = request.json["entry"]["field_2"]
    print("email = ", email)
    return ("email = " + str(request.json["entry"]["field_2"]))


if __name__ == "__main__":
    app.run(debug=True)


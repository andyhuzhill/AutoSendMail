#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-24 20:35:34
# @Author  : andyhuzhill (andyhuzhill@gmail.com)
# @Link    : link
# @Version : 1.0.0

from flask import Flask, request, make_response, render_template, url_for, redirect

app = Flask(__name__)

from send_mail import send_mail


@app.route("/<string:job>", methods=["POST"])
def index_post(job):
    print("job = ", job)
    email = request.json["entry"]["field_2"]
    print("email = ", email)
    
    return ("email = " + str(request.json["entry"]["field_2"]))


@app.route("/", methods=["GET"])
def index_get(job = None):
    if job is not None:
        print("job = ", job)
    return render_template("index.html")


@app.route("/setting", methods=["GET", "POST"])
def setting():
    if request.method == "GET":
        return render_template("setting.html")
    else:
        return make_response("Ok", 200)


if __name__ == "__main__":
    app.run(debug=True)


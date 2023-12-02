# from flask import Flask,request

# def addition(a,b)->int:
#     return a+b
# addition(3,2)
# """now ww have to call these function from any system"""
# app = Flask(__name__)

# @app.route("/home")
# def hom_page():
#     return f"Home page"
# @app.route("/sub")
# def substraction()->int:
#     """is return substration """
#     return 10+5
# @app.route("/name")
# def print_name():
#     data = request.args.get('name')
#     return f"Hello {data}"
# if __name__ == "__main__":
#     app.run(host="0.0.0.0")


import os

import os.path



print(os.path.dirname("templates"))

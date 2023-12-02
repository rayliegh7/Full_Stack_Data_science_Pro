from flask import Flask, render_template,jsonify,request
import os 

app = Flask(__name__)

# Define the route for the home page
@app.route("/")
def show_page():
    return render_template("Resources/api_21th_oct/templates/index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
 
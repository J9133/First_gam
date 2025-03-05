from flask import Flask, render_template, request
from random import uniform

app = Flask(__name__)

p_h = "hi"

@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def home():
    
    p_h = "hi"
  #  if request.method == "POST":
    #     p_h =  request.form.get("I")
         
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
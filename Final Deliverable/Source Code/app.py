from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def getHomePage():
    return render_template("Chatbot.html")


app.run(debug=True)
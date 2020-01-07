from flask import Flask , render_template , redirect 

app = Flask(__name__)

@app.route("/")
def home():
    # return("Hello World")
    return render_template("index.html")

if __name__ == "__main__" :
    app.run()
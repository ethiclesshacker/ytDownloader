from flask import Flask , render_template , redirect , url_for , request, send_file
import ytDownloader

app = Flask(__name__)

@app.route("/",methods=["POST","GET"])
def home():
    if(request.method=="POST"):
        link = request.form["link"]
        downloadLink = ytDownloader.getFile(link)
        return render_template("index.html",downloadLink = downloadLink)

    return render_template("index.html",downloadLink = '/')


if __name__ == "__main__" :
    app.run(debug=True)
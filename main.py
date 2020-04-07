from flask import Flask , render_template , redirect , url_for , request, send_file
from yt import Youtube

app = Flask(__name__)

@app.route("/",methods=["POST","GET"])
def home():
    if(request.method=="POST"):
        link = request.form["link"]
        YT = Youtube(link)
        downloadLinks = YT.getLinks()
        titles = downloadLinks.keys()
        links = downloadLinks.values()
        print("links = ",links)
        print("titles = ",titles)
        return render_template("index.html",len=len(links),links=list(links),titles=list(titles))

    return render_template("index.html",len=0)


if __name__ == "__main__" :
    app.run()
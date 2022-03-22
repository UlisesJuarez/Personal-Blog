from pdb import post_mortem
from flask import Flask,render_template
import requests

post=requests.get("https://api.npoint.io/65036dfcf8a72fc447aa").json()

app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
    print(post)
    for i in post:
        print(i)
    return render_template('index.html',all_posts=post)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(port=5000,debug=True)
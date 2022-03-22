from pdb import post_mortem
from flask import Flask,render_template
import requests

posts=requests.get("https://api.npoint.io/65036dfcf8a72fc447aa").json()

app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
    return render_template('index.html',all_posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<int:index>")
def post(index):
    identifier = None
    for blog_post in posts:
        if blog_post["id"] == index:
            identifier = blog_post
    return render_template("post.html", post=identifier)

if __name__ == '__main__':
    app.run(port=5000,debug=True)
from flask import Flask , render_template,url_for,request

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/news")
def news():
    return render_template("news.html")

@app.route("/program")
def program():
    return render_template("program.html")

@app.route("/resources")
def resources():
    return render_template("resources.html")

@app.route("/sdgs")
def sdgs():
    return render_template("sdgs.html")

@app.route("/usercontact" , methods=["GET","POST"])
def usercontact():
    if request.method=="POST":
        name=request.form["name"]
        email=request.form["email"]
        message=request.form["message"]
    contact_details=[name, email, message]
    return contact_details    
    
if __name__=="__main__":
    app.run(debug=True)
   
    
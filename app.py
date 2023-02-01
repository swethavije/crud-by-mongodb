from flask import Flask,render_template,request,url_for,redirect
from pymongo import MongoClient


app=Flask(__name__)


client=MongoClient("mongodb://127.0.0.1:27017")
@app.route("/",methods=["POST","GET"])
def display():
    client=MongoClient("mongodb://127.0.0.1:27017")
    database=client.curd
    collection=database.userdata
    result=collection.find()
    a=[]
    for i in result:
        a.append(i)
    client.close()
    return render_template("index.html",data=a)


@app.route("/add",methods=["POST","GET"])
def add():
    client=MongoClient("mongodb://127.0.0.1:27017")
    if request.form.get("id")!=None:
        id=request.form.get("id")
        name=request.form.get("name")
        language=request.form.get("language")
        skill=request.form.get("skill")
        database=client.curd
        collection=database.userdata
        collection.insert_one({
            "id":id,
            "name":name,
            "language":language,
            "skill":skill
        })
        print("inserted")
        client.close()
        return redirect(url_for("display"))
    return render_template("add.html")


@app.route("/edit/<id>",methods=["POST","GET"])
def edit(id):
    client=MongoClient("mongodb://127.0.0.1:27017")
    if request.form.get("id")!=None:
        id=request.form.get("id")
        name=request.form.get("name")
        language=request.form.get("language")
        skill=request.form.get("skill")
        client=MongoClient("mongodb://127.0.0.1:27017")
        database=client.curd
        collection=database.userdata
        collection.update_one({"id": id}, {"$set": {"name": name, "language": language,"skill":skill}})
        client.close()
        return redirect(url_for("display"))
    
    client=MongoClient("mongodb://127.0.0.1:27017")
    database=client.curd
    collection=database.userdata
    x=collection.find_one({"id":id})
    dic={"id":x.get("id"),"name":x.get("name"),"language":x.get("language"),"skill":x.get("skill")}
    client.close()
    return render_template("edit.html",data=dic)


@app.route("/delete/<id>")
def delete(id):
    client=MongoClient("mongodb://127.0.0.1:27017")
    database=client.curd
    collection=database.userdata
    collection.delete_one({"id":id})
    client.close()
    return redirect(url_for("display"))

if __name__=="__main__":
    app.run(debug=True)
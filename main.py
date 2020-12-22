from flask import Flask , render_template ,request , redirect , url_for
from flask import Flask, jsonify
import json
from  flask_restful import Api,Resource
import  pymysql


app = Flask(__name__)
conn = pymysql.connect('localhost','root','','db_work')

url = 'http://127.0.0.1:5000/test'

@app.route("/")
def showData():
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM people")
        rows = cur.fetchall()
        return render_template('index.html',datas=rows)

@app.route("/test")
def showData2():
    with conn.cursor() as cur:
         cur.execute("SELECT * FROM people")
         rows = cur.fetchall()
         json_datatest = json.dumps(rows)
         return render_template('test.html',datas=json_datatest)


@app.route("/people")
def showFrom():
        return render_template('addpeople.html')


@app.route("/delete/<string:id_data>",methods=['GET'])
def delete(id_data):
    with conn.cursor() as cur:
        cur.execute("DELETE FROM people WHERE id=%s",(id_data))
        conn.commit()
    return redirect(url_for('showData'))


@app.route("/insert",methods=['POST'])
def insert():
    if request.method=="POST":
        fname = request.form['firstname']
        lname = request.form['lastname']
        phone = request.form['phone']
        with conn.cursor() as cursor:
            sql="INSERT INTO `people`(`firstname`, `lastname`, `phone`) VALUES (%s,%s,%s)"
            cursor.execute(sql,(fname,lname,phone))
            conn.commit()
        return redirect(url_for('showData'))


@app.route("/update",methods=['POST'])
def update():
    if request.method=="POST":
        id_update = request.form['id']
        fname = request.form['firstname']
        lname = request.form['lastname']
        phone = request.form['phone']
        with conn.cursor() as cursor:
            sql="update people set firstname=%s,lastname=%s,phone=%s where id=%s"
            cursor.execute(sql,(fname,lname,phone,id_update))
            conn.commit()
        return redirect(url_for('showData'))



if __name__ == "__main__":
    app.run(debug=True)
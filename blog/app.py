from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from os import error


app = Flask(__name__)
app.secret_key = 'many random bytes'

#db_config = {
   # "host": "remotemysql.com",
   # "user": "QyYiCxuWS2",
   # "password": "DIeOFa6xzf",
   # "database": "QyYiCxuWS2",
   # "cursorclass": cursors.DictCursor
#}

#app.config['MYSQL_HOST'] = 'localhost'
#app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = ''
#app.config['MYSQL_DB'] = 'crud'

app.config['MYSQL_HOST'] = 'remotemysql.com'
app.config['MYSQL_USER'] = 'QyYiCxuWS2'
app.config['MYSQL_PASSWORD'] = 'DIeOFa6xzf'
app.config['MYSQL_DB'] = 'QyYiCxuWS2'

mysql = MySQL(app)

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM blogs Order by created_time desc")
    blogs = cur.fetchall()
    cur.close()
    


    return render_template('index.html', blogs=blogs )

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/resignation")
def resignation():
    return render_template("resignation.html")

@app.route('/add', methods = ['POST'])
def insert():

    if request.method == "POST":
        flash("Data Inserted Successfully")
        title = request.form['title']
        content = request.form['content']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO blogs (title, content) VALUES (%s, %s)", (title, content))
        mysql.connection.commit()
        return redirect(url_for('Index'))

#@app.route("/edit/<id>")
#def edit(id):
    #blogs = blogs.get(id)
    #return render_template("edit.html",blogs = blogs)




@app.route("/<id>", methods = ['GET'])
def edit(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM blogs WHERE id = %s", id)
    post = cur.fetchone()
    cur.close()
    
    return render_template("edit.html", post =post)

@app.route('/<id>',methods=['POST'])
def update():

    if request.method == 'POST':
        id_data = request.form['id']
        title = request.form['title']
        content = request.form['content']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE blogs
               SET title=%s, content=%s
               WHERE id=%s
            """, (title, content, id_data))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('Index'))

if __name__ == "__main__":
    app.run(debug=True)
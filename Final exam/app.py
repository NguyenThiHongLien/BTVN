from flask import Flask, render_template, Response, request, redirect

app = Flask(__name__)

#@app.route("/")
#def index():
    #return "Hello from server"

movies = {
    "1": {
        "id": 101,
        "title": "Squid Game",
        "year": 2021
    },
    "2": {
        "id": 102,
        "title": "My name",
        "year" : 2020
    }
}

#Jinja
@app.route("/")
def index():
    return render_template("index.html", movies = movies)

#@app.route("/")
#def index():
    #return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

#path param
@app.route("/movies/<movie_id>")
def detail(movie_id):
    movie = movies.get(movie_id)
    #return Response(render_template("movie.html", movie=movie), status=404, mimetype="text/html")
    return render_template("movie.html", movie=movie)

@app.route('/movies', methods=["GET"])
def render_form():
    return render_template("new-movie.html")


@app.route('/movies', methods=["POST"])
def new_movie():
    title=request.form["title"]
    year=request.form["year"]
    movies[3] = {"id":103, "title": title, "year": year}
    #return "Đã nhận yêu cầu post"
    return redirect("/", code =302)



if __name__ == "__main__":
    app.run(debug=True)
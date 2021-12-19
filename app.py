from flask import Flask, render_template, request
from random import random, randrange
from moviedb import photos, filmwebMovies


app = Flask(__name__)



class Changing:
    random_number = randrange(125)
    score = 0


    def change_random_number(self):
        self.random_number = randrange(125)
        return

    def add_point(self):
        self.score+=1
        return

    def zero_score(self):
        self.score = 0
        return
    

changing = Changing()

@app.route('/', methods=["POST", "GET"])
def home():
    if request.method == "POST":
        if(request.form.get("action1") == "Zaczynamy" or request.form.get("action1") == "graj jeszcze raz"):
            changing.zero_score()
            changing.change_random_number()
            return render_template("question_page.html", imgUrl=filmwebMovies[changing.random_number]["url"])
            
        user_input = request.form.get("input")

        if(request.form.get("action1") == "next"):
            changing.change_random_number()
            changing.add_point()
            return render_template("question_page.html", imgUrl=filmwebMovies[changing.random_number]["url"], wynik = changing.score)

        if(request.form.get("action1") == "Sprawdz"):
            if(user_input.lower()+" " != filmwebMovies[changing.random_number]["title"].lower()):
                temp = changing.score
                changing.zero_score()
                return render_template("incorrect.html", wynik = temp, imgTitle = filmwebMovies[changing.random_number]["title"])
            else:
                return render_template("correct.html", imgUrl=filmwebMovies[changing.random_number]["url"], wynik = changing.score, imgTitle = filmwebMovies[changing.random_number]["title"], year = filmwebMovies[changing.random_number]["year"] )
            
        if(request.form.get("action1") == "koniec gry"):
            changing.zero_score()
            changing.change_random_number()
            return render_template("index.html")

    return render_template("index.html", imgUrl=photos[changing.random_number]["url"])

    


if __name__ == "__main__":
    app.run(debug=True)
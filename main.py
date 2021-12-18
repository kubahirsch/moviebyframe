from flask import Flask, render_template, request
from random import randrange
from moviedb import photos, filmwebMovies


app = Flask(__name__)



class Changing:
    x = randrange(125)
    score = 0


    def change_x(self):
        self.x = randrange(125)
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
            changing.change_x()
            return render_template("question_page.html", imgUrl=filmwebMovies[changing.x]["url"])
            
        user_input = request.form.get("input")

        if(request.form.get("action1") == "next"):
            changing.change_x()
            changing.add_point()
            return render_template("question_page.html", imgUrl=filmwebMovies[changing.x]["url"], wynik = changing.score)

        if(request.form.get("action1") == "Sprawdz"):
            if(user_input.lower()+" " != filmwebMovies[changing.x]["title"].lower()):
                temp = changing.score
                changing.zero_score()
                return render_template("incorrect.html", wynik = temp, imgTitle = filmwebMovies[changing.x]["title"])
            else:
                return render_template("correct.html", imgUrl=filmwebMovies[changing.x]["url"], wynik = changing.score, imgTitle = filmwebMovies[changing.x]["title"], year = filmwebMovies[changing.x]["year"] )
            
        if(request.form.get("action1") == "koniec gry"):
            changing.zero_score()
            changing.change_x()
            return render_template("index.html")

    return render_template("index.html", imgUrl=photos[changing.x]["url"])

    


if __name__ == "__main__":
    app.run(debug=True)
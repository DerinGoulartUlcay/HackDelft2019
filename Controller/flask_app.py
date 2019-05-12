"""
Computer Science Minor Project
Group 11
2018-2019
"""
"""
TODO:
    MUSTS:
    Fix web_scraping
    Fix rating
    Add "RECOMMEND" button

    WANTS:
    Caching
    View of divs in index
"""

from flask import Flask, render_template, request, redirect, url_for
import Model.parser as parser
# import Controller.web_scraping as ws


app = Flask(__name__, template_folder="../View/templates", static_folder="../View/static")

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


@app.route('/', methods=['GET', 'POST'])
def index():
    """Renders a sample page."""
    if request.method == 'POST':
        for i in request.form.keys():
            if i == 'tag':
                query = request.form['tag']
                matched_movies, matched_movies_ids = model_object.search(query)

                max_size = 5
                if len(matched_movies) - 1 > max_size:
                    top_matched_movies = matched_movies[:max_size]
                    top_matched_movies_ids = matched_movies_ids[:max_size]
                else:
                    top_matched_movies = matched_movies
                    top_matched_movies_ids = matched_movies_ids


                movie_images = []
                for movie in top_matched_movies:
                    movie_images.append(ws.get_movie_data(movie))
                result = zip(top_matched_movies, movie_images, top_matched_movies_ids)

                rated_movies = update_rated_movies()
                recommended_movies = get_recommended_movies()

                return render_template("index.html", rated_movies=rated_movies, results=result, recommendations = recommended_movies)

            elif 'rating-' in i:
                rating = int(i[7])
                rated_movie_id = i[9:]
                model_object.add_rating(USER_ID, rated_movie_id, rating)
                rated_movies = update_rated_movies()
                recommended_movies = get_recommended_movies()
                return render_template("index.html", rated_movies = rated_movies, recommendations = recommended_movies)

            elif i == "get_recommended_movies":
                update_recommendations()
                recommended_movies = get_recommended_movies()
                rated_movies = update_rated_movies()
                return render_template("index.html", rated_movies = rated_movies, recommendations = recommended_movies)

    else:
        rated_movies = update_rated_movies()
        return render_template("index.html", rated_movies = rated_movies)

def give_rating():
    rating = request.form['']
    movie_id = request.form['first_name']
    model_object.add_rating(USER_ID, movie_id, rating)



if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)

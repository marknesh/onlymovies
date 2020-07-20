from flask import render_template,redirect,request,url_for
from .models import  reviews

from .forms import ReviewForm
Review=reviews.Review

from app import app
from .request import get_movies,get_movie,search_movie,get_video

@app.route('/')
def index():

    popular=get_movies('popular')

    upcoming=get_movies('upcoming')

    now_showing=get_movies('now_playing')


   

    search_movie=request.args.get('movie_query')

    if search_movie:
        return redirect(url_for('search',movie_name=search_movie))
    else:
        return render_template('index.html',popular=popular,upcoming=upcoming,now_showing=now_showing)

@app.route('/movie/<int:id>')
def movie(id):
    movie=get_movie(id)
    video=get_video(id)
    
    title=f'{movie.title}'

    reviews=Review.get_reviews(movie.id)

    return render_template('movie.html',title=title,movie=movie,reviews=reviews,video=video)



@app.route('/search/<movie_name>')

def search(movie_name):
    movie_name_list=movie_name.strip().split(" ")
    movie_name_format="+".join(movie_name_list)

    searched_movies=search_movie(movie_name_format)
    title=f'search results for {movie_name}'
    return render_template('search.html', movies=searched_movies,title=title)



@app.route('/movie/review/new/<int:id>',methods=['GET','POST'])


def new_review(id):
    form=ReviewForm()
    movie=get_movie(id)

    if form.validate_on_submit():
        title=form.title.data
        review=form.review.data
        new_review=Review(movie.id,title,movie.poster,review)
        new_review.save_review()
        return redirect(url_for('movie',id=movie.id))

    title = f'{movie.title} review'
    return render_template('new_review.html',title = title, review_form=form, movie=movie)        
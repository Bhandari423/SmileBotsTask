import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
import imdb
import django

django.setup()

from movie.models import MovieDetail
from faker import Faker

fakegen = Faker()
movieDB = imdb.IMDb()
movie_list = movieDB.get_bottom100_movies()


def populatemovie(N):
    for i in range(N):
        movies = movieDB.get_movie(movie_list[i].movieID)

        fake_title = movies['title']
        fake_director = movies['director'][0]
        fake_genre = movies['genre']
        fake_rating = movies['rating']
        fake_year = movies['year']
        fake_votes = movies['votes']
        fake_kind = movies['kind']

        user = MovieDetail.objects.get_or_create(title=fake_title, director=fake_director, genre=fake_genre, rating=fake_rating, year=fake_year, votes=fake_votes, kind=fake_kind)[0]


if __name__ == '__main__':
    print('POPULATING DATABASE')
    populatemovie(10)
    print('COMPLETED')

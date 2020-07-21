class Config:

    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}&append_to_response=similar&language=en-US'
    VIDEO_URL='http://api.themoviedb.org/3/movie/{}/videos?api_key={}'
    SIMILAR_MOVIES_URL='https://api.themoviedb.org/3/movie/{}/similar?api_key={}&language=en-US'
    DEBUG = True
class ProdConfig:

    DEBUG = True

class DevConfig:

    DEBUG = True
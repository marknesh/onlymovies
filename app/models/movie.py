class Movie:

   def __init__(self,id,title,overview,poster,vote_average,vote_count,videos,release_date,backdrop_path):
        self.id =id
        self.title = title
        self.overview = overview
        self.poster = 'https://image.tmdb.org/t/p/w500/'+ poster
        self.vote_average = vote_average
        self.vote_count = vote_count
        self.videos=videos
        self.release_date=release_date
        self.backdrop_path='https://image.tmdb.org/t/p/w500/'+ backdrop_path
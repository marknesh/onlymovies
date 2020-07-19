import unittest

from models import movie

Movie=movie.Movie



class MovieTest(unittest.TestCase):


    def setUp(self):

        self.new_movie=Movie(1234,'bad boys','awsome','https://ww.image.com',5.6,12345)



    def test_instance(self):
        self.assertTrue(isinstance(self.new_movie,Movie))   



if __name__ == '__main__':
    unittest.main()
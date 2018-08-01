from fresh_tomatoes import open_movies_page
from media import Movie

# Film Coco
coco = Movie('Coco',
             'https://m.media-amazon.com/images/M'
             '/MV5BYjQ5NjM0Y2YtNjZkNC00ZDhkLWJjMWItN2QyNzFkMDE3ZjAxXkEyXkFqcGdeQXVyODIxMzk5NjA@._V1_UY268_CR3,0,182,'
             '268_AL_.jpg',
             'https://www.youtube.com/watch?v=zNCz4mQzfEI')

# Film The Shawshank Redemption
shawn = Movie('The Shawshank Redemption',
              'https://m.media-amazon.com/images/M'
              '/MV5BMDFkYTc0MGEtZmNhMC00ZDIzLWFmNTEtODM1ZmRlYWMwMWFmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_.jpg',
              'https://www.youtube.com/watch?v=6hB3S9bIaco')

# Film list
movies = [coco, shawn]

# Generate html and open in browser
open_movies_page(movies)

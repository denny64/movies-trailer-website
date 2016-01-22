import fresh_tomatoes
import media

"""
Generates a movie trailer website

To run: python entertainment_center.py

To add another movie to the webpage, follow the Toy Story example below.
The arguments in the Movie class are set in the following order:
    - Movie Title
    - Movie Storyline
    - Poster Image
    - Trailer Youtube
    - Genre
    - Language
    - Release Date
    - Runtime

After you have created a movie instance, add the variable to the movies array.
"""

toy_story = media.Movie("Toy Story",
                        "A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room.",
                        "http://vignette4.wikia.nocookie.net/disney/images/4/4c/Toy-story-movie-posters-4.jpg/revision/latest?cb=20140816182710",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                        "Animation, Adventure, Comedy",
                        "English",
                        "22 Nov 1995",
                        "81 min"
                        )

jurassic_park = media.Movie("Jurassic Park",
                            "Huge advancements in scientific technology have enabled a mogul to create an island full of living dinosaurs. John Hammond has invited four individuals, along with his two grandchildren, to join him at Jurassic Park. But will everything go according to plan? A park employee attempts to steal dinosaur embryos, critical security systems are shut down and it now becomes a race for survival with dinosaurs roaming freely over the island.",
                            "https://www.movieposter.com/posters/archive/main/142/MPW-71462",
                            "https://youtu.be/lc0UehYemQA",
                            "Adventure, Sci-Fi, Thriller",
                            "English, Spanish",
                            "11 Jun 1993",
                            "127 min"
                            )

avatar = media.Movie("Avatar",
                    "A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
                    "http://imgs.abduzeedo.com/files/articles/Avatar/4154691473_fa5a635992_o.jpg",
                    "https://www.youtube.com/watch?v=5PSNL1qE6VY",
                    "Action, Adventure, Fantasy",
                    "English, Spanish",
                    "18 Dec 2009",
                    "162 min"
                    )

the_martian = media.Movie("The Martian",
                        "During a manned mission to Mars, Astronaut Mark Watney is presumed dead after a fierce storm and left behind by his crew. But Watney has survived and finds himself stranded and alone on the hostile planet. With only meager supplies, he must draw upon his ingenuity, wit and spirit to subsist and find a way to signal to Earth that he is alive.",
                        "http://static.hd-trailers.net/images/the-martian-104112-poster-xlarge.jpg",
                        "https://youtu.be/ej3ioOneTy8",
                        "Adventure, Comedy, Drama",
                        "English, Mandarin",
                        "02 Oct 2015",
                        "144 min"
)


movies = [toy_story, jurassic_park, avatar, the_martian]

fresh_tomatoes.open_movies_page(movies)

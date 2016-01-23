Movie Trailer Website
===================================

To run: `python entertainment_center.py`

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

You can add movies onto the websvite by using this format:
```
the_avengers = media.Movie("The Avengers",
                           "As the Clone Wars sweep through the galaxy, the heroic Jedi Knights struggle to maintain order and restore peace. More and more systems are falling prey to the forces of the dark side as the Galactic Republic slips further and further under the sway of the Separatists and their never-ending droid army. Anakin Skywalker and his Padawan learner Ahsoka Tano find themselves on a mission with far-reaching consequences, one that brings them face-to-face with crime lord Jabba the Hutt. But Count Dooku and his sinister agents, including the nefarious Asajj Ventress, will stop at nothing to ensure that Anakin and Ahsoka fail at their quest.",
                           "http://ifanboy.com/wp-content/uploads/2012/02/avengers-assemble-the-avengers-gets-new-title-and-official-poster-81282-470-75.jpg",
                           "https://youtu.be/rvEK4--EpbQ",
                           "Action, Sci-Fi, Thriller",
                           "English, Russian",
                           "04 May 2012",
                           "143 min"
)
```

After this, add the variable (in this case, the_avengers) to the movies array:

`movies = [toy_story, jurassic_park, avatar, the_martian, star_wars, the_avengers]`

Screenshots
==============
![My img](https://github.com/denny64/movies-trailer-website/blob/master/screen1.png)
![My img](https://github.com/denny64/movies-trailer-website/blob/master/screen2.png)

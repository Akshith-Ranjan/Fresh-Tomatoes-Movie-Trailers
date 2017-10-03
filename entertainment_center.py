import fresh_tomatoes
import media


# Movie objects.
firstdates = media.Movie(
    "50 First Dates",
    "American romantic comedy film directed by Peter Segal",
    "https://upload.wikimedia.org/wikipedia/en/9/9d/50FirstDates.jpg",
    "https://www.youtube.com/watch?v=H1SVxJZTgI4")

thegodfather = media.Movie(
    "The Godfather",
    "American crime film directed by Francis Ford Coppola",
    "https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg",
    "https://www.youtube.com/watch?v=sY1S34973zA")

deadpool = media.Movie(
    "Deadpool",
    "American superhero film based on the Marvel Comics",
    "https://upload.wikimedia.org/wikipedia/en/4/46/Deadpool_poster.jpg",
    "https://www.youtube.com/watch?v=OuH3zDs2y3s")

theuglytruth = media.Movie(
    "The Ugly Truth",
    "American romantic comedy film",
    "https://upload.wikimedia.org/wikipedia/en/a/ad/Ugly_truth.jpg",
    "https://www.youtube.com/watch?v=DvsZtGxsvV0")

crazystupidlove = media.Movie(
    "Crazy, Stupid, Love",
    "American romantic comedy film directed by Glenn Ficarra",
    "https://upload.wikimedia.org/wikipedia/en/7/78/CrazyStupidLovePoster.jpg",
    "https://www.youtube.com/watch?v=8iCwtxJejik")

three = media.Movie(
    "300",
    "American epic war film",
    "https://upload.wikimedia.org/wikipedia/en/5/5c/300poster.jpg",
    "https://www.youtube.com/watch?v=WorI5HPWbpg")

idiots = media.Movie(
    "3 Idiots",
    "Indian coming of age comedy-drama film",
    "https://upload.wikimedia.org/wikipedia/en/d/df/3_idiots_poster.jpg",
    "https://www.youtube.com/watch?v=xvszmNXdM4w")

# movies variable is a list of all the movie objects.
movies = [deadpool, theuglytruth, firstdates, thegodfather, crazystupidlove,
          three, idiots]

# Creates a Webpage using the MovieObjects and opens the webpage in a Browser.
fresh_tomatoes.open_movies_page(movies)

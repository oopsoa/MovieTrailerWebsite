import movie
import fresh_tomatoes

image_dir = "../movie_posters/"

galaxy = movie.Movie("Guardians of the Galaxy 2",
                     "https://www.youtube.com/watch?v=c3986gGp3Qs",
                     image_dir+"Galaxy2.png")

avatar = movie.Movie("Avatar",
                     "https://www.youtube.com/watch?v=a0CDJZu4M5I",
                     image_dir+"Avatar.png")

gladiator = movie.Movie("Gladiator",
                        "https://www.youtube.com/watch?v=l-kV68xPVnM",
                        image_dir+"Gladiator.png")

planetofapes = movie.Movie("Planet Of Apes",
                           "https://www.youtube.com/watch?v=3KWAxBlZKMA",
                           image_dir+"PlanetOfApes.png")

tothebone = movie.Movie("To The Bone",
                        "https://www.youtube.com/watch?v=705yRfs6Dbs",
                        image_dir+"ToTheBone.png")

wishupon = movie.Movie("Wish Upon",
                       "https://www.youtube.com/watch?v=fkKaDoUh_so",
                       image_dir+"WishUpon.png")

movies_list = [galaxy, avatar, gladiator, planetofapes, tothebone, wishupon]
fresh_tomatoes.open_movies_page(movies_list)

import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=azyK_k52R1w")

avatar = media.Movie("Toy Story",
                        "A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
                        "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY")

arrival = media.Movie("Arrival",
                        "Linguistics professor Louise Banks (Amy Adams) leads an elite team of investigators when gigantic spaceships touch down in 12 locations around the world.",
                        "http://static.rogerebert.com/uploads/movie/movie_poster/arrival-2016/large_Arrival-Poster-2016.jpg",
                        "https://www.youtube.com/watch?v=tFMo3UJ4B4g")

interstellar = media.Movie("Interstellar",
                        "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_UY1200_CR69,0,630,1200_AL_.jpg",
                        "https://www.youtube.com/watch?v=0vxOhd4qlnA")

inception = media.Movie("Inception",
                        "A thief, who steals corporate secrets through use of dream-sharing technology, is given the inverse task of planting an idea into the mind of a CEO.",
                        "http://www.impawards.com/2010/posters/inception.jpg",
                        "https://www.youtube.com/watch?v=YoHD9XEInc0")
movies = [toy_story, avatar, arrival, interstellar, inception]
fresh_tomatoes.open_movies_page(movies)

# print toy_story.storyline
# avatar.show_trailer()
# toy_story.show_trailer()
# print avatar.storyline

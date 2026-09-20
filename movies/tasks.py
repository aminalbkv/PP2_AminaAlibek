# Here is a list of movies
movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]


# Here is a function that checks one movie
def good_movie(movie):
    return movie["imdb"] > 5.5


# Here is a function that returns all good movies
def good_movies(movie_list):
    result = []

    for movie in movie_list:
        if movie["imdb"] > 5.5:
            result.append(movie)

    return result


# Here is a function that returns movies from a category
def movies_by_category(movie_list, category):
    result = []

    for movie in movie_list:
        if movie["category"] == category:
            result.append(movie)

    return result


# Here is a function that calculates average IMDB
def average_imdb(movie_list):
    total_score = 0

    for movie in movie_list:
        total_score += movie["imdb"]

    return total_score / len(movie_list)


# Here is a function that calculates average IMDB by category
def category_average(movie_list, category):
    total_score = 0
    movie_count = 0

    for movie in movie_list:
        if movie["category"] == category:
            total_score += movie["imdb"]
            movie_count += 1

    if movie_count == 0:
        return 0

    return total_score / movie_count


# Here are examples for all five tasks
print("Task 1:", good_movie(movies[0]))

print("\nTask 2:")
for movie in good_movies(movies):
    print(movie["name"])

print("\nTask 3:")
for movie in movies_by_category(movies, "Romance"):
    print(movie["name"])

print("\nTask 4:")
print(average_imdb(movies))

print("\nTask 5:")
print(category_average(movies, "Romance"))
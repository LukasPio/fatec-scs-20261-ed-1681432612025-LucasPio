catalog = {}

def add_movie(movie_id, title, director):
    if movie_id in catalog:
        print("A movie with this ID already exists.")
    else:
        catalog[movie_id] = {
            "title": title,
            "director": director
        }
        print("Movie added successfully.")

def search_movie(movie_id):
    movie = catalog.get(movie_id)
    if movie:
        print(f"ID: {movie_id} | Title: {movie['title']} | Director: {movie['director']}")
    else:
        print("Movie not found.")

def remove_movie(movie_id):
    removed = catalog.pop(movie_id, None)
    if removed:
        print("Movie removed successfully.")
    else:
        print("Movie not found for removal.")

def list_all():
    if not catalog:
        print("\nThe catalog is empty.")
    else:
        print("\n--- Movie List ---")
        for m_id, data in catalog.items():
            print(f"ID: {m_id} | Title: {data['title']} | Director: {data['director']}")

while True:
    print("\n--- MENU ---")
    print("1 - Add movie")
    print("2 - Search movie")
    print("3 - Remove movie")
    print("4 - List all")
    print("0 - Exit")

    option = input("Choose an option: ")

    if option == "1":
        movie_id = input("Enter movie ID: ")
        title = input("Enter title: ")
        director = input("Enter director: ")
        add_movie(movie_id, title, director)

    elif option == "2":
        movie_id = input("Enter movie ID: ")
        search_movie(movie_id)

    elif option == "3":
        movie_id = input("Enter movie ID: ")
        remove_movie(movie_id)

    elif option == "4":
        list_all()

    elif option == "0":
        print("Exiting...")
        break

    else:
        print("Invalid option, try again.")
movie_list = []

continuer = "y"

print("Veillez rentrez des films")


while continuer == "y":
    film = input("Entrez un film : ")
    if film.lower() in [film[0].lower() for film in movie_list]:
        print("Ce film est deja present dans la list")
        continue
    note = input("Veillez rentrez une note : ")
    movie_list.append((film, note))
    continuer = input("Voulez vous continuer y/n : ")
    print('')

movie_list.sort()

print(movie_list)


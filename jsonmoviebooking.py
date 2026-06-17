import json
from pathlib import Path

class MovieBooking:
    database = "Movies.json"
    data = []

    if Path(database).exists():
        with open(database, "r") as Myfile:
            data = json.load(Myfile)

    @classmethod
    def __update(cls):
        with open(cls.database, "w") as Myfile:
            json.dump(cls.data, Myfile, indent=4)

    def add_movie(self):
        movie = {
            "movie_name": input("Enter movie name: "),
            "available_seats": int(input("Enter seats: "))
        }

        self.data.append(movie)
        self.__update()
        print("Movie added successfully!")

# Create object and call method
obj = MovieBooking()
obj.add_movie()
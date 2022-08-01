import csv


def read_notes_from_csv():
    with open("films.csv", "r") as file:
        f = csv.DictReader(file)
        for note in f:
            print(note['Notes'])


def add_notes_to_csv(note):
    with open("films.csv", "a") as file:
        file.write(f',{note},')


def highest_rate_films():
    with open("films.csv", "r") as file:
        f = csv.DictReader(file)
        for rate in f:
            try:
                if int(rate['Rate']) > 4:
                    print(rate['Film'])
            except:
                print(end='')


def lowest_rate_films():
    with open("films.csv", "r") as file:
        f = csv.DictReader(file)
        for rate in f:
            try:
                if int(rate['Rate']) <= 2:
                    print(rate['Film'])
            except:
                print(end='')


def average_rate_of_all_films():
    with open("films.csv", "r") as file:
        f = csv.DictReader(file)
        counter = 0
        avg = 0
        for i in f:
            avg += int(i["Rate"])
            counter += 1
        print(round(avg/counter, 2))


read_notes_from_csv()
add_notes_to_csv("some note")
highest_rate_films()
lowest_rate_films()
average_rate_of_all_films()

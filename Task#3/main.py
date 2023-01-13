import json


def count_legs():
    try:
        animals = json.load(open('animals.json'))
        legs = {"pigs": 4, "chickens": 2, "cows": 4}
        sum_of_legs = 0
        try:
            for i in animals:
                sum_of_legs += animals[i] * legs[i]
            json.dump(sum_of_legs, open('result.json', 'w'))
            return print(sum_of_legs)
        except KeyError:
            print(f'The number of legs of a {i} is missing in the system')
    except FileNotFoundError:
        print("File 'animals.json' not found")


count_legs()
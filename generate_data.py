import json
from faker import Faker

fake = Faker()

def main():

    for i in range(0, 10):
        place = fake.local_latlng('DE')
        print(place)


if __name__ == "__main__":
    main()

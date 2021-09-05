import json
from faker import Faker

fake = Faker()

def main():
    
    print("latitude,longitude,place_name,country_code,timezone")

    for i in range(0, 10):
        place = fake.local_latlng('DE')
        print(','.join(place))


if __name__ == "__main__":
    main()

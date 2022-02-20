import json
from faker import Faker
from itertools import chain

fake = Faker()

def main():
    
    print("datetime,latitude,longitude,place_name,country_code,timezone,measure")

    for i in range(0, 10000):
        datetime = fake.date_time_this_month().strftime("%Y-%m-%d %H:%M:%S")
        place = fake.location_on_land()
        measure = str(fake.random_int(min=1, max=100))
        print(f"{datetime},{','.join(place)},{measure}")


if __name__ == "__main__":
    main()

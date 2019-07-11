def city_country(name, country):
    city = name + ":" + country
    return city


while True:
    print("Please tell your city")
    name = input("The name is: ")
    country = input("The country is: ")
    city = city_country(name, country)
    print(city)
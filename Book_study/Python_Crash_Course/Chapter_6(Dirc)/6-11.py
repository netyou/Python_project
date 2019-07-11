cities = {
    'Beijing': {
        'country': 'China',
        'population': 'A lot',
        'fact': 'Big and poor and strong',
    },
    'Tokyo': {
        'country': 'Japan',
        'population': 'a little',
        'fact': 'FBI warmming',
    },
    'London': {
        'country': 'England',
        'population': 'many',
        'fact': 'gentleman',
    },
}
for city, message in cities.items():
    print("The message in this " + city + " is: ")
    print("\tCountry: " + message['country'])
    print("\tPopulation: " + message['population'])
    print("\tFact: " + message['fact'])
for city,message in cities.items():
    print("The message in this " + city + " is: ")
    for k, v in message.items():
        print("\t" + k + ": " + v)
    print("\n")
rivers_country = {
    'nile' : 'egypt',
    'Long river' : 'China',
    'xx' : 'zz',

}
for river,country in rivers_country.items():
    print("The " + river + "runs through " + country)
for river in rivers_country.keys():
    print(river)
for country in rivers_country.values():
    print(country)
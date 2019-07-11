def place(city, country, population=''):
    city = city.title()
    country = country.title()
    back = city + ',' + country + ' - population ' + str(population)
    return back


a = place('beijng', 'china', 50000)
print(a)
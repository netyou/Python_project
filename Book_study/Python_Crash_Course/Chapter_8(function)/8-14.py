def car(producer, model, **info):
    car_info = dict()
    car_info['car_producer'] = producer
    car_info['car_model'] = model
    for key, value in info.items():
        car_info[key] = value
    return car_info


car2 = car('subaru', 'outback', color='blue', tow_package='True')
for k, v in car2.items():
    print(k + ":" + v)

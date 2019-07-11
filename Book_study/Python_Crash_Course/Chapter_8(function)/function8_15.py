def car(producer, model, **info):
    '''
    汽车的生产商，型号，和它的其他信息
    :param producer: 生产商
    :param model: 型号
    :param info: 其他信息
    :return: 车子的基本信息
    '''
    car_info = dict()
    car_info['car_producer'] = producer
    car_info['car_model'] = model
    for key, value in info.items():
        car_info[key] = value
    return car_info
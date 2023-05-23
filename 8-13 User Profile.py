def car_profile(model, model_version, **car_information):
    '''Making car card'''
    car_information["model"] = model
    car_information["model_version"] = model_version
    return car_information

car_1 = car_profile("Honda", "Civic", color="Blue",)

print(f"\nCar that is on checking is: \n\t{car_1}")
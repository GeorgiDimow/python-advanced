def forecast(*info):
    sorted_list = []
    sunny_weather = sorted(filter(lambda x: x[1] == "Sunny", info), key=lambda x: x[0])
    cloudy_weather = sorted(filter(lambda x: x[1] == "Cloudy", info), key=lambda x: x[0])
    rainy_weather = sorted(filter(lambda x: x[1] == "Rainy", info), key=lambda x: x[0])
    sorted_list.extend(sunny_weather)
    sorted_list.extend(cloudy_weather)
    sorted_list.extend(rainy_weather)

    return '\n'.join([' - '.join(x) for x in sorted_list])


print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))

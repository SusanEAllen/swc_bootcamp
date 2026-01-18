def fahr_to_kelvin(temp):
    return ((temp - 32.0) * 5.0/9.0) + 273.15


def kelvin_to_celsius(temp):
    return temp - 273.15


def fahr_to_celsius(temp):
    return kelvin_to_celsius(fahr_to_kelvin(temp))
    
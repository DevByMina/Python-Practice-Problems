def degCtoForK(celsius,to):
    if to=="fahrenheit":
        fahrenheit = (celsius*(9/5))+32
        return fahrenheit
    elif to=="kelvin":
        kelvin = celsius+273
        return kelvin

print(degCtoForK(28,"kelvin"))
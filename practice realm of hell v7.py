temp = -23
Is_raining = False
Is_sunny = False

if temp >= 28 and Is_sunny:
    print("It is hot outside")
    print("It is Sunny")
elif temp <= 0 and Is_sunny:
    print("it is cold outside")
    print("it is sunny")
elif 20 > temp >0 and Is_sunny:
    print("It is warm outside")
    print("It is sunny outside")

if temp >= 28 and not Is_sunny:
    print("It is hot outside")
    print("It is Cloudy")
elif temp <= 0 and not Is_sunny:
    print("it is cold outside")
    print("it is Cloudy")
elif 20 > temp >0 and  not Is_sunny:
    print("It is warm outside")
    print("It is Cloudy")
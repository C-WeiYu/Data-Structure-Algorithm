def centuryFromYear(year):
    if year%100 != 0:
        number=int(year/100)+1
    else:
        number=year/100
    return number

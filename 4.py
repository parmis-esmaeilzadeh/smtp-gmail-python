import datetime as dt

today = dt.datetime.now()
hr = today.hour
wd = today.weekday()
match wd:
    case 0:
        print('mo')
    case 1:
        print("tu")
    case 2:
        print('we')
    case 3:
        print("th")
    case 4:
        print("fr")
    case 5:
        print("sa")
    case 6:
        print("su")

print(wd)

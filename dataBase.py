import pandas as pd


def generateId(path, paramater):
    data = load(path)

    if data.empty:
        return 1
    else:
        print(data[paramater].max())
        return int(data[paramater].max())

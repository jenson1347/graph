import math

def funcDataCreator(low_border,high_border,countOfPoints,name_func):
    #Вход: ниж. граница, верх. границя, название
    #Выход: файл со значениями функции на интервале от lb to hb
    #Зачем: генерировать файл со значениями при нажатии кнопки, предварительно введя номер функции в lineedit
    #parts = abs(high_border-low_border)/countOfPoints
    name = 0
    match name_func:
        case 1:
            name = "sin(x)"
        case 2:
            name = "cos(x)"
        case 3:
            name = "tg(x)"
        case 4:
            name = "ctg(x)"
        case 5:
            name = "1/x"
        case 6:
            name = "sin(x) + cos(x)"
        case 7:
            name = "x^2"
    #задание функций
    with open(f"func_{name_func}", "w") as file:
        if name_func == 1:
            file.write(f"{name}\n")
            while True:
                if low_border >= high_border:
                    try:
                        file.write(f"{str(high_border)},{round(math.sin(high_border), 5)}\n")
                        low_border += countOfPoints
                        break
                    except:
                        file.write(f"{str(low_border)},\n")
                        low_border += countOfPoints
                        break
                try:
                    file.write(f"{str(round(low_border,5))},{round(math.sin(low_border),5)}\n")
                    low_border += countOfPoints
                except:
                    file.write(f"{str(round(low_border,5))},\n")
                    low_border += countOfPoints
        if name_func == 2:
            file.write(f"{name}\n")
            while True:
                if low_border >= high_border:
                    try:
                        file.write(f"{str(high_border)},{round(math.cos(high_border),5)}\n")
                        low_border += countOfPoints
                        break
                    except:
                        file.write(f"{str(high_border)},\n")
                        low_border += countOfPoints
                        break
                try:
                    file.write(f"{str(round(low_border,5))},{round(math.cos(low_border), 5)}\n")
                    low_border += countOfPoints
                except:
                    file.write(f"{str(round(low_border,5))},\n")
                    low_border += countOfPoints
        if name_func == 3:
            file.write(f"{name}\n")
            while True:
                if low_border >= high_border:
                    try:
                        file.write(f"{str(high_border)},{round(math.tan(high_border),5)}\n")
                        low_border += countOfPoints
                        break
                    except:
                        file.write(f"{str(high_border)},\n")
                        low_border += countOfPoints
                        break
                try:
                    file.write(f"{str(round(low_border,5))},{round(math.tan(low_border), 5)}\n")
                    low_border += countOfPoints
                except:
                    file.write(f"{str(round(low_border,5))},\n")
                    low_border += countOfPoints
        if name_func == 4:
            file.write(f"{name}\n")
            while True:
                if low_border >= high_border:
                    try:
                        file.write(f"{str(high_border)},{round(1/math.tan(high_border),5)}\n")
                        low_border += countOfPoints
                        break
                    except:
                        file.write(f"{str(high_border)},\n")
                        low_border += countOfPoints
                        break
                try:
                    file.write(f"{str(round(low_border,5))},{round(1 / math.tan(low_border), 5)}\n")
                    low_border += countOfPoints
                except:
                    file.write(f"{str(round(low_border,5))},\n")
                    low_border += countOfPoints
        if name_func == 5:
            file.write(f"{name}\n")
            while True:
                if low_border >= high_border:
                    try:
                        num = 1/high_border
                        file.write(f"{str(high_border)},{round(num,5)}\n")
                        low_border += countOfPoints
                        break
                    except:
                        file.write(f"{str(high_border)},\n")
                        low_border += countOfPoints
                        break
                try:
                    num = 1/low_border
                    file.write(f"{str(round(low_border,5))},{round(num, 5)}\n")
                    low_border += countOfPoints
                except:
                    file.write(f"{str(round(low_border,5))},Error\n")
                    low_border += countOfPoints

        if name_func == 6:
            file.write(f"{name}\n")
            while True:
                if low_border >= high_border:
                    try:
                        file.write(f"{str(high_border)},{round(math.sin(high_border)+math.cos(high_border),5)}\n")
                        low_border += countOfPoints
                        break
                    except:
                        file.write(f"{str(high_border)},\n")
                        low_border += countOfPoints
                        break
                try:
                    file.write(f"{str(round(low_border,5))},{round(math.sin(low_border) + math.cos(low_border), 5)}\n")
                    low_border += countOfPoints
                except:
                    file.write(f"{str(round(low_border,5))},\n")
                    low_border += countOfPoints
        if name_func == 7:
            file.write(f"{name}\n")
            while True:
                if low_border >= high_border:
                    try:
                        file.write(f"{str(high_border)},{low_border**2}\n")
                        low_border += countOfPoints
                        break
                    except:
                        file.write(f"{str(high_border)},\n")
                        low_border += countOfPoints
                        break
                try:
                    file.write(f"{str(round(low_border,5))},{low_border**2}\n")
                    low_border += countOfPoints
                except:
                    file.write(f"{str(round(low_border,5))},\n")
                    low_border += countOfPoints
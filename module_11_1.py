import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import pandas as pd


# Модуль matplotlib и numpy - Рисование сферы (Каркасная поверхность)
legend_1 = ['Сфера']
u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
x = np.cos(u)*np.sin(v)
y = np.sin(u)*np.sin(v)
z = np.cos(v)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(x, y, z)
ax.legend(legend_1)
plt.show()


# Работа с модулем pillow
im = Image.open('kasatka1.bmp')
print(im.format, im.size, im.mode)
im.thumbnail((1000, 1000))  # уменьшение изображения
im.save('kasatka_thumbnail.jpg')
im.close()

im = Image.open('kasatka1.bmp')
im_crop = im.crop((200, 150, 1720, 930))    # обрезка изображения
im_crop.save('kasatka_cropped.jpg')
im.close()

im = Image.open('kasatka1.bmp')
im_rotate = im.rotate(90)   # Поворот на 90 гр.
im_rotate.save('kasatka_rotated.jpg')
im.close()

im = Image.open('kasatka1.bmp')
im_gray = im.convert('L')   # Изменение цвета - градации серого
im_gray.save('kasatka_grayscale.jpg')
im.close()


# Работа с модулем pandas
line_d = {}
with open('data.txt', mode='r', encoding='utf8') as file:
    for line in file:
        line = line.split()
        line_l = []
        for i in range(1, len(line)):
            line_l.append(int(line[i]))
        line_d.update({line[0]: line_l})
df1 = pd.DataFrame(line_d)
print(df1)  # Вывод таблицы
print(df1[df1['D'] > 18])   # Вывод строк, где D > 18
print(df1.head(2))  # Вывод 2-х строк от начала
print(df1.tail(3))  # Вывод 3-х строк от конца
print(df1.index)    # Вывод индексов таблицы
print(df1.columns)  # Вывод столбцов таблицы
print(df1.to_numpy())   # преобразование таблицы в список списков (двумерный массив)
print(df1.dtypes)   # вывод типа данных в столбцах
print(df1['D'])     # вывод всех строк столбца D
print(df1[1:3])     # вывод всех столбцов с индексами от 1 до 2
print(df1.loc[:,['A','B']])     # вывод всех строк столбцов A и B
print(df1.loc[2:4, ['D']])      # вывод строк с индексами от 2 до 4 столбца D
print(df1.mean())   # вывод среднего значения столбцов
print(df1.mean(axis=1))     # вывод среднего значения строк
print(df1.agg(lambda x: np.mean(x) * 2))    # применение лямбда-функции к таблице
                                            # (среднее значение столбца умноженное на 2)

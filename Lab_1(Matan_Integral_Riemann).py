import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches


def draw_base():
    y = lambda x: np.sin(x)
    x = np.linspace(0, 2 * np.pi, 100)

    plt.plot(x, y(x), 'r')

    plt.axis([0, 7, -1.1, 1.1])
    xnumbers = np.linspace(0, 7, 15)
    ynumbers = np.linspace(-1, 1, 11)
    plt.xticks(xnumbers)
    plt.yticks(ynumbers)
    plt.axhline(0, color='black')
    plt.grid()


def draw_rectangle(x, y, width, height):
    ax.add_patch(patches.Rectangle((x, y), width, height, edgecolor='blue', facecolor='red', fill=False, lw=2))


def int_sum():

    n = int(input('Введите n - кол-во точек разбиения:\n'))
    pos = input('Выберите оснащение:\nl -левые, c - центральные, r - Правые\n')
    delta = 2 * np.pi / n
    p = 0
    int_sum = 0
    if pos == 'r':
        p = delta
    elif pos == 'c':
        p = delta / 2
    for i in range(n):
        k = delta * i
        x0 = k
        y0 = np.sin(x0 + p)
        draw_rectangle(x0, 0, delta, y0)
        int_sum += delta * y0
    print(f'Интегральная сумма равна {int_sum}')


if __name__ == '__main__':
    fig, ax = plt.subplots()
    draw_base()
    int_sum()
    plt.show()

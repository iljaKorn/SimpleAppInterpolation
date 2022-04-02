import matplotlib.pyplot as plt
import numpy as np


def lagranz(x, y, t):
    z = 0
    for j in range(len(y)):
        p1 = 1
        p2 = 1
        for i in range(len(x)):
            if i == j:
                p1 = p1 * 1;
                p2 = p2 * 1
            else:
                p1 = p1 * (t - x[i])
                p2 = p2 * (x[j] - x[i])
        z = z + y[j] * p1 / p2
    return z


def main():
    x_points = []
    y_points = []
    fig, ax = plt.subplots(figsize=(10, 10), num="Cubic Splines Simple App")

    curve, = ax.plot(x_points, y_points, "-g")
    points, = ax.plot(x_points, y_points, "*")

    def on_click(event):
        x_new_point, y_new_point = ax.transData.inverted().transform([event.x, event.y])
        x_points.append(x_new_point)
        y_points.append(y_new_point)

        if len(x_points) > 1 and len(x_points) == len(y_points):
            x_curve_points = np.linspace(np.min(x_points), np.max(x_points), 1000)
            y_curve_points = [lagranz(x_points, y_points, i) for i in x_curve_points]
            curve.set_xdata(x_curve_points)
            curve.set_ydata(y_curve_points)
        points.set_xdata(x_points)
        points.set_ydata(y_points)

        fig.canvas.draw()

    plt.xlim([-100, 100])
    plt.ylim([-100, 100])
    fig.canvas.mpl_connect('button_press_event', on_click)
    plt.show()


if __name__ == '__main__':
    main()

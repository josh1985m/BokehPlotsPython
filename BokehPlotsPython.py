from bokeh.plotting import figure, show
from numpy import random
w = []
z = []
x = 1
for i in range(0, 10):
    y = (3 * x) + 1
    x = x + 1
    while y != 1:
        if (y % 2) == 0:
            y = y/2
            w.append(x)
            z.append(y)
        else:
            y = (3 * y) + 1
            w.append(y)
            z.append(x)

print(w)
print(z)
p = figure(title="y = 3x+1 if even y = y/2 odd y = 3y+1 until y = 1 then x + 1 begin again", x_axis_label='x', y_axis_label='y')
p.line(w, z, legend_label='Formula plot', line_width=2)
show(p)


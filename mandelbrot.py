"""The Mandelbrot set is is the set of complex numbers c for witch
the sequence z_0 = c, z_(n+1) = (z_n)**2 + c does not diverge. This
program will generate an image of the Mandelbrot set, deciding if
each pixel belongs or not testing if in the first 1000 iterations it
diverges.
"""
import Image

# Setting image size
width = 2100
height = 1200

# Setting the interval to be covered by the image
x_inf = -2.5
x_sup = 1.0
y_inf = -1.0
y_sup = 1.0

# Where should the image file be saved
path = "./mandelbrot.png"


def mandelbrot(x0, y0):
    """Testing if a point belongs to the set"""
    cont = 0
    x = x0
    y = y0

    while cont < 1000:
        x, y = x*x - y*y + x0, 2*x*y + y0
        if x*x + y*y > 4:
            break
        cont += 1

    return cont


def scale(interval, n, ini, fin):
    """Assign values to pixels in a scale"""
    return n*(fin - ini)/interval + ini

# Generating a blank file and getting access to each pixel
mandel = Image.new('RGB', (width, height), "white")
mapa = mandel.load()

# Colouring each pixel
for i in range(width):
    x0 = scale(width, i, x_inf, x_sup)

    for j in range(height):
        y0 = scale(height, j, y_inf, y_sup)
        result = mandelbrot(x0, y0)

        if result == 1000:
            # If after 1000 iterations it didn't escape, we will
            # believe it is in the Mandelbrot set and paint it black
            mapa[i, j] = (0, 0, 0)
        else:
            # Colouring the others depending on how long it took then
            # to escape
            mapa[i, j] = (result, result, result)

mandel.save(path)

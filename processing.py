from PIL import Image, ImageOps
import math

def Brightness(img_input, coldepth, tingkat_brightness=30):
    if coldepth != 24:
        img_input = img_input.convert("RGB")
    img_output = Image.new("RGB", img_input.size)
    pixels_output = img_output.load()
    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r, g, b = img_input.getpixel((i, j))
            pixels_output[i, j] = (
                max(0, min(255, r + tingkat_brightness)),
                max(0, min(255, g + tingkat_brightness)),
                max(0, min(255, b + tingkat_brightness)),
            )
    return img_output.convert(img_input.mode) if coldepth != 24 else img_output

#sobel
def sobel(img_input, coldepth):
    if coldepth != 24:
        img_input = img_input.convert("RGB")
    gx_kernel = [
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1],
    ]

    gy_kernel = [
        [-1, -2, -1],
        [0, 0, 0],
        [1, 2, 1],
    ]

    offset = len(gx_kernel) // 2
    img_output = Image.new("L", img_input.size)
    pixels = img_output.load()
    width, height = img_input.size

    for i in range(offset, width - offset):
        for j in range(offset, height - offset):
            gx = 0
            gy = 0
            for k in range(len(gx_kernel)):
                for l in range(len(gx_kernel[k])):
                    pixel = img_input.getpixel((i + k - offset, j + l - offset))
                    intensity = sum(pixel) / 3
                    gx += intensity * gx_kernel[k][l]
                    gy += intensity * gy_kernel[k][l]
            magnitude = int(math.sqrt(gx**2 + gy**2))
            magnitude = min(255, max(0, magnitude))
            pixels[i, j] = 255 - magnitude  

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output

def PowerLawoperasion(img_input, coldepth, C, gamma):
    if coldepth != 24:
        img_input = img_input.convert("RGB")
    # rumusnya = S = C*(r**gamma)
    img_output = Image.new("RGB", img_input.size)
    pixels_output = img_output.load()

    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r, g, b = img_input.getpixel((i, j))

            r_norm = r / 255.0
            g_norm = g / 255.0
            b_norm = b / 255.0

            _r = int(C * (r_norm**gamma) * 255.0)
            _g = int(C * (g_norm**gamma) * 255.0)
            _b = int(C * (b_norm**gamma) * 255.0)

            _r = max(0, min(255, _r))
            _g = max(0, min(255, _g))
            _b = max(0, min(255, _b))
            pixels_output[i, j] = (_r, _g, _b)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output

def Lontar(img_input, coldepth):
    img = Brightness(img_input, coldepth)
    img = sobel(img, coldepth)
    img = PowerLawoperasion(img, coldepth, C=1, gamma=3)

    return img

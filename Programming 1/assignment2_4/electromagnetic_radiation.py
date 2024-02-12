line = input("Enter the wavelength of the electromagnetic radiation in metres:\n")
wl = float(line)
if 0.0 < wl <= 10 * 10 ** (-12):
    print("The radiation is gamma radiation.")
    print("The radiation is highly dangerous!")
elif 0.01 * 10 ** (-9) < wl <= 10 * 10 ** (-9):
    print("The radiation is X-radiation.")
elif 10 * 10 ** (-9) < wl <= 400 * 10 ** (-9):
    print("The radiation is ultraviolet radiation.")
elif 400 * 10 ** (-9) < wl <= 700 * 10 ** (-9):
    print("The radiation is visible light.")
    if 400 * 10 ** (-9) < wl <= 450 * 10 ** (-9):
        print("The light is violet.")
    elif 450 * 10 ** (-9) < wl <= 490 * 10 ** (-9):
        print("The light is blue.")
    elif 490 * 10 ** (-9) < wl <= 560 * 10 ** (-9):
        print("The light is green.")
    elif 560 * 10 ** (-9) < wl <= 590 * 10 ** (-9):
        print("The light is yellow.")
    elif 590 * 10 ** (-9) < wl <= 630 * 10 ** (-9):
        print("The light is orange.")
    elif 630 * 10 ** (-9) < wl <= 700 * 10 ** (-9):
        print("The light is red.")
elif 700 * 10 ** (-9) < wl <= 1 * 10 ** (-3):
    print("The radiation is infrared light.")
elif 1 * 10 ** (-3) < wl <= 1:
    print("The radiation is microwaves.")
elif 1 < wl <= 100000 * 10 ** 3:
    print("The radiation is radio waves.")
elif wl == 0:
    print("The wavelength doesn't correspond to any type of radiation.")
elif wl < 0:
    print("The wavelength doesn't correspond to any type of radiation.")
elif wl > 100000 * 10 ** 3:
    print("The wavelength doesn't correspond to any type of radiation.")

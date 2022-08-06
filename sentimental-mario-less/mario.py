import cs50


# checking input
while True:
    h = cs50.get_int("Height: ")
    if h > 0 and h < 9:
        break

# drawing the pyramid
for i in range(h):
    print(" " * (h - i - 1), end="")
    print("#" * (i + 1), end="\n")
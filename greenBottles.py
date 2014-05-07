bottles = int(input("how many bottles do you have on your wall"))
import time

while bottles >= 1:
    print()
    print("{0} green bottles, hanging on the wall".format(bottles))
    time.sleep(1.5)
    print("{0} green bottles, hanging on the wall".format(bottles))
    time.sleep(1.5)
    print("And if 1 green bottle should acidentally fall,")
    time.sleep(1.5)
    print("They'll be {0} green bottles hanging on the wall.".format(bottles-1))

    bottles = bottles - 1

    time.sleep(2)
    print()
    print()

import sys
import mypackage # не понимаю, почему ругается - ведь импортирует
from mypackage.utils import *

print("Path:")
print(sys.path)

print("")
print("Package:")
print(mypackage)

if __name__ == "__main__":
    print("Module called directly")
else:
    print("Name is {}".format(__name__))

print(multiply(2, 3))

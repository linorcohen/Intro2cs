import random

file_loc = "C:/Users/DELL/CLionProjects/C_Workshop/ex2-linorcohen/cmake-build-debug/files_test/test"+str(i)+".txt"
f = open(file_loc, "w")
for i in range(5):
    num1 = random.randint(-10, 1001)
    num2 = random.randint(-10, 1001)
    num3 = random.randint(-10, 1001)
    f.write(str(num1) + "," + str(num2) + "," + str(num3))
    f.close()

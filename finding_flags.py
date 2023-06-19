import os

file_name = 1
i = 0

for i in range(1000):
    os.chdir("{}".format(file_name))
    f = open("flag.txt")
    print(f.readline())
    f.close()
    os.chdir("..")
    file_name = file_name + 1
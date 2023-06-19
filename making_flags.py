import os

file_name = 1
i = 0

for i in range(2000):
    os.mkdir("{}".format(file_name))
    os.chdir("{}".format(file_name))
    f = open("flag.txt", 'w')
    f.write("${null}")
    os.chdir("..")
    file_name = file_name + 1
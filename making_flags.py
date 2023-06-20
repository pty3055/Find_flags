import os
import random
import flag_list

file_name = 1
i = 0

for i in range(2000):
    os.mkdir("{}".format(file_name))
    os.chdir("{}".format(file_name))
    f = open("flag.txt", 'w')
    f.write("${null}")
    os.chdir("..")
    file_name = file_name + 1

flag_file = random.randrange(1,1001)

flag = random.choice(flag_list.flags)


os.chdir("{}".format(flag_file))
g = open("flag.txt","w")
g.write(line.replace("${null}", flag))
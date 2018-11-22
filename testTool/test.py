import argparse
import re
import random
import string

def findint(string):
    string = "xxxx[134]"
    return re.findall("\d+",string)[0]


# string = "int256[20]"
# sb = string[0:string.find("[")]
# sa = string[string.find("["):]
#
# print(int(re.findall("\d+",sb)[0]))
# print(int(re.findall("\d+",sa)[0]))


# for num in range(1):
#     print(num)

ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
print(ran_str)
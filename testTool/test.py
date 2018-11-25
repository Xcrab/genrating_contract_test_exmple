import argparse
import re
import random
import string
import binascii

# def generateData(type):
#
#     if type.find("int") is not -1:
#         #int类型的长度，例如int256中的256
#         dataLen = 0
#         #int数组的长度，单个数字为0
#         listLen = 0
#         reData = []
#         #把类型中的数字全部提取出来
#         lenList = re.findall("\d+",type)
#         #如果是int256[256]
#         if (len(lenList) >1) and type.find("[") is not -1:
#             dataLen = int(lenList[0])
#             listLen = int(lenList[1])
#         #如果是int256[]
#         elif (len(lenList) == 1) and type.find("[") is not -1:
#             dataLen = int(lenList[0])
#             listLen = random.randint(0,1024)
#         #如果是int256
#         else:
#             dataLen = int(lenList[0])
#             listLen = 1
#
#         for num in range(listLen):
#             if type[0] == "u":
#                 reData.append(random.randint(0,1 << dataLen))
#             else:
#                 reData.append(random.randint(-1 << (dataLen-1),1 << (dataLen - 1) - 1))
#         return reData

def reRanS():
    my_sample = ['a','b','c','d','e','f']
    my_sample += string.digits
    s = random.sample(my_sample, 20)
    return s

# for num in range(20):
#     print(reRanS())

s = ''.join(random.sample(string.ascii_letters + string.digits, 20))
print(s)
ss = binascii.b2a_hex(s.encode("utf8"))
sss = str(ss)
print("0x" + sss[2:len(sss)-1])
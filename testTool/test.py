import argparse
import re
import random
import string
import binascii

def generateData(type):

    if type.find("byte") is not -1:
        dataLen = 0
        listLen = 0
        reData = []
        lenList = re.findall("\d+",type)
        #byte
        if len(type) == 4:
            dataLen = 1
            listLen = 1
        #bytes32
        elif (len(lenList) == 1) and type.find("[") == -1:
            dataLen = int(lenList[0])
            listLen = 1
        #byte[32]
        elif (len(lenList) == 1) and type.find("[") is not -1:
            dataLen = 32
            listLen = int(lenList[0])
        #byte[]
        else:
            dataLen = 32
            listLen = random.randint(0,1024)

        for num in range(listLen):
            s = ''.join(random.sample(string.ascii_letters + string.digits, dataLen))
            ss = binascii.b2a_hex(s.encode("utf8"))
            sss = str(ss)
            reData.append("0x" + sss[2:len(sss)-1])
        return reData

print(generateData("byte[]"))
# s = ''.join(random.sample(string.ascii_letters + string.digits, 20))
# print(s)
# ss = binascii.b2a_hex(s.encode("utf8"))
# sss = str(ss)
# print("0x" + sss[2:len(sss)-1])
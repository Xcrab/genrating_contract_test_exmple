import argparse
import re
import random
import string
import binascii
import os
import demjson

#通用读取函数，读取json文件
def getJsonData(file_path):
    with open(file_path,"r") as f:
        data = f.read()
        f.close()
        data = demjson.decode(data,"utf-8")
        return data


def test():
    dir = "../Test_random_data/"
    item = "ChangeValue.json"
    no = random.randint(0,9)
    randData = getJsonData(os.path.join(os.path.abspath(dir), str(no) + item))

    exlines = []
    for oneFun in randData:
        typeData = ()
        exline = ("await instace.%s(" % (oneFun["name"]))

        for oneType in oneFun["types"]:
            for key,value in oneType.items():
                if key.find("int"):
                    if len(value) == 1:
                        exline = exline + str(value[0]) + ","
                    else:
                        exline = exline + str(value) + ","

                else:
                    if len(value) == 1:
                        exline = exline + "\"" + str(value[0]) + "\"" + ","
                    else:
                        exline = exline + "\"" + str(value) + "\"" + ","
        if exline[:len(exline)] == ",":
            exline = exline[:len(exline) - 1]
        exline += ")"
        exlines.append(exline)
    print(exlines)
    # exline = ""
    # for i in range(10):
    #     exline += ("it('test %d',async() => {" % i)
    #     for line in randData:
    #         funName = line.name
    #     exline += "})"
    # return randData
    return 0


test()
# dist = {"a":"1","b":2}
# for d in dist.items():
#     print(d.key())


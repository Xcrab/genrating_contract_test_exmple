import os
import argparse
import demjson
import re
import random
import string
from _pysha3 import keccak_224, keccak_256, keccak_384, keccak_512

#分类型生成不同的参数
def generateData(type):

    #如果参数类型为整形
    if type.find("int"):
        dataLen = 0
        listLen = 0
        #存放返回数据，为一个数组
        reData = []
        #如果为数组以"["为分界获取类型长度和数组长度
        #暂时还没考虑多维数组
        if type.find("["):
            dataLen = int(re.findall("\d+",type[0:type.find("[")])[0])
            listLen = int(re.findall("\d+", type[type.find("["):])[0])
        else:
            dataLen = int(re.findall("\d+", type)[0])
            listLen = 1

        for num in range(listLen):
            if type[0] == "u":
                reData.append(random.randint(0,1 << dataLen))
            else:
                reData.append(-1 << (dataLen-1),1 << (dataLen - 1) - 1)
        return reData


    if type.find("address"):
        return 2

    if type.find("bool"):
        flag = random.randint(0,1)
        if flag == 1:
            return True
        else:
            return False

    if type.find("byte"):
        dataLen = 0
        if len(type) == 4:
            dataLen = 1

        return 4

    if type.find("string"):
        sLen = random.randint(0,100)
        sData = ''.join(random.sample(string.ascii_letters + string.digits, sLen))
        return sData

    return 0


#处理签名，将所有的函数名与参数类型进行整理
def getFunSig(fun):
    if "name" not in fun:
        return None
    name = fun["name"]
    if "inputs" not in fun:
        return name+"()"
    else:
        inputs = fun["inputs"]
        types = list()
        for input in inputs:
            types.append(input["type"])
        dict = {"name":name,"types":types}
        return dict
    pass

#获取所有函数
def getFuns(abi):
    funs = list()
    for ele in abi:
        if "type" in ele and ele["type"] == "function":
           funs.append(ele)
    return funs
    pass

#获取文件的内容并转化为UTF8的json
def getAbi(file_path):
    with open(file_path,"r") as f:
        data = f.read()
        f.close()
        abi = demjson.decode(data,"utf-8")
        return abi

def solve_file(dir,item):
    #用于存储函数名name,参数类型types
    sigs = []
    # 设置生成测试用例的地址
    exmple_path = "../Test_case"

    # 判断是否有该路径，没有就创建
    if not os.path.exists(exmple_path):
        os.mkdir(exmple_path)
    #首先获取abi内容转化为json
    #然后之保留funtion部分abi
    abi = getAbi(os.path.join(os.path.abspath(dir), item))
    if abi:
        funs = getFuns(abi)
        if funs:
            for fun in funs:
                sigs.append(getFunSig(fun))

    print(abi)
    print(sigs)
    return 0

def solve_dir(dir):
    return 0

def main():
    global args
    parser = argparse.ArgumentParser()
    group = parser.add_argument_group('Model 1')
    groupex = group.add_mutually_exclusive_group(required=True)

    groupex.add_argument("-c", "--contract", type=str, dest="contract",
                         help="set the contract name whose function signature pair will be calculated")
    groupex.add_argument("-a", "--all", help="handle all contracts in directory specified by option '--bin_dir'",
                         action="store_true")
    groupex2 = group.add_mutually_exclusive_group(required=True)
    groupex2.add_argument("-ad", "--abi_dir", type=str, dest="abi_dir",
                          help="set the contracts' bin directory where to get function signature pair")
    args = parser.parse_args()
    if args.contract:
       if args.contract.find("."):
           args.contract = args.contract.split(".")[0]+".abi"
    if args.abi_dir:
        if args.abi_dir[-1] == "/":
            args.abi_dir = args.abi_dir[:len(args.abi_dir)-1]
    if not args.all:
        solve_file(args.abi_dir,args.contract)
    else:
        solve_dir(args.abi_dir)
    pass


if __name__=="__main__":
    main()
    pass
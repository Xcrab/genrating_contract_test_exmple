import os
import argparse
import demjson
import re
import random
import string
import copy
import binascii
from _pysha3 import keccak_224, keccak_256, keccak_384, keccak_512

#通用读取函数，读取json文件
def getJsonData(file_path):
    with open(file_path,"r") as f:
        data = f.read()
        f.close()
        data = demjson.decode(data,"utf-8")
        return data

#自动生成测试用例(test)
def generateTestCase(item):
    #读取随机产生的数据
    dir = "../Test_random_data/"
    no = random.randint(0, 9)
    randData = getJsonData(os.path.join(os.path.abspath(dir),str(no) + item + ".json"))

    #存放各个函数的执行语句 await instance.xxx(param1,param2,...)
    exlines = []
    for oneFun in randData:
        typeData = ()
        exline = ("await instace.%s(" % (oneFun["name"]))

        for oneType in oneFun["types"]:
            for key, value in oneType.items():
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
        if exline[:len(exline)].find(",") is not -1:
            exline = exline[:len(exline) - 1]
        exline += ")"
        exlines.append(exline)

    m_path = "../test_case/"
    if not os.path.exists(m_path):
        os.mkdir(m_path)
    f = open(os.path.join(os.path.abspath(m_path),item+"test.js"),"w+")
    try:
        f.write("const %s = artifacts.require(\"./%s.sol\")\n" % (item,item))
        f.write("contract('%s', async (accounts) => {\n" % item)
        f.write("const owner = accounts[0]\n")
        f.write("let instance\n")
        f.write("beforeEach('setup contract for each test',async() => {\n")
        f.write("instance = await %s.new()\n" % item)
        f.write("})\n")
        #根据随机生成的数据生成测试用例
        f.write("it('test %d',async() => {\n")
        for l in exlines:
            f.write(l + "\n")
        f.write("})\n")
        f.write("})\n")
    except:
        print("生成测试用例发生错误")
    return 0


#自动生成迁移文件(migrations)
#用文本生成的策略
def generateMigration(item):
    m_path = "../test_migrations_file/"
    if not os.path.exists(m_path):
        os.mkdir(m_path)
    f = open(os.path.join(os.path.abspath(m_path),item + ".js"),"w+")
    try:
        f.write("var %s = artifacts.require(\"./%s.sol\");\n" % (item,item))
        f.write("module.exports = function(deployer){\n")
        f.write("deployer.deploy(%s)\n" % (item))
        f.write("};\n")
    except:
        print("生成迁移文件发生错误")

def generateDataJson(sigs,itemJsonName,no = 0):
    exmple_path = "../Test_random_data"
    # 判断是否有该路径，没有就创建
    if not os.path.exists(exmple_path):
        os.mkdir(exmple_path)
    f = open(os.path.join(os.path.abspath(exmple_path), str(no) + itemJsonName), "w+")
    for items in sigs:
        alldata=[]
        alldata.clear()
        for item in items["types"]:
            #print(item)
            try:
                dict = {}
                dict.clear()
                reData = generateData(item)
                dict[item] = reData
                alldata.append(dict)
            except:
                print("ERROR")
                print(item)
        items["types"] = alldata
    print("生成测试数据")
    print(sigs)
    print("  ")
    ##########测试中间变量
    sjson = demjson.encode(sigs)
    f.write(sjson)
    f.close()
    print(sjson)

#分类型生成不同的参数
#如果是数组则返回[1,2,3,4,5],如果不是数组则返回单个数据[1]
def generateData(type):
    #如果参数类型为整形
    if type.find("int") is not -1:
        # int类型的长度，例如int256中的256
        dataLen = 0
        # int数组的长度，单个数字为0
        listLen = 0
        reData = []
        # 把类型中的数字全部提取出来
        lenList = re.findall("\d+", type)
        # 如果是int256[256]
        if (len(lenList) > 1) and type.find("[") is not -1:
            dataLen = int(lenList[0])
            listLen = int(lenList[1])
        # 如果是int256[]
        elif (len(lenList) == 1) and type.find("[") is not -1:
            dataLen = int(lenList[0])
            listLen = random.randint(0, 1024)
        # 如果是int256
        else:
            dataLen = int(lenList[0])
            listLen = 1
        for num in range(listLen):
            if type[0] == "u":
                reData.append(random.randint(0, 1 << dataLen))
            else:
                reData.append(random.randint(-1 << (dataLen - 1), 1 << (dataLen - 1) - 1))
        return reData

    if type.find("address") is not -1:
        #1、目前是随机生成
        #2、后续优化会从已有地址中随机选取地址
        reData = []
        s = ''.join(random.sample(string.ascii_letters + string.digits, 20))
        ss = binascii.b2a_hex(s.encode("utf8"))
        sss = str(ss)
        reData.append("0x" + sss[2:len(sss) - 1])
        return reData

    if type.find("bool") is not -1:
        flag = random.randint(0,1)
        if flag == 1:
            return True
        else:
            return False

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
        #byte[] & bytes
        else:
            dataLen = 32
            listLen = random.randint(0,1024)

        for num in range(listLen):
            s = ''.join(random.sample(string.ascii_letters + string.digits, dataLen))
            ss = binascii.b2a_hex(s.encode("utf8"))
            sss = str(ss)
            reData.append("0x" + sss[2:len(sss)-1])
        return reData

    if type.find("string") is not -1:
        reData = []
        sLen = random.randint(0,64)
        sData = ''.join(random.sample(string.ascii_letters + string.digits, sLen))
        reData.append(sData)
        return reData
    return -1

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

def solve_file(dir,item_flie):
    #用于存储函数名name,参数类型types
    sigs = []
    # 设置生成测试用例的地址
    exmple_path = "../Test_random_data"
    # 判断是否有该路径，没有就创建
    if not os.path.exists(exmple_path):
        os.mkdir(exmple_path)

    itemJsonName = item_flie[:len(item_flie)-3]+"json"
    itemJsName = item_flie[:len(item_flie)-4]
    #首先获取abi内容转化为json
    #然后只保留funtion部分abi
    abi = getAbi(os.path.join(os.path.abspath(dir), item_flie))
    if abi:
        funs = getFuns(abi)
        if funs:
            for fun in funs:
                sigs.append(getFunSig(fun))

    #生成随机数据测试文件
    for i in range(10):
        #注意这里是深拷贝
        cpsigs = copy.deepcopy(sigs)
        generateDataJson(cpsigs,itemJsonName,i)
    #自动生成迁移文件
    generateMigration(itemJsName)
    #自动生成测试用例
    generateTestCase(itemJsName)
    pass

#批量处理文件
def solve_dir(dir):
    dirs = os.listdir(dir)
    for item in dirs:
        try:
            solve_file(dir,item)
        except:
            continue
    pass

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
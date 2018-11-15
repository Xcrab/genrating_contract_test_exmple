import os
import argparse



#读取路径中的文件内内容
def get_abi_sign(file_path):
    # 用来存放每行的内容
    data = []
    data.clear()
    with open(file_path,"r") as f:
        for line in f:
            data.append(line.strip())
        f.close()
        #调试使用语句
        print(data)
        return data
    pass

#分解函数签名
def disassemble_sign(txtData):
    signBefore = []
    signAfter = []
    for line_no in range(len(txtData)):
        ss = txtData[line_no]
        signBefore.append(ss.split(":")[0])
        signAfter.append(ss.split(":")[1])
    return signBefore,signAfter

#根据数据类型随机生成测试数据
def genrating_rand_data():
    return 0

#生成单个合约的测试用例
def solve_file(abi_sign,dir):
    #设置生成测试用例的地址
    exmple_path = "../Test_case"

    #判断是否有该路径，没有就创建
    if not os.path.exists(exmple_path):
        os.mkdir(exmple_path)

    txtData = get_abi_sign(os.path.join(os.path.abspath(dir),abi_sign))

    #将原始的函数签名进行分离
    signBefore,signAfter = disassemble_sign(txtData)
    print(signBefore)
    print(signAfter)

    print(txtData)
    pass

#生成多个合约的测试用例
def solve_dir(dir):
    return 0





def main():
    global args
    parser = argparse.ArgumentParser()
    parser.description = "将得到的函数签名自动生成测试用例"

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-as","--abi_sign",type = str,help="选择要生成测试用例的合约的函数选择器",
                       dest="abi_sign")
    group.add_argument("-a","--all",help="将目录下所有的函数选择器都生成测试用例",dest="all",
                       action="store_true")

    parser.add_argument("-asd","--abi_sign_dir",type=str,help="所要生成测试用例文件的目录",
                        dest="abi_sign_dir")

    args = parser.parse_args()

    if args.abi_sign:
        if args.abi_sign.find("."):
            args.abi_sign = args.abi_sign.split(".")[0] + ".abi"

    if args.abi_sign_dir:
        if args.abi_sign_dir[-1] == "/":
            args.abi_sign_dir = args.abi_sign_dir[:len(args.abi_sign_dir) - 1]

    if not args.all:
        #处理单个文件
        solve_file(args.abi_sign,args.abi_sign_dir)
    else:
        #处理文件夹里面所有文件
        return 0
    return 0

if __name__=="__main__":
    main()
    pass
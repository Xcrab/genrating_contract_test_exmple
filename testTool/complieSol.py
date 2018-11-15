import os
import argparse

#编译单个文件
def solve_file(contract,sol_dir):
    #设置编译路径
    sabi_path = "../test_exmple_abi"
    sbin_path = "../test_exmple_bin"

    #判断是否有该文件，没有就生成
    if not os.path.exists(sabi_path):
        os.mkdir(sabi_path)
    if not os.path.exists(sbin_path):
        os.mkdir(sbin_path)

    #启动编译并保存到指定路径
    ins = "solc --abi --overwrite " + sol_dir + "/" + contract + " -o " + sabi_path
    sabi = os.popen(ins)
    ins = "solc --bin --overwrite " + sol_dir + "/" + contract + " -o " + sbin_path
    sbin = os.popen(ins)

    #调试使用
    print(sabi)
    print(sbin)

#处理同一个目录下的所有文件
def solve_dir(sol_dir):
    dirs = os.listdir(sol_dir)
    for item in dirs:
        try:
            solve_file(item,sol_dir)
        except:
            continue

def main():
    # parser = argparse.ArgumentParser()
    # parser.add_argument("echo")
    # args = parser.parse_args()
    # print(args)
    # print(args.echo)
    global args

    parser = argparse.ArgumentParser()
    parser.description = "编译所有在制定目录下智能合约文件"

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-c","--contract",type = str,help="选择要编译的合约",dest="contract")
    group.add_argument("-a","--all",help="处理目录下的所有合约",dest="all",action="store_true")

    parser.add_argument("-sd","--sol_dir",type=str,help="所要编译文件的目录",dest="sol_dir")

    args = parser.parse_args()

    if args.contract:
        if args.contract.find("."):
            args.contract = args.contract.split(".")[0]+".sol"

    if args.sol_dir:
        if args.sol_dir[-1] == "/":
            args.sol_dir = args.sol_dir[:len(args.sol_dir) - 1]

    if not args.all:
        #处理单个文件
        solve_file(args.contract,args.sol_dir)
    else:
        #处理文件夹里面所有文件
        solve_dir(args.sol_dir)


if __name__ == "__main__":
    main()
    pass
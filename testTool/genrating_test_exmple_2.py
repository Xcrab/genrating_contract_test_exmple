import os
import argparse
import demjson
from _pysha3 import keccak_224, keccak_256, keccak_384, keccak_512

def getAbi(file_path):
    with open(file_path,"r") as f:
        data = f.read()
        f.close()
        abi = demjson.decode(data,"utf-8")
        return abi

def solve_file(dir,item):
    # 设置生成测试用例的地址
    exmple_path = "../Test_case"

    # 判断是否有该路径，没有就创建
    if not os.path.exists(exmple_path):
        os.mkdir(exmple_path)

    abi = getAbi(os.path.join(os.path.abspath(dir), item))
    print(abi)
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
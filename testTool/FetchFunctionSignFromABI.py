import os
import re
import  sys
import  argparse
import demjson
import  sha3
import  hashlib
from _pysha3 import keccak_224, keccak_256, keccak_384, keccak_512

def getFiles(path):
    files = os.listdir(path)
    return files
    pass

def getRawContractName(file_name):
    pattern = re.compile(r'\s*(\S+)\..*')
    m = pattern.match(file_name)
    if m:
        name = m.group(1)
        return name
    return None
    pass

def getAbi(file_path):
    with open(file_path,"r") as f:
        data = f.read()
        f.close()
        abi = demjson.decode(data,"utf-8")
        return abi

def getFuns(abi):
    funs = list()
    for ele in abi:
        if "type" in ele and ele["type"] == "function":
           funs.append(ele)
    return funs
    pass

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
        typesStr = ",".join(types)
        return name+"("+typesStr+")"
    pass

def getFunId(Sig):
    # hashlib.s?
    s = keccak_256()
    s.update(Sig.encode("utf8"))
    hex = s.hexdigest()
    bytes4 = "0x"+hex[:8]
    return bytes4
    pass

def test():
    sig = "approve(address,uint256)"
    print(getFunId(sig))
    pass

def solve_file(abi_dir,abi_item):
    funid_path = "../test_exmple_abi_sign/"
    if not os.path.exists(funid_path):
        os.mkdir(funid_path)
    f = open(os.path.join(os.path.abspath(funid_path), abi_item), "w+")
    abi = getAbi(os.path.join(os.path.abspath(abi_dir), abi_item))
    if abi:
            funs = getFuns(abi)
            if funs:
                for fun in funs:
                    sig = getFunSig(fun)
                    id = getFunId(sig)
                    f.write(":".join([id, sig]))
                    f.write("\n")
    f.close()
    pass

def solve_dir(abi_dir):
    dirs = os.listdir(abi_dir)
    for item in dirs:
        try:
            solve_file(abi_dir,item)
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
    #test()
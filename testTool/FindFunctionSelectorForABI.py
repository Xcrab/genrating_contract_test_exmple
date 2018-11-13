import os
import sys
import argparse

Code_lines = []
Jump_table = {}

##抽取函数签名
def readFunSigs():
    funSigs_line_no = 0
    fun_sigs_line_no = []
    funSigs = []
    while funSigs_line_no < len(Code_lines):
        if Code_lines[funSigs_line_no] == "STOP":
            break
        if Code_lines[funSigs_line_no].startswith("PUSH4") and Code_lines[funSigs_line_no + 1] == "EQ":
            funSigs.append([Code_lines[funSigs_line_no].split()[1], int(Code_lines[funSigs_line_no + 2].split()[1], 16)])
        funSigs_line_no += 1
    return funSigs
    pass

def solve_dir(dir):
    return 0

##将初始化部分代码删除，保留运行时的代码
def clearLines(lines):
    global Code_lines
    nlines = []
    for line in lines:
        Code_lines.append(line.split(":")[1].strip())
    runtime_part_line_no = 0
    for line_no in range(len(Code_lines)):
        line = Code_lines[line_no]
        ##文章的工具初始化结束标记为CODECOPY
        if line == "CODECOPY" and Code_lines[line_no + 1] == "PUSH1 0x00" and Code_lines[line_no + 2] == "RETURN":
            if Code_lines[line_no + 3] == "STOP":
                runtime_part_line_no = line_no + 4
            else:
                runtime_part_line_no = line_no + 3
            break
    if runtime_part_line_no > 0:
        delta = int(lines[runtime_part_line_no].split(":")[0])
        Code_lines = Code_lines[runtime_part_line_no:]
        lines = lines[runtime_part_line_no:]
    else:
        dalte = 0
    print("dalte:",delta)
    for line_no in range(len(Code_lines)):
        Jump_table[int(lines[line_no].split(":")[0].strip()) - delta] = line_no
    return Code_lines

def solve_file(bin_dir,bin_item):
    global args
    if not os.path.exists("./sig"):
        os.mkdir("./sig")
    disam_data_lines = os.popen('evm disasm ' + bin_dir + "/" + bin_item).readlines()
    Code_lines.clear()
    Jump_table.clear()
    try:
        Lines = clearLines(disam_data_lines[1:])
        print(Lines)
    except IndexError:
         return
    fun_sigs = readFunSigs()
    print(fun_sigs)



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
    groupex2.add_argument("-bd", "--bin_dir", type=str, dest="bin_dir",
                          help="set the contracts' bin directory where to get function signature pair")
    args = parser.parse_args()
    if args.contract:
        if args.contract.find("."):
            args.contract = args.contract.split(".")[0] + ".bin"
    if args.bin_dir:
        if args.bin_dir[-1] == "/":
            args.bin_dir = args.bin_dir[:len(args.bin_dir) - 1]
    if not args.all:
        solve_file(args.bin_dir, args.contract)
    else:
        solve_dir(args.bin_dir)
    pass

if __name__ == "__main__":
    main()
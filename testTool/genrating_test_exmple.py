import os
import argparse

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

    return 0

if __name__=="__main__":
    main()
    pass
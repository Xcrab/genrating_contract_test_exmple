import argparse
import re
import random
import string
import binascii
import os
import demjson


#构造合约账户池程池
def contructAccountsPool():

    account_path = "../test_Accounts/"
    if not os.path.exists(account_path):
        os.mkdir(account_path)
    f = open(os.path.join(os.path.abspath(account_path),"Accounts.json"),"w+")
    dict={}
    accountsStorePath = "/home/xcrab/ethTest"
    ins = ("geth --datadir \"%s\" account list" % accountsStorePath)
    accountData = os.popen(ins)
    for line in accountData.readlines():
        accountNO = line[:7] + line[9]
        account = line[len(line)-41:len(line)-1]
        dict[accountNO] = account

    fjson = demjson.encode(dict)
    print(fjson)
    print(dict)
    f.write(fjson)
    f.close()

contructAccountsPool()
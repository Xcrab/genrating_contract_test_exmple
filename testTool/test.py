import argparse
import re
import random
import string
import binascii
import os

def generateMigration(item):
    m_path = "../test_migrations_file/"
    if not os.path.exists(m_path):
        os.mkdir(m_path)
    f = open(os.path.join(os.path.abspath(m_path),item+".js"),"w+")
    f.write("var %s = artifacts.require('./%s.sol');\n" % (item,item))
    f.write("module.exports = function(deployer){\n");
    f.write("deployer.deploy(%s)\n" % (item));
    f.write("};\n")


generateMigration("Hello")
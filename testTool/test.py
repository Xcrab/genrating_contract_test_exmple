import argparse


def findint(string):
    string = "xxxxxxxintxxxxxx"
    if string.find("int"):
        return True
    else:
        return False



print(findint("xxx"))

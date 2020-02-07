import time
import os



def aryLenSync(ary1, ary2):
    i = 0
    if len(ary1) == len(ary2):
        i
    else:
        if len(ary1) > len(ary2):
            i = len(ary1) - len(ary2)
            for ii in range(0,i):
                ary2.append('@@@')
        else:
            i = len(ary2)-len(ary1)
            for ii in range(0,i):
                ary1.append('@@@')




def getConvData(str):
    return str.replace('\n','')


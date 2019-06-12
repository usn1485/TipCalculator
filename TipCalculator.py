import math
import os
import random
import re
import sys

n1= float(input())
Bill=int(n1)
n2= float(input())
percent=int(n2)
#splitBoolean= input()
n3=float(input())
noOfppl=int(n3)

'''Bill=100
percent=15
noOfppl=3
tipSplit=0'''

def tipCalculator(bill,tip):
    Tip = bill*( tip /100 )
    return Tip

Tipsplit = tipCalculator(Bill,percent)    
print(Tipsplit)
if noOfppl > 1:
     FinalTip=Tipsplit/noOfppl
     print(f"Tip Split for {noOfppl} is:{FinalTip}")
else :
     FinalTip=Tipsplit
     print(f"Tip for this table is : {FinalTip}")
#print(FinalTip)

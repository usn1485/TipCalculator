#Importing the required Modules
import math
import os
import random
import re
import sys

#Taking user input for Bill, Percent, Split Boolean and No of ppl to split the Tip between.

Bill=float(input("Enter the Bill Amount:"))


# Wrote a function to calculate Tip.
def tipCalculator(bill,percent):
  if(percent<1):
    tipPercent=percent*100
    print(f"TipPercent after converting:{tipPercent}")
    Tip = bill*( tipPercent / 100 )  
  else:
    Tip = bill*( percent / 100 )

  return Tip

if(Bill>0):
     percent=float(input("Enter the Tip Percent:"))

     if(percent>0):
          Tip = tipCalculator(Bill,percent) 
          print(Tip)
          splitBool=(input("Do you want to split the tip? y/n?").strip().upper())
          print(type(splitBool))
          print(splitBool)
          if splitBool=="Y":
               noOfppl=int(input("Enter the No. of ppl you want to split the tip in:"))
               if(noOfppl>1):                
                    FinalTip= round(( Tip/noOfppl),2)
                    print(f"Tip Split for {noOfppl} people is:${FinalTip} cents each.")
               elif (noOfppl==1):
                    print(f"Tip for this table is:${round(Tip,2)}")   
               else : 
                    print("Tip should be paid by 1 or more people.") 
          elif splitBool=="N":
               print(f"Tip for ${Bill} bill amount is:${round(Tip,2)}")
          else: 
               print("Please Enter Y or N characters only.")
         
     else:
       print("Percent must be positive")
else: 
     print("The Bill amount must be greater than zero")

 
    


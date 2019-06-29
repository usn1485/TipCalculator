#Import the required Modules
import math
import os


#Take user input for Bill amount.
Bill=float(input("Enter the Bill Amount:"))

# Write function to calculate Tip.
def tipCalculator(bill,percent):
    # convert the percent input to whole number if it is given as 0.15 
  if(percent<1):
    tipPercent=percent*100
    Tip = bill*( tipPercent / 100 )                   
  else:
    Tip = bill*( percent / 100 )
  return Tip

# Verify if Bill amount is Positive else throw error
if(Bill>0):
     #Take user input for Tip Percent
     percent=float(input("Enter the Tip Percent:"))

     if(percent>0):
          Tip = tipCalculator(Bill,percent) 

          #Check if user want to split the Tip amount?
          splitBool=(input("Do you want to split the tip? y/n?").strip().upper())
          
          #Verify if user wants to split and then split the Tip amount.
          if splitBool=="Y":
               # Take user input for no of people they want to split Tip between.
               noOfppl=int(input("Enter the No. of ppl you want to split the tip in:"))

               #If no of people are more than 1 then do the calculation to divide tip equally.
               if(noOfppl>1):                
                    FinalTip= round(( Tip/noOfppl),2)
                    print(f"Tip Split for {noOfppl} people is ${FinalTip}cents each.")
               #If user changes mind and decides not to split. 
               elif (noOfppl==1):
                    print(f"Tip for this table is ${round(Tip,2)}cents.")  
               # if user enters 0 or something else.       
               else : 
                    print("Tip should be paid by 1 or more people. Please check the input.") 
          # If user doesn't want to split the Tip amount, calculate the Tip for per table          
          elif splitBool=="N":
               print(f"Tip for this table is ${round(Tip,2)}cents")
          #If user enters Other than Y/ N characters, print warning.      
          else: 
               print("Please Enter Y or N characters only.")
     #if user enters Negative or 0 Percent value, print warning  
     else:
       print("Percent must be positive")
#If user enters the Bill amount 0 or negative, print warning       
else: 
     print("The Bill amount must be greater than zero")

 
    


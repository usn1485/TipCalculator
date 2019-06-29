#Import the required Modules
import math
import os


#Take user input for bill amount.
bill=float(input("Enter the bill Amount:"))

# Write function to calculate tip.
def tipCalculator(bill,percent):
    # convert the percent input to whole number if it is given as 0.15 
  if(percent<1):
    tipPercent=percent*100
    tip = bill*( tipPercent / 100 )                   
  else:
    tip = bill*( percent / 100 )
  return tip

# Verify if bill amount is Positive else throw error
if(bill>0):
     #Take user input for tip Percent
     percent=float(input("Enter the tip Percent:"))

     # Verify if Percentage is Positive else throw error
     if(percent>0):

          # Calculate Tip for the given Bill Amount.
          tip = tipCalculator(bill,percent) 

          #Check if user want to split the tip amount.
          splitBool=(input("Do you want to split the tip? y/n?").strip().upper())
          
          #Verify if user wants to split and then split the tip amount.
          if splitBool=="Y":
               # Take user input for no of people they want to split tip between.
               noOfppl=int(input("Enter the No. of ppl you want to split the tip in:"))

               #If no of people are more than 1 then do the calculation to divide tip equally.
               if(noOfppl>1):                
                    FinalTip= round(( tip/noOfppl),2)
                    print(f"tip Split for {noOfppl} people is ${FinalTip}cents each.")
               #If user changes mind and decides not to split. 
               elif (noOfppl==1):
                    print(f"tip for this table is ${round(tip,2)}cents.")  
               # if user enters 0 or something else.       
               else : 
                    print("tip should be paid by 1 or more people. Please check the input.") 
          # If user doesn't want to split the tip amount, calculate the tip for per table          
          elif splitBool=="N":
               print(f"tip for this table is ${round(tip,2)}cents")
          #If user enters Other than Y/ N characters, print warning.      
          else: 
               print("Please Enter Y or N characters only.")
     #if user enters Negative or 0 Percent value, print warning  
     else:
       print("Percent must be positive")
#If user enters the bill amount 0 or negative, print warning       
else: 
     print("The bill amount must be greater than zero")

 
    


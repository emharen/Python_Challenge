# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 15:27:38 2019

@author: emhar
"""
#import libraries
import os
import csv

#create lists 
PL=[]
Months=[]
change=[]

#Open and read budget_data.csv 
csvpath = os.path.join('budget_data.csv')

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    #label header 
    csv_header = next(csvreader)
   
 #Fill Profit/Losses(PL) and Months lists 
    for line in csvreader:
      
     
        PL.append(int(line[1]))

        Months.append(line[0]) 
        
#fill the change in profits list 
for i in range(len(PL)-1):
    
    change.append(int(PL[i+1]-PL[i]))
average_change=round((sum(change)/len(change)),2)
    
#print financial analysis sheet 
print("Financial Analysis")
print("........................................")
print("Total Months: "+ str(len(Months)))
print("Total: $" +str(sum(PL)))
print("Greatest Increase in Profits: $" + str(max(change)))
print("Greatest Decrease in Profits : $"+ str(min(change)))
print("Average Change: $" + str(average_change))

# Set variable for output file
output_file = os.path.join("PyBank_final.txt")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write in rows
    writer.writerow(["Financial Analysis"])
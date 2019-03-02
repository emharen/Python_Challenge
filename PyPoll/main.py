# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 15:28:02 2019

@author: emhar
"""

#import libraries
import os
import csv

#Create Lists
V_ID=[]
County=[]
Candidate=[]
UniqueList=[]
percent=[]

#Open and read election_data.csv 
csvpath = os.path.join('election_data.csv')

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
  #label header 
    csv_header = next(csvreader)
   
   #Append lists  
    for line in csvreader:
        V_ID.append(line[0])
        County.append(line[1])
        Candidate.append(line[2])
    
      #Append list of unique candidates
        if line[2] not in UniqueList:
            UniqueList.append(line[2])
            
#Create dictionary with total number of votes for each candidate 
result_dict = dict( [ (i, Candidate.count(i)) for i in set(Candidate) ] )            
length=int(len(V_ID))


#find percentage of total votes for each candidate 
for x in result_dict:
    number = result_dict[x]
    key = x
    percent.append(round(((int(number)) / length)*100,2))
  
    
#Print final report 
print("Election Results")
print(".........................")
print("Total Votes: " + str(length))
print(".........................")
print(UniqueList[0]+": " + "(" + str(result_dict["Khan"]) + ") " + str(percent[3]) + "%")
print(UniqueList[1]+": " + "(" + str(result_dict["Correy"]) + ") " + str(percent[1]) + "%")
print(UniqueList[2]+": " + "(" + str(result_dict["Li"]) + ") " + str(percent[2]) + "%")
print(UniqueList[3]+": " + "(" + str(result_dict["O'Tooley"]) + ") " + str(percent[0]) + "%")
print(".........................")
#find max value in dictionary and print the key 
key = max(result_dict, key = lambda k: result_dict[k])  
print(f"Winner is: {key}")  


# Set variable for output file
output_file = os.path.join("PyPoll_final.txt")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write in rows
    writer.writerow(["Election Results"])
    writer.writerow(["........................."])
    writer.writerow(['Total Votes: ' + str(length)])
    writer.writerow(["........................."])
    writer.writerow([UniqueList[0]+": " + "(" + str(result_dict["Khan"]) + ") " + str(percent[3]) + "%"])
    writer.writerow([UniqueList[1]+": " + "(" + str(result_dict["Correy"]) + ") " + str(percent[1]) + "%"])
    writer.writerow([UniqueList[2]+": " + "(" + str(result_dict["Li"]) + ") " + str(percent[2]) + "%"])
    writer.writerow([UniqueList[3]+": " + "(" + str(result_dict["O'Tooley"]) + ") " + str(percent[0]) + "%"])
    writer.writerow(["........................."])
    writer.writerow(["Winner is: " + key])
 

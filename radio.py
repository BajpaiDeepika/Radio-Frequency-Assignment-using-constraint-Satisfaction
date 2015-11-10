
# Constraints Satisfaction Problem

# 
# Name: Deepika Bajpai
# User Id: dbajpai
#
#*********************************************************************************************************************************************************
# Report:
 
#                                1. Problem Formulation: 
# The problem was formulated  in three steps using the problem of map-coloring:
#
# 1. First I sorted the states in terms of maximum neighbors to least number of neighbors. This gave me the most constrained states.
# The the next step was to make a function to assign frequencies to states that two adjacent states(neighbors) should not get the same frequency. For this I created a dictionary for all neighbors and then I ran the loop so that for every
# state, assign the frequency from the frequency list if it has not been already assigned to any of its neighbor states.
# This approach followed the algorithm of arc consistency.
#
# 2. The next step is to check the constraints through the input legacy constraints file.I created two separate lists for storing the constrained states and their frequencies and fixed them.
# Then I deleted the constrained states from my total states list and started assigning frequencies to the rest of the states using arc consistency.
# 
# 3. Backtracking:Whenever the program will run out of frequencies to assign to the states as all the frequencies have already been taken by its neighbors, it uses the 
#  the concept of backtracking .It will take the neighbors of the state for which frequency assignment was none and will start re-assigning frequency to them.It 
#  eeps the track of number of backtracks using a global variable.
#
#  
#                    
#

##**********************************************************************************************************************************************************************************

import sys
from collections import OrderedDict
from pprint import pprint
import os
AllStates = []
CountBacktrack=0
FinallistOfStates=[]
with open('adjacent-states','r') as f:
            for line in f:
 
                AllStates.append(line.split(None, 1)[0]) # add only first word      
Frequency = ['A', 'B', 'C', 'D']
freq1=Frequency[:]
neighbors = {}        
neighbors['Alaska']=[]
neighbors['Alabama']=['Mississippi','Tennessee','Georgia','Florida']
neighbors['Arkansas']=['Missouri','Tennessee','Mississippi','Louisiana','Texas','Oklahoma']
neighbors['Arizona']=['California','Nevada','Utah','Colorado','New_Mexico']
neighbors['California']=['Oregon','Nevada','Arizona']
neighbors['Colorado']=['Wyoming','Nebraska','Kansas','Oklahoma','New_Mexico','Arizona Utah']
neighbors['Connecticut']=['New_York','Massachusetts','Rhode_Island']
neighbors['Delaware']=['Maryland','Pennsylvania','New_Jersey']
neighbors['Florida']=['Alabama','Georgia']
neighbors['Georgia']=['Florida','Alabama','Tennessee','North_Carolina','South_Carolina']
neighbors['Hawaii']=[]
neighbors['Iowa']= ['Minnesota','Wisconsin','Illinois','Missouri','Nebraska','South_Dakota']
neighbors['Idaho']= ['Montana','Wyoming','Utah','Nevada','Oregon','Washington']
neighbors['Illinois']=['Indiana','Kentucky','Missouri','Iowa','Wisconsin']
neighbors['Indiana']=['Michigan','Ohio','Kentucky','Illinois']
neighbors['Kansas']=['Nebraska','Missouri','Oklahoma','Colorado']
neighbors['Kentucky']=['Indiana','Ohio','West_Virginia','Virginia','Tennessee','Missouri','Illinois']
neighbors['Louisiana']=['Texas','Arkansas','Mississippi']
neighbors['Massachusetts']=['Rhode_Island','Connecticut','New_York','New_Hampshire','Vermont']
neighbors['Maryland']=['Virginia','West_Virginia','Pennsylvania','Delaware']
neighbors['Maine']=['New_Hampshire']
neighbors['Michigan']=['Wisconsin','Indiana','Ohio']
neighbors['Minnesota']=['Wisconsin','Iowa','South_Dakota','North_Dakota']
neighbors['Missouri']=['Iowa','Illinois','Kentucky','Tennessee','Arkansas','Oklahoma','Kansas','Nebraska']
neighbors['Mississippi']=['Louisiana','Arkansas','Tennessee','Alabama']
neighbors['Montana']=['North_Dakota','South_Dakota','Wyoming','Idaho']
neighbors['North_Carolina']=['Virginia','Tennessee','Georgia','South_Carolina']
neighbors['North_Dakota']=['Minnesota','South_Dakota','Montana']
neighbors['Nebraska']=['South_Dakota','Iowa Missouri','Kansas','Colorado','Wyoming']
neighbors['New_Hampshire']=['Vermont','Maine','Massachusetts']
neighbors['New_Jersey']=['Delaware','Pennsylvania','New_York']
neighbors['New_Mexico']=['Arizona','Utah','Colorado','Oklahoma','Texas']
neighbors['Nevada']=['Idaho','Utah','Arizona','California','Oregon']
neighbors['New_York']=['New_Jersey','Pennsylvania','Vermont','Massachusetts','Connecticut']
neighbors['Ohio']=['Pennsylvania','West_Virginia','Kentucky','Indiana','Michigan']
neighbors['Oklahoma']=['Kansas','Missouri','Arkansas','Texas','New_Mexico','Colorado']
neighbors['Oregon']=['California','Nevada','Idaho','Washington']
neighbors['Pennsylvania']=['New_York','New_Jersey','Delaware','Maryland','West_Virginia','Ohio']
neighbors['Rhode_Island']=['Connecticut','Massachusetts']
neighbors['South_Carolina']=['Georgia','North_Carolina']
neighbors['South_Dakota']=['North_Dakota','Minnesota','Iowa','Nebraska','Wyoming','Montana']
neighbors['Tennessee']=['Kentucky','Virginia','North_Carolina','Georgia','Alabama','Mississippi','Arkansas','Missouri']
neighbors['Texas']=['New_Mexico','Oklahoma','Arkansas','Louisiana']
neighbors['Utah']=['Idaho','Wyoming','Colorado','New_Mexico','Arizona','Nevada']
neighbors['Virginia']=['North_Carolina','Tennessee','Kentucky','West_Virginia','Maryland'] 
neighbors['Vermont']=['New_York','New_Hampshire','Massachusetts']
neighbors['Washington']=['Idaho','Oregon']
neighbors['Wisconsin']=['Michigan','Minnesota','Iowa','Illinois']
neighbors['West_Virginia']=['Ohio','Pennsylvania','Maryland','Virginia','Kentucky']
neighbors['Wyoming']=['Montana','South_Dakota','Nebraska','Colorado','Utah Idaho']

AssignedFreuency = {}  # A dictionary which will store the State Name as Key and it frequency as Value
constState=[]  #It will store the states having constraints
ConstFreq=[]   #It will store the frequency of constrained states
   
def IsValidFrequency(state, frequency):
    
    for neighbor in neighbors.get(state): 
        frequency_of_neighbor = AssignedFreuency.get(neighbor)
                 
        if frequency_of_neighbor == frequency:
            return False
    return True

def Assign_frequency(state):
    
    for frequency in Frequency:
       
        if (IsValidFrequency(state, frequency)==True):
            return frequency
       
def backtrack(state):
    
    global CountBacktrack
    CountBacktrack=CountBacktrack+1    
    for neighbor in neighbors.get(state):
        freq1.remove(AssignedFreuency[neighbor])  
        for frequ in freq1:
            if (IsValidFrequency(neighbor, frequ)==True):
                freq1.append(frequ)
                return frequ
                
        break
               
def main():
    constState=[]  #It will store the states having constraints
    ConstFreq=[]   #It will store the frequency of constrained states
    ConstrainFileInput=sys.argv[1]
    if os.stat(ConstrainFileInput).st_size <= 1:
        print("")
    else:
        with open(ConstrainFileInput,'r') as f1:
            for line in f1:
                constState.append(line.split(None, 1)[0])
                ConstFreq.append(line.split(None)[1])
            #print constState
            #print ConstFreq

    
    N=len(constState)
    NewAllStates=AllStates[:]
    data = OrderedDict(sorted(neighbors.items(), key=lambda x: len(x[1])))
    FinallistOfStates=data.keys()
    
    for i in range(0,N):        
        AssignedFreuency[constState[i]]=ConstFreq[i]
        FinallistOfStates.remove(constState[i])
        
    #print len(FinallistOfStates)
    for state in reversed(FinallistOfStates):      
        AssignedFreuency[state] = Assign_frequency(state)
        if AssignedFreuency[state] is None:
            AssignedFreuency[state]=backtrack(state)
    return AssignedFreuency

AssignedFreuency=main()
#print AssignedFreuency
#*********************Printing on Console***********************************************************************************
for key, value in AssignedFreuency.iteritems() :
    print key, value
print "Number of backtracks:",CountBacktrack
#*********************Printing on New Output Text File "Results.txt"*********************************************************************************** 
filename ="results.txt"
NewOutputFile = open(filename, 'w')
for key, value in AssignedFreuency.iteritems() :
    NewOutputFile.write("%s %s\n" % (key,value))
NewOutputFile.write("Number of backtracks:")
NewOutputFile.write("%s" % CountBacktrack)
NewOutputFile.close()

#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import random

#-------------------------------F I T N E S S      F U N C T I O N--------------------------------------
def fitnessFunction (my_list):

  arr=np.array(my_list)


  temp1=0
  temp2=0
  fitnessCounter=0
  fitnessValue=0

  for x in range (0,8):
    #print ('Evaluating for QUEEN ' + str(x+1))

    #---EVALUATING DIAGONALS TOWARDS THE RIGHT
    count=1
    for i in range (x,7):

      a=arr[x]

      temp1=a+count
      temp2=a-count
      b=arr[x+count]

      if (temp1<=8):
        if (temp1==b):
          #print('collision found at column: ' + str(i+1) + ", row: " + str(b))
          fitnessCounter=fitnessCounter+1


      if (temp2>=1): 
        if (temp2==b):
          #print('collision found at column: ' + str(i+1) + ", row: " + str(b))
          fitnessCounter=fitnessCounter+1
      
      count=count+1

    #---EVALUATING HORIZONTALS TOWARDS THE RIGHT
    cc1=arr[x]
    for i in range (x,7):
      
      b=arr[i+1]
      if (b==cc1):
        #print('collision found at column: ' + str(i+1) + ", row: " + str(cc1))
        fitnessCounter=fitnessCounter+1


    #---EVALUATING DIAGONALS TOWARDS THE LEFT
    count2=1;
    for i in range(x,0,-1):
      a=arr[x]

      temp1=a+count2
      temp2=a-count2
      b=arr[x-count2]
      if (temp1<=8):
        if (temp1==b):
          #print('collision found at column: ' + str(i-1) + ", row: " + str(b))
          fitnessCounter=fitnessCounter+1


      if (temp2>=1): 
        if (temp2==b):
          #print('collision found at column: ' + str(i-1) + ", row: " + str(b))
          fitnessCounter=fitnessCounter+1

      count2=count2+1

    #---EVALUATING HORIZONTALS TOWARDS THE LEFT      
    cc2=arr[x]
    for i in range (x,0,-1):
      
      b=arr[i-1]
      if (b==cc2):
        #print('collision found at column: ' + str(i-1) + ", row: " + str(cc2))
        fitnessCounter=fitnessCounter+1

    #print('\n')    



  fitnessValue = 28 - (fitnessCounter/2)
  return fitnessValue

#------------------------------C R O S S O V E R      F U N C T I O N-----------------------------

def crossover(parent_x, parent_y):
  child1=[]
  child2=[]
  temp_child_List=[]
  divider=np.random.randint(1,7)
  #print(divider)


  for x in range (0,divider):
    a=parent_x[x]
    child1.insert(x,a)
  for x in range (divider,8):
    a=parent_y[x]
    child1.insert(x,a)
  temp_child_List.append(child1)



  for x in range (0,divider):
    a=parent_y[x]
    child2.insert(x,a)
  for x in range (divider,8):
    a=parent_x[x]
    child2.insert(x,a)
  temp_child_List.append(child2)

  return temp_child_List

#------------------------------M U T A T I O N      F U N C T I O N---------------------------------

def mutate(child_List):
  mutated_List=[[],[],[],[]]
  for x in range (0,4):
    child=child_List[x]
    index=np.random.randint(0,7)
    value=np.random.randint(1,9)
    child[index]=value
    mutated_List[x]=child
  return mutated_List















#-----------------------------------I N I T I A L I Z I N G--------------------------------------

#population= [ [1,4,3,6,4,7,8,4] , [4,2,5,7,4,5,7,3] , [3,5,3,7,1,2,4,6] , [3,4,1,6,4,2,3,6] ]
flag=0
specialIndex=0
mutation_threshold=0.3
iterationNumber=0;

p0=np.random.randint(1,9,8)
p1=np.random.randint(1,9,8)
p2=np.random.randint(1,9,8)
p3=np.random.randint(1,9,8)
population=[p0,p1,p2,p3]

#-----------------------R U N N I N G    G E N E T I C    A L G O R I T H M---------------------------

while (1>0):

  fitness_Score_List=[]
  fitness_Probability_List=[]
  totalFitness=0
  child_List=[]
  new_fitness_Score_List=[]
  selected_Population=[]


  #CALCULATING FTINESS OF EACH MEMBER
  for x in range (0,4):
    a=fitnessFunction(population[x])
    fitness_Score_List.insert(x, a)

  #CALCULATING TOTAL FITNESS
  for x in range (0,4):
    totalFitness = totalFitness + fitness_Score_List[x]

  #CALCULATING PROBABLITY OF EACH MEMBER/ PROBABILITY OF BEING CHOSEN
  for x in range (0,4):
    a = (fitness_Score_List[x])/totalFitness
    fitness_Probability_List.insert(x, a)



  cc3= [0,1,2,3] 
  size=4
  p = fitness_Probability_List
  selection_Index = np.random.choice(cc3,size,True,p)


  for x in range (0,4):
    a=population[selection_Index[x]]
    selected_Population.insert(x,a)
  #----------------selection done---------------

  parent_x1=selected_Population[0]
  parent_y1=selected_Population[1]
  parent_x2=selected_Population[2]
  parent_y2=selected_Population[3]

  temp_child_List1=crossover(parent_x1,parent_y1)
  for x in range(0,2):
    child_List.insert(x,temp_child_List1[x])

  temp_child_List2=crossover(parent_x2,parent_y2)
  count3=0
  for x in range (2,4):
    child_List.insert(x,temp_child_List2[count3])
    count3=count3+1

  #-------------crossover done----------------

  randmutation=random.uniform(0,1)
  if (randmutation<mutation_threshold):
    mutated_List=mutate(child_List)
    population=mutated_List
  else:
    population=child_List
  #-------------mutation done--------------------


  for x in range (0,4):
    a=fitnessFunction(population[x])
    new_fitness_Score_List.insert(x, a)

  for x in range (0,4):
    a=new_fitness_Score_List[x]
    if(a==28):
      flag=1
      specialIndex=x

  iterationNumber=iterationNumber+1

  if (flag==1):
    break

#----------------------------------------P R I N T I N G    R E S U L T---------------------------

print(population[specialIndex])
print('Total number of iteration required: '+ str(iterationNumber))


#-------------------T E S T I N G    F I T N E S S    O F    F I N A L   C H I L D--------------------
finalChild=[]
finalFitness=0
finalChild=population[specialIndex]
finalFitness=fitnessFunction(finalChild)
print('Final fitness is: '+ str(finalFitness))


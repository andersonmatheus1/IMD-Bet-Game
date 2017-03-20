
# coding: utf-8

# In[1]:

import random
import pandas as pd


level = int(input("Enter with the current floor\n" ))
number_epoch = 100#input("Enter with numbers of epoch\n" )
number_rounds = 500#input("Enter with numbers of rounds\n" )

epoch = []
rounds = []

def dice():
    value = random.randint(1,6)
    return value

def round():
    temp_floor = level
    high_value = 0
    count = 0
    for i in range(0, number_rounds):
        
        for j in range(0, number_epoch):
            value_dice = dice()
            
            if value_dice < 3:
                temp_floor = temp_floor - 1
                if temp_floor < 0:
                    temp_floor = 0
            elif value_dice > 2 and value_dice < 6:
                temp_floor = temp_floor + 1
                
            elif value_dice == 6:
                value_dice = dice()
                temp_floor = temp_floor + value_dice
                

            epoch.append(temp_floor)
            ...
            if temp_floor > high_value:
                high_value = temp_floor
               
            ...
            count = count + 1
              
            
        temp_floor = temp_floor = 0        
        rounds.append(epoch)
        #print(high_value)

round()
for i in range(0,number_rounds):
    for j in range(0,number_epoch):
        print(rounds[i][j])
    print("\n")
        


import random 

 #1 
results = ["Yes", "Maybe", "No", "Yes"]
counterY = 0
counterM= 0
counterN = 0
for i in range(len(results)):
 if results[i] == "Yes":
   counterY += 1
 elif results[i] == "No":
     counterN += 1 
 elif results[i] == "Maybe":
     counterM += 1


# 2 
ages = [2,5,3,19,20,21,70]
legal = 0 
illegal = 0
for i in range(len(ages)):
  if ages[i] < 18:
    illegal += 1
  elif ages[i] >= 18:
    legal += 1
    
    
    
#3 
prices = [12, 56, 70, 80, 90, 123, 55]

#a
under20 = 0
between20and49 = 0
higher50 = 0 

for i in range(len(prices)):
  if prices[i] < 20:
    under20 += 1
  elif 20 <= prices[i] < 50:
    between20and49 += 1
  elif prices[i] >= 50:
    higher50 += 1
    
    
# b 

for i in range(len(prices)):
  prices[i] += 2

# c

for i in range(len(prices)):
  prices[i] += 1.05
  
#d 

for i in range(len(prices)):
  prices[i] += 0.8
  

  
  
  
  

  
  
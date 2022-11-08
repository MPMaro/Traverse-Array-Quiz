import random


#1 
month = [ "Januaray", "June", "July"]

# 2

word1 = []
for x in range(700):
    word1.append("joy")
    
  #3  
word2 = []
for x in range(500):
    word2.append(7)
    
  #4
num1 = []
for x in range(5000):
 num = random.randrange(0,100)
 num1.append(num)
 
 
# 5
num2 = []
for x in range(300):
 numa = random.randrange(0,40)
 num2.append(numa)


 # 6
num3 = []
for x in range(20, 801, 4):
    num3.append(x)

# 7
num4 = []
for x in range(100, 9, -2):
        num4.append(x)
        
        
# 8 
colors_str = "red,orange,yellow,green,blue,indigo,violet"
newc = colors_str.split(",")

# 9 
cities_str = "Edmonton;Calgary;Vancouver;Saskatoon;Winnipeg"
newcties = cities_str.split(";")

# 10
userloop = True
name = []
while userloop:
    userinput = input("Please add a name")
    if userinput == "done":
        userloop = False
    else:
        name.append(userinput)


        
   
   
   

    
  
    



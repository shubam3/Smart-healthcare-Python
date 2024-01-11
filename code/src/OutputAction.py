import datetime 
  
  
def getdate(): 
  
    # to get date and time 
    return datetime.datetime.now() 
  
def selectname(): 
    
    name = {1: "Nilesh", 2: "Shanu"} 
    b = {1: "Food", 2: "Exercise"} 
      
    for key, value in name.items(): 
  
        print("Press", key, "for", value, "\n", end="") 
          
    n = int(input("type here..")) 
      
    if n > 2: 
        print("error select 1 or 2") 
        exit() 
    else: 
        return n 
  
  
def select_file_action(): 
    
    a = {1: "Log", 2: "Retrieve"} 
      
    for key, value in a.items(): 
  
        # taking input of function that user wants to 
        print("Press", key, "for", value, "\n", end="") 
  
    x = int(input("type here..")) 
      
    if x > 2: 
        print("error select 1 or 2") 
        exit() 
    else: 
        return x 
  
  
def select_task(): 
    
    b = {1: "Food", 2: "Exercise"} 
      
    for key, value in b.items(): 
        
        # ask user to choose between food  
        # and exercise 
        print("Press", key, "for", value, "\n", end="") 
  
    y = int(input("type here..")) 
      
    if y > 2: 
        print("error select 1 or 2") 
        exit() 
    else: 
        return y 
  
  
def action(n, x, y): 
    
    # condition no 1 
    if n == 1 and x == 1 and y == 1: 
        value = input("type here\n") 
  
        with open("nilesh food.txt", "a") as nileshfood: 
  
           
            nileshfood.write(str([str(getdate())]) + ": " + value + "\n") 
            print("successfully written") 
  
    # condition no 2 
    elif n == 1 and x == 1 and y == 2: 
        value = input("type here\n") 
  
       
        with open("nilesh exercise.txt", "a") as nileshexercise: 
  
           
            nileshexercise.write(str([str(getdate())]) + ": " + value + "\n") 
            print("successfully written") 
  
    # condition 3 
    elif n == 2 and x == 1 and y == 1: 
        value = input("type here\n") 
  
        # printing date and time 
        with open("shanu food.txt", "a") as shanufood: 
  
            # printing date and time 
            shanufood.write(str([str(getdate())]) + ": " + value + "\n") 
            print("successfully written") 
  
    # condition 4 
    elif n == 2 and x == 1 and y == 2: 
        value = input("type here\n") 
  
       
        with open("shanu exercise.txt", "a") as shanuexercise: 
  
           
            shanuexercise.write(str([str(getdate())]) + ": " + value + "\n") 
            print("successfully written") 
  
    # condition 5 
    elif n == 1 and x == 2 and y == 1: 
  
       
        with open("nilesh food.txt", "r") as nileshfood: 
            a = nileshfood.read() 
            print(a) 
  
    # condition no 6 
    elif n == 1 and x == 2 and y == 2: 
  
       
        with open("nilesh exercise.txt", "r") as nileshexercise: 
            a = nileshexercise.read() 
            print(a) 
  
     
    elif n == 2 and x == 2 and y == 1: 
  
       
        with open("shanu food.txt", "r") as shanufood: 
            a = shanufood.read() 
            print(a) 
  
    
    elif n == 2 and x == 2 and y == 2: 
  
        
        with open("shanu exercise.txt", "r") as shanuexercise: 
            a = shanuexercise.read() 
            print(a) 
  
  
n = selectname() 
x = select_file_action() 
y = select_task() 
action(n, x, y) 
def action(n, x, y): 
  
 
    if n == 1 and x == 1 and y == 1: 
        value = input("type here\n") 
  
        with open("nilesh food.txt", "a") as nileshfood: 
  
           
            nileshfood.write(str([str(getdate())]) + ": " + value + "\n") 
            print("successfully written") 
  
    elif n == 1 and x == 1 and y == 2: 
  
        value = input("type here\n") 
          
      
        with open("nilesh exercise.txt", "a") as nileshexercise: 
  
            
            nileshexercise.write(str([str(getdate())]) + ": " + value + "\n") 
            print("successfully written") 
  
  
    elif n == 2 and x == 1 and y == 1: 
  
        value = input("type here\n") 
          
      
        with open("shanu food.txt", "a") as shanufood: 
  
            # printing date and time 
            shanufood.write(str([str(getdate())]) + ": " + value + "\n") 
            print("successfully written") 
  
  
    elif n == 2 and x == 1 and y == 2: 
  
        value = input("type here\n") 
  
        
        with open("shanu exercise.txt", "a") as shanuexercise: 
  
           
            shanuexercise.write(str([str(getdate())]) + ": " + value + "\n") 
            print("successfully written") 
  
   
    elif n == 1 and x == 2 and y == 1: 
  
      
        with open("nilesh food.txt", "r") as nileshfood: 
  
            a = nileshfood.read() 
            print(a) 
  
    
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
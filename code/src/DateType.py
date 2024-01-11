def selectname(): 
  
    name = {1: "aman", 2: "shivam"} 
    b = {1: "Food", 2: "Exercise"} 
  
    for key, value in name.items(): 
  
        # taking input of name 
        print("Press", key, "for", value, "\n", end="") 
  
    n = int(input("type here..")) 
  
    if n > 2: 
        print("error select 1 or 2") 
        exit() 
    else: 
        return n
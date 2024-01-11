def select_file_action(): 
  
    a = {1: "Log", 2: "Retrieve"} 
    for key, value in a.items(): 
  
       
        print("Press", key, "for", value, "\n", end="") 
  
    x = int(input("type here..")) 
    if x > 2: 
        print("error select 1 or 2") 
        exit() 
    else: 
        return x
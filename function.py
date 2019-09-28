import math
funcs={"sqrt":math.sqrt,"log":math.log, "log10":math.log10}
f="start"
while f != "stop": 
    n=int(input("enter number: "))
    f=input("Function to perform or stop: ")
    if not f in funcs:
        print("No such function")
    else:
        print("applying function %s to %d gives %f"%(f,n,funcs[f](n)))
        

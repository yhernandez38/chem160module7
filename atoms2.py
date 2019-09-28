names= ["H", "He", "Li", "Be"]
masses = [1.088, 4.003, 6.941, 9.012]
dict2={}
for i in range (len(names)):
    dict2[names[i]]=masses[i]
print(dict2)
print(dict2["He"])
print( "O" in dict2)
      

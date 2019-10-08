outputlist = []
for i in examplelist:
    if i>2 or i <-2.5:
        outputlist = outputlist + [i**2]
        
print(outputlist)

outputlist = [ x**2 for x in examplelist if (x>2) or (x<-2.5) ]
print(outputlist)
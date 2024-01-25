
import random 

spelaren = str (input ('Välj mellan sten, sax eller påse: '))
print('Du valde :'+ spelaren)

list=["sten","sax","påse"]

for datorn in random.sample(list,1):
    
    print('Datorn valde :'+ datorn)
    
    #Regelarna: sten vinner över sax, sax vinner över påse, och påse vinner över sten. 
    #Om båda väljer samma alternativ blir det oavgjort.
    
    if (spelaren=="sten" and datorn =="sax") or \
       (spelaren=="sax" and datorn =="påse") or\
       (spelaren=="påse" and datorn =="sten"):
           print('Spelaren vinner den här omgången! ')

    elif  spelaren== datorn:
      print('Det blev oavgjort!')
      
    else:
      print('Datorn  vinner den här omgången! ')
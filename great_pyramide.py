import os

i = 0
base = [' ',' ',' ',' ',' ',' ',' ',' ',' ','*']
translation = ''

def translator(base, translation):
    for z in range(1,len(base)):
        translation += base[z]       
    print(translation)        

for i in range(0,5):
    translator(base, translation) 
    del base[0]    
    del base[1]
    base += ' - *'

k = 0

base = [' ', ' ', ' ','*',' ','-',' ','*',' ','-',' ','*',' ','-', ' ','*', ' ', ' ']

for i in range(0,4):
    translator(base, translation) 
    del base[0]
    del base[1]
    for k in range(0,2*i+4):
        base[k] = ' '
    
os.system('Pause')

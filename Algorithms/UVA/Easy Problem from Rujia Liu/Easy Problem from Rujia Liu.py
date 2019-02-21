import sys


#Nomizo auto diavazi ta panta me tin mia
#allText = sys.stdin.readlines() 
#print(allText)  

# diavase tin proti grammi , me to rstrip vgale to \n apo to telos me to split ' ' kopse oti exei mesa sta keno 
# theoro dedomeno oti exei dio noumera opote ksero oti tha epistrepsi dio noumnera kai ta xono sto n kai to q 
n, q = sys.stdin.readline().rstrip().split(' ')

# Diavase tous n arithmous pao tin deuteri grammi
# den to thelouem array opos eipame optoe prepei na to allaksis
array_me_arithmous = list(map(int, sys.stdin.readline().rstrip().split(' ')))

array_dict = {}
for i,v in enumerate(array_me_arithmous):
    if v in array_dict:
        array_dict[v].append(i+1)
    else:
        array_dict[v] = [i+1]


for index in range(int(q)):
    # diavase tin Q(index) grammi
    j, query = (list(map(int, sys.stdin.readline().rstrip().split(' '))))
    # magic!!!!!
    if query in array_dict:
        lista_thesewn = array_dict[query]
        if j <= len(lista_thesewn):
            print(lista_thesewn[j-1])
        else:
            print(0)
    else:
        print(0)

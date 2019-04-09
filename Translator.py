conversor = {' ':' ','a':'4','b':'8','c':'(','d':'|)','e':'3','f':'|=','g':'6','h':'#','i':'1','j':'_|','k':'|<','l':'|_','m':'|v|','n':'|v','o':'0','p':'|*','q':'()_','r':'2','s':'5','t':'7','u':'(_)','v':'\/','x':'><','y':"'/",'z':'7_','w':'vv'}

nome1 = "Alexandre Augusto"
leet_name = []

for letra in nome1:
    leet_name.append(conversor[letra.lower()])

print(nome1+": "+"".join(leet_name))

nome2 = "Daniel Hassan"
leet_name = []

for letra in nome2:
    leet_name.append(conversor[letra.lower()])

print(nome2+": "+"".join(leet_name))
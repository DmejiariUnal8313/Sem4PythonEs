capitales={'Caldas':'Manizales','Risaralda':'Pereira'}
print(capitales['Caldas'])
capitales['Quindio']='Armenia'
print(capitales)
capitales['Tolima']='Ibagué'
print(len(capitales))
for k in capitales:
    print(capitales[k], "es capital de", k)
del capitales['Tolima']
print(capitales)
    

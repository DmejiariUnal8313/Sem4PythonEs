comidas = ['huevos', 'brocoli', 'guisante', 'sal', 'filete']
for k in range (len(comidas) - 1):
    if len (comidas[k]) < len(comidas[k+1]):
        print(k)
        

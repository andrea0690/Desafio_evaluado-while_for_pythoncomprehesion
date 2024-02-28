responde_estimulos = input('El paciente responde a estimulos?, Responda si/no: ')

if responde_estimulos == 'si':
    print('Valorar la necesidad de llevarlo al hospital más cercano')
    print('Fin')
else:
    print('Abrir la via aerea')
    respira = input('El paciente respira?, Responda si/no: ')
    
    if respira == 'si':
        print('Permitirle posición de suficiente ventilación')
        print('Fin')
    else:
        print('Administrar 5 ventilaciones y llamar a la ambulancia')
        
        llego_ambulacia = None
        
        while llego_ambulacia != 'si':
            
            signos_vitales = input('El paciente tiene signos vitales?, Responda si/no: ')
            if signos_vitales == 'si':
                print('Reevaluar, a la espera de la ambulancia')
            else:
                print('Administar compresiones toracicas hasta que llegue la ambulancia')
                
            llego_ambulacia = input('Llegó la ambulancia?, Responda si/no: ')
            
        print('Fin')
            
        
        
    
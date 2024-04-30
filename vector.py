import os
lista__animales_nombre = []
lista_animales_codigo = []
item = 0
def fnt_limpiar():
    os.system('cls')
    print('---------- juan jose---------- ')

def fnt_agregar_orden(nombre):
    fnt_limpiar()
    global item
    if nombre == '':
        input('escribe un nombre <ENTER>    ')
    else:
        lista__animales_nombre.append(nombre)
        lista_animales_codigo.append(item)
        item += 1
        input('registrado con exit <ENTER> ')
        
        
def fnt_mostrar ():
    fnt_limpiar()
    for i in range(len(lista__animales_nombre)):
        print(lista_animales_codigo[i], '-', lista__animales_nombre[i])
    input(' fin  <ENTER> ')

         


sw = True

while sw == True:
    opcion = input('\n1. agregar por orden(append) \n2. agregar por posicion(insert)  \n3. eliminar por orden(pop) \n4. eliminar por posicion(pop) \n5.mostrar \n6. salir \n-> ')
    if opcion =='5':
        fnt_mostrar()
    elif opcion =='1':
        nombre = input (' nombre del animal -> ')
        fnt_agregar_orden(nombre.upper())
        
    elif opcion == '6':
        input (' fin del programa <ENTER> ')
        sw = False
    
        
        
         
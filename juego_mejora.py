#Se importan los modulos necesarios.
from tkinter import *
import tkinter.messagebox
from random import *

global dificult
global leer
global inicio_de_la_partida

#Inicio de la partida almacena un booleano que nos indica si el programa ya inicio y
#confirmar jugada indica si ya se ha realizado alguna jugada.
inicio_de_la_partida=False
confirmar_jugada=False

#Abrimos el archivo que almacena las partidas del kakuro.
leer_lista=open("kakuro2018partidas - copia.txt","r")
linea=leer_lista.readlines()

#Abrimos el archivo que almacena la configuración del kakuro.
leer_config=open("kakuro2018configuracion.txt","r")
linea_c=leer_config.readlines()
for x in linea_c:
    if x=="Dificultad = Easy\n":
        dificult="Easy"
    elif x=="Dificultad = Medium\n":
        dificult="Medium"
    elif x=="Dificultad = Hard\n":
        dificult="Hard"

partidas_Easy=eval(linea[0])
partidas_Medium=eval(linea[1])
partidas_Hard=eval(linea[2])

#Importante! Cerrar el archivo.
leer_lista.close
leer_config.close


def cambiar_matriz():
    """Función nos permite cambiar la matriz de acuerdo a la dificultad seleccionada.
    Además usa la función colocar para desplegar el tablero en la pantalla."""
    
    global inicio_de_la_partida
    global partida
    
    inicio_de_la_partida=True
    
    r=randint(0,1)
    if dificult=="Easy":
        partida=partidas_Easy[r]
    elif dificult=="Medium":
        partida=partidas_Medium[r]
    elif dificult=="Hard":
        partida=partidas_Hard[r]

    #Se revisa si hay claves dobles.
    dobles=check(partida)
    dobles_text=check_text(partida)

    #Cambiar la matriz por cada uno de los digitos que se encuentren en partida.
    for cuadro in partida:
        tipo=cuadro[0]
        num=cuadro[1]
        fila=cuadro[2]
        columna=cuadro[3]
        casillas=cuadro[4]

        ubicacion=[fila,columna]
        conf=ubicacion in dobles
        if conf==True:
            pass
        else:
            copy_fila=fila-1
            copy_columna=columna-1
            if tipo==1:
                Change(copy_fila,copy_columna,"\\"+str(num))
            else:
                Change(copy_fila,copy_columna,str(num)+"\\")

        #Desplegar las casillas en blanco que tendrá la clave.
        while casillas!=0:
            if tipo==1:
                columna+=1
            else:
                fila+=1
            casillas-=1
            copy_fila=fila-1
            copy_columna=columna-1
            Change(copy_fila,copy_columna,0)
    
    #Si hay dobles, grabar en la matriz un string que contenga los valores de la clave doble.
    if dobles!=[]:
        cont=0
        for ubicacion in dobles:
            numeros=dobles_text[cont]
            cont+=1
            copy_fila=ubicacion[0]-1
            copy_columna=ubicacion[1]-1
            Change(copy_fila,copy_columna,str(numeros[1])+"\\"+str(numeros[0]))

    #Utilizar la función colocar para desplegar el tablero.
    colocar()


Matriz=[[-2,-2,-2,-2,-2,-2,-2,-2,-2],
        [-2,-2,-2,-2,-2,-2,-2,-2,-2],
        [-2,-2,-2,-2,-2,-2,-2,-2,-2],
        [-2,-2,-2,-2,-2,-2,-2,-2,-2],
        [-2,-2,-2,-2,-2,-2,-2,-2,-2],
        [-2,-2,-2,-2,-2,-2,-2,-2,-2],
        [-2,-2,-2,-2,-2,-2,-2,-2,-2],
        [-2,-2,-2,-2,-2,-2,-2,-2,-2],
        [-2,-2,-2,-2,-2,-2,-2,-2,-2]]


def Revisar():
    """Función que, como su nombre indica, revisa los valores de las columnas
    y de las filas. Si se repite un dígito o si la suma de los números de la
    columna o fila no da el indicado por la clave manda un error."""
    
    global Error
    cont1=0
    Error=False
    while cont1!=(len(Matriz)):
        string=False
        linea=Matriz[cont1]
        cont2=-1
        while cont2!=len(linea)-1:
            Salir=False
            cont2+=1
            string=linea[cont2]
            if type(string)==str:
                Numeros_str=Revisar_String(string)
                #Revisar Vertical
                if Numeros_str[1]==0:
                    result=0
                    num=False
                    p=cont1+1
                    lista_numeros=[]
                    while type(num)!=str and p<9:
                        num=Matriz[p][cont2]
                        if num==0:
                            Salir=True
                            pass
                        elif num==-2:
                            break
                        elif type(num)!=str:
                            result+=num
                            #Revisar que el numero no este en la columna.
                            if num in lista_numeros:
                                return tkinter.messagebox.showerror("Error","Se repiten numero en la columna")
                            else:
                                lista_numeros.append(num)
                        else:
                            break
                        p+=1
                    if Numeros_str[0]==result or Salir==True:
                        pass
                    else:
                        Error=True
                        break
                #Revisar Horizontal
                elif Numeros_str[0]==0:
                    result=0
                    num=False
                    p=cont2+1
                    lista_numeros=[]
                    while type(num)!=str and p<9:
                        num=Matriz[cont1][p]
                        if num==0:
                            Salir=True
                            pass
                        elif num==-2:
                            break
                        elif type(num)!=str:
                            result+=num
                            if num in lista_numeros:
                                return tkinter.messagebox.showerror("Error","Se repiten numero en la columna")
                            else:
                                lista_numeros.append(num)
                        else:
                            break
                        p+=1
                    if Numeros_str[1]==result or Salir==True:
                        pass
                    else:
                        Error=True
                        break
                #Revisar Doble
                else:
                    result=0
                    num=False
                    p=cont1+1
                    lista_numeros=[]
                    while type(num)!=str and p<9:
                        num=Matriz[p][cont2]
                        if num==0:
                            Salir=True
                            pass
                        elif num==-2:
                            break
                        elif type(num)!=str:
                            result+=num
                            lista_numeros.append(num)
                        else:
                            break
                        p+=1
                    if Numeros_str[0]==result or Salir==True:
                        pass
                    else:
                        Error=True
                    Salir=False
                    result=0
                    num=False
                    p=cont2+1
                    lista_numeros=[]
                    while type(num)!=str and p<9:
                        num=Matriz[cont1][p]
                        if num==0:
                            Salir=True
                            pass
                        elif num==-2:
                            break
                        elif type(num)!=str:
                            lista_numeros.append(num)
                            result+=num
                        else:
                            break
                        p+=1
                    if Numeros_str[1]==result or Salir==True:
                        pass
                    else:
                        Error=True
                if Error==True:
                    break
                
        cont1+=1
    if Error==True:
        tkinter.messagebox.showerror("Error","Error en la fila o columna.")

        
def Revisar_String(string):
    """Función que revisa un string. Se utiliza para revisar las claves.
    Si la clave es doble, su salida va a ser una tupla con el valor del
    número antes y despues del "\"."""
    cont=0
    num1=""
    num2=""
    slash=False

    #Colocar todos los elementos que puedan ser convertidos en enteros en un lado
    #de la tupla hasta encontrar un elemento que no pueda ser convertido en entero.
    #Todos los valores despues de este van a ser el segundo valor de la tupla.
    while cont!=len(string):
        dig=string[cont]
        try:
            dig=int(dig)
            if slash==False:
                num1+=str(dig)
            else:
                num2+=str(dig)
        except:
            slash=True
        cont+=1
    if num1=="":
        num1=0
    if num2=="":
        num2=0
    return int(num1),int(num2)


def Revision_final():
    term=False
    for pos in Matriz:
        for pos2 in pos:
            if pos2==0:
                term=True
                break
            else:
                term=False
        if term==True:
            break
    if term==False and Error==False:
        if MultiNivel==True:
            Change_Multinivel()
        else:
            tkinter.messagebox.showinfo("FELICIDADES!","¡EXCELENTE! JUEGO COMPLETADO.")

    
def Terminar():
    global Matriz
    """Función que elimina el juego y digita otro."""
    conf=tkinter.messagebox.askyesno("Terminar","¿Seguro que desea terminar el juego?")
    #Si responde si a la pregunta se borra todo.
    if conf==True:
        borrar_juego()
    else:
        pass
    Matriz=[[-2,-2,-2,-2,-2,-2,-2,-2,-2],
        [-2,-2,-2,-2,-2,-2,-2,-2,-2],
        [-2,-2,-2,-2,-2,-2,-2,-2,-2],
        [-2,-2,-2,-2,-2,-2,-2,-2,-2],
        [-2,-2,-2,-2,-2,-2,-2,-2,-2],
        [-2,-2,-2,-2,-2,-2,-2,-2,-2],
        [-2,-2,-2,-2,-2,-2,-2,-2,-2],
        [-2,-2,-2,-2,-2,-2,-2,-2,-2],
        [-2,-2,-2,-2,-2,-2,-2,-2,-2]]
    destruir_botones()
    crear_botones()
    cambiar_matriz()
            

################################################################    Botones de pantalla     #####################################################################
def colocar():
    """Función que despliega el tablero en la pantalla."""

    #Para cada cuadro se crea un boton. Primero se lee la matriz con la posición del botón,
    #si el valor es -2 significa que es un cuadro negro donde no se puede colocar ningun número;
    #si el valor es 0 significa que es un cuadro donde se puede colocar un número; si el valor
    #se encuentra entre 1 y 9 significa que el usuario esta cargando una partida por lo cual ese
    #cuadro tiene que quedar con el mismo valor; y si no es ninguno de los anteriores significa que
    #el valor es una clave la cual la vamos a colocar en el cuadro sin ponerle ningún comando.
    
    result=str(Matriz[0][0])
    aux=["1","2","3","4","5","6","7","8","9"]
    if result=="-2":
        cuadroA1.config(padx=19,pady=8)
    elif result=="0":
        A1text=StringVar()
        cuadroA1.config(textvariable=A1text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(A1text,Matriz[0],Matriz[0]))
    elif result in aux:
        A1text=StringVar()
        A1text.set(result)
        cuadroA1.config(textvariable=A1text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(A1text,0,0))
    else:
        cuadroA1.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(0,0))        
    cuadroA1.grid(column=0,row=0)

    result=str(Matriz[0][1])
    if result=="-2":
        cuadroA2.config(padx=19,pady=8)
    elif result=="0":
        A2text=StringVar()
        cuadroA2.config(textvariable=A2text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(A2text,0,1))
    elif result in aux:
        A2text=StringVar()
        A2text.set(result)
        cuadroA2.config(textvariable=A2text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(A2text,0,1))
    else:
        cuadroA2.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(0,1))
    cuadroA2.grid(column=1,row=0)

    result=str(Matriz[0][2])
    if result=="-2":
        cuadroA3.config(padx=19,pady=8)
    elif result=="0":
        A3text=StringVar()
        cuadroA3.config(textvariable=A3text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(A3text,0,2))
    elif result in aux:
        A3text=StringVar()
        A3text.set(result)
        cuadroA3.config(textvariable=A3text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(A3text,0,2))
    else:
        cuadroA3.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(0,2))
    cuadroA3.grid(column=2,row=0)

    result=str(Matriz[0][3])
    if result=="-2":
        cuadroA4.config(padx=19,pady=8)
    elif result=="0":
        A4text=StringVar()
        cuadroA4.config(textvariable=A4text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(A4text,0,3))
    elif result in aux:
        A4text=StringVar()
        A4text.set(result)
        cuadroA4.config(textvariable=A4text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(A4text,0,3))
    else:
        cuadroA4.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(0,3))
    cuadroA4.grid(column=3,row=0)

    result=str(Matriz[0][4])
    if result=="-2":
        cuadroA5.config(padx=19,pady=8)
    elif result=="0":
        A5text=StringVar()
        cuadroA5.config(textvariable=A5text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(A5text,0,4))
    elif result in aux:
        A5text=StringVar()
        A5text.set(result)
        cuadroA5.config(textvariable=A5text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(A5text,0,4))
    else:
        cuadroA5.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(0,4))
    cuadroA5.grid(column=4,row=0)

    result=str(Matriz[0][5])
    if result=="-2":
        cuadroA6.config(padx=19,pady=8)
    elif result=="0":
        A6text=StringVar()
        cuadroA6.config(textvariable=A6text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(A6text,0,5))
    elif result in aux:
        A6text=StringVar()
        A6text.set(result)
        cuadroA6.config(textvariable=A6text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(A6text,0,5))
    else:
        cuadroA6.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(0,5))
    cuadroA6.grid(column=5,row=0)

    result=str(Matriz[0][6])
    if result=="-2":
        cuadroA7.config(padx=19,pady=8)
    elif result=="0":
        A7text=StringVar()
        cuadroA7.config(textvariable=A7text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(A7text,0,6))
    elif result in aux:
        A7text=StringVar()
        A7text.set(result)
        cuadroA7.config(textvariable=A7text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(A7text,0,6))
    else:
        cuadroA7.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(0,6))
    cuadroA7.grid(column=6,row=0)

    result=str(Matriz[0][7])
    if result=="-2":
        cuadroA8.config(padx=19,pady=8)
    elif result=="0":
        A8text=StringVar()
        cuadroA8.config(textvariable=A8text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(A8text,0,7))
    elif result in aux:
        A8text=StringVar()
        A8text.set(result)
        cuadroA8.config(textvariable=A8text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(A8text,0,7))
    else:
        cuadroA8.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(0,7))
    cuadroA8.grid(column=7,row=0)

    result=str(Matriz[0][8])
    if result=="-2":
        cuadroA9.config(padx=19,pady=8)
    elif result=="0":
        A9text=StringVar()
        cuadroA9.config(textvariable=A9text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(A9text,0,8))
    elif result in aux:
        A9text=StringVar()
        A9text.set(result)
        cuadroA9.config(textvariable=A9text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(A9text,0,8))
    else:
        cuadroA9.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(0,8))
    cuadroA9.grid(column=8,row=0)

#####

    result=str(Matriz[1][0])
    if result=="-2":
        cuadroB1.config(padx=19,pady=8)
    elif result=="0":
        B1text=StringVar()
        cuadroB1.config(textvariable=B1text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(B1text,1,0))
    elif result in aux:
        B1text=StringVar()
        B1text.set(result)
        cuadroB1.config(textvariable=B1text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(B1text,1,0))
    else:
        cuadroB1.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(1,0))
    cuadroB1.grid(column=0,row=1)

    result=str(Matriz[1][1])
    if result=="-2":
        cuadroB2.config(padx=19,pady=8)
    elif result=="0":
        B2text=StringVar()
        cuadroB2.config(textvariable=B2text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(B2text,1,1))
    elif result in aux:
        B2text=StringVar()
        B2text.set(result)
        cuadroB2.config(textvariable=B2text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(B2text,1,1))
    else:
        cuadroB2.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(1,1))
    cuadroB2.grid(column=1,row=1)

    result=str(Matriz[1][2])
    if result=="-2":
        cuadroB3.config(padx=19,pady=8)
    elif result=="0":
        B3text=StringVar()
        cuadroB3.config(textvariable=B3text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(B3text,1,2))
    elif result in aux:
        B3text=StringVar()
        B3text.set(result)
        cuadroB3.config(textvariable=B3text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(B3text,1,2))
    else:
        cuadroB3.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(1,2))
    cuadroB3.grid(column=2,row=1)

    result=str(Matriz[1][3])
    if result=="-2":
        cuadroB4.config(padx=19,pady=8)
    elif result=="0":
        B4text=StringVar()
        cuadroB4.config(textvariable=B4text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(B4text,1,3))
    elif result in aux:
        B4text=StringVar()
        B4text.set(result)
        cuadroB4.config(textvariable=B4text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(B4text,1,3))
    else:
        cuadroB4.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(1,3))
    cuadroB4.grid(column=3,row=1)

    result=str(Matriz[1][4])
    if result=="-2":
        cuadroB5.config(padx=19,pady=8)
    elif result=="0":
        B5text=StringVar()
        cuadroB5.config(textvariable=B5text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(B5text,1,4))
    elif result in aux:
        B5text=StringVar()
        B5text.set(result)
        cuadroB5.config(textvariable=B5text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(B5text,1,4))
    else:
        cuadroB5.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(1,4))
    cuadroB5.grid(column=4,row=1)

    result=str(Matriz[1][5])
    if result=="-2":
        cuadroB6.config(padx=19,pady=8)
    elif result=="0":
        B6text=StringVar()
        cuadroB6.config(textvariable=B6text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(B6text,1,5))
    elif result in aux:
        B6text=StringVar()
        B6text.set(result)
        cuadroB6.config(textvariable=B6text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(B6text,1,5))
    else:
        cuadroB6.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(1,5))
    cuadroB6.grid(column=5,row=1)

    result=str(Matriz[1][6])
    if result=="-2":
        cuadroB7.config(padx=19,pady=8)
    elif result=="0":
        B7text=StringVar()
        cuadroB7.config(textvariable=B7text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(B7text,1,6))
    elif result in aux:
        B7text=StringVar()
        B7text.set(result)
        cuadroB7.config(textvariable=B7text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(B7text,1,6))
    else:
        cuadroB7.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(1,6))
    cuadroB7.grid(column=6,row=1)

    result=str(Matriz[1][7])
    if result=="-2":
        cuadroB8.config(padx=19,pady=8)
    elif result=="0":
        B8text=StringVar()
        cuadroB8.config(textvariable=B8text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(B8text,1,7))
    elif result in aux:
        B8text=StringVar()
        B8text.set(result)
        cuadroB2.config(textvariable=B8text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(B8text,1,7))
    else:
        cuadroB8.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(1,7))
    cuadroB8.grid(column=7,row=1)

    result=str(Matriz[1][8])
    if result=="-2":
        cuadroB9.config(padx=19,pady=8)
    elif result=="0":
        B9text=StringVar()
        cuadroB9.config(textvariable=B9text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(B9text,1,8))
    elif result in aux:
        B9text=StringVar()
        B9text.set(result)
        cuadroB9.config(textvariable=B9text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(B9text,1,8))
    else:
        cuadroB9.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(1,8))
    cuadroB9.grid(column=8,row=1)

#####

    result=str(Matriz[2][0])
    if result=="-2":
        cuadroC1.config(padx=19,pady=8)
    elif result=="0":
        C1text=StringVar()
        cuadroC1.config(textvariable=C1text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(C1text,2,0))
    elif result in aux:
        C1text=StringVar()
        C1text.set(result)
        cuadroC1.config(textvariable=C1text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(C1text,2,0))
    else:
        cuadroC1.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(2,0))
    cuadroC1.grid(column=0,row=2)

    result=str(Matriz[2][1])
    if result=="-2":
        cuadroC2.config(padx=19,pady=8)
    elif result=="0":
        C2text=StringVar()
        cuadroC2.config(textvariable=C2text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(C2text,2,1))
    elif result in aux:
        C2text=StringVar()
        C2text.set(result)
        cuadroC2.config(textvariable=C2text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(C2text,2,1))
    else:
        cuadroC2.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(2,1))
    cuadroC2.grid(column=1,row=2)

    result=str(Matriz[2][2])
    if result=="-2":
        cuadroC3.config(padx=19,pady=8)
    elif result=="0":
        C3text=StringVar()
        cuadroC3.config(textvariable=C3text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(C3text,2,2))
    elif result in aux:
        C3text=StringVar()
        C3text.set(result)
        cuadroC3.config(textvariable=C3text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(C3text,2,2))
    else:
        cuadroC3.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(2,2))
    cuadroC3.grid(column=2,row=2)

    result=str(Matriz[2][3])
    if result=="-2":
        cuadroC4.config(padx=19,pady=8)
    elif result=="0":
        C4text=StringVar()
        cuadroC4.config(textvariable=C4text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(C4text,2,3))
    elif result in aux:
        C4text=StringVar()
        C4text.set(result)
        cuadroC4.config(textvariable=C4text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(C4text,2,3))
    else:
        cuadroC4.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(2,3))
    cuadroC4.grid(column=3,row=2)

    result=str(Matriz[2][4])
    if result=="-2":
        cuadroC5.config(padx=19,pady=8)
    elif result=="0":
        C5text=StringVar()
        cuadroC5.config(textvariable=C5text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(C5text,2,4))
    elif result in aux:
        C5text=StringVar()
        C5text.set(result)
        cuadroC5.config(textvariable=C5text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(C5text,2,4))
    else:
        cuadroC5.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(2,4))
    cuadroC5.grid(column=4,row=2)

    result=str(Matriz[2][5])
    if result=="-2":
        cuadroC6.config(padx=19,pady=8)
    elif result=="0":
        C6text=StringVar()
        cuadroC6.config(textvariable=C6text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(C6text,2,5))
    elif result in aux:
        C6text=StringVar()
        C6text.set(result)
        cuadroC6.config(textvariable=C6text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(C6text,2,5))
    else:
        cuadroC6.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(2,5))
    cuadroC6.grid(column=5,row=2)

    result=str(Matriz[2][6])
    if result=="-2":
        cuadroC7.config(padx=19,pady=8)
    elif result=="0":
        C7text=StringVar()
        cuadroC7.config(textvariable=C7text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(C7text,2,6))
    elif result in aux:
        C7text=StringVar()
        C7text.set(result)
        cuadroC7.config(textvariable=C7text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(C7text,2,6))
    else:
        cuadroC7.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(2,6))
    cuadroC7.grid(column=6,row=2)

    result=str(Matriz[2][7])
    if result=="-2":
        cuadroC8.config(padx=19,pady=8)
    elif result=="0":
        C8text=StringVar()
        cuadroC8.config(textvariable=C8text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(C8text,2,7))
    elif result in aux:
        C8text=StringVar()
        C8text.set(result)
        cuadroC8.config(textvariable=C8text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(C8text,2,7))
    else:
        cuadroC8.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(2,7))
    cuadroC8.grid(column=7,row=2)

    result=str(Matriz[2][8])
    if result=="-2":
        cuadroC9.config(padx=19,pady=8)
    elif result=="0":
        C9text=StringVar()
        cuadroC9.config(textvariable=C9text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(C9text,2,8))
    elif result in aux:
        C9text=StringVar()
        C9text.set(result)
        cuadroC9.config(textvariable=C9text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(C9text,2,8))
    else:
        cuadroC9.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(2,8))
    cuadroC9.grid(column=8,row=2)

#####

    result=str(Matriz[3][0])
    if result=="-2":
        cuadroD1.config(padx=19,pady=8)
    elif result=="0":
        D1text=StringVar()
        cuadroD1.config(textvariable=D1text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(D1text,3,0))
    elif result in aux:
        D1text=StringVar()
        D1text.set(result)
        cuadroD1.config(textvariable=D1text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(D1text,3,0))
    else:
        cuadroD1.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(3,0))
    cuadroD1.grid(column=0,row=3)

    result=str(Matriz[3][1])
    if result=="-2":
        cuadroD2.config(padx=19,pady=8)
    elif result=="0":
        D2text=StringVar()
        cuadroD2.config(textvariable=D2text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(D2text,3,1))
    elif result in aux:
        D2text=StringVar()
        D2text.set(result)
        cuadroD2.config(textvariable=D2text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(D2text,3,1))
    else:
        cuadroD2.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(3,1))
    cuadroD2.grid(column=1,row=3)

    result=str(Matriz[3][2])
    if result=="-2":
        cuadroD3.config(padx=19,pady=8)
    elif result=="0":
        D3text=StringVar()
        cuadroD3.config(textvariable=D3text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(D3text,3,2))
    elif result in aux:
        D3text=StringVar()
        D3text.set(result)
        cuadroD3.config(textvariable=D3text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(D3text,3,2))
    else:
        cuadroD3.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(3,2))
    cuadroD3.grid(column=2,row=3)

    result=str(Matriz[3][3])

    if result=="-2":
        cuadroD4.config(padx=19,pady=8)
    elif result=="0":
        D4text=StringVar()
        cuadroD4.config(textvariable=D4text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(D4text,3,3))
    elif result in aux:
        D4text=StringVar()
        D4text.set(result)
        cuadroD4.config(textvariable=D4text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(D4text,3,3))
    else:
        cuadroD4.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(3,3))
    cuadroD4.grid(column=3,row=3)

    result=str(Matriz[3][4])
    if result=="-2":
        cuadroD5.config(padx=19,pady=8)
    elif result=="0":
        D5text=StringVar()
        cuadroD5.config(textvariable=D5text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(D5text,3,4))
    elif result in aux:
        D5text=StringVar()
        D5text.set(result)
        cuadroD5.config(textvariable=D5text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(D5text,3,4))
    else:
        cuadroD5.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(3,4))
    cuadroD5.grid(column=4,row=3)

    result=str(Matriz[3][5])
    if result=="-2":
        cuadroD6.config(padx=19,pady=8)
    elif result=="0":
        D6text=StringVar()
        cuadroD6.config(textvariable=D6text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(D6text,3,5))
    elif result in aux:
        D6text=StringVar()
        D6text.set(result)
        cuadroD6.config(textvariable=D6text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(D6text,3,5))
    else:
        cuadroD6.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(3,5))
    cuadroD6.grid(column=5,row=3)

    result=str(Matriz[3][6])
    if result=="-2":
        cuadroD7.config(padx=19,pady=8)
    elif result=="0":
        D7text=StringVar()
        cuadroD7.config(textvariable=D7text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(D7text,3,6))
    elif result in aux:
        D7text=StringVar()
        D7text.set(result)
        cuadroD7.config(textvariable=D7text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(D7text,3,6))
    else:
        cuadroD7.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(3,6))
    cuadroD7.grid(column=6,row=3)

    result=str(Matriz[3][7])
    if result=="-2":
        cuadroD8.config(padx=19,pady=8)
    elif result=="0":
        D8text=StringVar()
        cuadroD8.config(textvariable=D8text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(D8text,3,7))
    elif result in aux:
        D8text=StringVar()
        D8text.set(result)
        cuadroD8.config(textvariable=D8text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(D8text,3,7))
    else:
        cuadroD8.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(3,7))
    cuadroD8.grid(column=7,row=3)

    result=str(Matriz[3][8])
    if result=="-2":
        cuadroD9.config(padx=19,pady=8)
    elif result=="0":
        D9text=StringVar()
        cuadroD9.config(textvariable=D9text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(D9text,3,8))
    elif result in aux:
        D9text=StringVar()
        D9text.set(result)
        cuadroD9.config(textvariable=D9text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(D9text,3,8))
    else:
        cuadroD9.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(3,8))
    cuadroD9.grid(column=8,row=3)

#####

    result=str(Matriz[4][0])
    if result=="-2":
        cuadroE1.config(padx=19,pady=8)
    elif result=="0":
        E1text=StringVar()
        cuadroE1.config(textvariable=E1text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(E1text,4,0))
    elif result in aux:
        E1text=StringVar()
        E1text.set(result)
        cuadroE1.config(textvariable=E1text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(E1text,4,0))
    else:
        cuadroE1.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(4,0))
    cuadroE1.grid(column=0,row=4)

    result=str(Matriz[4][1])
    if result=="-2":
        cuadroE2.config(padx=19,pady=8)
    elif result=="0":
        E2text=StringVar()
        cuadroE2.config(textvariable=E2text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(E2text,4,1))
    elif result in aux:
        E2text=StringVar()
        E2text.set(result)
        cuadroE2.config(textvariable=E2text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(E2text,4,1))
    else:
        cuadroE2.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(4,1))
    cuadroE2.grid(column=1,row=4)

    result=str(Matriz[4][2])
    if result=="-2":
        cuadroE3.config(padx=19,pady=8)
    elif result=="0":
        E3text=StringVar()
        cuadroE3.config(textvariable=E3text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(E3text,4,2))
    elif result in aux:
        E3text=StringVar()
        E3text.set(result)
        cuadroE3.config(textvariable=E3text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(E3text,4,2))
    else:
        cuadroE3.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(4,2))
    cuadroE3.grid(column=2,row=4)

    result=str(Matriz[4][3])
    if result=="-2":
        cuadroE4.config(padx=19,pady=8)
    elif result=="0":
        E4text=StringVar()
        cuadroE4.config(textvariable=E4text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(E4text,4,3))
    elif result in aux:
        E4text=StringVar()
        E4text.set(result)
        cuadroE4.config(textvariable=E4text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(E4text,4,3))
    else:
        cuadroE4.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(4,3))
    cuadroE4.grid(column=3,row=4)

    result=str(Matriz[4][4])
    if result=="-2":
        cuadroE5.config(padx=19,pady=8)
    elif result=="0":
        E5text=StringVar()
        cuadroE5.config(textvariable=E5text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(E5text,4,4))
    elif result in aux:
        E5text=StringVar()
        E5text.set(result)
        cuadroE5.config(textvariable=E5text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(E5text,4,4))
    else:
        cuadroE5.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(4,4))
    cuadroE5.grid(column=4,row=4)

    result=str(Matriz[4][5])
    if result=="-2":
        cuadroE6.config(padx=19,pady=8)
    elif result=="0":
        E6text=StringVar()
        cuadroE6.config(textvariable=E6text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(E6text,4,5))
    elif result in aux:
        E6text=StringVar()
        E6text.set(result)
        cuadroE6.config(textvariable=E6text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(E6text,4,5))
    else:
        cuadroE6.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(4,5))
    cuadroE6.grid(column=5,row=4)

    result=str(Matriz[4][6])
    if result=="-2":
        cuadroE7.config(padx=19,pady=8)
    elif result=="0":
        E7text=StringVar()
        cuadroE7.config(textvariable=E7text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(E7text,4,6))
    elif result in aux:
        E7text=StringVar()
        E7text.set(result)
        cuadroE7.config(textvariable=E7text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(E7text,4,6))
    else:
        cuadroE7.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(4,6))
    cuadroE7.grid(column=6,row=4)

    result=str(Matriz[4][7])
    if result=="-2":
        cuadroE8.config(padx=19,pady=8)
    elif result=="0":
        E8text=StringVar()
        cuadroE8.config(textvariable=E8text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(E8text,4,7))
    elif result in aux:
        E8text=StringVar()
        E8text.set(result)
        cuadroE8.config(textvariable=E8text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(E8text,4,7))
    else:
        cuadroE8.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(4,7))
    cuadroE8.grid(column=7,row=4)

    result=str(Matriz[4][8])
    if result=="-2":
        cuadroE9.config(padx=19,pady=8)
    elif result=="0":
        E9text=StringVar()
        cuadroE9.config(textvariable=E9text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(E9text,4,8))
    elif result in aux:
        E9text=StringVar()
        E9text.set(result)
        cuadroE9.config(textvariable=E9text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(E9text,4,8))
    else:
        cuadroE9.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(4,8))
    cuadroE9.grid(column=8,row=4)

#####

    result=str(Matriz[5][0])
    if result=="-2":
        cuadroF1.config(padx=19,pady=8)
    elif result=="0":
        F1text=StringVar()
        cuadroF1.config(textvariable=F1text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(F1text,5,0))
    elif result in aux:
        F1text=StringVar()
        F1text.set(result)
        cuadroF1.config(textvariable=F1text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(F1text,5,0))
    else:
        cuadroF1.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(5,0))
    cuadroF1.grid(column=0,row=5)

    result=str(Matriz[5][1])
    if result=="-2":
        cuadroF2.config(padx=19,pady=8)
    elif result=="0":
        F2text=StringVar()
        cuadroF2.config(textvariable=F2text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(F2text,5,1))
    elif result in aux:
        F2text=StringVar()
        F2text.set(result)
        cuadroF2.config(textvariable=F2text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(F2text,5,1))
    else:
        cuadroF2.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(5,1))
    cuadroF2.grid(column=1,row=5)

    result=str(Matriz[5][2])
    if result=="-2":
        cuadroF3.config(padx=19,pady=8)
    elif result=="0":
        F3text=StringVar()
        cuadroF3.config(textvariable=F3text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(F3text,5,2))
    elif result in aux:
        F3text=StringVar()
        F3text.set(result)
        cuadroF3.config(textvariable=F3text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(F3text,5,2))
    else:
        cuadroF3.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(5,2))
    cuadroF3.grid(column=2,row=5)

    result=str(Matriz[5][3])
    if result=="-2":
        cuadroF4.config(padx=19,pady=8)
    elif result=="0":
        F4text=StringVar()
        cuadroF4.config(textvariable=F4text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(F4text,5,3))
    elif result in aux:
        F4text=StringVar()
        F4text.set(result)
        cuadroF4.config(textvariable=F4text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(F4text,5,3))
    else:
        cuadroF4.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(5,3))
    cuadroF4.grid(column=3,row=5)

    result=str(Matriz[5][4])
    if result=="-2":
        cuadroF5.config(padx=19,pady=8)
    elif result=="0":
        F5text=StringVar()
        cuadroF5.config(textvariable=F5text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(F5text,5,4))
    elif result in aux:
        F5text=StringVar()
        F5text.set(result)
        cuadroF5.config(textvariable=F5text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(F5text,5,4))
    else:
        cuadroF5.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(5,4))
    cuadroF5.grid(column=4,row=5)

    result=str(Matriz[5][5])
    if result=="-2":
        cuadroF6.config(padx=19,pady=8)
    elif result=="0":
        F6text=StringVar()
        cuadroF6.config(textvariable=F6text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(F6text,5,5))
    elif result in aux:
        F6text=StringVar()
        F6text.set(result)
        cuadroF6.config(textvariable=F6text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(F6text,5,5))
    else:
        cuadroF6.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(5,5))
    cuadroF6.grid(column=5,row=5)

    result=str(Matriz[5][6])
    if result=="-2":
        cuadroF7.config(padx=19,pady=8)
    elif result=="0":
        F7text=StringVar()
        cuadroF7.config(textvariable=F7text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(F7text,5,6))
    elif result in aux:
        F7text=StringVar()
        F7text.set(result)
        cuadroF7.config(textvariable=F7text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(F7text,5,6))
    else:
        cuadroF7.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(5,6))
    cuadroF7.grid(column=6,row=5)

    result=str(Matriz[5][7])
    if result=="-2":
        cuadroF8.config(padx=19,pady=8)
    elif result=="0":
        F8text=StringVar()
        cuadroF8.config(textvariable=F8text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(F8text,5,7))
    elif result in aux:
        F8text=StringVar()
        F8text.set(result)
        cuadroF8.config(textvariable=F8text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(F8text,5,7))
    else:
        cuadroF8.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(5,7))
    cuadroF8.grid(column=7,row=5)

    result=str(Matriz[5][8])
    if result=="-2":
        cuadroF9.config(padx=19,pady=8)
    elif result=="0":
        F9text=StringVar()
        cuadroF9.config(textvariable=F9text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(F9text,5,8))
    elif result in aux:
        F9text=StringVar()
        F9text.set(result)
        cuadroF9.config(textvariable=F9text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(F9text,5,8))
    else:
        cuadroF9.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(5,8))
    cuadroF9.grid(column=8,row=5)

#####

    result=str(Matriz[6][0])
    if result=="-2":
        cuadroG1.config(padx=19,pady=8)
    elif result=="0":
        G1text=StringVar()
        cuadroG1.config(textvariable=G1text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(G1text,6,0))
    elif result in aux:
        G1text=StringVar()
        G1text.set(result)
        cuadroG1.config(textvariable=G1text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(G1text,6,0))
    else:
        cuadroG1.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(6,0))
    cuadroG1.grid(column=0,row=6)

    result=str(Matriz[6][1])
    if result=="-2":
        cuadroG2.config(padx=19,pady=8)
    elif result=="0":
        G2text=StringVar()
        cuadroG2.config(textvariable=G2text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(G2text,6,1))
    elif result in aux:
        G2text=StringVar()
        G2text.set(result)
        cuadroG2.config(textvariable=G2text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(G2text,6,1))
    else:
        cuadroG2.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(6,1))
    cuadroG2.grid(column=1,row=6)

    result=str(Matriz[6][2])
    if result=="-2":
        cuadroG3.config(padx=19,pady=8)
    elif result=="0":
        G3text=StringVar()
        cuadroG3.config(textvariable=G3text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(G3text,6,2))
    elif result in aux:
        G3text=StringVar()
        G3text.set(result)
        cuadroG3.config(textvariable=G3text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(G3text,6,2))
    else:
        cuadroG3.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(6,2))
    cuadroG3.grid(column=2,row=6)

    result=str(Matriz[6][3])
    if result=="-2":
        cuadroG4.config(padx=19,pady=8)
    elif result=="0":
        G4text=StringVar()
        cuadroG4.config(textvariable=G4text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(G4text,6,3))
    elif result in aux:
        G4text=StringVar()
        G4text.set(result)
        cuadroG4.config(textvariable=G4text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(G4text,6,3))
    else:
        cuadroG4.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(6,3))
    cuadroG4.grid(column=3,row=6)

    result=str(Matriz[6][4])
    if result=="-2":
        cuadroG5.config(padx=19,pady=8)
    elif result=="0":
        G5text=StringVar()
        cuadroG5.config(textvariable=G5text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(G5text,6,4))
    elif result in aux:
        G5text=StringVar()
        G5text.set(result)
        cuadroG5.config(textvariable=G5text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(G5text,6,4))
    else:
        cuadroG5.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(6,4))
    cuadroG5.grid(column=4,row=6)

    result=str(Matriz[6][5])
    if result=="-2":
        cuadroG6.config(padx=19,pady=8)
    elif result=="0":
        G6text=StringVar()
        cuadroG6.config(textvariable=G6text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(G6text,6,5))
    elif result in aux:
        G6text=StringVar()
        G6text.set(result)
        cuadroG6.config(textvariable=G6text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(G6text,6,5))
    else:
        cuadroG6.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(6,5))
    cuadroG6.grid(column=5,row=6)

    result=str(Matriz[6][6])
    if result=="-2":
        cuadroG7.config(padx=19,pady=8)
    elif result=="0":
        G7text=StringVar()
        cuadroG7.config(textvariable=G7text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(G7text,6,6))
    elif result in aux:
        G7text=StringVar()
        G7text.set(result)
        cuadroG7.config(textvariable=G7text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(G7text,6,6))
    else:
        cuadroG7.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(6,6))
    cuadroG7.grid(column=6,row=6)

    result=str(Matriz[6][7])
    if result=="-2":
        cuadroG8.config(padx=19,pady=8)
    elif result=="0":
        G8text=StringVar()
        cuadroG8.config(textvariable=G8text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(G8text,6,7))
    elif result in aux:
        G8text=StringVar()
        G8text.set(result)
        cuadroG8.config(textvariable=G8text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(G8text,6,7))
    else:
        cuadroG8.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(6,7))
    cuadroG8.grid(column=7,row=6)

    result=str(Matriz[6][8])
    if result=="-2":
        cuadroG9.config(padx=19,pady=8)
    elif result=="0":
        G9text=StringVar()
        cuadroG9.config(textvariable=G9text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(G9text,6,8))
    elif result in aux:
        G9text=StringVar()
        G9text.set(result)
        cuadroG9.config(textvariable=G9text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(G9text,6,8))
    else:
        cuadroG9.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(6,8))
    cuadroG9.grid(column=8,row=6)

#####

    result=str(Matriz[7][0])
    if result=="-2":
        cuadroH1.config(padx=19,pady=8)
    elif result=="0":
        H1text=StringVar()
        cuadroH1.config(textvariable=H1text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(H1text,7,0))
    elif result in aux:
        H1text=StringVar()
        H1text.set(result)
        cuadroH1.config(textvariable=H1text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(H1text,7,0))
    else:
        cuadroH1.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(7,0))
    cuadroH1.grid(column=0,row=7)

    result=str(Matriz[7][1])
    if result=="-2":
        cuadroH2.config(padx=19,pady=8)
    elif result=="0":
        H2text=StringVar()
        cuadroH2.config(textvariable=H2text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(H2text,7,1))
    elif result in aux:
        H2text=StringVar()
        H2text.set(result)
        cuadroH2.config(textvariable=H2text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(H2text,7,1))
    else:
        cuadroH2.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(7,1))
    cuadroH2.grid(column=1,row=7)

    result=str(Matriz[7][2])
    if result=="-2":
        cuadroH3.config(padx=19,pady=8)
    elif result=="0":
        H3text=StringVar()
        cuadroH3.config(textvariable=H3text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(H3text,7,2))
    elif result in aux:
        H3text=StringVar()
        H3text.set(result)
        cuadroH3.config(textvariable=H3text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(H3text,7,2))
    else:
        cuadroH3.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(7,2))
    cuadroH3.grid(column=2,row=7)

    result=str(Matriz[7][3])
    if result=="-2":
        cuadroH4.config(padx=19,pady=8)
    elif result=="0":
        H4text=StringVar()
        cuadroH4.config(textvariable=H4text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(H4text,7,3))
    elif result in aux:
        H4text=StringVar()
        H4text.set(result)
        cuadroH4.config(textvariable=H4text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(H4text,7,3))
    else:
        cuadroH4.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(7,3))
    cuadroH4.grid(column=3,row=7)

    result=str(Matriz[7][4])
    if result=="-2":
        cuadroH5.config(padx=19,pady=8)
    elif result=="0":
        H5text=StringVar()
        cuadroH5.config(textvariable=H5text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(H5text,7,4))
    elif result in aux:
        H5text=StringVar()
        H5text.set(result)
        cuadroH5.config(textvariable=H5text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(H5text,7,4))
    else:
        cuadroH5.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(7,4))
    cuadroH5.grid(column=4,row=7)

    result=str(Matriz[7][5])
    if result=="-2":
        cuadroH6.config(padx=19,pady=8)
    elif result=="0":
        H6text=StringVar()
        cuadroH6.config(textvariable=H6text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(H6text,7,5))
    elif result in aux:
        H6text=StringVar()
        H6text.set(result)
        cuadroH6.config(textvariable=H6text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(H6text,7,5))
    else:
        cuadroH6.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(7,5))
    cuadroH6.grid(column=5,row=7)

    result=str(Matriz[7][6])
    if result=="-2":
        cuadroH7.config(padx=19,pady=8)
    elif result=="0":
        H7text=StringVar()
        cuadroH7.config(textvariable=H7text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(H7text,7,6))
    elif result in aux:
        H7text=StringVar()
        H7text.set(result)
        cuadroH7.config(textvariable=H7text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(H7text,7,6))
    else:
        cuadroH7.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(7,6))
    cuadroH7.grid(column=6,row=7)

    result=str(Matriz[7][7])
    if result=="-2":
        cuadroH8.config(padx=19,pady=8)
    elif result=="0":
        H8text=StringVar()
        cuadroH8.config(textvariable=H8text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(H8text,7,7))
    elif result in aux:
        H8text=StringVar()
        H8text.set(result)
        cuadroH8.config(textvariable=H8text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(H8text,7,7))
    else:
        cuadroH8.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(7,7))
    cuadroH8.grid(column=7,row=7)

    result=str(Matriz[7][8])
    if result=="-2":
        cuadroH9.config(padx=19,pady=8)
    elif result=="0":
        H9text=StringVar()
        cuadroH9.config(textvariable=H9text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(H9text,7,8))
    elif result in aux:
        H9text=StringVar()
        H9text.set(result)
        cuadroH9.config(textvariable=H9text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(H9text,7,8))
    else:
        cuadroH9.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(7,8))
    cuadroH9.grid(column=8,row=7)

#####
    
    result=str(Matriz[8][0])
    if result=="-2":
        cuadroI1.config(padx=19,pady=8)
    elif result=="0":
        I1text=StringVar()
        cuadroI1.config(textvariable=I1text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(I1text,8,0))
    elif result in aux:
        I1text=StringVar()
        I1text.set(result)
        cuadroI1.config(textvariable=I1text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(I1text,8,0))
    else:
        cuadroI1.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(8,0))
    cuadroI1.grid(column=0,row=8)

    result=str(Matriz[8][1])
    if result=="-2":
        cuadroI2.config(padx=19,pady=8)
    elif result=="0":
        I2text=StringVar()
        cuadroI2.config(textvariable=I2text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(I2text,8,1))
    elif result in aux:
        I2text=StringVar()
        I2text.set(result)
        cuadroI2.config(textvariable=I2text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(I2text,8,1))
    else:
        cuadroI2.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(8,1))
    cuadroI2.grid(column=1,row=8)

    result=str(Matriz[8][2])
    if result=="-2":
        cuadroI3.config(padx=19,pady=8)
    elif result=="0":
        I3text=StringVar()
        cuadroI3.config(textvariable=I3text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(I3text,8,2))
    elif result in aux:
        I3text=StringVar()
        I3text.set(result)
        cuadroI3.config(textvariable=I3text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(I3text,8,2))
    else:
        cuadroI3.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(8,2))
    cuadroI3.grid(column=2,row=8)

    result=str(Matriz[8][3])
    if result=="-2":
        cuadroI4.config(padx=19,pady=8)
    elif result=="0":
        I4text=StringVar()
        cuadroI4.config(textvariable=I4text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(I4text,8,3))
    elif result in aux:
        I4text=StringVar()
        I4text.set(result)
        cuadroI4.config(textvariable=I4text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(I4text,8,3))
    else:
        cuadroI4.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(8,3))
    cuadroI4.grid(column=3,row=8)

    result=str(Matriz[8][4])
    if result=="-2":
        cuadroI5.config(padx=19,pady=8)
    elif result=="0":
        I5text=StringVar()
        cuadroI5.config(textvariable=I5text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(I5text,8,4))
    elif result in aux:
        I5text=StringVar()
        I5text.set(result)
        cuadroI5.config(textvariable=I5text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(I5text,8,4))
    else:
        cuadroI5.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(8,4))
    cuadroI5.grid(column=4,row=8)

    result=str(Matriz[8][5])
    if result=="-2":
        cuadroI6.config(padx=19,pady=8)
    elif result=="0":
        I6text=StringVar()
        cuadroI6.config(textvariable=I6text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(I6text,8,5))
    elif result in aux:
        I6text=StringVar()
        I6text.set(result)
        cuadroI6.config(textvariable=I6text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(I6text,8,5))
    else:
        cuadroI6.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(8,5))
    cuadroI6.grid(column=5,row=8)

    result=str(Matriz[8][6])
    if result=="-2":
        cuadroI7.config(padx=19,pady=8)
    elif result=="0":
        I7text=StringVar()
        cuadroI7.config(textvariable=I7text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(I8text,8,6))
    elif result in aux:
        I8text=StringVar()
        I8text.set(result)
        cuadroI8.config(textvariable=I8text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(I8text,8,6))
    else:
        cuadroI7.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(8,6))
    cuadroI7.grid(column=6,row=8)

    result=str(Matriz[8][7])
    if result=="-2":
        cuadroI8.config(padx=19,pady=8)
    elif result=="0":
        I8text=StringVar()
        cuadroI8.config(textvariable=I8text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(I8text,8,7))
    elif result in aux:
        I8text=StringVar()
        I8text.set(result)
        cuadroI8.config(textvariable=I8text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(I8text,8,7))
    else:
        cuadroI8.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(8,7))
    cuadroI8.grid(column=7,row=8)

    result=str(Matriz[8][8])
    if result=="-2":
        cuadroI9.config(padx=19,pady=8)
    elif result=="0":
        I9text=StringVar()
        cuadroI9.config(textvariable=I9text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(I9text,8,8))
    elif result in aux:
        I9text=StringVar()
        I9text.set(result)
        cuadroI9.config(textvariable=I9text,padx=11.5,pady=8,bg="White",fg="Black",command=lambda:Click_pantalla(I9text,8,8))
    else:
        cuadroI9.config(text=result,padx=10,pady=7,bg="Red4",command=lambda:Click_jugadas(8,8))
    cuadroI9.grid(column=8,row=8)
##########################################################################################################################################################

    
def Change(fila,columna,numero):
    """Función que nos ayuda a cambiar un número en una posición de la matriz."""

    #Primero se obtiene la lista donde se encuentra el número, se borra el
    #número al que se quiere reemplazar y se coloca el nuevo.
    lista=Matriz[fila]
    del lista[columna]
    lista.insert(columna,numero)
    del Matriz[fila]
    Matriz.insert(fila,lista)
    
def check(lista):
    """Función que nos ayuda a descubrir la posición de las claves dobles
    que hay dentro de la partida."""
    dobles_posicion=[]
    y=[]
    for cuadro in lista:
        num=cuadro[1]
        fila=cuadro[2]
        columna=cuadro[3]
        cont=0
        result=0
        while cont<len(lista):
            boton=lista[cont]
            ubicacion=[fila,columna]
            if fila==boton[2] and columna==boton[3]:
                result+=1
                if result==2:
                    text=[num,boton[1]]
                    x=ubicacion in dobles_posicion
                    if x==False:
                        dobles_posicion.append(ubicacion)
                        y.append(text)
            cont+=1
    return dobles_posicion

def check_text(lista):
    """Función que nos ayuda a descubrir el valor de las claves dobles
    que hay en la partida."""
    dobles_posicion=[]
    y=[]
    for cuadro in lista:
        num=cuadro[1]
        fila=cuadro[2]
        columna=cuadro[3]
        cont=0
        result=0
        while cont<len(lista):
            boton=lista[cont]
            ubicacion=[fila,columna]
            if fila==boton[2] and columna==boton[3]:
                result+=1
                if result==2:
                    text=[num,boton[1]]
                    x=ubicacion in dobles_posicion
                    if x==False:
                        dobles_posicion.append(ubicacion)
                        y.append(text)
            cont+=1
    return y

def Click(valor,color):
    """Función que ayuda a cambiar el color de los botones con los
    números(1-9) y hace global una variable con el número seleccionado."""
    
    global dig
    global txt
    global boton1
    global boton2
    global boton3
    global boton4
    global boton5
    global boton6
    global boton7
    global boton8
    global boton9
    if valor==1:
        txt="1"
        boton1.config(bg=color)
        boton2.config(bg="Black")
        boton3.config(bg="Black")
        boton4.config(bg="Black")
        boton5.config(bg="Black")
        boton6.config(bg="Black")
        boton7.config(bg="Black")
        boton8.config(bg="Black")
        boton9.config(bg="Black")
          
    elif valor==2:
        txt="2"
        boton1.config(bg="Black")
        boton2.config(bg=color)
        boton3.config(bg="Black")
        boton4.config(bg="Black")
        boton5.config(bg="Black")
        boton6.config(bg="Black")
        boton7.config(bg="Black")
        boton8.config(bg="Black")
        boton9.config(bg="Black")
        dig=2
        
    elif valor==3:
        txt="3"
        boton1.config(bg="Black")
        boton2.config(bg="Black")
        boton3.config(bg=color)
        boton4.config(bg="Black")
        boton5.config(bg="Black")
        boton6.config(bg="Black")
        boton7.config(bg="Black")
        boton8.config(bg="Black")
        boton9.config(bg="Black")
        dig=3
        
    elif valor==4:
        txt="4"
        boton1.config(bg="Black")
        boton2.config(bg="Black")
        boton3.config(bg="Black")
        boton4.config(bg=color)
        boton5.config(bg="Black")
        boton6.config(bg="Black")
        boton7.config(bg="Black")
        boton8.config(bg="Black")
        boton9.config(bg="Black")
        dig=4
        
    elif valor==5:
        txt="5"
        boton1.config(bg="Black")
        boton2.config(bg="Black")
        boton3.config(bg="Black")
        boton4.config(bg="Black")
        boton5.config(bg=color)
        boton6.config(bg="Black")
        boton7.config(bg="Black")
        boton8.config(bg="Black")
        boton9.config(bg="Black")
        dig=5
        
    elif valor==6:
        txt="6"
        boton1.config(bg="Black")
        boton2.config(bg="Black")
        boton3.config(bg="Black")
        boton4.config(bg="Black")
        boton5.config(bg="Black")
        boton6.config(bg=color)
        boton7.config(bg="Black")
        boton8.config(bg="Black")
        boton9.config(bg="Black")
        dig=6
        
    elif valor==7:
        txt="7"
        boton1.config(bg="Black")
        boton2.config(bg="Black")
        boton3.config(bg="Black")
        boton4.config(bg="Black")
        boton5.config(bg="Black")
        boton6.config(bg="Black")
        boton7.config(bg=color)
        boton8.config(bg="Black")
        boton9.config(bg="Black")
        dig=7
        
    elif valor==8:
        txt="8"
        boton1.config(bg="Black")
        boton2.config(bg="Black")
        boton3.config(bg="Black")
        boton4.config(bg="Black")
        boton5.config(bg="Black")
        boton6.config(bg="Black")
        boton7.config(bg="Black")
        boton8.config(bg=color)
        boton9.config(bg="Black")
        dig=8
        
    elif valor==9:
        txt="9"
        boton1.config(bg="Black")
        boton2.config(bg="Black")
        boton3.config(bg="Black")
        boton4.config(bg="Black")
        boton5.config(bg="Black")
        boton6.config(bg="Black")
        boton7.config(bg="Black")
        boton8.config(bg="Black")
        boton9.config(bg=color)
        dig=9

l_jugadas=[]
l_rehacer=[]
def Click_pantalla(var,fila,columna):
    """Función que coloca el número seleccionado en la columna de números(1-9)
    y lo coloca en el botón presionado en el tablero."""
    #La variable emergencia funciona para que el botón de "Borrar Jugada" funcione.
    global emergencia
    
    global Num_rehacer
    global confirmar_jugada

    confirmar_jugada=True

    #Colocar en var, que va a ser el texto del botón presionado en el tablero, el valor
    #que se desea.
    var.set(txt)
    Click(int(txt),"Black")
    emergencia=var
    Num_rehacer=var.get()
    l_jugadas.append([var,Num_rehacer])
    Change(fila,columna,int(txt))
    #Revisar que las columna y las filas esten sin ningún error.
    Revisar()
    Revision_final()

def deshacer_jugada():
    if confirmar_jugada==True:
        VAR=l_jugadas[-1][0]
        VAR.set("")
        l_rehacer.append([VAR,l_jugadas[-1][1]])
        del l_jugadas[-1]
    else:
        tkinter.messagebox.showerror("Error","No se ha realizado ninguna jugada.")

def rehacer_jugada():
    if confirmar_jugada==True:
        VAR=l_rehacer[-1][0]
        VAR.set(l_rehacer[-1][1])
        l_jugadas.append([VAR,l_rehacer[-1][1]])
        del l_rehacer[-1]
    else:
        tkinter.messagebox.showerror("Error","No se ha realizado ninguna jugada.")

def borrar_jugada():
    """Función que funciona para borrar la última jugada realizada dejando la casilla
    un espacio en blanco para que el jugador pueda digitar el número nuevamente."""

    #Revisar que la partida haya comenzado, de lo contrario avisar.
    if inicio_de_la_partida==True:
        try:
            preg=tkinter.messagebox.askyesno("Borrar jugada","¿Seguro que desea borrar la jugada?")
            if preg==True:
                emergencia.set("")

            else:
                pass
        except:
            tkinter.messagebox.showerror("Error","No se ha realizado ninguna jugada.")
    else:
        tkinter.messagebox.showerror("Error","No se ha comenzado el juego.")


def borrar_juego():
    """Fución que borra todo el tablero dejando en blanco todas las casillas."""

    #Revisar que la partida haya comenzado, de lo contrario avisar.
    #El proceso es el mismo realizado por revisar_matriz, pero esta
    #función no va a leer la partida del archivo.
    global inicio_de_la_partida
    if inicio_de_la_partida==True:
        preg=tkinter.messagebox.askyesno("Borrar jugada","¿Seguro que desea borrar el juego?")
        if preg==True:
            dobles=check(partida)
            dobles_text=check_text(partida)

            for cuadro in partida:
                tipo=cuadro[0]
                num=cuadro[1]
                fila=cuadro[2]
                columna=cuadro[3]
                casillas=cuadro[4]

                ubicacion=[fila,columna]
                conf=ubicacion in dobles
                if conf==True:
                    pass
                else:
                    copy_fila=fila-1
                    copy_columna=columna-1
                    if tipo==1:
                        Change(copy_fila,copy_columna,"\\"+str(num))
                    else:
                        Change(copy_fila,copy_columna,str(num)+"\\")

                while casillas!=0:
                    if tipo==1:
                        columna+=1
                    else:
                        fila+=1
                    casillas-=1
                    copy_fila=fila-1
                    copy_columna=columna-1
                    Change(copy_fila,copy_columna,0)
            

            if dobles!=[]:
                cont=0
                for ubicacion in dobles:
                    numeros=dobles_text[cont]
                    cont+=1
                    copy_fila=ubicacion[0]-1
                    copy_columna=ubicacion[1]-1
                    Change(copy_fila,copy_columna,str(numeros[1])+"\\"+str(numeros[0]))
            colocar()
        else:
            pass
    else:
        tkinter.messagebox.showerror("Error","No se ha comenzado el juego.")


def Guardar():
    """Función que guarda la partida en un archivo."""

    #Primero se abre el archivo borando todo lo que tenga dentro.
    G=open("kakuro2018juegoactual.txt","w")

    #Se escribe en el la matriz, dificultad, partida y el nombre del jugador.
    G.write(str(Matriz)+"\n")
    G.write("Dificultad = "+str(dificult)+"\n")
    G.write(str(partida)+"\n")
    G.write(Caja_nombre.get())

    #Cerrar archivo.
    G.close()

    x=tkinter.messagebox.askyesno("Salir","¿Va a continuar jugando?")
    if x==True:
        pass
    else:
        pantalla.destroy()
        
    

def Cargar():
    """Función que carga la partida de un archivo."""
    global inicio_de_la_partida
    global partida
    global Matriz

    #Se verifica que la partida haya comenzado.
    inicio_de_la_partida=True

    #Se abre el archivo y leer cada linea.
    G=open("kakuro2018juegoactual.txt","r")
    Linea=G.readlines()

    #La linea 1 contiene la dificultad.
    x=Linea[1]
    if x=="Dificultad = Easy\n":
        dificult="Easy"
        
    elif x=="Dificultad = Medium\n":
        dificult="Medium"
        
    elif x=="Dificultad = Hard\n":
        dificult="Hard"

    #Linea 3 contiene el nombre del jugador.
    Nombre=StringVar()
    Caja_nombre.config(textvariable=Nombre)
    Nombre.set(Linea[3])

    #Linea 2 contiene la partida.
    partida=eval(Linea[2])

    #Utilizar casi el mismo procedimiento de cambiar_matriz solo que sin leer
    #la partida del archivo.
    dobles=check(partida)
    dobles_text=check_text(partida)

    for cuadro in partida:
        tipo=cuadro[0]
        num=cuadro[1]
        fila=cuadro[2]
        columna=cuadro[3]
        casillas=cuadro[4]

        ubicacion=[fila,columna]
        conf=ubicacion in dobles
        if conf==True:
            pass
        else:
            copy_fila=fila-1
            copy_columna=columna-1
            if tipo==1:
                Change(copy_fila,copy_columna,"\\"+str(num))
            else:
                Change(copy_fila,copy_columna,str(num)+"\\")

        while casillas!=0:
            if tipo==1:
                columna+=1
            else:
                fila+=1
            casillas-=1
            copy_fila=fila-1
            copy_columna=columna-1
            Change(copy_fila,copy_columna,0)
    

    if dobles!=[]:
        cont=0
        for ubicacion in dobles:
            numeros=dobles_text[cont]
            cont+=1
            copy_fila=ubicacion[0]-1
            copy_columna=ubicacion[1]-1
            Change(copy_fila,copy_columna,str(numeros[1])+"\\"+str(numeros[0]))

    #Linea 0 contiene la matriz.
    Matriz=eval(Linea[0])
    colocar()



def destruir_botones():
    cuadroA1.destroy()
    cuadroA2.destroy()
    cuadroA3.destroy()
    cuadroA4.destroy()
    cuadroA5.destroy()
    cuadroA6.destroy()
    cuadroA7.destroy()
    cuadroA8.destroy()
    cuadroA9.destroy()
    cuadroB1.destroy()
    cuadroB2.destroy()
    cuadroB3.destroy()
    cuadroB4.destroy()
    cuadroB5.destroy()
    cuadroB6.destroy()
    cuadroB7.destroy()
    cuadroB8.destroy()
    cuadroB9.destroy()
    cuadroC1.destroy()
    cuadroC2.destroy()
    cuadroC3.destroy()
    cuadroC4.destroy()
    cuadroC5.destroy()
    cuadroC6.destroy()
    cuadroC7.destroy()
    cuadroC8.destroy()
    cuadroC9.destroy()
    cuadroD1.destroy()
    cuadroD2.destroy()
    cuadroD3.destroy()
    cuadroD4.destroy()
    cuadroD5.destroy()
    cuadroD6.destroy()
    cuadroD7.destroy()
    cuadroD8.destroy()
    cuadroD9.destroy()
    cuadroE1.destroy()
    cuadroE2.destroy()
    cuadroE3.destroy()
    cuadroE4.destroy()
    cuadroE5.destroy()
    cuadroE6.destroy()
    cuadroE7.destroy()
    cuadroE8.destroy()
    cuadroE9.destroy()
    cuadroF1.destroy()
    cuadroF2.destroy()
    cuadroF3.destroy()
    cuadroF4.destroy()
    cuadroF5.destroy()
    cuadroF6.destroy()
    cuadroF7.destroy()
    cuadroF8.destroy()
    cuadroF9.destroy()
    cuadroG1.destroy()
    cuadroG2.destroy()
    cuadroG3.destroy()
    cuadroG4.destroy()
    cuadroG5.destroy()
    cuadroG6.destroy()
    cuadroG7.destroy()
    cuadroG8.destroy()
    cuadroG9.destroy()
    cuadroH1.destroy()
    cuadroH2.destroy()
    cuadroH3.destroy()
    cuadroH4.destroy()
    cuadroH5.destroy()
    cuadroH6.destroy()
    cuadroH7.destroy()
    cuadroH8.destroy()
    cuadroH9.destroy()
    cuadroI1.destroy()
    cuadroI2.destroy()
    cuadroI3.destroy()
    cuadroI4.destroy()
    cuadroI5.destroy()
    cuadroI6.destroy()
    cuadroI7.destroy()
    cuadroI8.destroy()
    cuadroI9.destroy()
    
    
def kakuro():
    """Función que despliega la interfaz gráfica del kakuro con todos sus elentos listos
    para comenzar a jugar."""

    #Colocamos las variables globales necesarias para el resto de funciones.
    global pantalla
    global txt
    global boton1
    global boton2
    global boton3
    global boton4
    global boton5
    global boton6
    global boton7
    global boton8
    global boton9
    global Caja_nombre

    #Creamos la ventana editando el nombre, color, posición, etc.
    pantalla=Toplevel()
    pantalla.title("Kakuro")
    pantalla.geometry("950x500+350+20")
    pantalla.configure(bg="Black")
    etiqueta=Label(pantalla,text="Kakuro",bg="Black",fg="Red3",
                   font=("Chiller",40)).place(x=750,y=0)

    #Variable que va a almacenar los dígitos cada vez que los botones de
    #números sean presionados.
    txt=StringVar()

    #Lista de los botones(1-9)
    boton1=Button(pantalla,text="1",bg="Black",fg="White",font=("Arial",15),
                  padx=25,command=lambda:Click(1,"Slate Grey"))
    boton1.place(x=500,y=20)

    
    boton2=Button(pantalla,text="2",bg="Black",fg="White",font=("Arial",15),
                  padx=25,command=lambda:Click(2,"Slate Grey"))
    boton2.place(x=500,y=60)

    
    boton3=Button(pantalla,text="3",bg="Black",fg="White",font=("Arial",15),
                  padx=25,command=lambda:Click(3,"Slate Grey"))
    boton3.place(x=500,y=100)

    
    boton4=Button(pantalla,text="4",bg="Black",fg="White",font=("Arial",15),
                  padx=25,command=lambda:Click(4,"Slate Grey"))
    boton4.place(x=500,y=140)

    
    boton5=Button(pantalla,text="5",bg="Black",fg="White",font=("Arial",15),
                  padx=25,command=lambda:Click(5,"Slate Grey"))
    boton5.place(x=500,y=180)

    
    boton6=Button(pantalla,text="6",bg="Black",fg="White",font=("Arial",15),
                  padx=25,command=lambda:Click(6,"Slate Grey"))
    boton6.place(x=500,y=220)

    
    boton7=Button(pantalla,text="7",bg="Black",fg="White",font=("Arial",15),
                  padx=25,command=lambda:Click(7,"Slate Grey"))
    boton7.place(x=500,y=260)

    
    boton8=Button(pantalla,text="8",bg="Black",fg="White",font=("Arial",15),
                  padx=25,command=lambda:Click(8,"Slate Grey"))
    boton8.place(x=500,y=300)

    
    boton9=Button(pantalla,text="9",bg="Black",fg="White",font=("Arial",15),
                  padx=25,command=lambda:Click(9,"Slate Grey"))
    boton9.place(x=500,y=340)
    

    #Colocar los botones principales con su configuración.
    boton_Iniciar=Button(pantalla,text="Iniciar\nJuego",bg="Navy",fg="Black",font=("Arial",13),
                  padx=20,command=cambiar_matriz).place(x=650,y=60)
    boton_BorrarJugada=Button(pantalla,text="Borrar\nJugada",bg="Red4",fg="Black",font=("Arial",13),
                  padx=20,command=borrar_jugada).place(x=650,y=120)
    boton_Terminar=Button(pantalla,text="Terminar\nJuego",bg="Navy",fg="Black",font=("Arial",13),
                  padx=20,command=Terminar).place(x=650,y=180)
    boton_BorrarJuego=Button(pantalla,text="Borrar\nJuego",bg="Red4",fg="Black",font=("Arial",13),
                  padx=20,command=borrar_juego).place(x=650,y=240)
    boton_Top10=Button(pantalla,text="TOP\n10",bg="Gold",fg="Black",font=("Arial",13),
                  padx=20).place(x=650,y=300)
    boton_Guardar=Button(pantalla,text="Guardar Juego",bg="Black",fg="White",
                         font=("Arial",15),command=Guardar).place(x=60,y=410)
    boton_Cargar=Button(pantalla,text="Cargar Juego",bg="Black",fg="White",
                         font=("Arial",15),command=Cargar).place(x=280,y=410)

    
    boton_deshacer=Button(pantalla,text="Deshacer\nJugada",bg="Gray",font=("Arial",13),
                          padx=20,command=deshacer_jugada).place(x=800,y=60)
    boton_rehacer=Button(pantalla,text="Rehacer\nJugada",bg="Gray",font=("Arial",13),
                          padx=20,command=rehacer_jugada).place(x=800,y=120)

    crear_botones()
    #Colocar la caja de texto donde el jugador coloca su nombre.
    Nombre=Label(pantalla,text="Nombre del Jugador:",bg="Black",fg="White",
                 font=("Arial",15)).place(x=550,y=410)
    Caja_nombre=Entry(pantalla,bg="gray",fg="Black",width=20)
    Caja_nombre.focus()
    Caja_nombre.place(x=745,y=416)
    
    #Colocar una etiquta que le indica al usuario en que dificultad esta jugando.
    if dificult=="Easy":
        Neurona=Label(pantalla,text="Nivel: 1 Neurona",bg="Black",fg="White",
                     font=("Arial",15)).place(x=550,y=450)
    elif dificult=="Medium":
        Neurona=Label(pantalla,text="Nivel: 2 Neuronas",bg="Black",fg="White",
                     font=("Arial",15)).place(x=550,y=450)
    elif dificult=="Hard":
        Neurona=Label(pantalla,text="Nivel: 3 Neuronas",bg="Black",fg="White",
                     font=("Arial",15)).place(x=550,y=450)

    #Solamente crear los botones del tablero sin colocarles valores ni posiciones.
def crear_botones():
    """Función para crear los botones"""
    global cuadroA1
    cuadroA1=Button(pantalla,bg="Black",fg="White",justify="center")
    global cuadroA2
    cuadroA2=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroA3
    cuadroA3=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroA4
    cuadroA4=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroA5
    cuadroA5=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroA6
    cuadroA6=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroA7
    cuadroA7=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroA8
    cuadroA8=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroA9
    cuadroA9=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)

    global cuadroB1
    cuadroB1=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroB2
    cuadroB2=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroB3
    cuadroB3=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroB4
    cuadroB4=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroB5
    cuadroB5=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroB6
    cuadroB6=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroB7
    cuadroB7=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroB8
    cuadroB8=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroB9
    cuadroB9=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)

    global cuadroC1
    cuadroC1=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroC2
    cuadroC2=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroC3
    cuadroC3=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroC4
    cuadroC4=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroC5
    cuadroC5=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroC6
    cuadroC6=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroC7
    cuadroC7=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroC8
    cuadroC8=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroC9
    cuadroC9=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    
    global cuadroD1   
    cuadroD1=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroD2
    cuadroD2=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroD3
    cuadroD3=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroD4
    cuadroD4=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroD5
    cuadroD5=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroD6
    cuadroD6=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroD7
    cuadroD7=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroD8
    cuadroD8=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroD9
    cuadroD9=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)

    global cuadroE1
    cuadroE1=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroE2
    cuadroE2=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroE3
    cuadroE3=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroE4
    cuadroE4=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroE5
    cuadroE5=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroE6
    cuadroE6=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroE7
    cuadroE7=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroE8
    cuadroE8=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroE9
    cuadroE9=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)

    global cuadroF1        
    cuadroF1=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroF2
    cuadroF2=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroF3
    cuadroF3=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroF4
    cuadroF4=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroF5
    cuadroF5=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroF6
    cuadroF6=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroF7
    cuadroF7=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroF8
    cuadroF8=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroF9
    cuadroF9=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    
    global cuadroG1
    cuadroG1=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroG2
    cuadroG2=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroG3
    cuadroG3=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroG4
    cuadroG4=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroG5
    cuadroG5=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroG6
    cuadroG6=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroG7
    cuadroG7=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroG8
    cuadroG8=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroG9
    cuadroG9=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)

    global cuadroH1
    cuadroH1=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroH2
    cuadroH2=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroH3
    cuadroH3=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroH4
    cuadroH4=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroH5
    cuadroH5=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroH6
    cuadroH6=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroH7
    cuadroH7=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroH8
    cuadroH8=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroH9
    cuadroH9=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    
    global cuadroI1
    cuadroI1=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroI2
    cuadroI2=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroI3
    cuadroI3=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroI4
    cuadroI4=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroI5
    cuadroI5=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroI6
    cuadroI6=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroI7
    cuadroI7=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroI8
    cuadroI8=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    global cuadroI9
    cuadroI9=Button(pantalla,bg="Black",fg="White",justify="center",padx=7,pady=7)
    


    







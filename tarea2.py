import os
class grafica:
    def graphMATRIZ(self,fila,columna,posY,posX):
        #INICIO DE LA LISTA
        #SE CREA EL PUNTO DOT.; W ES PARA ESCRIBIR EN EL ARCHIVO
        f=open("graficoMATRIZ.dot","w")
        #SE INICIA EL DIAGRAMA
        f.write("digraph G {\n")
        #SE ESTABLECE LA FORMA CUADRADA
        f.write(" node [shape=record];\n")
        #SE ESTABLECE FORMA HORIZONTAL
        f.write("struct3 [shape=record,label=\" {\n")
        #SE CREAN DOS NODOS NULL
        Struct = ''
        #RELACIONES ENTRE NODOS
        for i in range (fila):#filas
            Struct += "{"
            for c in range (columna):#columnas
                if c == columna-1:
                    if c == posX-1 and i== posY-1:
                        Struct +="X"
                    else:
                        Struct +=str(matriz[i][c])
                else:
                    if c == posX-1 and i== posY-1:
                        Struct +="X"+"|"
                    else:
                        Struct +=str(matriz[i][c])+"|"
            if i == fila-1:
                Struct += "}"
            else:
                Struct += "}|"
        #SE CIERRA EL GRAFICO
        f.write(Struct+'\n')
        f.write("}\" \n ];"+'\n')
        f.write('}')
        f.close()
        #SE TRANSFORMA EL .DOT A .JPG (EL NOMBRE .DOT TIENE QUE SER EL DE ARRIBA, EL .JPG PUEDE SER DIFERENTE)
        os.system("dot.exe -Tjpg graficoMATRIZ.dot -o graficoMATRIZ.jpg")
        #SE ABRE EL ARCHIVO .JPG
        os.system("graficoMATRIZ.jpg")

















if __name__ == "__main__":
    GRAFICA = grafica()
    salir=False
    while(not salir):
        print("-------Menu Principal---------\n"+
        "Mapeo Lexografico\n"+
        "1. Filas Cosecutivas\n"+
        "2. Columnas Consecutivas"
        )
        num = input("Ingrese su opcion: ")

        if num == "1":
            print("-----Filas Consecutivas-----")
            filas = input("Ingrese cantidad de filas: ")
            columnas = input("Ingrese cantidad de columnas: ")

            matriz = []
            lista = []

            for i in range (int(filas)):
                matriz.append([0]*int(columnas))
            
            cont = 0
            for i in range (int(filas)):#filas
                for c in range (int(columnas)):#columnas
                    matriz[i][c] = cont
                    lista.extend([cont])
                    cont += 1

            
            print(matriz)

            columnas2 = input("Ingrese # de columnas a linealizar: ")
            filas2 = input("Ingrese # de fila a linealizar: ")

            posicion = (int(filas2)-1)*(int(columnas))+(int(columnas2)-1)
            
            print('valor de la posicion XY en la matriz: {}'.format(matriz[int(filas2)-1][int(columnas2)-1]))
            print('posicion linealizada en la lista: {}'.format(posicion))
            print('valor de la posicion linealizada de la lista: {}'.format(lista[posicion]))
            print(lista)
            GRAFICA.graphMATRIZ(int(filas),int(columnas),int(filas2),int(columnas2))

            f=open("graficoFILAConsecutiva2.dot","w")
            f.write("digraph G {\n")
            f.write("rankdir=LR;\n")
            f.write(" node [shape=record];\n")
            f.write("struct3 [shape=record,label=\" \n")
            Struct = '{'
            for i in range (len(lista)):#filas
                if i == len(lista)-1:
                    if i == posicion:
                            Struct +="X"
                    else:
                        Struct +=str(lista[i])
                else:
                    if i == posicion:
                        Struct +="X|"
                    else:
                        Struct +=str(lista[i])+"|"
            f.write(Struct+'\n')
            f.write("}\" \n ];"+'\n')
            f.write('}')
            f.close()
            os.system("dot.exe -Tjpg graficoFILAConsecutiva2.dot -o graficoFILAConsecutiva2.jpg")
            os.system("graficoFILAConsecutiva2.jpg")

        if num == "2":
            print("-----Columnas Consecutivas-----")
            filas = input("Ingrese cantidad de filas: ")
            columnas = input("Ingrese cantidad de columnas: ")

            matriz = []
            lista = []

            for i in range (int(filas)):
                matriz.append([0]*int(columnas))
            
            cont = 0
            for i in range (int(filas)):#filas
                for c in range (int(columnas)):#columnas
                    matriz[i][c] = cont
                    cont += 1
            
            for i in range (int(columnas)):#columnas
                for c in range (int(filas)):#filas
                    lista.extend([matriz[c][i]])
            
            print(matriz)

            columnas2 = input("Ingrese # de columnas a linealizar: ")
            filas2 = input("Ingrese # de fila a linealizar: ")
            
            posicion = (int(columnas2)-1)*(int(filas))+(int(filas2)-1)

            print('valor de la posicion XY en la matriz: {}'.format(matriz[int(filas2)-1][int(columnas2)-1]))
            print('posicion linealizada en la lista: {}'.format(posicion))
            print('valor de la posicion linealizada de la lista: {}'.format(lista[posicion]))
            print(lista)
            GRAFICA.graphMATRIZ(int(filas),int(columnas),int(filas2),int(columnas2))

            f=open("graficoColumnaConsecutiva2.dot","w")
            f.write("digraph G {\n")
            f.write("rankdir=LR;\n")
            f.write(" node [shape=record];\n")
            f.write("struct3 [shape=record,label=\" \n")
            Struct = '{'
            for i in range (len(lista)):#filas
                if i == len(lista)-1:
                    if i == posicion:
                            Struct +="X"
                    else:
                        Struct +=str(lista[i])
                else:
                    if i == posicion:
                        Struct +="X|"
                    else:
                        Struct +=str(lista[i])+"|"
            f.write(Struct+'\n')
            f.write("}\" \n ];"+'\n')
            f.write('}')
            f.close()
            os.system("dot.exe -Tjpg graficoColumnaConsecutiva2.dot -o graficoColumnaConsecutiva2.jpg")
            os.system("graficoColumnaConsecutiva2.jpg")
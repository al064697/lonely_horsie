#código de probabilidad y estadística

#recursos
new_line = '\n'
red = '\u001B[31m'
white = '\u001B[37m'

#definiendo lista con valores de casillas
horse = [1,8] 

#definiendo el valor de las casillas
rows = 0 #filas
cols = 0 #columnas

#caso 1: forma A = (xrows = 2 + counter, ycols = 1 + counter)
print(new_line, new_line, 'case 1: Form A = (xrows = 2 + counter, ycols = 1 + counter)', new_line)

#sacando los valores de las casillas en donde podría saltar el caballo
for counter in range(1, 7):
    rows = 2 + counter
    cols = 1 + counter
    horse = [f'xrows = {rows}', f'ycols= {cols}']

    #imprimiendo el resultado
    print(red, horse, new_line, new_line)
    
#caso 2: forma B = (xrows = 1 + counter, ycols = 2 + counter)
print(white, 'case 2: Form A = (xrows = 1 + counter, ycols = 2 + counter)', new_line)

#sacando los valores de las casillas en donde podría saltar el caballo
for counter in range(1, 7):
    rows = 1 + counter
    cols = 2 + counter
    horse = [f'xrows = {rows}', f'ycols= {cols}']

    #imprimiendo el resultado
    print(red, horse, new_line)
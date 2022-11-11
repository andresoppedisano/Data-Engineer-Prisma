from opcode import opname


archivo = open("cuento.txt")

texto = archivo.read()

n=0

for i in texto:
    if i == "\n":
        n += 1

print(n)

#print(archivo.read())
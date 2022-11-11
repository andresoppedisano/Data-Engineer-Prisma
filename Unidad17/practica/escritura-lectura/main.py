# Este escribe el archivo "test.txt"
with open("test.txt","w") as f: 
    f.write("test string")

# Este lee el texto en la terminal
with open("test.txt","r") as f:
    print(f.read())

# r: abrir en modo lectura
# w: abre escribiendo,
# a: Abrir en modo de adjuntar (comience desde EOF, cree un nuevo archivo si es necesario)
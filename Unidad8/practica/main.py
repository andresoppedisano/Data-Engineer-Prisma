# Sin PEP8
def r(x):
    y, z = x.split()
    print(z, y, sep=", ")

r('Luis Ocampos')



# Con PEP8
def reverse_name(name):
    first_name, last_name = name.split()
    print(last_name, first_name, sep=", ")

reverse_name('Luis Ocampos')

# Conexión a mi base de datos PostgreSQL

import psycopg2

try:
    connection=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Pa$$w0rd',
        database='test'
    )

    print("Conexión exitosa")
    cursor=connection.cursor()
    cursor.execute("Select version()")
    row=cursor.fetchone()
    print(row)
    cursor.execute("SELECT * FROM customer")  # Acá consultamos por todos los clientes
    rows=cursor.fetchall()
    for row in rows:
        print(row)        
except Exception as ex:
    print(ex)
finally:
    connection.close() # Cerramos conexión
    print("Conexión finalizada.")








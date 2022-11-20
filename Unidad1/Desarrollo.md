1. Creamos el directorio "Unidad1" para el ejercicio.

2. Instalar módulo "venv"

3. Crear dos ambientes virtuales (Ambiente1 y Ambiente2)


4. Activar ambiente 1, instalar la última versión de pandas y matplotlib y desactivar el ambiente.

        .\Ambiente1\Scripts\activate

        pip install matplotlib pandas

        deactivate
    
5. Activar ambiente 2, instalar la versión inmediata anterior a la última versión de pandas y la de matplotlib en el ambiente 2.

        .\Ambiente2\Scripts\activate

        pip install matplotlib==3.5.2 pandas==1.4.4

         deactivate

6. El último paso es activar el Ambiente1 y ejecutar el siguiente comando para generar el requirements.txt

         pip freeze > Ambiente1/requirements.txt
     
7. Ahora ejecutamos el mísmo comando dentro del Ambiente2.

        pip freeze > Ambiente2/requirements.txt

• Creamos la base de datos 'NewDataBase' desde Compass.
Accedemos desde la consola con el siguiente comando:

    `use NewDataBase`



• Procedo a crear 2 colecciones y las listamos con el siguiente comando:
Se visualiza las colecciones creadas ('Oficio' y 'Persona').

    `Show collections`



• Insertamos un documento:
Insertamos los datos de una persona.

`db.Persona.insertOne({_id:1,Nombre:'Sergio',Apellido:'Rodríguez'})`



• Insertamos varios documentos con un solo comando:
Insertamos los datos de dos personas más.

`db.Persona.insertMany([{id:2,Nombre:'José',Apellido:'Guevara'},{id:3,Nombre:'Ronaldo',Apellido:'Martínez'}])`



• Listar los documentos existentes en una colección:

`db.Persona.find()`



• Realizar un update en un registro:
Cambiamos el nombre del primer registro 'Sergio' a 'Martín'.

`db.Persona.updateOne({_id:1}, {$set:{Nombre:'Martín'} } )`



• Listar un documento específico dentro de la colección:
Con el siguiente comando vamos a listar puntualmente el registro que fué actualizado en el paso anterior para corroborar los cambios.

`db.Persona.find({_id:{$gte:1} } )`



• Realizar un update a varios registros de forma simultánea:
Actualizamos el id de todos los registros y los reemplazamos por el número 4 con el siguiente comando

`db.Persona.updateMany({}, {$set: {id:4}})`

-Listamos todos los registros actualizados para ver reflejados los cambios
`db.Persona.find()`



-- Listar los nombres de los proveedores cuya ciudad contenga la cadena de texto “Ramos”.

SELECT Nombre
FROM Proveedor
Where Ciudad Like '%Ramos%'


/* Listar los códigos de los materiales que provea el proveedor 4 y no los provea el proveedor 5.
Se debe resolver de 3 formas.*/

Select CodMat
From Provisto_Por
Where CodProv = 4 AND CodMat NOT IN (Select CodMat from Provisto_Por Where CodProv = 5)

-- (NOT EXISTS)
SELECT CodMat
FROM Provisto_por as pp
WHERE CodProv = 4 AND NOT EXISTS (SELECT 1
FROM Provisto_por as pp2
WHERE CodProv = 5 and pp.CodMat=pp2.CodMat)

-- (EXCEPT)
Select CodMat
From Provisto_Por
Where CodProv = 4
Except
Select CodMat
From Provisto_Por
Where CodProv = 5


-- Listar los materiales, código y descripción, provistos por proveedores de la ciudad de Ramos Mejía.

Select m.*
from Material m inner join Provisto_Por pp on
m.CodMat=pp.CodMat
inner join Proveedor p on p.CodProv=pp.CodProv
where p.Ciudad ='Ramos Mejía'


/* Listar los proveedores y materiales que provee. 
La lista resultante debe incluir a aquellos proveedores que no proveen ningún material.*/



/* Listar los artículos que cuesten más de $30 o que estén compuestos por el material 2.*/

Select A.Codart
From Articulo A INNER JOIN Compuesto_Por C ON
A.CodArt = C.CodArt
Where A.Precio > 30
UNION
Select C.CodArt
From Compuesto_Por C
Where CodMat = '2'


-- Listar los artículos de Mayor precio.

Select A.CodArt, A.Descripcion, A.Precio
From Articulo as A
Where A.Precio > (Select AVG(Precio)
From Articulo)


--Listar los proveedores que proveen más de 3 materiales.

Select pp.CodProv, COUNT(*) as Cantidad
From Provisto_Por as pp
Group By pp.CodProv
Having COUNT(*)>3


/*Crear una vista para el caso de los proveedores que proveen más de 4 materiales.
Mostrar la forma de invocar esa vista.*/

Create View vista_proveedores_con_mas_de_cuatro_materiales as
Select pp.CodProv, COUNT(*) as Cantidad
From Provisto_Por as pp
Group By pp.CodProv
Having COUNT(*)>4

--Forma de invocar la lista
Select * from vista_proveedores_con_mas_de_cuatro_materiales


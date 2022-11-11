select *
from almacen as a
where a.nro > 4

--Se pide, listar los nombres de los proveedores de la ciudad de La Plata.

SELECT Nombre
FROM Proveedor
WHERE Ciudad = 'La Plata'--Se pide, Listar los proveedores cuya localidad contenga la cadena de texto “Plata”
SELECT *
FROM Proveedor
WHERE Ciudad LIKE '%Plata%'


--Se pide, listar los códigos de los materiales que provea el proveedor 3 y no los provea el proveedor 2.

Select CodMat
From Provisto_Por
Where CodProv = 3 AND CodMat NOT IN (Select CodMat
from Provisto_Por
Where CodProv = 2)


--Se pide, listar los códigos de los materiales que provea el proveedor 3 y no los provea el proveedor 2. (NOT EXISTS)

SELECT CodMat
FROM Provisto_por as pp
WHERE CodProv = 3 AND NOT EXISTS (SELECT 1
FROM Provisto_por as pp2
WHERE CodProv = 2 and pp.CodMat=pp2.CodMat)


--Se pide, listar los códigos de los materiales que provea el proveedor 3 y no los provea el proveedor 2. (EXCEPT)

Select CodMat
From Provisto_Por
Where CodProv = 3
Except
Select CodMat
From Provisto_Por
Where CodProv = 2

--Se pide, Listar los materiales, código y descripción, provistos por proveedores de la ciudad de La Plata.

select m.*
from Material m inner join Provisto_Por pp on
m.CodMat=pp.CodMat
inner join Proveedor p on p.CodProv=pp.CodProv
where p.Ciudad ='La Plata'--utilizaremos en el select el operador DISTINCT. El mismo sirve para evitar que aparezcan tuplas duplicadasselect DISTINCT m.*
from material m inner join Provisto_Por pp on
m.CodMat=pp.CodMat
inner join proveedor p on p.CodProv=pp.CodProv
where p.ciudad ='La Plata'/* Listar todos los artículos y los materiales por los que están compuestos, informando “null” en el campo “material” para el caso de los artículos que no están compuestos por ningún material.*/SELECT A.CodArt,A.Descripcion, c.codMat
FROM Articulo A LEFT JOIN Compuesto_por C ON
A.CodArt = C.CodArt/* Se pide, Listar todos los artículos y materiales por los cuales están compuestos.
Mostrar artículos sin materiales y Materiales que no componen ningún artículo.*/select a.CodArt, a.Descripcion, m.CodMat as
material_compuesto, m.Descripcion
from articulo a full outer join Compuesto_Por cp on
a.CodArt=cp.CodArt
full outer join material m on m.CodMat=cp.CodMat-- Se pide, Listar los artículos que cuesten más de $100 o que estén compuestos por el material 1.

SELECT A.CodArt
FROM Articulo A INNER JOIN Compuesto_por C ON
A.CodArt = C.CodArt
WHERE A.Precio>100
UNION
SELECT C.CodArt
FROM Compuesto_por C
WHERE C.CodMat = '1'


--Se pide, Listar los artículos que cuesten más de $100 o que estén compuestos por el material 1 (Sin eliminar duplicados).

SELECT A.CodArt
FROM Articulo A INNER JOIN Compuesto_por C ON
A.CodArt = C.CodArt
WHERE A.Precio>100
UNION ALL
SELECT C.CodArt
FROM Compuesto_por C
WHERE C.CodMat = '1'


-- Se solicita, listar los artículos cuyo precio superan la media. (AVG)

Select A.CodArt, A.Descripcion
From Articulo as A
Where A.Precio > (Select AVG(Precio)
From Articulo)


-- Se pide, Listar los códigos de los artículos compuestos por más de 2 materiales.

Select cp.Codart, COUNT(*) as cantidad
From Compuesto_Por as cp
Group By cp.CodArt
Having COUNT(*)>2

-- Para solicitar un ordenamiento en formato descendente utilizaremos: ORDER BY nombre_campo DESCselect cp.CodArt, count(*) as cantidad
from Compuesto_Por cp
GROUP BY cp.CodArt
HAVING count(*)>2
ORDER BY cp.CodArt DESC

-- Creando vista

CREATE VIEW v_articulos_con_mas_de_dos_materiales as
select cp.CodArt, count(*) as cantidad
from Compuesto_Por cp
GROUP BY cp.CodArt
HAVING count(*)>2-- Select de la vistaSELECT *
FROM v_articulos_con_mas_de_dos_materiales


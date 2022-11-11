select *
from almacen as a
where a.nro > 4

--Se pide, listar los nombres de los proveedores de la ciudad de La Plata.

SELECT Nombre
FROM Proveedor
WHERE Ciudad = 'La Plata'
SELECT *
FROM Proveedor
WHERE Ciudad LIKE '%Plata%'


--Se pide, listar los c�digos de los materiales que provea el proveedor 3 y no los provea el proveedor 2.

Select CodMat
From Provisto_Por
Where CodProv = 3 AND CodMat NOT IN (Select CodMat
from Provisto_Por
Where CodProv = 2)


--Se pide, listar los c�digos de los materiales que provea el proveedor 3 y no los provea el proveedor 2. (NOT EXISTS)

SELECT CodMat
FROM Provisto_por as pp
WHERE CodProv = 3 AND NOT EXISTS (SELECT 1
FROM Provisto_por as pp2
WHERE CodProv = 2 and pp.CodMat=pp2.CodMat)


--Se pide, listar los c�digos de los materiales que provea el proveedor 3 y no los provea el proveedor 2. (EXCEPT)

Select CodMat
From Provisto_Por
Where CodProv = 3
Except
Select CodMat
From Provisto_Por
Where CodProv = 2

--Se pide, Listar los materiales, c�digo y descripci�n, provistos por proveedores de la ciudad de La Plata.

select m.*
from Material m inner join Provisto_Por pp on
m.CodMat=pp.CodMat
inner join Proveedor p on p.CodProv=pp.CodProv
where p.Ciudad ='La Plata'
from material m inner join Provisto_Por pp on
m.CodMat=pp.CodMat
inner join proveedor p on p.CodProv=pp.CodProv
where p.ciudad ='La Plata'
FROM Articulo A LEFT JOIN Compuesto_por C ON
A.CodArt = C.CodArt
Mostrar art�culos sin materiales y Materiales que no componen ning�n art�culo.*/
material_compuesto, m.Descripcion
from articulo a full outer join Compuesto_Por cp on
a.CodArt=cp.CodArt
full outer join material m on m.CodMat=cp.CodMat

SELECT A.CodArt
FROM Articulo A INNER JOIN Compuesto_por C ON
A.CodArt = C.CodArt
WHERE A.Precio>100
UNION
SELECT C.CodArt
FROM Compuesto_por C
WHERE C.CodMat = '1'


--Se pide, Listar los art�culos que cuesten m�s de $100 o que est�n compuestos por el material 1 (Sin eliminar duplicados).

SELECT A.CodArt
FROM Articulo A INNER JOIN Compuesto_por C ON
A.CodArt = C.CodArt
WHERE A.Precio>100
UNION ALL
SELECT C.CodArt
FROM Compuesto_por C
WHERE C.CodMat = '1'


-- Se solicita, listar los art�culos cuyo precio superan la media. (AVG)

Select A.CodArt, A.Descripcion
From Articulo as A
Where A.Precio > (Select AVG(Precio)
From Articulo)


-- Se pide, Listar los c�digos de los art�culos compuestos por m�s de 2 materiales.

Select cp.Codart, COUNT(*) as cantidad
From Compuesto_Por as cp
Group By cp.CodArt
Having COUNT(*)>2


from Compuesto_Por cp
GROUP BY cp.CodArt
HAVING count(*)>2
ORDER BY cp.CodArt DESC

-- Creando vista

CREATE VIEW v_articulos_con_mas_de_dos_materiales as
select cp.CodArt, count(*) as cantidad
from Compuesto_Por cp
GROUP BY cp.CodArt
HAVING count(*)>2
FROM v_articulos_con_mas_de_dos_materiales

-- 1. Mostrar el precio máximo de los productos de la tabla PRODUCTS por línea de producto y renombrar ese campo como Precio_Maximo

Select MAX(buyPrice) as Precio_Maximo from products p 
Group By p.productLine ;


-- 5. Mostrar en una tabla el número de cada orden, la cantidad y la fecha de envío (shippedDate)

Select o.orderNumber, od.quantityordered, o.shippeddate
From orders o, orderdetails od
where o.orderNumber = od.orderNumber ;


-- 9. Obtener una lista con los nombres de clientes y la cantidad de ordenes que se emitieron para ellos.

Select c.customerName, count(o.orderNumber) as Ordenes
From customers c, orders o 
Where c.customerNumber = o.customerNumber
Group By c.customerName;


/* 13. Obtenga los codigos de producto, nombre, linea a la que pertenecen y descripción de aquellos en los cuales la descripción del producto
contenga la palabra "features"*/

Select productcode, productname,productline,productdescription
From products
Except
Select productcode, productname,productline,productdescription
From products Where productdescription Not Like '%features%';











 
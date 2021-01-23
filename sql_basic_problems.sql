-- @Author: Uthsavi KP
-- @Date: 2021-01-19 03:39:12
-- @Last Modified by: Uthsavi KP
-- @Last Modified time: 2021-01-19 04:26:32
-- @Title: Practice exercise on mysql commands.

SELECT * FROM sql_store.products;
-- 1. Return all the products- name, unit price, new price(unit price * 1.1) 
SELECT name, unit_price, unit_price*1.1  AS new_price FROM products;

-- 2. Get the orders placed this year
SELECT * FROM orders WHERE order_date > "2019-01-01";

-- 3. From the order items table, get the items
-- for order #6
-- where the total price is greater than 30
SELECT * FROM sql_store.order_items;
SELECT * FROM order_items WHERE order_id = 6 AND quantity * unit_price > 30;

-- 4. Return products with
-- quantity in stock equal to 49, 38, 72
SELECT * FROM products WHERE quantity_in_stock = 49 OR quantity_in_stock = 38 OR quantity_in_stock = 72;
-- or
SELECT * FROM PRODUCTS WHERE quantity_in_stock IN (49, 38, 72);

-- 5. Return customers born 
-- between 1/1/1990 and 1/1/2000
SELECT * FROM customers WHERE birth_date BETWEEN "1990-01-01" AND "2000-01-01";

-- 6. Get the customers whose 
-- addresses contain TRAIL or AVENUE
-- phone numbers end with 9
-- phone numbers which doesnot end with 9
SELECT * FROM customers WHERE address LIKE "%trail%" OR address LIKE "%avenue%";
SELECT * FROM customers WHERE phone LIKE "%9";
SELECT * FROM customers WHERE phone NOT LIKE "%9";
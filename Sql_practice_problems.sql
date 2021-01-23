-- @Author: Uthsavi KP
-- @Date: 2021-01-19 03:39:12
-- @Last Modified by: Uthsavi KP
-- @Last Modified time: 2021-01-23 09:57:25
-- @Title: Practice exercise on mysql commands.


USE sql_store;

SELECT * 
FROM customers
-- WHERE customer_id = 1
ORDER BY first_name;

SELECT first_name, last_name, points FROM customers;
SELECT first_name, last_name, points, points+10 FROM customers;
SELECT first_name, 
		last_name, 
        points, 
        (points+10)*100 
FROM customers;

-- using an alias to the column
-- SELECT first_name, last_name, points, points/2  AS discount_factor FROM customers;
-- to have space in the column name we have to surround it with quotes
SELECT first_name, last_name, points, points - 73  "discount_factor" FROM customers;
SELECT state FROM customers;
-- to get unique states(with Distinct keyword we can remove duplicates)
SELECT DISTINCT state FROM customers;

-- comparision operators(> , >= ,< , <= , = ,(!= or <> ))
SELECT * FROM customers WHERE points > 3000;
SELECT * FROM customers WHERE state = "VA";
SELECT * FROM customers WHERE state = "va";
SELECT * FROM customers WHERE birth_date > "1990-01-01";
-- multiple conditions with where 
SELECT * FROM customers WHERE birth_date >'1990-01-01'AND points > 1000; -- both conditions should be satisfied
SELECT * FROM customers WHERE birth_date > "1990-01-01" OR points > 1000; -- any one condition should be true
SELECT * FROM customers WHERE birth_date > "1990-01-01" OR
(points > 1000 AND state = "va");
SELECT * FROM customers WHERE NOT (birth_date > "1990-01-01" OR points > 1000);
SELECT * FROM customers WHERE birth_date <= "1990-01-01" AND points <=1000;

-- IN operator , NOT IN operator
SELECT * FROM customers WHERE state IN ('VA', 'FL', 'GA');   -- same as
SELECT * FROM customers WHERE state = "VA" OR state = "FL" OR state = "GA";
SELECT * FROM customers WHERE state NOT IN ("VA", "FL","GA");

-- Between Operator
SELECT * FROM customers WHERE points >= 1000 AND points <= 3000;
SELECT * FROM customers WHERE points BETWEEN 1000 AND 3000;

-- rows that match a specific string pattern using % sign
SELECT * FROM customers WHERE last_name like "b%"; -- fetches last name staring with b or B
SELECT * FROM customers WHERE last_name LIKE "brush%";
 -- fetches lst name having any no. of charactes befor and after b
SELECT * FROM customers WHERE last_name LIKe "%b%";
SELECT * FROM customers WHERE last_name LIKE "%y";

-- under score _ to match a single character
-- this is fetching last name, with first 5 character ending with y.
SELECT * FROM customers WHERE last_name LIKE "_____y"; 
-- getting customer with last name starting with b and ending with y
SELECT * FROM customers WHERE last_name LIKE "b____y";
-- % any no. of character , _ single charcter

-- REGEXP
SELECT * from customers WHERE last_name LIKE "%field%";
SELECT * FROM customers WHERE last_name REGEXP "field";
-- ^ indicates staring should match "field" , $ indicates end should be field
SELECT * FROM customers WHERE last_name REGEXP "^field";
SELECT * FROM customers WHERE last_name REGEXP "field$";
SELECT * FROM customers WHERE last_name REGEXP "field|mac";
SELECT * FROM customers WHERE last_name REGEXP "field|mac|rose";
SELECT * FROM customers WHERE last_name REGEXP "^field|mac|rose"; 
SELECT * FROM customers WHERE last_name REGEXP "field$|mac|rose";

-- VIEW
DROP VIEW IF EXISTS view;

CREATE VIEW view AS SELECT customers.customer_id, customers.points, orders.order_id, orders.comments 
FROM customers, orders 
WHERE customers.customer_id = orders.customer_id;
SELECT * FROM view;

CREATE VIEW view_orders AS
SELECT customers.customer_id , orders.order_date
FROM customers
INNER JOIN orders ON (customers.customer_id = orders.order_id);

SHOW CREATE VIEW `view_orders`;
SELECT * FROM view_orders;

-- INDEX
CREATE INDEX index_new ON customers(customer_id);
SHOW INDEX FROM customers;

-- TRIGGERS
DROP trigger IF EXISTS trigger_cust;
CREATE TRIGGER trigger_cust BEFORE INSERT ON customers FOR EACH ROW SET @sum = @sum + NEW.points;
SHOW TRIGGERS IN sql_store;

INSERT INTO `customers` VALUES (11,'Brad','MacCaffrey','1986-03-28','782-932-9754','0 Sage Terrace','Waltham','MA',2274);
DELETE FROM customers WHERE customer_id = 11;

-- DATE
SELECT SYSDATE();
SELECT SYSDATE() +1;
SELECT DATEDIFF("2021-01-23", "2021-01-01");
SELECT DATE_FORMAT("2021-01-23", "%Y");
-- @Author: Uthsavi KP
-- @Date: 2021-01-19 03:39:12
-- @Last Modified by: Uthsavi KP
-- @Last Modified time: 2021-01-19 04:26:32
-- @Title: Practice exercise on mysql commands.

DROP DATABASE IF EXISTS demotest;
CREATE DATABASE demotest ;
USE demotest;

-- CREATE

CREATE TABLE `Person`(
`Id` int(10) NOT NULL,
`first_name` varchar(50) NOT NULL,
`last_name` varchar(50) NOT NULL,
`age` int(10) NOT NULL,
`date` text,
PRIMARY KEY(`Id`));

INSERT INTO person VALUES (1,"John", "Smith", 32,('08:00:00'),('10:00:00'));
INSERT INTO person VALUES (2,"Bella", "Edward", 25,('08:00:00'),('10:00:00'));
INSERT INTO person VALUES (3, "Sabrina", "Spellman", 18,('08:00:00'),('10:00:00'));
INSERT INTO person VALUES (4, "Amy", "Speed", 40,('08:00:00'),('10:00:00'));
INSERT INTO person VALUES (5, "Jackson", "Wang", 27,('08:00:00'),('10:00:00'));
INSERT INTO person VALUES (6, "Selena", "Gilbert", 43,('08:00:00'),('10:00:00'));
INSERT INTO person VALUES (7, "Jake", "More", 22,('08:00:00'),('10:00:00'));
INSERT INTO person VALUES (8, "Namratha", "Agnel", 36,('08:00:00'),('10:00:00'));
INSERT INTO person VALUES (9, "Susan", "Yara", 48,('08:00:00'),('10:00:00'));
INSERT INTO person VALUES (10, "Grey", "Vas", 18,('08:00:00'),('10:00:00'));
INSERT INTO person VALUES (11, "Liam", "William", 37,('08:00:00'),('10:00:00'));
INSERT INTO person VALUES (12,"Bella", "Asher", 52,concat_ws(' - ','8:00:00','20:00:00'));

-- UPDATE

SET SQL_SAFE_UPDATES=0; -- disable
UPDATE person SET Age = 30 WHERE first_name = "Amy" AND last_name = "Speed";
SELECT * FROM person;

-- DELETE
SELECT first_name, last_name FROM person;
SELECT * FROM person WHERE first_name = "Bella" AND last_name = "Asher";
DELETE FROM person WHERE first_name = "Bella" AND last_name LIKE "Ashe_";

-- add a new column
ALTER TABLE person ADD city VARCHAR(50); 
UPDATE person SET city = "Ney York" WHERE first_name = "Jake";
UPDATE person SET city = "New Jersey" WHERE first_name = "Namratha";
UPDATE person SET city = "California" WHERE first_name = "Bella";
SELECT * FROM person
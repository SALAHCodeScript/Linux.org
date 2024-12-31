-- Create A New Table
CREATE TABLE employees (
    employee_id INT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    hourly_pay DECIMAL(5, 2) NOT NULL, --! DECIMAL(max, min)
    hire_date DATE
);

-- Display A Table
SELECT * FROM employees;

-- Display A Specific Column From A Table
SELECT first_name, last_name FROM employees;

-- Display A Table With A Statment
SELECT * FROM employees
WHERE employee_id = 1;
WHERE employee_id >= 1;
WHERE employee_id <= 1;
WHERE employee_id > 1;
WHERE employee_id < 1;
WHERE employee_id != 1;
WHERE hire_date IS NULL;
WHERE hire_date IS NOT NULL;
WHERE hire_date IS EMPTY;

-- Display A Specific Column From A Table With A Statment
SELECT first_name, last_name FROM employees
WHERE employee_id = 1;

-- Show Tables
SHOW tables;

-- Delete A Tables
DROP TABLE employees;

-- Rename A Table
RENAME TABLE employees TO workers;

-- Work With A Table
ALTER TABLE employees
/* (code) */;

-- Add Something To A Table
ALTER TABLE employees
ADD phone_number VARCHAR(15);

-- Rename Something In A Table
ALTER TABLE employees
RENAME COLUMN phone_number TO email;

-- Modify Something In A Table
ALTER TABLE employees
MODIFY COLUMN email VARCHAR(100)
MODIFY hire_date DATE NOT NULL;

-- Change Position Of Something After Another In A Table
ALTER TABLE employees
MODIFY COLUMN email VARCHAR(100);
AFTER last_name;

-- Change Position Of Something Before Another In A Table
ALTER TABLE employees
MODIFY COLUMN email VARCHAR(100);
BEFORE last_name;

-- Change Position Of Something To The First In A Table
ALTER TABLE employees
MODIFY COLUMN email VARCHAR(100);
FIRST;

-- Delete A Column In A Table
ALTER TABLE employees
DROP COLUMN email;

-- Insert A Value To A Table
INSERT INTO employees
VALUES (1, "Salah", "Ben", 50.00, "2024-11-30");

-- Insert Values To A Table
INSERT INTO employees
VALUES (1, "Salah", "Ben", 50.00, "2024-11-30"),
       (2, "Steve", "Jobs", 25.00, "2022-01-10"),
       (3, "Elon", "Mask", 20.00, "2024-05-20");

-- Insert A Specific Value To A Table
INSERT INTO employees (employee_id, first_name, last_name)
VALUES (1, "Salah", "Ben");

-- Update A Table
UPDATE employees;

-- Set A Data To Something When Update In A Table
UPDATE employees
SET hourly_pay = 10.25;

-- Set Multiple Data To Something When Update In A Table
UPDATE employees
SET hourly_pay = 10.25,
    hire_date = "2024-12-01";

-- Set A Date To Something In A Table With A Statment
UPDATE employees
SET hourly_pay = 10.25
WHERE employee_id = 3;

-- Delete Everything In A Table
DELETE FROM employees;

-- Delete Something In A Table With A Statment
DELETE FROM employees
WHERE employee_id = 3;

-- Will Not Save Point Automaticly
SET AUTOCOMMIT = OFF;

-- Save Current Point
COMMIT;

-- Undo Changes
ROLLBACK;

-- Built-in Functions: CURRENT_DATE(), CURRENT_TIME() And NOW()
CREATE TABLE the_time(
    my_date DATE,
    my_time TIME,
    my_datetime DATETIME;
);
INSERT INTO the_time
VALUES (CURRENT_DATE(), CURRENT_TIME() + 1, NOW());

-- Add A Unique Constraint When Create A Table
CREATE TABLE employees (
    employee_id INT,
    first_name VARCHAR(50),
    last_name VARCHAR(50) UNIQUE,
    hourly_pay DECIMAL(5, 2),
    hire_date DATE,
);

-- Add A Unique Constraint To A Column In A Table
ALTER TABLE employees
ADD CONSTRAINT UNIQUE(first_name);

-- Delete A Unique Constraint From A Table
ALTER TABLE employees
DROP UNIQUE first_name;

-- Add A Check Constraint When Create A Table
CREATE TABLE employees (
    employee_id INT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    hourly_pay DECIMAL(5, 2),
    hire_date DATE,
    CONSTRAINT chk_hourly_pay CHECK(hourly_pay >= 10.00);
);

-- Add A Check Constraint To A Table
ALTER TABLE employees
ADD CONSTRAINT chk_hourly_pay CHECK(hourly_pay >= 10.00);

-- Delete A Check Constraint From A Table
ALTER TABLE employees
DROP CHECK chk_hourly_pay;

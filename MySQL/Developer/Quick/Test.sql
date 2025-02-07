CREATE DATABASE mydb;

USE mydb;

CREATE TABLE employees(
    employee_id INT,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    hourly_pay DECIMAL(5, 2),
    CONSTRAINT chk_hourly_pay CHECK(hourly_pay >= 10.00)
);

INSERT INTO employees
VALUES (1, "Salah", "Ben", 12.00),
       (2, "Steve", "Jobs", 10.00),
       (3, "Elons", "Mask", 20.00);

SELECT * FROM employees;

DROP DATABASE mydb;


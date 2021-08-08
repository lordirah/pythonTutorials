use employees;

drop table if exists titles;
drop table if exists departments;
drop table if exists dept_emp;
drop table if exists dept_manager;
drop table if exists employees;
drop table if exists salaries;

CREATE TABLE titles (
  emp_no int,
  title string,
  from_date string,
  to_date string
  )
  row format delimited fields terminated by ',' lines terminated by '\n' stored as textfile;
  
  load data local inpath '/home/lordirah/Documents/data_files/titles.csv' into table titles;


CREATE TABLE departments (
    dept_no STRING,
  dept_name STRING
)
row format delimited fields terminated by ',' lines terminated by '\n' stored as textfile;

 load data local inpath '/home/lordirah/Documents/data_files/departments.csv' into table departments;

CREATE TABLE dept_emp (
    emp_no INT,
  dept_no STRING,
  from_date STRING,
  to_date STRING
)
row format delimited fields terminated by ',' lines terminated by '\n' stored as textfile;

 load data local inpath '/home/lordirah/Documents/data_files/dept_emp.csv' into table dept_emp;

CREATE TABLE dept_manager (
    emp_no int,
  dept_no STRING,
  from_date STRING,
  to_date STRING
)
row format delimited fields terminated by ',' lines terminated by '\n' stored as textfile;

 load data local inpath '/home/lordirah/Documents/data_files/dept_manager.csv' into table dept_manager;

CREATE TABLE employees (
    emp_no int ,
  birth_date string,
  first_name string,
  last_name string,
  gender string,
  hire_date string
)
row format delimited fields terminated by ',' lines terminated by '\n' stored as textfile;

 load data local inpath '/home/lordirah/Documents/data_files/employees.csv' into table employees;

CREATE TABLE salaries (
    emp_no INT,
  salary int,
  from_date string,
  to_date string
)
row format delimited fields terminated by ',' lines terminated by '\n' stored as textfile;

 load data local inpath '/home/lordirah/Documents/data_files/salaries.csv' into table salaries;
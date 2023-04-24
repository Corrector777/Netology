
 

CREATE TABLE IF NOT EXISTS Departments (
	id SERIAL PRIMARY KEY,
	name VARCHAR(40) NOT NULL
);

CREATE TABLE IF NOT EXISTS Employees (
	id SERIAL PRIMARY KEY,
	id_department INTEGER references Departments(id),
	name VARCHAR(60) NOT null,
	id_boss INTEGER REFERENCES Employees(id)
);


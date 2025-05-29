create table salesman(s_id integer primary key auto_increment,s_name varchar(20),s_city varchar(20),s_commission real);
insert into salesman (s_name,s_city,s_commission) values
('kamlesh', 'mumbai', 5),
('mahesh', 'indore', 10),
('kamlesh', 'delhi', 17);
create table customers (c_id integer primary key auto_increment,c_name varchar(20),city varchar(20),grade integer,s_id integer);
insert into customers (c_name, city, grade, s_id) values
('uday', 'rajkot', 120, 22),
('shivam', 'surat', 130, 33),
('munir', 'rajkot', 140, 44),
('nisar', 'rajkot', 150, 33);
select c.c_name AS customer_name,c.city AS customer_city,s.s_name AS salesman_name ,s.s_commission AS commission
FROM customers c JOIN salesman s ON c.s_id = s.s_id;

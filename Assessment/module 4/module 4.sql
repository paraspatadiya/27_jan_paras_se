create database assesment2;
create table products(p_id integer primary key auto_increment,p_name varchar(30),p_price integer,p_code varchar(20));
insert into products (p_name,p_price,p_code) values
('keyboard','200','10'),
('mouse','150','11'),
('ram','3000','12'),
('speaker','600','13'),
('cabinet','7000','15'),
('coolingfan','3000','16'),
('motherboard','9900','17'),
('mousepad','50','18');
select * from products;
select p_name,p_price from products where p_price >= 250 order by p_price desc,p_name asc;
select p_name,p_price from products order by p_price asc limit 1;
select p_code as product_code, avg(p_price) as average_price from products group by p_code;
select avg(p_price) as average_total_price from products;

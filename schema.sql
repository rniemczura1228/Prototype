drop table if exists posts;

create table posts (
     id integer primary key autoincrement,
     name varchar(64),
     number_parts integer,
     created_date varchar(24),
     updated_date varchar(24)
);
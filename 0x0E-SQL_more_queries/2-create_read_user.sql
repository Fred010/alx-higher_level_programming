-- creates the database hbtn_0d_2 and the user user_0d_2
-- user_0d_2 should have only SELECT privilege in the database hbtn_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- create user_0d_2 with only SELECT privilege
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
-- grant the select privilge in the database
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;

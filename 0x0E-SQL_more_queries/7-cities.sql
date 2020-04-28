-- create database
-- create table inside it
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(id INT NOT NULL AUTO_INCREMENT,
states_id INT NOT NULL, name VARCHAR(256) NOT NULL, PRIMARY KEY(ID), FOREIGN KEY(states_id) REFERENCES
hbtn_0d_usa.states(id));

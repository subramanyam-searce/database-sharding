CREATE DATABASE user_country_a_k;

USE user_country_a_k;

CREATE TYPE gender AS ENUM('M', 'F');

CREATE TABLE app_user (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR,
    date_of_birth DATE,
    gender gender,
    age INT,
    country VARCHAR
);

CREATE DATABASE user_country_l_z;

USE user_country_l_z;

CREATE TYPE gender AS ENUM('M', 'F');

CREATE TABLE app_user (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR,
    date_of_birth DATE,
    gender gender,
    age INT,
    country VARCHAR
);
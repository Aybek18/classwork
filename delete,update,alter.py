--CREATE TABLE developers(id SERIAL PRIMARY KEY, name VARCHAR, skill VARCHAR, programming_lang VARCHAR DEFAULT 'HTML');
-- ALTER TABLE DEVELOPERS RENAME COLUMN SKILL TO AGE ;

-- INSERT INTO DEVELOPERS(NAME, AGE, PROGRAMMING_LANG) VALUES( 'BAKYT',23,'PYTHON');
-- INSERT INTO DEVELOPERS(NAME, AGE, PROGRAMMING_LANG) VALUES( 'BEKA',15,'JAVA');
-- INSERT INTO DEVELOPERS(NAME, AGE, PROGRAMMING_LANG) VALUES( 'GULYA',30,'JAVASCRIPT');
-- INSERT INTO DEVELOPERS(NAME, AGE, PROGRAMMING_LANG) VALUES( 'BEKA',39,'ASSEMBLER');
-- ALTER TABLE DEVELOPERS ADD COLUMN CASH INT;
-- INSERT INTO DEVELOPERS(NAME, AGE, PROGRAMMING_LANG,CASH) VALUES( 'KATYA',16,'PYTHON', 3000);
-- update developers SET age='27' where age>'25';
-- COMMENT ON COLUMN DEVELOPERS.NAME IS 'ИМЯ ПОЛЬЗОВАТЕЛЯ';
-- update developers SET name='Ekaterina' where name='KATYA';
-- CREATE TABLE kyrgyzstan(id SERIAL PRIMARY KEY, name VARCHAR, population INT);
-- insert into kyrgyzstan(name,population) VALUES ('Chuy', 100000);
-- insert into kyrgyzstan(name,population) VALUES ('Osh', 200000);
-- insert into kyrgyzstan(name,population) VALUES ('Naryn', 300000);
-- alter table kyrgyzstan ADD COLUMN teams VARCHAR;
-- alter table kyrgyzstan RENAME COLUMN population to participants;
-- DELETE from kyrgyzstan where participants=300000;
-- UPDATE kyrgyzstan SET participants=participants-7000  WHERE participants>80000;
-- CREATE TABLE companies(id SERIAL PRIMARY KEY, Name VARCHAR, Price INT);
-- insert into companies(Name,Price) VALUES('Iphone', 100);
-- ALTER TABLE companies add COLUMN country VARCHAR;
-- insert into companies(Name,Price, country) VALUES('Samsung', 120, 'Korea');
-- insert into companies(Name,Price, country) VALUES('Nokia', 1000, 'Kyrgyzstan');
-- insert into companies(Name,Price, country) VALUES('Xiaomi', 1, 'Uzbekistan');
-- insert into companies(Name,Price, country) VALUES('Google', 0, 'USA');
-- CREATE TABLE cars(id Serial PRIMARY key, Name VARCHAR, Price INT DEFAULT 300)
-- insert into cars(Name,Price) VALUES('MB',1000);
-- ALTER TABLE cars add COLUMN country VARCHAR;
-- insert into cars(Name,Price, country) VALUES('Audi', 300, 'Germany');
-- insert into cars(Name,Price, country) VALUES('BMW', 12000, 'Germany');
-- insert into cars(Name,Price, country) VALUES('Tulpar', 10000000, 'Kyrgyzstan');
-- update cars SET country='Germany' where id=4;
-- DELETE from cars where price<1000;

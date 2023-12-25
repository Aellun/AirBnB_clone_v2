-- configures a MySQL Test server for the project.
-- If the database doesn't exist, create it
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- If the user doesn't exist, create it
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Grant privileges to the user hbnb_test on the database hbnb_test_db
GRANT ALL PRIVILEGES ON hbnb_test_db . * TO 'hbnb_test'@'localhost';
-- Grant SELECT privilege to the user hbnb_test on the database performance_schema
GRANT SELECT ON performance_schema . * TO 'hbnb_test'@'localhost';


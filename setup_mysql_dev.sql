-- configure a MySQL server for the project.
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;# check if DB exist else create
# Grant privileges to the user hbnb_dev on the database hbnb_dev_db
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
# Grant SELECT privilege to the user hbnb_dev on the database performance_schema
GRANT ALL PRIVILEGES ON hbnb_dev_db . * TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema . * TO 'hbnb_dev'@'localhost';


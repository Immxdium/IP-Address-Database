# IP Address Database Program

## Overview

This Python program connects to a MySQL database to store and manage IP addresses.
It includes basic functionality for creating a database connection, creating a table,
and inserting IP addresses into the table. Logging is implemented to track successful
operations and errors. The log file is created after you run the script.

## Features

- Connect to a My SQL database
- Create a table to store IP addresses
- Insert IP addresses into the table
- Log operations and errors

## Requirements

- Python 3 (Most recent version)
- MySQL Server (Most recent version)

## Create a Virtual Environment in bash

- python -m venv venv
- venv\Scripts\activate # For Windows
- source venv/bin/activate # For maxOS/Linux

# Running the Script in bash

- python db_operations.py

## Installation

### 1. **Set up MySQL Database**

1. **Create a Database:**

    Open MySQL Workbench or another MySQL client and run:

    CREATE DATABASE ip_addresses;

2. **Create a new user:**(Optional)

    CREATE USER 'new_user'@'localhost' IDENTIFIED BY 'NewPassword';

3. **Grant all privileges to the new user:**

    GRANT ALL PRIVILEGES ON *.* TO 'new_user'@'localhost' WITH GRANT OPTION;

4. **Check Existing Users**

    SELECT User, Host FROM mysql.user WHERE User = 'root';

5. **Modify Existing User**

    ALTER USER 'root'@'localhost' IDENTIFIED BY 'NewPassword!';

6. **Drop and Recreate User**(be careful with this, it can affect permissions)

    DROP USER 'root'@'localhost';

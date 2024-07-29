import mysql.connector
from mysql.connector import Error
import logging

# Set up logging configuration
logging.basicConfig(
    filename='db_operations.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def create_connection():
    """Create a database connection."""
    try:
        connection = mysql.connector.connect(
            host='host_name',             # MySQL host
            user='your_username',         # MySQL username        
            password='your_password',     # MySQL password
            database='ip_addresses',      # MySQL database
            port='your_port_number'       # MySQL Port Number
        )
        if connection.is_connected():
            logging.info("Connected to MySQL database")
            return  connection
    except Error as e:
        logging.error(f"Error connecting to MySQL database: {e}")
        return None
    
def create_table(connection):
    """Create a table to store IP addresses."""
    try:
        cursor = connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS ip_addresses (
            id INT AUTO_INCREMENT PRIMARY KEY,
            ip_addresses VARCHAR(45) NOT NULL                      
        )
        """)
        connection.commit()
        logging.info("Table created successfully")
    except Error as e:
        logging.error(f"Error creating table: {e}")

def insert_ip_address(connection, ip_address):
    """Insert an IP address into the table."""
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO ip_addresses (ip_address) VALUES (%s)", (ip_address,))
        connection.commit()
        logging.info(f"IP Address {ip_address} inserted successfully")
    except Error as e:
        logging.error(f"Error inserting IP Address {ip_address}: {e}")

def main():
    """Main function to execute the script."""
    connection = create_connection()
    if connection:
        try:
            create_table(connection)
            ip_address = '192.168.1.1'  # Example IP address
            insert_ip_address(connection, ip_address)
        finally:
            if connection.is_connected():
                connection.close()
                logging.info("Database connection closed")

if __name__ == "__main__":
    main()
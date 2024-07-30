import sys
sys.path.append('../..')

from util import DatabaseUtil

if __name__ == '__main__':
    # Database connection parameters
    dbname = 'eassistant'
    user = 'postgres'
    password = '1234'
    host = 'localhost'
    port = '5431'

    # SQL file path
    table_file_path = 'create-tables.sql'

    # Create DatabaseManager instance
    db_util = DatabaseUtil(dbname, user, password, host, port)

    # Create database if it doesn't exist
    db_util.create_db()

    # Execute SQL file to set up tables
    db_util.execute_sql_file(table_file_path)
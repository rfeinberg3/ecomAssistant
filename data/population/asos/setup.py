import os, sys
sys.path.append(os.path.abspath('.'))

from dbmanager import DatabaseManager

if __name__ == '__main__':
    # Database connection parameters
    host = os.environ.get('POSTGRES_HOST')
    port = os.environ.get('POSTGRES_PORT')
    dbname = os.environ.get('POSTGRES_DB')
    user = os.environ.get('POSTGRES_USER')
    password = os.environ.get('POSTGRES_PASSWORD')

    # SQL file path
    abs_path = os.path.abspath('./population/asos')
    table_file_path = abs_path + '/create-tables.sql'

    # Create DatabaseManager instance
    db_util = DatabaseManager(dbname, user, password, host, port)

    # Create database if it doesn't exist
    db_util.create_db()

    # Execute SQL file to set up tables
    db_util.execute_sql_file(table_file_path)
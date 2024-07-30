import psycopg2

class DatabaseUtil:
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port

    def create_db(self):
        conn = psycopg2.connect(dbname='postgres', user=self.user, password=self.password, host=self.host, port=self.port)
        conn.autocommit = True
        cur = conn.cursor()
        
        cur.execute(f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{self.dbname}'")
        exists = cur.fetchone()

        if exists == None:
            cur.execute(f"CREATE DATABASE {self.dbname};")
            print(f"Database '{self.dbname}' created.")
        else:
            print(f"Database '{self.dbname}' already exists.")
        
        cur.close()
        conn.close()

    def execute_sql_file(self, file_path):
        conn = psycopg2.connect(dbname=self.dbname, user=self.user, password=self.password, host=self.host, port=self.port)
        cur = conn.cursor()

        with open(file_path, 'r') as sql_file:
            sql_script = sql_file.read()
            cur.execute(sql_script)
        
        conn.commit()
        cur.close()
        conn.close()
        print(f"SQL script from {file_path} executed successfully.")
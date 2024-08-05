import pandas
import psycopg2
from psycopg2 import sql
from psycopg2.extras import RealDictCursor

class DatabaseManager:
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port

    def is_db(self) -> bool:
        try:
            with psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            ) as conn:
                return True
        except psycopg2.Error:
            return False

    def is_table(self, table_name: str) -> None:
        ''' Returns False if table is already in database.
        ### Args:
            table_name: Name of table to check if exists.
        '''
        try:
            with psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            ) as conn:
                with conn.cursor() as cur:
                    cur.execute(sql.SQL(
                        "SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = {})"
                    ).format(sql.Identifier(table_name)))
                    return cur.fetchone()[0]
        except psycopg2.Error:
            return True

    def create_db(self) -> None:
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

    def execute_sql_file(self, file_path: str) -> None:
        conn = psycopg2.connect(dbname=self.dbname, user=self.user, password=self.password, host=self.host, port=self.port)
        cur = conn.cursor()

        with open(file_path, 'r') as sql_file:
            sql_script = sql_file.read()
            cur.execute(sql_script)
        
        conn.commit()
        cur.close()
        conn.close()
        print(f"SQL script from {file_path} executed successfully.")

    def table_to_pandas(self, table_name: str) -> pandas.DataFrame:
        conn = psycopg2.connect(dbname=self.dbname, user=self.user, password=self.password, host=self.host, port=self.port)
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(f"SELECT * FROM {table_name}")
            rows = cur.fetchall()
            
            # Convert rows to a list of dictionaries, then to df
            data = [dict(row) for row in rows]
            data = pandas.DataFrame(data)
            conn.close()
        return data
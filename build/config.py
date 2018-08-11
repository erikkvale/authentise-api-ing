import psycopg2

class DbConfig:
    """
    Quick class to initialize a postgres
    connection string for psycopg2 DBAPI
    """
    def __init__(self, username, password, database,
                 host='localhost', port=5432):
        self.username = username
        self.password = password
        self.database = database
        self.host = host
        self.port = port

    @property
    def conn_str(self):
        return (
            'postgresql+psycopg2://'
            '{username}:'
            '{password}@'
            '{host}:'
            '{port}/'
            '{database}'.format(**vars(self))
        )

DB_URI = DbConfig('postgres', 'Gunnar14', 'authentise').conn_str
DB_TRACK = False




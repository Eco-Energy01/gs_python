import oracledb

def connect_db():
    try:
        dsn = "oracle.fiap.com.br:1521/orcl"
        conn = oracledb.connect(
            user='rm557334',
            password='010703',
            dsn=dsn
        )
        return conn
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

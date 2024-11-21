import oracledb
from db_connection import connect_db

def cadastrar_cliente(nome, telefone, cpf, email, senha, endereco):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        try:
            query = "INSERT INTO T_GS_CLIENTE (nome, telefone, cpf, email, senha, endereco) VALUES (:1, :2, :3, :4, :5, :6)"
            cursor.execute(query, (nome, telefone, cpf, email, senha, endereco))
            conn.commit()
            print("Cliente cadastrado com sucesso!")
        except Exception as e:
            print(f"Erro ao cadastrar cliente: {e}")
        finally:
            cursor.close()
            conn.close()

def excluir_cliente(id_cliente):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        try:
            query = "DELETE FROM T_GS_CLIENTE WHERE id_cliente = :1"
            cursor.execute(query, (id_cliente,))
            conn.commit()
            print("Cliente excluído com sucesso!")
        except Exception as e:
            print(f"Erro ao excluir cliente: {e}")
        finally:
            cursor.close()
            conn.close()

def alterar_cliente(id_cliente, nome, telefone, cpf, email, senha, endereco):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        try:
            query = """UPDATE T_GS_CLIENTE 
                       SET nome = :1, telefone = :2, cpf = :3, email = :4, senha = :5, endereco = :6
                       WHERE id_cliente = :7"""
            cursor.execute(query, (nome, telefone, cpf, email, senha, endereco, id_cliente))
            conn.commit()
            print("Cliente alterado com sucesso!")
        except Exception as e:
            print(f"Erro ao alterar cliente: {e}")
        finally:
            cursor.close()
            conn.close()

def consultar_clientes(filtro=""):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        try:
            query = f"SELECT * FROM T_GS_CLIENTE WHERE {filtro}" if filtro else "SELECT * FROM T_GS_CLIENTE"
            cursor.execute(query)
            resultados = cursor.fetchall()
            return resultados
        except Exception as e:
            print(f"Erro ao consultar clientes: {e}")
        finally:
            cursor.close()
            conn.close()

# Função de login
def login(email, senha):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        try:
            query = "SELECT id_cliente FROM T_GS_CLIENTE WHERE email = :1 AND senha = :2"
            cursor.execute(query, (email, senha))
            resultado = cursor.fetchone()
            if resultado:
                return resultado[0]
            else:
                print("Login ou senha inválidos.")
                return None
        except Exception as e:
            print(f"Erro ao tentar login: {e}")
        finally:
            cursor.close()
            conn.close()

def cadastrar_duvida(id_cliente, mensagem, assunto):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        try:
            query = "INSERT INTO T_GS_DUVIDA (id_cliente, mensagem, assunto) VALUES (:1, :2, :3)"
            cursor.execute(query, (id_cliente, mensagem, assunto))
            conn.commit()
            print("Dúvida cadastrada com sucesso!")
        except Exception as e:
            print(f"Erro ao cadastrar dúvida: {e}")
        finally:
            cursor.close()
            conn.close()

def cadastrar_investimento(area_de_interesse, empresa, setor, telefone, valor_investimento):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        try:
            query = """INSERT INTO T_GS_INVESTIMENTO (area_de_interesse, empresa, setor, telefone, valor_investimento)
                       VALUES (:1, :2, :3, :4, :5)"""
            cursor.execute(query, (area_de_interesse, empresa, setor, telefone, valor_investimento))
            conn.commit()
            print("Investimento registrado com sucesso!")
        except Exception as e:
            print(f"Erro ao registrar investimento: {e}")
        finally:
            cursor.close()
            conn.close()

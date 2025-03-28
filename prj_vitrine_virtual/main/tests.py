# from django.test import TestCase
import sqlite3

DB_PATH = "prj_vitrine_virtual/db.sqlite3"


class DB_manipulation:
    def __init__(self):
        pass

    def exibir_tabelas_db(self):
        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tabelas = cursor.fetchall()
        print("Lista de tabelas presentes no banco de dados:")
        for tabela in tabelas:
            print(f"    {tabela[0]}")
        print("\n")
        connection.close()

    def exibir_nomes_colunas(self, nome_tabela: str):
        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
        cursor.execute(f"PRAGMA table_info({nome_tabela.lower()});")
        colunas = cursor.fetchall()
        print(f"Lista de colunas presentes na tabela {nome_tabela.capitalize()}")
        for coluna in colunas:
            print(f"    {coluna[1]}")
        connection.close()

    def exibir_dados_tabela(self, nome_tabela: str):
        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM {nome_tabela.lower()};")
        dados = cursor.fetchall()
        print(f"\nDados da tabela {nome_tabela.capitalize()}:")
        for linha in dados:
            print(f"    {linha}")
        connection.close()

    def apagar_linha_tabela(self, nome_tabela: str, id: int):
        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM {nome_tabela.lower()} WHERE id = ?", (id,))
        connection.commit()
        connection.close()

    def inserir_categoria(self, name: str):
        pass

    def inserir_item(self):
        pass

    def inserir_imagem(self):
        pass


if __name__ == "__main__":
    manipulador = DB_manipulation()
    # manipulador.exibir_tabelas_db()

    # manipulador.exibir_nomes_colunas("main_category")
    # manipulador.exibir_dados_tabela("main_category")

    # manipulador.exibir_nomes_colunas("main_item")
    # manipulador.exibir_dados_tabela("main_item")

    # manipulador.exibir_nomes_colunas("main_image")
    manipulador.exibir_dados_tabela("main_image")

    # manipulador.exibir_nomes_colunas("auth_user")
    # manipulador.exibir_dados_tabela("auth_user")

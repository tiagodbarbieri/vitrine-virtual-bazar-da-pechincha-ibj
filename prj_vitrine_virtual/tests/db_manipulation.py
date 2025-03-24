# from ..prj_vitrine_virtual.vitrine_virtual.settings import BASE_DIR
import sqlite3

# DB_PATH = BASE_DIR / "db.sqlite3"
DB_PATH = "prj_vitrine_virtual/db.sqlite3"


def exibir_tabela(nome_tabela: str):
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM main_{nome_tabela.lower()};")
    dados = cursor.fetchall()
    print(f"\nDados da tabela {nome_tabela.capitalize()}:")
    for linha in dados:
        print(linha)
    connection.close()


def apagar_linha(nome_tabela: str, id: int):
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute(f"DELETE FROM main_{nome_tabela.lower()} WHERE id = ?", (id,))
    connection.commit()
    connection.close()


def inserir_categoria(new_category: str):
    pass


def inserir_item():
    pass


def inserir_imagem():
    pass


def exibir_nomes_colunas(nome_tabela):
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute(f"PRAGMA table_info(main_{nome_tabela.lower()});")
    colunas = cursor.fetchall()
    for coluna in colunas:
        print(coluna[1])


if __name__ == "__main__":
    exibir_tabela("Category")
    # exibir_tabela("Item")
    # exibir_tabela("Image")
    # inserir_categoria("vestuário")
    # apagar_linha("category", 4)
    # exibir_nomes_colunas("Category")

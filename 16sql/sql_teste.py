import sqlite3

con = sqlite3.connect("escola_v2.db")
cur = con.cursor()

cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
tabelas = cur.fetchall()

if not tabelas:
    print("Nenhuma tabela encontrada no banco 'escola_v2.db'.")
else:
    print("Tabelas encontradas no banco 'escola_v2.db':\n")
    for tabela in tabelas:
        nome_tabela = tabela[0]
        print(f"Tabela: {nome_tabela}")

        cur.execute(f"PRAGMA table_info({nome_tabela});")
        colunas = [col[1] for col in cur.fetchall()]
        print(f"   Colunas: {', '.join(colunas)}")

        cur.execute(f"SELECT * FROM {nome_tabela}")
        registros = cur.fetchall()
        if registros:
            print("   Registros:")
            for linha in registros:
                print("    ", linha)
        else:
            print("   (sem registros)\n")

con.close()


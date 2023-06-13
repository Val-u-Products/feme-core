import psycopg2

# Configuración de la conexión a la base de datos
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="48349632"
)

# Ejecución de la consulta de borrado
cur = conn.cursor()
cur.execute("""
    SELECT table_name
    FROM information_schema.tables
    WHERE table_schema = 'public'
""")
tables = cur.fetchall()
for table in tables:
    cur.execute(f"DROP TABLE IF EXISTS {table[0]} CASCADE")
conn.commit()

# Cierre de la conexión a la base de datos
cur.close()
conn.close()
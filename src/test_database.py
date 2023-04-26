import psycopg2
import time

# Configurar la conexión a la base de datos
conn = psycopg2.connect(
    host="val-u-data.chno4t1xw66s.sa-east-1.rds.amazonaws.com",
    database="postgres",
    user="postgres",
    password="X31AveWXXKoAxOGBOAgH"
)

# Consulta de ejemplo
query = "SELECT * FROM estudiantes_tabla"

# Realizar 10,000 consultas en un bucle
for i in range(1000):
    start_time = time.time()  # registrar el tiempo de inicio de la consulta
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    end_time = time.time()  # registrar el tiempo de finalización de la consulta
    print(f"Consulta {i+1} - Filas: {len(rows)} - Tiempo de ejecución: {end_time-start_time:.2f} segundos")
    cursor.close()

# Cerrar la conexión a la base de datos
conn.close()
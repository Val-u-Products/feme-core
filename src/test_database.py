import psycopg2
import time

# Configurar la conexión a la base de datos
conn = psycopg2.connect(
    host="34.95.240.188",
    database="postgres",
    user="postgres",
    password="Val-udevops12345#"
)

# Consulta de ejemplo
query = "SELECT * FROM estudiantes_tabla"

# Realizar 10,000 consultas en un bucle
for i in range(5000):
    start_time = time.time()  # registrar el tiempo de inicio de la consulta
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    end_time = time.time()  # registrar el tiempo de finalización de la consulta
    print(f"Consulta {i+1} - Filas: {len(rows)} - Tiempo de ejecución: {end_time-start_time:.2f} segundos")
    cursor.close()

# Cerrar la conexión a la base de datos
conn.close()
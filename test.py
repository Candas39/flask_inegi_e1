import sqlite3

def create_database(name_base):
    conn = sqlite3.connect(name_base)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS establecimientos (
            CLEE TEXT PRIMARY KEY,
            tipo_establecimiento TEXT,
            latitud REAL ,
            longitud REAL ,
            nombre TEXT
        )
    ''')

#create_database("inegi_test.db")
conn = sqlite3.connect('inegi_test.db')

# Crear un cursor
cursor = conn.cursor()

# Ejecutar una consulta SQL con filtro
cursor.execute('SELECT * FROM establecimientos')

# Obtener todos los resultados de la consulta
resultados = cursor.fetchall()
print(resultados)
# Cerrar la conexión
conn.close()

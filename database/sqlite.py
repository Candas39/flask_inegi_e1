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


def insert_data(data, name_base, tipo_establecimiento):
    conn = sqlite3.connect(name_base)
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT CLEE FROM establecimientos')
        array_clee = cursor.fetchall()
        array_clee = [elemento for tupla in array_clee for elemento in tupla]
        for establecimiento in data:
            if establecimiento['CLEE'] in array_clee:
                pass
            else:
                cursor.execute('''
                INSERT INTO establecimientos (CLEE, tipo_establecimiento, latitud, longitud, nombre)
                VALUES (?, ?, ?, ?, ?)
                ''', (establecimiento['CLEE'], tipo_establecimiento,
                  float(establecimiento['Latitud']), float(establecimiento['Longitud']), establecimiento['Nombre']))
        
        conn.commit()
        conn.close()
        return 200
    except ValueError:
        conn.commit()
        conn.close()
        return ValueError
    

def filter_data(palabra_clave):
    conn = sqlite3.connect('inegi_test.db')
    cursor = conn.cursor()
    query = "SELECT * FROM establecimientos WHERE nombre LIKE ?"
    cursor.execute(query, ('%' + palabra_clave + '%',))
    resultados = cursor.fetchall()
    print(resultados)
    conn.close()
    columnas = [desc[0] for desc in cursor.description]
    data = [dict(zip(columnas, fila)) for fila in resultados]
    return data
from flask import Flask, jsonify, request
import pyodbc
import pymysql

app = Flask(__name__)

# Configuración de la conexión a SQL Server
server = 'us-east.connect.psdb.cloud'
databases = 'poligonostlc'

username = '0cv28h5f1h1csdel4y6p'
clave = 'pscale_pw_17erBbPBTK1q3dPc7ZhnmgFE52sgZ2s02qUBrGeAMxG'

conn=pymysql.connect(user=username, password=clave,host=server,  database=databases,port=3306,ssl={'ssl': {'ca': 'path/to/cert.pem'}})
"""cursor=conn.cursor()"""

'''sql_query = "select * from poligonos where nodo='PI05A' ;"
cursor.execute(sql_query)
datos=cursor.fetchall()

print(datos[0][1])'''


@app.route('/ping')
def ping():
    return 'Pong!'

# Endpoint para obtener la zona dado el nodo
@app.route('/poligonos/<string:nodo>/zona', methods=['GET'])
def get_user_age(nodo):
    nod='PI05A'
    cursor = conn.cursor()
    sql_query = f'select * from poligonos where nodo="{nodo}";'
    '''f'select * from poligonos WHERE nodo={nod};'''
    cursor.execute(sql_query)
    zona = cursor.fetchall()
    cursor.close()
    if zona:
        return jsonify({'zona': zona[0][1]})
    else:
        return jsonify({'error': 'Usuario no encontrado'})



if __name__ == '__main__':
    app.run()



from flask import Flask, jsonify, request
import pyodbc
import pymysql
from credenciales from server

app = Flask(__name__)

# Configuración de la conexión a SQL Server
conn=pymysql.connect(user=username, password=clave,host=server,  database=databases,port=3306,ssl={'ssl': {'ca': 'path/to/cert.pem'}})

@app.route('/ping')
def ping():
    return jsonify({'message': 'Pong!'})

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



from flask import Flask, jsonify, request
import pyodbc
import pymysql
from credenciales import server,clave,username,databases

from flask_cors import CORS

app = Flask(__name__)
CORS(app) # habilita CORS para la aplicación Flask


# Configuración de la conexión a SQL Server
conn=pymysql.connect(user=username, password=clave,host=server,  database=databases,port=3306,ssl={'ssl': {'ca': 'path/to/cert.pem'}})


@app.route('/ping')
def ping():
    return jsonify({'message': 'Pong!'})

# Endpoint para obtener la zona dado el nodo
@app.route('/poligonos/<string:nodo>/zona', methods=['GET'])
def get_user_age(nodo):
   
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


# Endpoint para obtener NODO , PARTIDO , JEFATURA del cliente
@app.route('/cl', methods=['POST'])
def get_nodo_partido():
      
    cliente=request.get_json()['idcliente'] #si el id se de consulta entra por json, si el id de consuta entra por form-data usar request.form['id_cliente']

    cursor = conn.cursor()
    sql_query = f'select * from clientes where idcliente="{cliente}";'
    cursor.execute(sql_query)
    datos = cursor.fetchall()
    cursor.close()
    print(datos)
    if datos:
        return jsonify({'Partido': datos[0][1], 
                         'Nodo':datos[0][3],
                         'Jefatura':datos[0][4],
        })
    else:
        return jsonify({'error': 'Usuario no encontrado'})




if __name__ == '__main__':
    app.run()



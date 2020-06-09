import mysql.connector
from mysql.connector import Error
import json

def exec_query(quer, database, host, user, password):
    maindata = {"data": [], "error": ""}
    connection = None
    try:
        connection = mysql.connector.connect(host=host,database=database,user=user,password=password, use_pure = False)

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(quer)
            ques = quer.lower().split()
            if ques[0] in {'desc', 'show', 'select'}:
                #cursor.execute("DESC Laptop")
                row = cursor.fetchone()
                num_fields = len(cursor.description)
                field_names = [i[0] for i in cursor.description]
                # col_list=[]
                # print(field_names)
                val = []
                while row is not None:
                    da = {}
                    
                    for k in range(len(row)):
                        da[field_names[k]] = str(row[k])
                    maindata['data'].append(da)
                    row = cursor.fetchone()        
            maindata['status'] = 'ok'
            # print(re)

    # except Error:
    #     print("Error while connecting to mysql",Error)
    #     maindata['result'] = 'failure'
    except Error as e:
        maindata['error'] = str(e)
        maindata['status'] = "error"
        print(e)
        
    finally:
       if connection:
           if connection.is_connected():
                cursor.close()
                connection.close()
    return maindata

def checkConnection(database, host, user, password):
    connection = None
    try:
        connection = mysql.connector.connect(host=host,database=database,user=user,password=password, use_pure = False)
        return True
    except:
        return False
    finally:
        if connection:
            if connection.is_connected():
                connection.close()
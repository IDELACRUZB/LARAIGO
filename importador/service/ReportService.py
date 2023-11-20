import pandas as pd
import pymysql
import json
from datetime import datetime
import os
import re

class ReportService:
    def loadData(self,filePath, tableName : str, dbName : str, tipo, fecha_insert, properties : {}, renameColumns : {}, converters : []):
        filePath = filePath

        # Nombre de la tabla
        dbTable = tableName

        percentage = {}
        for convert in converters:
            percentage[convert] = self.convertToPercentage
        
        # Lee el archivo EXCEL con pandas
        #df = pd.read_excel( filePath,  sheet_name=0, engine='openpyxl', skiprows=0, dtype=properties, converters=percentage)
        if tipo == 'csv':
            df = pd.read_csv(filePath, sep='|', dtype=str, header=0, encoding='ISO-8859-1')
        elif tipo == 'excel':
            df = pd.read_excel(filePath, dtype=str, header=0)

        if fecha_insert:
            df.insert(0, 'fecha', fecha_insert)

        #df =df.loc[df.iloc[:, 0] != "~Total"]

        # Renombrar la columna        
        df.columns = df.columns.str.strip()
        df.rename(columns=renameColumns, inplace=True)

        # Formatear las columnas
        df = df.fillna(value='')
        df.columns = df.columns.str.lower()
        df.columns = df.columns.str.replace(r'^\d+\.-\s*', '', regex=True)
        df.columns = df.columns.str.replace('\n', '')
        df.columns = df.columns.str.strip()
        df.columns = df.columns.str.replace(' ', '_')
        df.columns = df.columns.str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
        df.columns = df.columns.str.lstrip('_')

        def limpiar_encabezados(encabezado):
            return re.sub(r'\W+', '_', encabezado)
        #Limpia  2 o mas"_" seguidos, "_" del final del texto y limita a 35 caracteres
        def underscores(text):
            text = re.sub(r"\_+", "_", text)
            text = text.rstrip("_")
            text = text[:35]
            return text
        df.columns = df.columns.map(limpiar_encabezados)
        df.columns = df.columns.map(underscores)

        """
        print(df.columns)
        for i in df.columns:
            print(i)
        exit() #"""
        # Configurar la conexión a la base de datos
        properties = self.getProperties()
        conn = pymysql.connect(
            host=properties['DB_HOST'],
            database= dbName,
            user=properties['DB_USER'],
            password=properties['DB_PASSWORD'],
            port=3306
        )

        try:
            # Crear un cursor y comenzar una transacción
            cur = conn.cursor()
            cur.execute("START TRANSACTION;")
            #cur.execute(f"TRUNCATE TABLE {dbTable};")
            
            sqlHeading = "`"+"`,`".join(df.columns)+"`"
            
            chunks = [df[i:i + 200] for i in range(0, df.shape[0], 200)]

            
            for chunk in chunks:
                values = [tuple(row) for _, row in chunk.iterrows()]
                try:
                    # Ejecutar el comando INSERT INTO para cada grupo de 50 filas
                    consulta = f"""INSERT INTO {dbTable} ({sqlHeading}) VALUES ({', '.join(['%s'] * len(df.columns))});"""
                    cur.executemany(consulta, values)
                    conn.commit()
                    #print(f"Se insertaron con éxito {len(chunk)} filas")
                except Exception as e:
                    print("Ocurrió un error:", e)


                            
            print('Se ejecuto correctamente la consulta: ' + dbName + " / " + tableName)

        except Exception as e:
            # Revertir la transacción si hay un error            
            conn.rollback()    
            print("Hubo un error al importar la informacion: " + str(e) )
            return 400 
            
        finally:
            # Cerrar la conexión a la base de datos
            cur.close()
            conn.close()

        return 200
    
    def getProperties(self):
        config_data = None
        with open('./importador/config.json') as config_file:
            config_data = json.load(config_file)

        return config_data
    
    def convertToPercentage(self,x):
        return "{:.2f}%".format(x * 100)

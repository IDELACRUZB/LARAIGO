from web_scraper import descargaReportes
from isdb import TablaValidacion2
import time
import datetime
import subprocess

# Paso 1: Descarga de Reportes
#Rango de fechas para descarga de Reportes
D0 =  datetime.date.today()
D_1 =  D0 + datetime.timedelta(days=-1)
inicio = str(D_1) #'2023-08-04'
fin = str(D_1) #None#'2023-08-08'

fecD0 = False
username = "E8232037"
password = "claro2020"

tablaValidacion = TablaValidacion2()
tablaValidacion.crearBD()
tablaValidacion.crearTabla()
tablaValidacion.truncateTable()

descarga = descargaReportes()
def logueo():
    descarga.login()
    descarga.iniciarSesion(username, password)
    inicioSesion = descarga.validaInicioSesion()

    while not inicioSesion:
        descarga.reiniciar()
        descarga.login()
        descarga.iniciarSesion(username, password)
        inicioSesion = descarga.validaInicioSesion()
    else:
        print('Inicio de Sesion Exitosa')
        pass
        
logueo()

fecD0 = False
contador_descargas = 1

campana = "renovacion_especial"

# ===== I. Reporte Clasificaciones =====
def re_clasificaciones():
    nombreAsignado = 'renovacion_especial_clasificaciones_'
    try:
        descarga.limpia_carpeta_descargas()
        descarga.reporte_clasificaciones(inicio, fin)
        descarga.descomprime_zip()
        descarga.remove_zip()
        nombre = descarga.nombreReporte(nombreAsignado, inicio, fin, fecD0)
        destino = descarga.directoryPath + r'/carga\renovacion_especial\clasificaciones'
        descarga.renombrarReubicar(nombre, 'csv', destino)

        datos=[(contador_descargas, campana, nombreAsignado, 1)]
        tablaValidacion.agregarVariosDatos(datos)
    except Exception as e:
        datos=[(contador_descargas, campana, nombreAsignado, 0)]
        tablaValidacion.agregarVariosDatos(datos)
        pass

re_clasificaciones()
ultimoRegistro = tablaValidacion.leerDatos()
descargo = ultimoRegistro[0][3]

while descargo == 0:
    tablaValidacion.deleteTable(contador_descargas)

    descarga.reiniciar()
    logueo()

    re_clasificaciones()
    ultimoRegistro = tablaValidacion.leerDatos()
    descargo = ultimoRegistro[0][3]
else:
    contador_descargas += 1
    print(f"Descargo reporte clasificaiones")
    pass

# ===== II. Reporte Productividad Asesores =====
def re_productividad_asesores():
    nombreAsignado = 'renovacion_especial_productividad_asesores_'
    try:
        descarga.limpia_carpeta_descargas()
        descarga.reporte_productividad_asesores(inicio, fin)
        nombre = descarga.nombreReporte(nombreAsignado, inicio, fin, fecD0)
        destino = descarga.directoryPath + r'/carga\renovacion_especial\productividad_asesores'
        descarga.renombrarReubicar(nombre,'xlsx', destino)

        datos=[(contador_descargas, campana, nombreAsignado, 1)]
        tablaValidacion.agregarVariosDatos(datos)
    except Exception as e:
        datos=[(contador_descargas, campana, nombreAsignado, 0)]
        tablaValidacion.agregarVariosDatos(datos)
        pass

re_productividad_asesores()
ultimoRegistro = tablaValidacion.leerDatos()
descargo = ultimoRegistro[0][3]

while descargo == 0:
    tablaValidacion.deleteTable(contador_descargas)

    descarga.reiniciar()
    logueo()

    re_productividad_asesores()
    ultimoRegistro = tablaValidacion.leerDatos()
    descargo = ultimoRegistro[0][3]
else:
    contador_descargas += 1
    print(f"Descargo reporte Productividad Asesores")
    pass

# ===== III. Reporte Clasificaciones =====
def re_tickets():
    nombreAsignado = 'renovacion_especial_tickets_'
    try:
        descarga.limpia_carpeta_descargas()
        descarga.reporte_tickets(inicio, fin)
        descarga.descomprime_zip()
        descarga.remove_zip()
        nombre = descarga.nombreReporte(nombreAsignado, inicio, fin, fecD0)
        destino = descarga.directoryPath + r'/carga\renovacion_especial\tickets'
        descarga.renombrarReubicar(nombre, 'csv', destino)

        datos=[(contador_descargas, campana, nombreAsignado, 1)]
        tablaValidacion.agregarVariosDatos(datos)
    except Exception as e:
        datos=[(contador_descargas, campana, nombreAsignado, 0)]
        tablaValidacion.agregarVariosDatos(datos)
        pass

re_tickets()
ultimoRegistro = tablaValidacion.leerDatos()
descargo = ultimoRegistro[0][3]

while descargo == 0:
    tablaValidacion.deleteTable(contador_descargas)

    descarga.reiniciar()
    logueo()

    re_tickets()
    ultimoRegistro = tablaValidacion.leerDatos()
    descargo = ultimoRegistro[0][3]
else:
    contador_descargas += 1
    print(f"Descargo reporte Tickets")
    pass

# ===== Fin descarga reportes Renovacion Especial ======
print(f"Se descargaron los reportes del día {inicio} al {fin} de la campaña {campana}")
descarga.cerrarSesion()
descarga.gameOver()

# ===== * ===== ===== * ===== ===== * ===== ===== * ===== ===== * =====
#                               Parte 2
# ===== * ===== ===== * ===== ===== * ===== ===== * ===== ===== * =====

username = "E8232991"
password = "LARAIGO2023"

descarga.reiniciar()
logueo()

fecD0 = False
contador_descargas = 1

campana = "retenciones"

# ===== I. Reporte Clasificaciones =====
def re_clasificaciones():
    nombreAsignado = 'retenciones_clasificaciones_'
    try:
        descarga.limpia_carpeta_descargas()
        descarga.reporte_clasificaciones(inicio, fin)
        descarga.descomprime_zip()
        descarga.remove_zip()
        nombre = descarga.nombreReporte(nombreAsignado, inicio, fin, fecD0)
        destino = descarga.directoryPath + r'/carga\retenciones\clasificaciones'
        descarga.renombrarReubicar(nombre, 'csv', destino)

        datos=[(contador_descargas, campana, nombreAsignado, 1)]
        tablaValidacion.agregarVariosDatos(datos)
    except Exception as e:
        datos=[(contador_descargas, campana, nombreAsignado, 0)]
        tablaValidacion.agregarVariosDatos(datos)
        pass

re_clasificaciones()
ultimoRegistro = tablaValidacion.leerDatos()
descargo = ultimoRegistro[0][3]

while descargo == 0:
    tablaValidacion.deleteTable(contador_descargas)

    descarga.reiniciar()
    logueo()

    re_clasificaciones()
    ultimoRegistro = tablaValidacion.leerDatos()
    descargo = ultimoRegistro[0][3]
else:
    contador_descargas += 1
    print(f"Descargo reporte clasificaiones")
    pass

# ===== II. Reporte Productividad Asesores =====
def re_productividad_asesores():
    nombreAsignado = 'retenciones_productividad_asesores_'
    try:
        descarga.limpia_carpeta_descargas()
        descarga.reporte_productividad_asesores(inicio, fin)
        nombre = descarga.nombreReporte(nombreAsignado, inicio, fin, fecD0)
        destino = descarga.directoryPath + r'/carga\retenciones\productividad_asesores'
        descarga.renombrarReubicar(nombre,'xlsx', destino)

        datos=[(contador_descargas, campana, nombreAsignado, 1)]
        tablaValidacion.agregarVariosDatos(datos)
    except Exception as e:
        datos=[(contador_descargas, campana, nombreAsignado, 0)]
        tablaValidacion.agregarVariosDatos(datos)
        pass

re_productividad_asesores()
ultimoRegistro = tablaValidacion.leerDatos()
descargo = ultimoRegistro[0][3]

while descargo == 0:
    tablaValidacion.deleteTable(contador_descargas)

    descarga.reiniciar()
    logueo()

    re_productividad_asesores()
    ultimoRegistro = tablaValidacion.leerDatos()
    descargo = ultimoRegistro[0][3]
else:
    contador_descargas += 1
    print(f"Descargo reporte Productividad Asesores")
    pass

# ===== III. Reporte Clasificaciones =====
def re_tickets():
    nombreAsignado = 'retenciones_tickets_'
    try:
        descarga.limpia_carpeta_descargas()
        descarga.reporte_tickets(inicio, fin)
        descarga.descomprime_zip()
        descarga.remove_zip()
        nombre = descarga.nombreReporte(nombreAsignado, inicio, fin, fecD0)
        destino = descarga.directoryPath + r'/carga\retenciones\tickets'
        descarga.renombrarReubicar(nombre, 'csv', destino)

        datos=[(contador_descargas, campana, nombreAsignado, 1)]
        tablaValidacion.agregarVariosDatos(datos)
    except Exception as e:
        datos=[(contador_descargas, campana, nombreAsignado, 0)]
        tablaValidacion.agregarVariosDatos(datos)
        pass

re_tickets()
ultimoRegistro = tablaValidacion.leerDatos()
descargo = ultimoRegistro[0][3]

while descargo == 0:
    tablaValidacion.deleteTable(contador_descargas)

    descarga.reiniciar()
    logueo()

    re_tickets()
    ultimoRegistro = tablaValidacion.leerDatos()
    descargo = ultimoRegistro[0][3]
else:
    contador_descargas += 1
    print(f"Descargo reporte Tickets")
    pass

# ===== Fin descarga reportes ======

print(f"Se descargaron los reportes del día {inicio} al {fin} de la campaña {campana}")
descarga.cerrarSesion()
descarga.gameOver()

# Paso 2: Carga la base de datos al servidor
#subprocess.call(['python', './importador/controller.py'])
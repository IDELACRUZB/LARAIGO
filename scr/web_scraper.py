import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, UnexpectedAlertPresentException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.service import Service
from PIL import Image
from io import BytesIO
import pyautogui
import os
import glob
import zipfile
import shutil
import datetime
import random
import subprocess
import string

class descargaReportes():
    def __init__(self):
        self.directoryPath = os.getcwd()
        self.defaultPathDownloads = self.directoryPath + r'\temp'
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("prefs", {
            "download.default_directory": self.defaultPathDownloads,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        })

        self.options.add_argument("--ignore-certificate-errors")
        self.url = "https://claro.laraigo.com/sign-in"
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.maximize_window()

    def reiniciar(self):
        self.__init__()

    def login(self):
        self.driver.get(self.url)
        time.sleep(1)
    
    def iniciarSesion(self, username, password):
        wait = WebDriverWait(self.driver, 60)
        inputUser = wait.until(EC.presence_of_element_located((By.NAME, "usr")))
        inputUser.send_keys(username)
        time.sleep(2)

        inputPassword = self.driver.find_element(By.NAME, "password")
        inputPassword.send_keys(password)
        time.sleep(2)

        btnLogIn = self.driver.find_element(By.XPATH, '//button/span[@class="MuiButton-label"]')
        btnLogIn.click()
        time.sleep(5)

    def validaInicioSesion(self):
        wait = WebDriverWait(self.driver, 60)
        ajustes = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[class="App"]')))
        if ajustes:
            return True
        else:
            return False

    def cerrarSesion(self):
        logoImagen = self.driver.find_element(By.XPATH, '//span/span/span[@class="MuiBadge-root"]')
        logoImagen.click()
        time.sleep(1)

        cerrarSesion = self.driver.find_element(By.XPATH, '//span[@class="MuiButton-label" and text()="Cerrar Sesión"]')
        cerrarSesion.click()
        time.sleep(1)

    def cantidad_zip(self):
        ruta_carpeta = self.defaultPathDownloads
        extension = '*.zip'
        patron_busqueda = os.path.join(ruta_carpeta, extension)
        archivos = glob.glob(patron_busqueda)
        cantidad_archivos = len(archivos)
        return cantidad_archivos
    
    def cantidad_excel(self):
        ruta_carpeta = self.defaultPathDownloads
        extension = '*.xlsx'
        patron_busqueda = os.path.join(ruta_carpeta, extension)
        archivos = glob.glob(patron_busqueda)
        cantidad_archivos = len(archivos)
        return cantidad_archivos
    
    # ====== 1. Reporte Clasificaciones ======
    def reporte_clasificaciones(self, fecha_inicio, fecha_fin):
        self.url_reportes = "https://claro.laraigo.com/reports"
        self.driver.get(self.url_reportes)
        time.sleep(5)
        

        clasificaciones = self.driver.find_element(By.XPATH, '//img[@title="Clasificaciones"]')
        clasificaciones.click()
        time.sleep(1)

        calendario = self.driver.find_element(By.XPATH, '//div[contains(@class,"jss")]/div/button/span[@class="MuiButton-label"]')
        calendario.click()
        time.sleep(1)

        fecha_inicio = datetime.datetime.strptime(fecha_inicio, '%Y-%m-%d')
        periodo_inicio = int(datetime.datetime.strftime(fecha_inicio, '%Y%m'))
        fecha_fin = datetime.datetime.strptime(fecha_fin, '%Y-%m-%d')
        periodo_fin = int(datetime.datetime.strftime(fecha_fin, '%Y%m'))

        # Selecciona fecha Inicio
        anio_inicio = fecha_inicio.year
        mes_inicio = fecha_inicio.month - 1
        dia_inicio = fecha_inicio.day

        anio_lista = self.driver.find_element(By.CSS_SELECTOR, '[class="rdrYearPicker"]')
        anio_lista.click()
        time.sleep(1)
        selecciona_anio = self.driver.find_element(By.CSS_SELECTOR, f'[value="{anio_inicio}"]')
        selecciona_anio.click()
        time.sleep(1)

        mes_lista = self.driver.find_element(By.CSS_SELECTOR, '[class="rdrMonthPicker"]')
        mes_lista.click()
        time.sleep(1)
        selecciona_anio = self.driver.find_element(By.CSS_SELECTOR, f'[value="{mes_inicio}"]')
        selecciona_anio.click()
        time.sleep(1)

        dia_inicio = self.driver.find_element(By.XPATH, f'//div[@class="rdrDays"]/button/span[@class="rdrDayNumber"]/span[text()="{dia_inicio}"]')
        dia_inicio.click()
        time.sleep(1)

        #Selecciona fecha fin
        anio_fin = fecha_fin.year
        mes_fin = fecha_fin.month - 1
        dia_fin = fecha_fin.day

        if periodo_inicio == periodo_fin:
            dia_fin = self.driver.find_element(By.XPATH, f'//div[@class="rdrDays"]/button/span[@class="rdrDayNumber"]/span[text()="{dia_fin}"]')
            dia_fin.click()
            time.sleep(1)
        else:
            anio_lista = self.driver.find_element(By.CSS_SELECTOR, '[class="rdrYearPicker"]')
            anio_lista.click()
            time.sleep(1)
            selecciona_anio = self.driver.find_element(By.CSS_SELECTOR, f'[value="{anio_fin}"]')
            selecciona_anio.click()
            time.sleep(1)

            mes_lista = self.driver.find_element(By.CSS_SELECTOR, '[class="rdrMonthPicker"]')
            mes_lista.click()
            time.sleep(1)
            selecciona_anio = self.driver.find_element(By.CSS_SELECTOR, f'[value="{mes_fin}"]')
            selecciona_anio.click()
            time.sleep(1)

            dia_inicio = self.driver.find_element(By.XPATH, f'//div[@class="rdrDays"]/button/span[@class="rdrDayNumber"]/span[text()="{dia_fin}"]')
            dia_inicio.click()
            time.sleep(1)

        aplicar = self.driver.find_element(By.XPATH, '//span[@class="MuiButton-label" and text()="Aplicar"]')
        aplicar.click()
        time.sleep(1)

        btn_buscar = self.driver.find_element(By.XPATH, '//span[text()="Buscar"]')
        btn_buscar.click()
        time.sleep(1)

        WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[class="MuiTableBody-root"]')))
        time.sleep(1)

        cantidad_zip_inicial = self.cantidad_zip()

        btn_descargar = self.driver.find_element(By.XPATH, '//span[@class="MuiButton-label" and text()="Descargar"]')
        btn_descargar.click()

        #Valida que la descarga concluya
        cantidad_zip_final = cantidad_zip_inicial
        while cantidad_zip_final == cantidad_zip_inicial:
            time.sleep(1)
            cantidad_zip_final = self.cantidad_zip()
        else:
            pass

        time.sleep(1)

    # ====== 2. Reporte Productividad Asesores ======
    def reporte_productividad_asesores(self, fecha_inicio, fecha_fin):
        self.url_reportes = "https://claro.laraigo.com/reports"
        self.driver.get(self.url_reportes)
        time.sleep(5)

        productividad_asesores = self.driver.find_element(By.XPATH, '//img[@title="Productividad de asesores"]')
        productividad_asesores.click()
        time.sleep(1)

        calendario = self.driver.find_element(By.XPATH, '//div[contains(@class,"jss")]/div/button/span[@class="MuiButton-label"]')
        calendario.click()
        time.sleep(1)

        fecha_inicio = datetime.datetime.strptime(fecha_inicio, '%Y-%m-%d')
        periodo_inicio = int(datetime.datetime.strftime(fecha_inicio, '%Y%m'))
        fecha_fin = datetime.datetime.strptime(fecha_fin, '%Y-%m-%d')
        periodo_fin = int(datetime.datetime.strftime(fecha_fin, '%Y%m'))

        # Selecciona fecha Inicio
        anio_inicio = fecha_inicio.year
        mes_inicio = fecha_inicio.month - 1
        dia_inicio = fecha_inicio.day

        anio_lista = self.driver.find_element(By.CSS_SELECTOR, '[class="rdrYearPicker"]')
        anio_lista.click()
        time.sleep(1)
        selecciona_anio = self.driver.find_element(By.CSS_SELECTOR, f'[value="{anio_inicio}"]')
        selecciona_anio.click()
        time.sleep(1)

        mes_lista = self.driver.find_element(By.CSS_SELECTOR, '[class="rdrMonthPicker"]')
        mes_lista.click()
        time.sleep(1)
        selecciona_anio = self.driver.find_element(By.CSS_SELECTOR, f'[value="{mes_inicio}"]')
        selecciona_anio.click()
        time.sleep(1)

        dia_inicio = self.driver.find_element(By.XPATH, f'//div[@class="rdrDays"]/button/span[@class="rdrDayNumber"]/span[text()="{dia_inicio}"]')
        dia_inicio.click()
        time.sleep(1)

        #Selecciona fecha fin
        anio_fin = fecha_fin.year
        mes_fin = fecha_fin.month - 1
        dia_fin = fecha_fin.day

        if periodo_inicio == periodo_fin:
            dia_fin = self.driver.find_element(By.XPATH, f'//div[@class="rdrDays"]/button/span[@class="rdrDayNumber"]/span[text()="{dia_fin}"]')
            dia_fin.click()
            time.sleep(1)
        else:
            anio_lista = self.driver.find_element(By.CSS_SELECTOR, '[class="rdrYearPicker"]')
            anio_lista.click()
            time.sleep(1)
            selecciona_anio = self.driver.find_element(By.CSS_SELECTOR, f'[value="{anio_fin}"]')
            selecciona_anio.click()
            time.sleep(1)

            mes_lista = self.driver.find_element(By.CSS_SELECTOR, '[class="rdrMonthPicker"]')
            mes_lista.click()
            time.sleep(1)
            selecciona_anio = self.driver.find_element(By.CSS_SELECTOR, f'[value="{mes_fin}"]')
            selecciona_anio.click()
            time.sleep(1)

            dia_inicio = self.driver.find_element(By.XPATH, f'//div[@class="rdrDays"]/button/span[@class="rdrDayNumber"]/span[text()="{dia_fin}"]')
            dia_inicio.click()
            time.sleep(1)

        aplicar = self.driver.find_element(By.XPATH, '//span[@class="MuiButton-label" and text()="Aplicar"]')
        aplicar.click()
        time.sleep(1)

        btn_actualizar = self.driver.find_element(By.XPATH, '//span[text()="Actualizar"]')
        btn_actualizar.click()
        time.sleep(1)

        WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[class="MuiTableBody-root"]')))
        time.sleep(1)

        cantidad_excel_inicial = self.cantidad_excel()
        
        #btn_descargar = self.driver.find_element(By.XPATH, '//span[@class="MuiButton-label" and text()="Descargar"]')
        #btn_descargar.click()
        #self.driver.execute_script("arguments[0].click();", btn_descargar)
        self.driver.execute_script("""document.evaluate('//span[@class="MuiButton-label" and text()="Descargar"]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click();""")
        #Valida que la descarga concluya
        cantidad_excel_final = cantidad_excel_inicial
        while cantidad_excel_final == cantidad_excel_inicial:
            time.sleep(1)
            cantidad_excel_final = self.cantidad_excel()
        else:
            pass

        time.sleep(1)
    
    # ====== 3. Reporte Productividad Asesores ======
    def reporte_tickets(self, fecha_inicio, fecha_fin):
        self.url_reportes = "https://claro.laraigo.com/tickets"
        self.driver.get(self.url_reportes)
        time.sleep(5)

        calendario = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/main/div[2]/div/div/div[2]/div[1]/div/div[1]/button[1]')
        calendario.click()
        time.sleep(1)

        fecha_inicio = datetime.datetime.strptime(fecha_inicio, '%Y-%m-%d')
        periodo_inicio = int(datetime.datetime.strftime(fecha_inicio, '%Y%m'))
        fecha_fin = datetime.datetime.strptime(fecha_fin, '%Y-%m-%d')
        periodo_fin = int(datetime.datetime.strftime(fecha_fin, '%Y%m'))

        # Selecciona fecha Inicio
        anio_inicio = fecha_inicio.year
        mes_inicio = fecha_inicio.month - 1
        dia_inicio = fecha_inicio.day

        anio_lista = self.driver.find_element(By.CSS_SELECTOR, '[class="rdrYearPicker"]')
        anio_lista.click()
        time.sleep(1)
        selecciona_anio = self.driver.find_element(By.CSS_SELECTOR, f'[value="{anio_inicio}"]')
        selecciona_anio.click()
        time.sleep(1)

        mes_lista = self.driver.find_element(By.CSS_SELECTOR, '[class="rdrMonthPicker"]')
        mes_lista.click()
        time.sleep(1)
        selecciona_anio = self.driver.find_element(By.CSS_SELECTOR, f'[value="{mes_inicio}"]')
        selecciona_anio.click()
        time.sleep(1)

        dia_inicio = self.driver.find_element(By.XPATH, f'//div[@class="rdrDays"]/button/span[@class="rdrDayNumber"]/span[text()="{dia_inicio}"]')
        dia_inicio.click()
        time.sleep(1)

        #Selecciona fecha fin
        anio_fin = fecha_fin.year
        mes_fin = fecha_fin.month - 1
        dia_fin = fecha_fin.day

        if periodo_inicio == periodo_fin:
            dia_fin = self.driver.find_element(By.XPATH, f'//div[@class="rdrDays"]/button/span[@class="rdrDayNumber"]/span[text()="{dia_fin}"]')
            dia_fin.click()
            time.sleep(1)
        else:
            anio_lista = self.driver.find_element(By.CSS_SELECTOR, '[class="rdrYearPicker"]')
            anio_lista.click()
            time.sleep(1)
            selecciona_anio = self.driver.find_element(By.CSS_SELECTOR, f'[value="{anio_fin}"]')
            selecciona_anio.click()
            time.sleep(1)

            mes_lista = self.driver.find_element(By.CSS_SELECTOR, '[class="rdrMonthPicker"]')
            mes_lista.click()
            time.sleep(1)
            selecciona_anio = self.driver.find_element(By.CSS_SELECTOR, f'[value="{mes_fin}"]')
            selecciona_anio.click()
            time.sleep(1)

            dia_inicio = self.driver.find_element(By.XPATH, f'//div[@class="rdrDays"]/button/span[@class="rdrDayNumber"]/span[text()="{dia_fin}"]')
            dia_inicio.click()
            time.sleep(1)

        aplicar = self.driver.find_element(By.XPATH, '//span[@class="MuiButton-label" and text()="Aplicar"]')
        aplicar.click()
        time.sleep(1)

        btn_buscar = self.driver.find_element(By.XPATH, '//span[text()="Buscar"]')
        btn_buscar.click()
        time.sleep(1)

        WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[class="MuiTableBody-root"]')))
        time.sleep(1)

        cantidad_zip_inicial = self.cantidad_zip()
        
        btn_descargar = self.driver.find_element(By.XPATH, '//span[@class="MuiButton-label" and text()="Descargar"]')
        btn_descargar.click()
        #self.driver.execute_script("arguments[0].click();", btn_descargar)

        #Valida que la descarga concluya
        cantidad_zip_final = cantidad_zip_inicial
        while cantidad_zip_final == cantidad_zip_inicial:
            time.sleep(1)
            cantidad_zip_final = self.cantidad_zip()
        else:
            pass

        time.sleep(1)
    
    # Funcion que reubicará las descargas en sus respectivas carpetas
    def renombrarReubicar(self, nuevoNombre, extension, carpetaDestino):
        ruta_descargas = self.directoryPath + r'/temp'
        archivos_descargados = sorted(glob.glob(os.path.join(ruta_descargas, '*')), key=os.path.getmtime, reverse=True)
        # Comprobar si hay archivos descargados
        if len(archivos_descargados) > 0:
            ultimo_archivo = archivos_descargados[0]
            # Cambiar el nombre del archivo --1er argumento de la funcion
            nuevo_nombre = f'{nuevoNombre}.{extension}' #xlsx, csv
            carpeta_destino = carpetaDestino
            # Comprobar si la carpeta de destino existe, si no, crearla
            if not os.path.exists(carpeta_destino):
                os.makedirs(carpeta_destino)
            # Ruta completa del archivo de destino
            ruta_destino = os.path.join(carpeta_destino, nuevo_nombre)
            # Mover el archivo a la carpeta de destino con el nuevo nombre
            shutil.move(ultimo_archivo, ruta_destino)

    # Funcion que crea el nombre del reporte
    def nombreReporte(self, name, finicio, ffin, fechaD0 = True):
        if fechaD0:
            fechaHora = datetime.datetime.now()
            fecha = fechaHora.strftime("%Y%m%d_%H%M%S")
            aleatorio = str(random.randint(100, 999))
            nameFile = name + fecha + '_' + aleatorio
        else:
            if ffin == None:
                ffin = finicio
            else:
                pass
            h = datetime.datetime.now()
            hora = h.strftime('%H%M%S')
            fechan = datetime.datetime.strptime(ffin, '%Y-%m-%d')
            fechan = fechan + datetime.timedelta(days=1)
            fecha = fechan.strftime("%Y%m%d_")
            aleatorio = str(random.randint(100, 999))
            nameFile = name + fecha + hora + '_' + aleatorio
        
        return nameFile

    def limpia_carpeta_descargas(self):
        # Ruta de la carpeta
        directorio_a_limpiar = self.defaultPathDownloads

        # Itera sobre todos los archivos en la carpeta
        for nombre_archivo in os.listdir(directorio_a_limpiar):
            ruta_completa = os.path.join(directorio_a_limpiar, nombre_archivo)

            # Verifica si es un archivo (ignorando subdirectorios)
            if os.path.isfile(ruta_completa):
                # Elimina el archivo
                os.remove(ruta_completa)
                print(f"Archivo eliminado: {ruta_completa}")

    def descomprime_zip(self):
        directorio_zip = self.defaultPathDownloads
        patron = "*.zip"

        archivos_zip = glob.glob(os.path.join(directorio_zip, patron))
        self.archivo_zip = archivos_zip[0]
        #exit()
        directorio_destino = directorio_zip
        with zipfile.ZipFile(self.archivo_zip, 'r') as zip_ref:
            zip_ref.extractall(directorio_destino)

    def remove_zip(self):
        os.remove(self.archivo_zip)

    def gameOver(self):
        self.driver.quit()








from googleapiclient.discovery import build
from google.oauth2 import service_account
from oauth2client.service_account import ServiceAccountCredentials
from decouple import config
import pandas as pd
import gspread

SHEET_ID = config('SHEET_ID')
SHEET_KEY_JSON = config('SHEET_KEY_JSON', default='key.json')

rango = "EA!A1:H6" #PARA REALIZAR PRUEBAS YA QUE SOLO SIRVE CON LA HOJA LLAMADA "EA"

def ObtenerNombreHojas(sheetID,sheetKey):    
    nombreHojas = []
    SCOPE = ['https://spreadsheets.google.com/feeds',
                'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(sheetKey, SCOPE)
    cliente = gspread.authorize(creds)
    spreadsheet_id = sheetID
    spreadsheet = cliente.open_by_key(spreadsheet_id)
    for hoja in spreadsheet.worksheets():
        nombreHojas.append(hoja.title)
        print(f'se leyo la hoja: {hoja.title}')
    return nombreHojas

def LeerSheets(IDsheets,key,rango):
    '''
    Se conecta a la API de google sheets para obtener la informacion deseada en los rangos especificados
    '''
    SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

    credenciales = service_account.Credentials.from_service_account_file(key, scopes=SCOPES)
    servicio = build('sheets', 'V4', credentials=credenciales)
    sheet = servicio.spreadsheets()
    resultado = sheet.values().get(spreadsheetId=IDsheets, range=rango).execute()
    values = resultado.get("values",[])
    return values

def CrearDataFrame(datos):
    dataFrame = pd.DataFrame(data=datos)
    # print()
    pass
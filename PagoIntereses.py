from googleapiclient.discovery import build
from google.oauth2 import service_account
from decouple import config

SHEET_ID = config('SHEET_ID')
SHEET_KEY_JSON = config('SHEET_KEY_JSON', default='key.json')

rango = "EA!A1:H6"

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
    print(values)

LeerSheets(SHEET_ID, SHEET_KEY_JSON, rango)
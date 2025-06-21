from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account

key = ".json"
sheetId = ""
rango = ""

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

LeerSheets(sheetId, key, rango)
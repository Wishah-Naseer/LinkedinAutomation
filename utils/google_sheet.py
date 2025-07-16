import gspread
from oauth2client.service_account import ServiceAccountCredentials

class GoogleSheetManager:
    def __init__(self, credentials_path, spreadsheet_url):
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_path, scope)
        self.client = gspread.authorize(creds)
        self.spreadsheet = self.client.open_by_url(spreadsheet_url)

    def clear_sheet(self, sheet_name):
        sheet = self.spreadsheet.worksheet(sheet_name)
        sheet.clear()

    def update_sheet(self, sheet_name, headers, data):
        sheet = self.spreadsheet.worksheet(sheet_name)
        sheet.clear()
        rows = [headers] + data
        sheet.update("A1", rows)

    def get_records(self, sheet_name):
        sheet = self.spreadsheet.worksheet(sheet_name)
        return sheet.get_all_records()

"""
Utility module for managing Google Sheets using gspread and OAuth2 credentials.
Provides a class to clear, update, and fetch records from a Google Sheet.
"""
import gspread
from oauth2client.service_account import ServiceAccountCredentials

class GoogleSheetManager:
    """
    Manages Google Sheets operations: clearing, updating, and retrieving records.
    """
    def __init__(self, credentials_path, spreadsheet_url):
        """
        Initialize the GoogleSheetManager with credentials and spreadsheet URL.
        Args:
            credentials_path (str): Path to the Google service account credentials JSON file.
            spreadsheet_url (str): URL of the target Google Spreadsheet.
        """
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_path, scope)
        self.client = gspread.authorize(creds)
        self.spreadsheet = self.client.open_by_url(spreadsheet_url)

    def clear_sheet(self, sheet_name):
        """
        Clear all data from the specified sheet.
        Args:
            sheet_name (str): Name of the worksheet to clear.
        """
        sheet = self.spreadsheet.worksheet(sheet_name)
        sheet.clear()

    def update_sheet(self, sheet_name, headers, data):
        """
        Clear the sheet and update it with new headers and data.
        Args:
            sheet_name (str): Name of the worksheet to update.
            headers (list): List of column headers.
            data (list of lists): Data rows to insert below the headers.
        """
        sheet = self.spreadsheet.worksheet(sheet_name)
        sheet.clear()
        rows = [headers] + data
        sheet.update("A1", rows)

    def get_records(self, sheet_name):
        """
        Retrieve all records from the specified sheet as a list of dictionaries.
        Args:
            sheet_name (str): Name of the worksheet to fetch records from.
        Returns:
            list: List of dictionaries representing each row.
        """
        sheet = self.spreadsheet.worksheet(sheet_name)
        return sheet.get_all_records()

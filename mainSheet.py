import gspread
import re
from datetime import date, datetime
import json


class MainSheet:

    def __init__(self):
        self.gc = gspread.service_account(filename="./resources/creds.json")
        with open("./resources/settings.json") as file:
            self.settings = json.load(file)

        if self.settings["loa_sheet_url"] != None:
            self.sh = self.gc.open_by_url(self.settings["loa_sheet_url"])
        else:
            print("loa_sheet_url needs to be set. Change this in settings.json.")

    def getBL(self):
        regExpression = re.compile(r'^STEAM_')
        worksheet = self.sh.worksheet(self.settings['blacklist_sheetname'])
        cells = worksheet.findall(regExpression)
        values = []
        for cell in cells:
            values.append(cell.value)

        return values

    def removeExpired(self):
        regExpression = re.compile(r'(^\d)')

        worksheet = self.sh.worksheet(self.settings['loa_sheetname'])
        cells = worksheet.findall(regExpression, in_column=self.settings['end_date_column'])  # Get all the end date cells to detect available lines

        if cells == []:  # If no LOAs
            return cells
        unformatted_row = self.settings['first_unformatted_row'] # This is the first row of LOA entries (skips the formatting)
        endRow = 0

        for cell in cells:
            if cell.row > endRow:
                endRow = cell.row


        names_column = self.settings['names_column']
        dates_column = self.settings['end_dates_column']
        data = worksheet.batch_get([names_column+str(unformatted_row)+':'+names_column+ str(endRow),  dates_column+str(unformatted_row)+':'+dates_column + str(endRow)])

        expiredIndex = []
        expiredLOANames = []

        names = data[0]
        end_dates = data[1]

        # The added skip_rows is because the index for python lists start at 0, whilst google sheet row indexes start at 1
        # also, we need to skip the formatting row.
        skip_rows = unformatted_row

        for i in range(0, len(end_dates)):
            try:
                datetime_obj = datetime.strptime(end_dates[i][0], '%m/%d/%Y')
                if datetime_obj < datetime.now():
                    expiredLOANames.append(names[i][0])
                    expiredIndex.append(skip_rows+i)
            except IndexError:
                expiredIndex.append(skip_rows+i)

        if expiredLOANames == []:
            return []


        expiredIndex.reverse()
        for index in expiredIndex:
            worksheet.delete_row(index)

        return expiredLOANames

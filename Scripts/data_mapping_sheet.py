# Create a blank Excel template for data mapping using openpyxl
from openpyxl import Workbook

# Create workbook and sheet
wb = Workbook()
ws = wb.active
ws.title = "Data_Mapping"

# Header columns for the mapping sheet
headers = [
    "Domain",
    "Legacy Table",
    "Legacy Column",
    "Target Table",
    "Target Column",
    "Transformation Rule",
    "Example / Notes"
]

ws.append(headers)

# Save file
file_path = "/mnt/data/data_mapping_template.xlsx"
wb.save(file_path)

file_path

import xlrd
import pyautogui
import decimal

from counter import counter

FLOAT_DECIMAL = '0.001'
ROW = 0
COLUMN = 0
XLS_SOURCE = '.xls'

def xlsfill(filename, row, col, sleep_time = 5):
    data = xlrd.open_workbook_xls(filename)
    table = data.sheets()[0]
    
    counter.count(sleep_time)
    
    for i in range(row):
        for j in range(col):
            c_output = decimal.Decimal(str(table.cell_value(i,j))).quantize(decimal.Decimal('0.001'))
            pyautogui.typewrite(str(c_output))
            pyautogui.hotkey('tab')


if __name__ == '__main__':
    xlsfill(XLS_SOURCE, ROW, COLUMN)

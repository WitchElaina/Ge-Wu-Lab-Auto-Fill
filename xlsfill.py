import xlrd
import pyautogui
import decimal

from counter import counter

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
    filename = str(input("input .xls file name:"))
    row = int(input("input row:"))
    col = int(input("input col:"))
    xlsfill(filename, row, col)

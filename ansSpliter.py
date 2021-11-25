import pyautogui
import counter

def splitGeWuAns(m_ans):
    return str(m_ans).split(',')

def autoFill(m_in):
    for i in m_in:
        pyautogui.typewrite(str(i))
        pyautogui.hotkey('tab')
        
if __name__ == '__main__':
    ans = str(input("Input GeWu Anwsers:"))
    inputs = splitGeWuAns(ans)
    counter.count(5)
    autoFill(inputs)
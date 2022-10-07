# Ge-Wu-Lab-Auto-Fill
Auto fill gewulab's blank from .xls or tampermonkey script.

支持从`.xls`格式的Excel中读取数据自动填充

支持从[timrockefeller](https://github.com/timrockefeller/gewu_fill)大佬的脚本中读取数据自动填充



## 环境

- Python3
- pyautogui
- xlrd

## 使用

克隆仓库到本地或下载代码

```sh
cd ~
git clone https://github.com/WitchElaina/Ge-Wu-Lab-Auto-Fill.git
cd Ge-Wu-Lab-Auto-Fill
```

安装运行环境

```
pip install pyautogui xlrd
```

### `ansSpliter.py`

输入脚本获得的答案字符串，并点击第一个答案所在的文本框，程序会自动进行分割并模拟键盘输入。

```sh
python ansSpliter.py
```

### `xlsfill.py`

该程序可以将`xls`格式的表格中的数据搬运到网页表格中，使用前需要设置以下全局变量

`XLS_SOURCE`        `xls`文件路径

`ROW`               表格行数

`COLUMN`            表格列数

`FLOAT_DEMCIMAL`    数据精度


设置后运行程序并点击网页表格中第一个单元格即可完成自动输入。

```sh
python xlsfill.py
```

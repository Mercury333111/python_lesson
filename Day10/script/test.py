
import os

# 获取当前工作目录
working_directory = os.getcwd()

print("当前工作目录：", working_directory)

# Jupyter Notebook
# script_folder = globals()['_dh'][0]
# Python Script
from os import path
script_folder = path.dirname(__file__)
print("文件所在目录：", script_folder)

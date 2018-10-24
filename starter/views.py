#coding=utf-8
import sys
import imp
imp.reload(sys)
from datetime import datetime
from flask import render_template
from starter import app
import os


# __file__ refers to the file settings.py 
APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
APP_DATA = os.path.join(APP_ROOT, 'data')


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/logger')
def logger():
    """Renders the logger page."""
    filepath = 'log/log.txt'
    return render_template(
        'logger.html',
        title='Logger Page',
        date= datetime.now().strftime("%Y-%m-%d %a"),
        content = readFile(filepath)
    )

def readFile(filepath):
    content = ""
    try:
        with open(os.path.join(APP_DATA, filepath)) as f:
            content=f.read()
    except FileNotFoundError as e:
        errorMsg = "文件不存在,请检查文件路径"
        content = "Error：" + errorMsg
        print(content)
    except MemoryError as e:
        errorMsg = "内存错误"
        content = "Error：" + errorMsg
        print(content)
    except SyntaxError as e:
        errorMsg = "系统错误"
        content = "Error：" + errorMsg
        print(content)
    finally:
        print("操作完毕.")
        # f.close()
        return content

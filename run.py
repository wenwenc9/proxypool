# -*- coding: utf-8 -*-
# @Time    : 2020-12-28 18:10
# @Author  : XuGuangJun
# @FileName: run.py
# @Software: PyCharm

from scheduler import Scheduler
from api import app


def main():
    s = Scheduler()
    s.run()
    app.run(host='0.0.0.0',port=5000,debug=True)

if __name__ == '__main__':
    main()

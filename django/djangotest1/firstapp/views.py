from django.shortcuts import render
from firstapp.models import TestTable
from django.http import HttpResponse
import sqlite3

# Create your views here.

def testdb(request):
    context = {}
    conn = sqlite3.connect('db.sqlite3')
    cu = conn.cursor()
    cu.execute('select name from sqlite_master where type = "table";')
    tables = cu.fetchall()
    tableslist = []
    for table in tables:
        tableslist.append(table[0])
    #print(tableslist)
    context['conlist'] = tableslist
    return render(request,"helloword.html",context)

def get_table(request):
    tablename = request.GET['table']
    sqlcol = 'PRAGMA table_info("'+ tablename + '");'
    sql = 'select * from "' + tablename + '";'
    conn = sqlite3.connect('db.sqlite3')
    cu = conn.cursor()
    cu.execute(sqlcol)
    ret = cu.fetchall()
    columnames = [item[1] for item in ret]
    #print(columnames)
    cu.execute(sql)
    ret = cu.fetchall()
    context = {}
    context['columnames'] = columnames
    context['content'] = ret
    #print(ret)
    return render(request,"showtable.html",context)

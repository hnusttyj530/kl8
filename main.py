# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 18:16:45 2021

@author: tyj
"""


import xlwt
import re
import pymysql
import xlrd

#分解成字符串数组
def cutText(text,length): 
     textArr = re.findall('.{'+str(length)+'}', text) 
     textArr.append(text[(len(textArr)*length):]) 
     return textArr 
 
#生成kl8.xls文件
def generateXls(sheet):
    row=1
    for line in open("kl8.txt","r"):
        lineStrList=line.split('	')
        sheet.write(row,0,lineStrList[0])
        sheet.write(row,1,lineStrList[1])
        strlist=cutText(lineStrList[2].strip('\n'),2)
        for s in range (0, len(strlist)-1):
            sheet.write(row,int(strlist[s])+1,"Y")       
        row=row+1
    book.save('kl8.xls')   
 
if __name__=='__main__':
    book = xlwt.Workbook() 
    sheet = book.add_sheet(u'sheet1',cell_overwrite_ok=True) 
    sheet.write(0,0,'id')
    sheet.write(0,1,'date')
    for col in range (2,82):
        sheet.write(0,col,col-1)
    generateXls(sheet)
        
            

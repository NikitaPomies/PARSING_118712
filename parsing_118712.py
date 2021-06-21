# -*- coding: utf-8 -*-
"""
Created on Sat May 22 23:51:01 2021

@author: nikit"""

from selenium import webdriver
import  time 
import xlsxwriter
Ville="Démouville"
workbook = xlsxwriter.Workbook('Démouville.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write("A1",Ville)
worksheet.write("B1","Nom")
worksheet.write("C1",'Téléphone')
web ='https://annuaire.118712.fr/?s=Démouville'
path=r'C:\Users\nikit\Desktop\interetspersos\prog\chromedriver_win32\chromedriver.exe'


driver = webdriver.Chrome(path)
driver.get(web)


time.sleep(4) #add implicit wait, if necessary

accept = driver.find_element_by_xpath('//*[@id="didomi-notice-agree-button"]')
accept.click()
time.sleep(3)

particulier=driver.find_element_by_xpath('//*[@id="propart-button"]')
particulier.click()
time.sleep(2)
test=driver.find_element_by_xpath('//*[@id="ui-id-3"]')
test.click()
time.sleep(3)
for _ in range(10):
    
    elem_en_plus=driver.find_element_by_xpath('//*[@id="more"]')
    elem_en_plus.click()
    time.sleep(5)
           
nums=[]
box = driver.find_element_by_xpath('//*[@id="lrArticlesBannerButtons"]')
articles = box.find_elements_by_tag_name('article')
#print(articles)
i=0
for  article in articles:
    
    if (article.find_element_by_class_name('actions-btn').size!=0):
        a=article.find_element_by_class_name('actions-btn')
    type_par=article.find_element_by_class_name('propart_text')
    if (type_par.text=='Particulier'):
        worksheet.write(i+1,0,Ville)
        name=article.find_element_by_class_name('titre')
        worksheet.write(i+1,1,name.text)
        
        #print("test",a.text)
        #print(a.text)
        
        if (a.find_element_by_tag_name('a').size!=0):
            b=a.find_element_by_tag_name('a')
            if (b.find_element_by_class_name('button_wording').size!=0):
                c=b.find_element_by_class_name('button_wording')
                worksheet.write(i+1,2,c.text)
                print(name.text,c.text)
        i+=1
            
    #print(b.text)
    
workbook.close()

    
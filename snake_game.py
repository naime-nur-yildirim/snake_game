# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 00:54:24 2021

@author: naimennyy
"""

import turtle
import time #programı yavaşlatmak için
import random

hiz = 0.15

pencere = turtle.Screen()  #pencere oluşturma
pencere.title('YILAN OYUNU') #title
pencere.bgcolor('black') #arka plan rengi
pencere.setup(width=600, height= 600) #pencere boyutu
pencere.tracer(0) #güncellemeyi engellemek için
#yılanın kafasını oluşturma

kafa = turtle.Turtle() 
kafa.speed(0) #başlangıçta hızı yok
kafa.shape('square') #kafanın şeklini belirleme
kafa.color('red') 
kafa.penup() #iz bırakmadan(yazı yazdırmayacak)
kafa.goto(0,100) #normal konumdayken (x,y) konumu
kafa.direction ='stop'

#yemi oluşturma
yem = turtle.Turtle() 
yem.speed(0) 
yem.shape('circle') 
yem.color('blue') 
yem.penup() 
yem.goto(0,0)
yem.shapesize(0.80 , 0.80)

kuyruklar = []
puan = 0

yaz = turtle.Turtle() 
yaz.speed(0) 
yaz.shape('square') 
yaz.color('white') 
yaz.penup() 
yaz.goto(0,260)
yaz.hideturtle()
yaz.write('PUAN: {} '.format(puan), align='center', font=('Courier',24,'normal'))


#hareketi sağlamak için ve döngü içinde sürekli çalışacak fonksiyon
def move():
    if kafa.direction == 'up':
        y=kafa.ycor()
        kafa.sety(y + 20) 
        
    if kafa.direction == 'down':
        y=kafa.ycor()
        kafa.sety(y - 20)
       
    if kafa.direction == 'right':
        x=kafa.xcor()
        kafa.setx(x + 20)
   
    if kafa.direction == 'left':
        x=kafa.xcor()
        kafa.setx(x - 20)
        
     #zıttı yönde olduğunda yılan hareket edemeyecektir    
def goUp(): 
    if kafa.direction != 'down':
        kafa.direction = 'up'

def goDown():
    if kafa.direction != 'up':
        kafa.direction = 'down'

def goRight():
    if kafa.direction != 'left':
        kafa.direction = 'right'
        
def goLeft():
    if kafa.direction != 'right':
        kafa.direction = 'left'

#klavye kontrolü
pencere.listen() #klavyeyi dinleme
pencere.onkey(goUp, 'Up') #up tuşuna basıldığında goUp fonksiyonunu çağır
pencere.onkey(goDown, 'Down') 
pencere.onkey(goRight, 'Right') 
pencere.onkey(goLeft, 'Left') 

 

while True:
    pencere.update() 
    #kenarlara çarpınca oyunun durması ve puannın sıfırlanması lazım
    
    if kafa.xcor() > 300 or kafa.xcor() < -300 or kafa.ycor() > 300 or kafa.ycor() < -300:
        time.sleep(1)
        kafa.goto(0,0)
        kafa.direction = 'stop'
        
        for kuyruk in kuyruklar:
            kuyruk.goto(1000,1000)
        
        kuyruklar = []
       
        puan = 0
        yaz.clear()
        yaz.write('PUAN: {} '.format(puan),align='center', font=('courier',24,'normal'))
        
        hiz = 0.15


    if kafa.distance(yem)<20:
        x = random.randint(-250, 250)
        y = random.randint(-250,250)
        yem.goto(x,y)
        
        puan = puan + 10
        yaz.clear()
        yaz.write('PUAN: {} '.format(puan),align='center', font=('Courier',24,'normal'))
        
        hiz = hiz + 0.001
        
        yeniKuyruk = turtle.Turtle() #yemi her yediğinde kafanınn sonuna kuyruk eklenmesini sağlayacak
        yeniKuyruk.speed(0)
        yeniKuyruk.shape('square')
        yeniKuyruk.color('white')
        yeniKuyruk.penup()
        kuyruklar.append(yeniKuyruk)
        
    for i in range(len(kuyruklar) - 1 , 0 , -1):
        x = kuyruklar[i - 1].xcor()
        y = kuyruklar[i - 1].ycor()

        kuyruklar[i].goto(x,y)
   
    if len(kuyruklar) > 0:
        x = kafa.xcor()
        y = kafa.ycor()
        kuyruklar[0].goto(x,y) 


    move()
    time.sleep(hiz)
    #hiz değişkeninin değerine göre programı yavaşlatır
    
    
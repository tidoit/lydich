#!/usr/bin/python
# -*- coding: UTF-8 -*-
import codecs
import random
tenque = [[],[],[],[],[],[],[],[]]
que = [[],[],[],[],[],[],[],[]]
#Nhap 64 que
#
with codecs.open('64que.csv', encoding='utf-8') as f64que:
	count=0

	for line in f64que:
		if count<=7:
			que[count]=line.split(',')
			count=count+1
		else:
			tenque[count-8]=line.split(',')
			count+=1
        
##

#Day la hang so chuyen so cua don tuong ra so thap phan roi the hien ra nhi phan
#vi du: Thien,co so ly la 1, the hien la 3 vach lien = 111, Dia so ly la 8, the hien la 3 vach dut =000
#Khon=000,Can=100,Kham=010,Ton=110,Chan=001,Ly=101,Doai=011,Kien=111
#   0       4         2       6        1       5       3        7
indexBinary='73516240'
execfile('amlich.py')
def timChanhTuongTheoBocBai(tayTrai,tayPhai):
	soLyTienTuong=(tayTrai+7)%8
	soLyHauTuong=(tayPhai+7)%8
	haoDong=(tayTrai+tayPhai+5)%6
	return soLyTienTuong, soLyHauTuong, haoDong
	
def timChanhTuongTheoNgay(hour,day,month,year):    
    ngayam=S2L(day,month,year)
    gioam=hour/2+hour%2+1
    #chuyen nam am ra so
    ngayam[2]=year%167-3
    soLyTienTuong=(ngayam[0]+ngayam[1]+ngayam[2]+7)%8
    soLyHauTuong=(ngayam[0]+ngayam[1]+ngayam[2]+7+gioam)%8
    #print indexBinary[tientuong-1], indexBinary[hautuong-1]
    print gioam
    haoDong=(ngayam[0]+ngayam[1]+ngayam[2]+gioam+5)%6
    print "Âm lich: ngày "+str(ngayam[0])+" tháng "+str(ngayam[1])+" năm "+str(ngayam[2])+". Hao dong: "+str(haoDong+1)
    
    return soLyTienTuong, soLyHauTuong, haoDong
    
def timHoTuong(tienChanhTuong,hauChanhTuong):
    #chuyen tu so ly cua don tuong ra ma nhi phan
    strTienChanhTuong='{0:03b}'.format(int(indexBinary[tienChanhTuong]))
    strHauChanhTuong='{0:03b}'.format(int(indexBinary[hauChanhTuong]))

    #strChanhTuong se co dang 000000,010101,111000,....
    strChanhTuong=strTienChanhTuong+strHauChanhTuong

    strTienHoTuong=strChanhTuong[1:4]
    strHauHoTuong=strChanhTuong[2:5]
    #print strTienBienTuong,strHauBienTuong
    
    #sau khi co ma nhi phan cua bien tuong thi chuyen ve so ly de in ra que    
    soLyTienHoTuong=indexBinary.find(str(int(strTienHoTuong,2)))
    soLyHauHoTuong=indexBinary.find(str(int(strHauHoTuong,2)))
    return soLyTienHoTuong, soLyHauHoTuong

def timBienTuong(tienChanhTuong,hauChanhTuong,haoDong):
    #chuyen tu so ly cua don tuong ra ma nhi phan
    strTienChanhTuong='{0:03b}'.format(int(indexBinary[tienChanhTuong]))
    strHauChanhTuong='{0:03b}'.format(int(indexBinary[hauChanhTuong]))

    #strChanhTuong se co dang 000000,010101,111000,....
    strChanhTuong=strTienChanhTuong+strHauChanhTuong    
    intVachDong=int(strChanhTuong[5-haoDong])
    intVachDong^=1    
    strBienTuong=strChanhTuong[:(5-haoDong)]+str(intVachDong)+strChanhTuong[(5-haoDong+1):]   
    soLyTienBienTuong=indexBinary.find(str(int(strBienTuong[0:3],2)))
    soLyHauBienTuong=indexBinary.find(str(int(strBienTuong[3:6],2)))
    
    return soLyTienBienTuong, soLyHauBienTuong   
    
def timChanhBienTuong(chanhTuong,bienTuong):
    if chanhTuong[2]<=2:
        return chanhTuong[1],bienTuong[1]
    else:
        return chanhTuong[0],bienTuong[0]
    
#Chuong trinh chinh
def layQueTheoNgay():
	hour=int(raw_input('Giờ: '))
	day=int(raw_input('Ngày: '))
	month=int(raw_input('Tháng: '))
	year=int(raw_input('Năm: '))
	chanhTuong=[0,0,0]
	bienTuong=[0,0]
	hoTuong=[0,0]
	chanhBienTuong=[0,0]

	chanhTuong=timChanhTuongTheoNgay(hour,day,month,year)
	hoTuong=timHoTuong(chanhTuong[0],chanhTuong[1])
	bienTuong=timBienTuong(chanhTuong[0],chanhTuong[1],chanhTuong[2])
	chanhBienTuong=timChanhBienTuong(chanhTuong,bienTuong)

	print que[chanhTuong[0]][chanhTuong[1]]+"            "+que[hoTuong[0]][hoTuong[1]]+"            "+que[bienTuong[0]][bienTuong[1]]+"            "+que[chanhBienTuong[0]][chanhBienTuong[1]]
	print tenque[chanhTuong[0]][chanhTuong[1]]+"  "+tenque[hoTuong[0]][hoTuong[1]]+"  "+tenque[bienTuong[0]][bienTuong[1]]+"  "+tenque[chanhBienTuong[0]][chanhBienTuong[1]]

def bocBai():
	laBai = random.choice( ('A','2','3','4','5','6','7','8','9','10','J','Q','K','A','2','3','4','5','6','7','8','9','10','J','Q','K','A','2','3','4','5','6','7','8','9','10','J','Q','K','A','2','3','4','5','6','7','8','9','10','J','Q','K') )
	if laBai in ['A','J','Q','K']:
		return 1
	else: return int(laBai)
	
def layQueTheoBocBai():
	laBaiTayTrai = bocBai()
	laBaiTayPhai = bocBai()
	chanhTuong=timChanhTuongTheoBocBai(laBaiTayTrai,laBaiTayPhai)
	hoTuong=timHoTuong(chanhTuong[0],chanhTuong[1])
	bienTuong=timBienTuong(chanhTuong[0],chanhTuong[1],chanhTuong[2])
	chanhBienTuong=timChanhBienTuong(chanhTuong,bienTuong)

	print que[chanhTuong[0]][chanhTuong[1]]+"            "+que[hoTuong[0]][hoTuong[1]]+"            "+que[bienTuong[0]][bienTuong[1]]+"            "+que[chanhBienTuong[0]][chanhBienTuong[1]]
	print tenque[chanhTuong[0]][chanhTuong[1]]+"  "+tenque[hoTuong[0]][hoTuong[1]]+"  "+tenque[bienTuong[0]][bienTuong[1]]+"  "+tenque[chanhBienTuong[0]][chanhBienTuong[1]]

## Chương trình chính
def layQueTheoSo():
	try:
		tienTuong=raw_input('Số đầu: ')
		hauTuong=raw_input('Số sau: ')
		chanhTuong=timChanhTuongTheoBocBai(int(tienTuong),int(hauTuong))
		hoTuong=timHoTuong(chanhTuong[0],chanhTuong[1])
		bienTuong=timBienTuong(chanhTuong[0],chanhTuong[1],chanhTuong[2])
		chanhBienTuong=timChanhBienTuong(chanhTuong,bienTuong)

		print que[chanhTuong[0]][chanhTuong[1]]+"            "+que[hoTuong[0]][hoTuong[1]]+"            "+que[bienTuong[0]][bienTuong[1]]+"            "+que[chanhBienTuong[0]][chanhBienTuong[1]]
		print tenque[chanhTuong[0]][chanhTuong[1]]+"  "+tenque[hoTuong[0]][hoTuong[1]]+"  "+tenque[bienTuong[0]][bienTuong[1]]+"  "+tenque[chanhBienTuong[0]][chanhBienTuong[1]]
	except:
		print 'Nhập vào số tự nhiên dương!'
	
while True:
	chonLua=raw_input('Lấy quẻ \ntheo ngày gõ n, \ntheo bốc bài gõ b, \ntheo số gõ t: ')
	if chonLua=='n':
		layQueTheoNgay()
	elif chonLua=='b':
		layQueTheoBocBai()
	elif chonLua=='t':
		layQueTheoSo()
	else:
		print "Chọn cho đúng!"
		break	

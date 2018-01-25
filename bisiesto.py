#coding: utf-8
def esBisiesto(anio):
	if (anio%4==0 and anio%100!=0) or anio%400==0:
		print anio,"es visiesto"
	else:
		print anio,"no es bisiesto"
esBisiesto(2000)
esBisiesto(2002)
esBisiesto(2003)


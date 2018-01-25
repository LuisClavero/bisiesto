#coding: utf-8
anio=input("Indica un año:")
if (anio%4==0 and anio%100!=0) or anio%400==0:
	print anio,"es visiesto"
else:
	print anio,"no es bisiesto"

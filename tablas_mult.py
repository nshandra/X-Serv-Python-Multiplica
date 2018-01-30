#!/usr/bin/python3

# 13.3. Tablas de multiplicar
for x in range(1,11):
	print("Tabla del ", x);
	print("-----------");
	for y in range(1,11):
		print(x, " por ", y, " es ", x*y);
		if y == 10:
			print('');
#Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
#*Пример:*
#385916 -> yes
#123456 -> no
s = input("Введите номер билета\n")
#print(len(s))
if len(s) != 6:
    print("Вы ввели неверное число")
else:
    first = int(s[0]) + int(s[1]) + int(s[2])
    second = int(s[3]) + int(s[4]) + int(s[5])
    print(first,second)
    if first == second:
        print(s," -> yes")
    else:
        print(s," -> no")

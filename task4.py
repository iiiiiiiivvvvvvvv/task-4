        #Вычислить число c заданной точностью d

# from math import pi

# d =  int(input("Введите число для заданной точности числа Пи:\n"))
# print(f'число Пи с заданной точностью {d} равно {round(pi, d)}')

        #Задайте натуральное число N.
        #Напишите программу, которая составит список простых множителей числа N.

# num = int(input("Введите число: "))
# i = 2 # первое простое число
# lst = []
# old = num
# while i <= num:
#     if num % i == 0:
#         lst.append(i)
#         num //= i
#         i = 2
#     else:
#         i += 1
# print(f"Простые множители числа {old} приведены в списке: {lst}")        

        #Задайте последовательность чисел.
        #Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# lst = list(map(int, input("Введите числа через пробел:\n").split()))
# print(f"Исходный список: {lst}")
# new_lst = []
# [new_lst.append(i) for i in lst if i not in new_lst]
# print(f"Список из неповторяющихся элементов: {new_lst}")

        #Задана натуральная степень k. Сформировать случайным образом список коэффициентов
        #(значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# k = int(input('Задайте натуральную степень многочлена k: '))
# import Func_coeff_polinom as cp 
# coeff_polynom = cp.fill_coefficients_polynomial_list(k)
# my_file = 'f_polinom4_4.txt'
# import Func_call_record_func as fc
# fc.call_record_func(k, coeff_polynom, my_file)      


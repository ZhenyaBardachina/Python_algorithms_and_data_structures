# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.


print('Введите две строчные латинские буквы: ')
a = input('Введите первую букву: ')
b = input('Введите вторую букву: ')
print(f'Первая введённая буква "{a}" находится на месте {ord(a)}, вторая буква "{b}" на месте {ord(b)}. Между ними {abs(ord(b) - ord(a))} '
      f'букв.')

"""Напишите функцию is_palindrome(s), которая проверяет,
является ли переданное число или строка палиндромом и возвращает True.
В противном случае возвращает False.
Палиндром - это число или текст, который читается одинаково и слева, и справа,
пробелы, знаки пунктуации и регистр символов не учитываются.
Требуется реализовать только функцию, решение не должно осуществлять операций ввода-вывода."""


# def IsPalindrome(S):
#     S = S.lower()
#     return S == S[::-1]

def is_palindrome(S='шалаш'):
    S = S.lower()
    if S == S[::-1]:
        return True
    else:
        return False
print(is_palindrome(input()))
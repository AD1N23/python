
def calc(num1, num2, act):
    if type(num1) and type(num2) not in [int, float]:
        raise TypeError('Числа должны соответствовать множеству Рациональных(Q) чисел ')
    if type(act) not in [str]:
        raise TypeError('Act пренадлежит типу string')
    if act == '+':
        return num1 + num2
    elif act == '-':
        return num1 - num2
    elif act == '/':
        return num1 / num2
    elif act == '*':
        return num1 * num2
    else:
        print('Что то пошло не так!')
        return -1
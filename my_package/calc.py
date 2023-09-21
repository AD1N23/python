from loguru import logger

logger.add("calc.log", format="{time} {level} {message}", level="DEBUG")


def calc(num1, num2, act):
    if type(num1) and type(num2) not in [int, float]:
        raise TypeError('Числа должны соответствовать множеству Рациональных(Q) чисел ')
    if type(act) not in [str]:
        raise TypeError('Act пренадлежит типу string')

    if act == '+':
        result = num1 + num2
    elif act == '-':
        result = num1 - num2
    elif act == '/':
        result = num1 / num2
    elif act == '*':
        result = num1 * num2
    else:
        print('Что то пошло не так!')
        result = None
    logger.info(f"\n Первое число : {num1}\n Второе чило : {num2}\n Действие : {act}\n {num1} {act} {num2} = {result}\n")

    return result

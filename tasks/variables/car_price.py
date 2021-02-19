"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Отредактировать функцию car_price, которая принимает стоимость автомобиля
без наценки

Функция должна прибавлять к ней несколько дополнительных сумм:
    - налог (18%),
    - регистрационный сбор (5%),
    - агентский сбор (500),
    - цену доставки (100)

ПРИМЕРЫ
--------------------------------------------------------------------------------
- car_price(6000) -> 7980.0
- car_price(30500) -> 38115.0
- car_price(17819) -> 22517.37
"""
TAX = 18
REGISTRATION_FEE = 5
AGENCY_FEE = 500
DELIVERY_PRICE = 100


def car_price(price: float) -> float:
    """Возвращает стоимость автомобиля с наценками

    :param price: стоимость автомобиля без наценок
    :type price: float

    :return: Стоимость автомобиля с наценками
    :rtype: float
    """
    result = None
    return result


if __name__ == '__main__':
    price_val = float(input('Введите стоимость автомобиля: '))
    print(f'Стоимость с наценками: {car_price(price_val)}')


class IncorrectVinNumber(Exception):

    def __init__(self, message):

        self.message = message


class IncorrectCarNumbers(Exception):

    def __init__(self, message):
        self.message = message



class Car:

    def __init__(self, model, vin_number, numbers):

        self.model = model

        if self.__is_valid_vin(vin_number):
            self.__vin_number = vin_number
        else:
            self.__vin_number = None

        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers
        else:
            self.__numbers = None

    def __is_valid_vin(self, vin_number):

        if (isinstance(vin_number, int) and
            vin_number in range(1000000, 10000000)):
            return True
        elif (isinstance(vin_number, int) and
              vin_number not in range(1000000, 10000000)):
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        else:
            raise IncorrectVinNumber('Некорректный тип vin номер')

    def __is_valid_numbers(self, numbers):

        if (isinstance(numbers, str) and
            len(numbers) == 6):
            return True
        elif (isinstance(numbers, str) and
              len(numbers) != 6):
            raise IncorrectCarNumbers('Неверная длина номера')
        else:
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')

    def get_vin(self):

        return self.__vin_number

    def get_numbers(self):

        return self.__numbers


try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')
  print(f'vin: {first.get_vin()}, number: {first.get_numbers()}')

print(f'*' * 30)

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')
  print(f'vin: {second.get_vin()}, number: {second.get_numbers()}')

print(f'*' * 30)

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')
  print(f'vin: {third.get_vin()}, number: {third.get_numbers()}')
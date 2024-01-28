import requests
import json


class ConversionException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConversionException(f'Невозможно перевести одинаковые монеты {base}.')


        try:
            amount = float(amount)
        except ValueError:
            raise ConversionException(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://v6.exchangerate-api.com/v6/1b4d1dcb7a8b73b4c33cc157/pair/{quote}/{base}/{amount}')
        total = json.loads(r.content)

        return total

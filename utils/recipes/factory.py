import datetime
import random
from random import randint

from faker import Faker


def rand_ratio():
    return f'https://loremflickr.com/{randint(840, 900)}/{randint(473, 573)}/cook,food/'


def data_hora_aleatoria():
    ano_atual = datetime.datetime.now().year
    ano_aleatorio = random.randint(2022, ano_atual)
    mes_aleatorio = random.randint(1, 12)
    dia_aleatorio = random.randint(1, 28)
    hora_aleatoria = random.randint(0, 23)
    minuto_aleatorio = random.randint(0, 59)

    data_hora = datetime.datetime(
        ano_aleatorio, mes_aleatorio, dia_aleatorio, hora_aleatoria, minuto_aleatorio)

    return data_hora.strftime('%d/%m/%Y às %H:%M')


fake = Faker('pt_BR')


def make_recipe():
    return {
        'id': fake.random_number(digits=4, fix_len=True),
        'title': fake.sentence(nb_words=6),
        'description': fake.sentence(nb_words=12),
        'preparation_time': fake.random_number(digits=2, fix_len=True),
        'preparation_time_unit': 'Minutos',
        'servings': fake.random_number(digits=2, fix_len=True),
        'servings_unit': 'Porçõe',
        'preparation_steps': fake.text(3000),
        'timestamp': data_hora_aleatoria(),
        'author': {
            'first_name': fake.first_name(),
            'last_name': fake.last_name()
        },
        'category': {
            'name': fake.word()
        },
        'cover': {
            'url': rand_ratio()
        }
    }


if __name__ == '__main__':
    from pprint import pprint
    pprint(make_recipe())

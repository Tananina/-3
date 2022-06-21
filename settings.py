# Валидные данные для авторизации
valid_email = 'vero.s86@mail.ru'
valid_password = '12345as'
# ------------------------------------------------------------------------------------------------

# Не валидные данные для авторизации
invalid_email = 'vero.s86@mail.ru'
invalid_password = '8888'
invalid_auth_key = {
  "key": "ea738148a1f19838e1c3731380e733e877b0ae729"
}
rotten_auth_key = {
  "key": "5bbb3d349e1290f5b2a51ff02c0529145a264976f25777a1557cd8eb"
}
# -----------------------------------------------------------------------------------------------


# Данные для добавления питомца
add_name = 'Догги'
add_age = '8'
add_animal_type = 'Sobaka'
add_pet_photo = 'images/cat1.jpg'
# -----------------------------------------------------------------------------------------------

# Данные для обновления информации о питомце
update_name = 'Барт'
update_age = '10'
update_animal_type = 'Wulf'
update_pet_photo = 'images/cat2.jpg'
# ----------------------------------------------------------------------------------------------


def generate_string(num):
    return "x" * num


def russian_chars():
    return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


def chinese_chars():
    return '的一是不了人我在有他这为之大来以个中上们'


def special_chars():
    return '|\\/!@#$%^&*()-_=+`~?"№;:[]{}'








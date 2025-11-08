import string
from password.new_password import generate_password

def test_password_characters():
    """Тест, что при генерации используются только допустимые символы"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Генерируем длинный пароль для более надежной проверки
    for char in password:
        assert char in valid_characters

def test_password_length():
    password_length = 10
    password = generate_password(password_length)
    assert len(password) == password_length

def test_password_uniqueness():
    password1 = generate_password(10)
    password2 = generate_password(10)
    assert password1 != password2

def test_password_empty():
    password = generate_password(10)
    if password == '':
        assert False, "пароль не может быть пустым"
    else:
        assert True

def test_password_minus_length():
    password_length = 10
    password = generate_password(password_length)
    if password_length < 0:
        assert False, "длина пароля не может быть отрицательной"
    else:
        assert True

def test_password_digits():
    password = generate_password(10)
    if any(char.isdigit() for char in password):
        assert True
    else:
        assert False, "пароль должен содержать цифры"
        
"""
Допиши еще один тест из предложенных. Или придумай свой.
Если сможешь написать больше, то будет круто!

Тест, что длина пароля соответствует заданной
Тест, что два сгенерированных подряд пароля различаются
"""
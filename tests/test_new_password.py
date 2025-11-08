import string
from password.new_password import generate_password

def test_password_characters():
    """Тест, что при генерации используются только допустимые символы"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Генерируем длинный пароль для более надежной проверки
    for char in password:
        assert char in valid_characters

"""
Допиши еще один тест из предложенных. Или придумай свой.
Если сможешь написать больше, то будет круто!

Тест, что длина пароля соответствует заданной
Тест, что два сгенерированных подряд пароля различаются
"""

def test_password_length():
    length = 5
    password = generate_password(length)
    assert len(password) == length, f"Ожидалась длина {length}, но получено {len(password)}"

def test_password_equal():
    password1 = generate_password(20)
    password2 = generate_password(20)
    assert password1 != password2, "Два подряд сгенерированных пароля совпали"

def test_not_empty():
    password = generate_password(10)
    assert password != "", "Пароль не должен быть пустым"
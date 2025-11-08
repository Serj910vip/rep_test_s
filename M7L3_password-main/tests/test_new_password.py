import string
from password.new_password import generate_password

def test_password_characters():
    """Тест, что при генерации используются только допустимые символы"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Генерируем длинный пароль для более надежной проверки
    for char in password:
        assert char in valid_characters

def test_password_length():
    """Тест, что длина пароля соответствует заданной"""
    for length in (1, 5, 12, 100):
        pwd = generate_password(length)
        assert isinstance(pwd, str)
        assert len(pwd) == length

def test_default_length():
    """Тест, что длина по умолчанию равна 12"""
    assert len(generate_password()) == 12

def test_passwords_are_different():
    """Тест, что два сгенерированных подряд пароля различаются"""
    pwd1 = generate_password(12)
    pwd2 = generate_password(12)
    assert pwd1 != pwd2
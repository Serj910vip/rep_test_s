import string
from password.new_password import generate_password

def test_password_characters():
    """Тест, что при генерации используются только допустимые символы"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100) 
    for char in password:
        assert char in valid_characters

def test_password_length():
    """Тест, что длина пароля соответствует заданной"""
    for length in [8, 12, 16, 20, 50]:
        password = generate_password(length)
        assert len(password) == length, f"Ожидалась длина {length}, получено {len(password)}"

def test_password_uniqueness():
    """Тест, что два сгенерированных подряд пароля различаются"""
    password1 = generate_password(12)
    password2 = generate_password(12)
    assert password1 != password2, "Пароли должны быть разными"

def test_password_not_empty():
    """Тест, что пароль не пустой"""
    password = generate_password(8)
    assert len(password) > 0, "Пароль не должен быть пустым"
    assert password.strip() != "", "Пароль не должен состоять только из пробелов"

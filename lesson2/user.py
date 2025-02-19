"""
Напишите класс User, имеющий следующие свойства и методы:

- __init__(self, name, password): конструктор, принимающий имя пользователя и пароль
- name: свойство, которое возвращает имя пользователя
- password: свойство, которое позволяет установить или изменить пароль пользователя
- is_admin: свойство, которое возвращает, является ли пользователь администратором или нет
- _is_admin: свойство-помощник, которое определяет, является ли пользователь администратором или нет
- login(self, password): метод, который проверяет, соответствует ли введенный пароль паролю пользователя
- logout(self): метод, который выходит из аккаунта пользователя (устанавливает значение свойства _is_logged_in в False при условии, что пользователь залогинен)

Для свойств name и password используйте декораторы @property и @password.setter.
"""


class User:
    def __init__(self, name, password, is_admin=False, is_logged_in=True):
        self.username = name
        self.user_password = password
        self._is_admin = is_admin
        self._is_logged_in = is_logged_in


    @property
    def name(self):
        return self.username


    @name.setter
    def name(self, new_name):
        self.username = new_name


    @property
    def password(self):
        return self.user_password


    @password.setter
    def password(self, new_password):
        self.user_password = new_password


    @property
    def is_admin(self):
        return self._is_admin


    def login(self, password):
        if self.user_password == password:
            return True
        return False


    def logout(self):
        self._is_logged_in = False



# код для проверки 
user1 = User("Alice", "qwerty")
print(user1.name)  # Alice
print(user1.password)  # qwerty
print(user1.is_admin)  # False

user1.password = "newpassword"
print(user1.password)  # newpassword

user1._is_admin = True
print(user1.is_admin)  # True

user1.login("newpassword")  # True
user1.logout()
print(user1._is_logged_in)

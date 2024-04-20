"""
Разработай систему управления учетными записями пользователей для небольшой компании.
Компания разделяет сотрудников на обычных работников и администраторов.
У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа.
Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень
доступа и могут добавлять или удалять пользователя из системы.

Требования:
1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе: ID,
имя и уровень доступа ('user' для обычных сотрудников).

2.Класс `Admin`: Этот класс должен наследоваться от класса `User`.
Добавь дополнительный атрибут уровня доступа, специфичный для администраторов ('admin').
Класс должен также содержать методы `add_user` и `remove_user`, которые позволяют добавлять
и удалять пользователей из списка (представь, что это просто список экземпляров `User`).

3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и
модификации снаружи. Предоставь доступ к необходимым атрибутам через методы
(например, get и set методы).
"""
import uuid


class User:

    def __init__(self, name, access_level):
        self.__name = name
        self.__access_level = access_level
        self.__id = uuid.uuid4()
        self.__office = None

    def _get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    def set_access_level(self, access_level):
        self.__access_level = access_level

    def get_office(self):
        return self.__office

    def set_office(self, office):
        self.__office = office

    def print_user(self):
        print(f"""ID: {self.__id} : Компания: {self.__office}
        Имя: {self._get_name()}. Уровень доступа: {self.__access_level}""")


class Admin(User):

    def __init__(self, name, access_level, office):
        super().__init__(name, access_level)
        self.__id = uuid.uuid4()
        self.__office = office
        self.users = []
        self.users.append(self)
        self.users[0].set_office(office)

    def add_user(self, name, access_level):
        self.users.append(User(name, access_level))
        self.users[-1].set_office(self.__office)
        print(f' --- {self._get_name()} принял сотрудника {self.users[-1]._get_name()} \
в компению {self.__office} --- ')

    def remove_user(self, name):
        for __user in self.users:
            if __user._get_name() == name:
                self.users.remove(__user)
                print(f' --- {self._get_name()} уволил сотрудника {__user._get_name()} \
из компании {self.__office} --- ')

    def set_user_access_level(self, name, access_level):
        for __user in self.users:
            if __user._get_name() == name:
                if access_level == 'admin' or access_level == 'user':
                    __user.set_access_level(access_level)
                    print(f'{self._get_name()} изменил уровень доступа \
{__user._get_name()} на {__user.get_access_level()}')
                else:
                    print('!  Неизвестый уровень доступа. Допустимые аргументы метода:\
admin, user !!!')

    def get_user(self, name):
        for __user in self.users:
            if __user._get_name() == name:
                return __user
        return None


# Создаем первого администратора
first_user = Admin('Сидоров И.П.', 'admin', '"Hot Line"')
first_user.print_user()

# создаем обычных сотрудников
first_user.add_user('Иванов П.В', 'user')
first_user.add_user('Петров С.С.', 'user')
first_user.add_user('Сергеев В.Н.', 'user')

print('\nСписок сотрудников:')
for user in first_user.users:
    user.print_user()

# удаляем двух сотрудников
first_user.remove_user('Иванов П.В')
first_user.remove_user('Сергеев В.Н.')

print('\nСписок сотрудников:')
for user in first_user.users:
    user.print_user()

# изменяем уровень доступа сотруднику
first_user.set_user_access_level('Петров С.С.', 'Админ')  # С ошибкой
first_user.set_user_access_level('Петров С.С.', 'admin')

# получаем сотрудника который есть в базе
new_admin = first_user.get_user('Петров С.С.')
if new_admin:
    new_admin.print_user()
else:
    print('--- Сотрудник не найден ---')

# получаем сотрудника, которого нет в базе
new_admin = first_user.get_user('Иванов П.В')
if new_admin:
    new_admin.print_user()
else:
    print('--- Сотрудник не найден ---')

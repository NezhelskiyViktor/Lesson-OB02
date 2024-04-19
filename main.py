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

    def __init__(self, name, access_level, db):
        self.__name = name
        self.__access_level = access_level
        self.__id = uuid.uuid4()
        db.append(self)
        print(f'Пользователь {name} добавлен')

    def get_name(self):
        return self.__name

    def print_name(self):
        print(f"""ID: {self.__id} : 
        Имя: {self.get_name()}. Уровень доступа: {self.__access_level}""")


class Admin(User):

    def __init__(self, name, access_level, db):
        super().__init__(name, access_level, db)
        self.__id = uuid.uuid4()
        self.__users = None

    def add_user(self, name, access_level, db):
        self.__users = User(name, access_level, db)
        return self.__users

    def remove_user(self, name, db):
        for __user in db:
            if __user.get_name() == name:
                db.remove(__user)
                print(f' --- Сотрудник {name} уволен --- ')

    def set_al(self, name, access_level, db):
        for __user in db:
            if __user.get_name() == name:
                if access_level == 'admin' or access_level == 'user':
                    self.__access_level = access_level
                    print(f'Уровень доступа пользователя {name} изменен на {access_level}')
                else:
                    print('Неизвестый уровень доступа. Допустимые аргументы метода:  admin, user')


database = []  # База данных сотрудников

# Создаем первого администратора
first_user = Admin('Иван Петрович Сидоров', 'admin', database)

# создаем обычных сотрудников
first_user.add_user('Петр Сидорович Иванов', 'user', database)
first_user.add_user('Виктор Андреевич Сидоров', 'user', database)
first_user.add_user('Сергей Петрович Иванов', 'user', database)

print('\nСписок пользователей:')
for user in database:
    user.print_name()

# удаляем двух сотрудников
first_user.remove_user('Петр Сидорович Иванов', database)
first_user.remove_user('Сергей Петрович Иванов', database)

print('\nСписок пользователей:')
for user in database:
    user.print_name()

# изменяем уровень доступа сотруднику
first_user.set_al('Виктор Андреевич Сидоров', 'admin', database)

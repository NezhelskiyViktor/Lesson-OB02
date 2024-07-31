import uuid


class User:
    def __init__(self, name, access_level, db):
        self.__name = name
        self.__access_level = access_level
        self.__id = uuid.uuid4()
        db.append(self)
        print(f'Пользователь {name} добавлен')

    def _get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    def set_access_level(self, access_level):
        self.__access_level = access_level

    def print_name(self):
        print(f"""ID: {self.__id} : 
        Имя: {self._get_name()}. Уровень доступа: {self.__access_level}""")


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
            if __user._get_name() == name:
                db.remove(__user)
                print(f' --- {self._get_name()} уволил сотрудника {__user._get_name()} --- ')

    def set_al(self, name, access_level, db):
        for __user in db:
            if __user._get_name() == name:
                if access_level == 'admin' or access_level == 'user':
                    __user.set_access_level(access_level)
                    print(f'\
{self._get_name()} изменил уровень доступа {__user._get_name()}\
 на {__user.get_access_level()}')
                else:
                    print('!  Неизвестый уровень доступа. Допустимые аргументы метода:  admin, user !!!')

    def get_user(self, name, db):
        for __user in db:
            if __user._get_name() == name:
                return __user
        return None


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
first_user.set_al('Виктор Андреевич Сидоров', 'Админ', database)
first_user.set_al('Виктор Андреевич Сидоров', 'admin', database)

# получаем сотрудника который есть в базе
new_admin = first_user.get_user('Виктор Андреевич Сидоров', database)
if new_admin:
    new_admin.print_name()
else:
    print('--- Сотрудник не найден ---')

# получаем сотрудника, которого нет в базе
new_admin = first_user.get_user('Cергей Андреевич Сидоров', database)
if new_admin:
    new_admin.print_name()
else:
    print('--- Сотрудник не найден ---')

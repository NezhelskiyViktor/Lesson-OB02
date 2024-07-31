# Наследование и инкапсуляция
## Задание

Разработай систему управления учетными записями пользователей для небольшой компании.
Компания разделяет сотрудников на обычных работников и администраторов.
У каждого сотрудника есть уникальный идентификатор (`ID`), имя и уровень доступа.
Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень
доступа и могут добавлять или удалять пользователя из системы.

### Требования:
1. Класс `User`: Этот класс должен инкапсулировать данные о пользователе: `ID`,
имя и уровень доступа (`user` для обычных сотрудников).

2. Класс `Admin`: Этот класс должен наследоваться от класса `User`.
Добавь дополнительный атрибут уровня доступа, специфичный для администраторов (`admin`).
Класс должен также содержать методы `add_user` и `remove_user`, которые позволяют добавлять
и удалять пользователей из списка (представь, что это просто список экземпляров `User`).

3. Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и
модификации снаружи. Предоставь доступ к необходимым атрибутам через методы
(например, `get` и `set` методы).

# 🛒 Django Shop (Models + Views)

Учебный проект интернет-магазина на Django.  
Реализованы модели, регистрация пользователей, каталог товаров и отзывы.

---

## 🚀 Функционал проекта

### 👤 Пользователи
- Регистрация пользователя  
- Вход / выход из аккаунта  
- Страница профиля

### 🛍 Магазин
- Главная страница со списком товаров  
- Фильтр товаров по категориям  
- Страница товара  
- Система отзывов  
- Авторизованные пользователи могут оставлять отзывы

### ⚙️ Админка
Через Django Admin можно управлять:
- пользователями
- категориями
- товарами
- заказами
- отзывами

---

## 🧱 Используемые технологии

- Python 3
- Django 5
- SQLite
- HTML (Django Templates)

---

## 📦 Модели проекта

### Category
Категории товаров
- name
- description

### Product
Товар магазина
- name
- description
- price
- image
- category
- created_at

### Order
Заказ пользователя
- user
- created_at
- is_paid

### OrderItem
Товар в заказе
- order
- product
- quantity

### Review
Отзывы на товары
- product
- user
- rating
- comment
- created_at

---

## 🔐 Авторизация

Используется кастомная модель пользователя:
AUTH_USER_MODEL = 'accounts.CustomUser'

Страницы:
- /accounts/register/
- /accounts/login/
- /accounts/profile/

---

## 🌐 Основные страницы сайта

| Страница | URL |
|---|---|
| Главная | / |
| Товар | /product/<id>/ |
| Регистрация | /accounts/register/ |
| Вход | /accounts/login/ |
| Профиль | /accounts/profile/ |
| Админка | /admin/ |

---

## ▶️ Запуск проекта

```bash
python -m venv venv
venv\Scripts\activate
pip install django pillow
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver


## Доработка по комментариям куратора

Задание выполнено в полном объеме:

- Добавлен Meta-класс в Product (db_table, unique_together)
- Реализован метод total_price в Order
- Выполнены ORM-запросы через Django Shell
- Добавлено поле stock и выполнен запрос товаров с количеством > 10
- Реализованы модели Cart и CartItem
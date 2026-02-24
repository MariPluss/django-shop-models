# 🛒 Django Shop (Models + Views)

Учебный проект интернет-магазина на Django.
Реализованы модели, регистрация пользователей, каталог товаров и отзывы.

---

## 🚀 Функционал проекта

### 👤 Пользователи

* Регистрация пользователя
* Вход / выход из аккаунта
* Страница профиля

### 🛍 Магазин

* Главная страница со списком товаров
* Фильтр товаров по категориям
* Страница товара
* Система отзывов
* Авторизованные пользователи могут оставлять отзывы

### ⚙️ Админка

Через Django Admin можно управлять:

* пользователями
* категориями
* товарами
* заказами
* отзывами

---

## 🧱 Используемые технологии

* Python 3
* Django 5
* SQLite
* HTML (Django Templates)

---

## 📦 Модели проекта

### Category

* name
* description

### Product

* name
* description
* price
* image
* category
* stock
* created_at

### Order

* user
* created_at
* is_paid

### OrderItem

* order
* product
* quantity

### Review

* product
* user
* rating
* comment
* created_at

### Cart (Бонус)

* user
* created_at

### CartItem (Бонус)

* cart
* product
* quantity

---

## 🔐 Авторизация

Используется кастомная модель пользователя:

AUTH_USER_MODEL = 'accounts.CustomUser'

---

## ▶️ Запуск проекта

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

# 🧪 Часть PRO — Выполнение требований куратора

## 🔹 Meta в модели Product

```python
class Meta:
    db_table = "shop_products"
    unique_together = ("category", "name")
```

✔ Название товара уникально в рамках категории
✔ Таблица БД переименована в `shop_products`

---

## 🔹 Метод total_price() в Order

```python
def total_price(self):
    return sum(item.product.price * item.quantity for item in self.items.all())
```

### Проверка в Django Shell

```python
order.total_price()
```

Результат:

```
Decimal('3198.00')
```

---

## 🔹 Работа с Django ORM (Shell)

### Создание категорий и товаров

```python
Category.objects.get_or_create(name="Телефоны")
Category.objects.get_or_create(name="Ноутбуки")
```

---

### Получить товары из категории

```python
Product.objects.filter(category__name="Телефоны")
```

Результат:

```
<QuerySet [<Product: iPhone 15>]>
```

---

### Получить все заказы пользователя

```python
Order.objects.filter(user=u)
```

---

### Получить отзывы для товара

```python
Review.objects.filter(product__name="MacBook Air M2")
```

Результат:

```
<QuerySet [<Review: Отзыв от marinadesigne@inbox.lv>, <Review: Отзыв от test@test.com>]>
```

---

### Товары с количеством на складе > 10

```python
Product.objects.filter(stock__gt=10)
```

Результат:

```
<QuerySet [<Product: iPhone 15>, <Product: MacBook Air M2>]>
```

---

## 🛒 Бонус

Реализованы модели:

* Cart
* CartItem

Миграции выполнены успешно.

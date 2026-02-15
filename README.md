# Django Shop Models (DZ Lite)

Домашнее задание по теме **Django Models и ORM**

## Реализовано

Созданы модели интернет-магазина:

- Category — категории товаров
- Product — товары
- Order — заказы пользователей
- OrderItem — товары в заказе
- Review — отзывы
- Использована встроенная модель User

## Связи между моделями

- Product → Category (ForeignKey)
- Order → User (ForeignKey)
- OrderItem → Order + Product (ForeignKey)
- Review → Product + User (ForeignKey)

## Meta классы

Использованы:
- ordering
- verbose_name
- verbose_name_plural

## Админка Django

Модели зарегистрированы в admin.py  
Добавлены:
- list_display
- list_filter
- search_fields
- Inline для OrderItem

## Работа через Django ORM (shell)

В Django shell были выполнены операции:

- создание категории
- создание товара
- получение и фильтрация товаров
- создание заказа
- добавление товара в заказ
- создание отзыва
- получение отзывов

## Запуск проекта

```bash
python manage.py migrate
python manage.py runserver

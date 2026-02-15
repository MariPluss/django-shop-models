from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, Review
from django.contrib.auth.decorators import login_required


# Главная страница магазина (список товаров + категории)
def product_list(request):
    category_id = request.GET.get("category")

    categories = Category.objects.all()

    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()

    return render(request, "shop/home.html", {
        "products": products,
        "categories": categories
    })


# Страница одного товара + отзывы + форма
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    reviews = product.reviews.all()

    # если пользователь отправил отзыв
    if request.method == "POST":
        if request.user.is_authenticated:
            rating = request.POST.get("rating")
            comment = request.POST.get("comment")

            Review.objects.create(
                product=product,
                user=request.user,
                rating=rating,
                comment=comment
            )

            return redirect("product_detail", pk=product.pk)

    return render(request, "shop/product_detail.html", {
        "product": product,
        "reviews": reviews
    })

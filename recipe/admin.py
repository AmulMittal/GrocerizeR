from django.contrib import admin
from recipe.models import Recipe, Ingredients, Cart, Category, MyCookBook,CartIngredient

admin.site.register(Recipe)
admin.site.register(Ingredients)
admin.site.register(Cart)
admin.site.register(Category)
admin.site.register(MyCookBook)
admin.site.register(CartIngredient)
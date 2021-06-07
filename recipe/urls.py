from django.urls import path
from recipe.views import index, recipe, my_cookbook, sprecipe, mycart, increment_decrement, remove_ingredient, mealplanner, search_recipe, search_recipe_ingredient

urlpatterns = [
    path('', index, name='index'),
    path('mealplanner/', mealplanner, name='mealplanner'),
    path('recipe/<int:pk>/', sprecipe, name='sprecipe'),
    # path('sprecipe_cart/<int:recipe_id>/', sprecipe_cart, name='sprecipe_cart'),
    path('recipe/<str:category_name>/', recipe, name='recipe_category'),
    path('recipe/', recipe, name='recipe'),
    path('mycookbook/<int:recipe_id>/', my_cookbook, name='my_cookbook_recipe'),
    path('mycookbook/', my_cookbook, name='my_cookbook'),
    path('cart/<int:ingredient_id>/',mycart, name='mycart_recipe'),
    path('cart/',mycart, name='mycart'),
    path('inc_dec/<int:cartingredient_id>/<str:action>/',increment_decrement, name='increment_decrement'),
    path('remove_ingredient/<int:cartingredient_id>/',remove_ingredient, name='remove_ingredient'), 
    path('search_recipe/',search_recipe, name='search_recipe'),
    path('search_recipe_ingredient/',search_recipe_ingredient, name='search_recipe_ingredient'),
     
]

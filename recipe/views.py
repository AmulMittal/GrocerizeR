from django.db.models.fields.related import create_many_to_many_intermediary_model
from django.shortcuts import render
from recipe.models import Cart, Category, Ingredients, Recipe, MyCookBook, CartIngredient
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from itertools import chain



def index(request):
    return render(request, 'index.html')

def mealplanner(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe/mealplanner.html',{'recipes': recipes})


def recipe(request, category_name=None):
    if request.method == 'GET':
        recipes = Recipe.objects.all()
        category_recipe = Category.objects.all()
        return render(request, 'recipe/recipe.html', {'recipes': recipes,'category_recipe':category_recipe})
    else:
        category = Category.objects.get(name=category_name)
        recipes = Recipe.objects.filter(category=category)
        category_recipe = Category.objects.all()
        return render(request, 'recipe/recipe.html', {'recipes': recipes,'category_recipe':category_recipe})



def sprecipe(request, pk):
    recipe_already_existed = False
    pricepergram = []
    recipe = Recipe.objects.get(id=pk)
    # recipe_exit = Cart.objects.filter(recipe=recipe)
    # if recipe_exit:
    #     recipe_already_existed = True
    for ingredient in recipe.ingredients.all():
        pricepergram.append((ingredient.price / ingredient.weight) * 100)
    ingredients = recipe.ingredients.all()
    mylist = zip ( ingredients, pricepergram )
    
    cartingredients = CartIngredient.objects.all()
    all_ingredients = []
    for carting in cartingredients:
        all_ingredients.append(carting.ingredients.id)
    
    
    return render(request, 'recipe/sprecipe.html', {'recipe': recipe , 'ingredients': mylist,'all_ingredients':all_ingredients})
    





def search_recipe(request):
    if request.method == 'POST':
        recipe_name = request.POST["recipe_name"]
        searched_recipes = Recipe.objects.filter(name__icontains=recipe_name)
        return render(request, 'recipe/recipe.html', {'recipes': searched_recipes})

def search_recipe_ingredient(request):
    if request.method == 'POST':
        recipeslist = []
        ingredient_name = request.POST["ingredient_name"]
        searched_ingredients = Ingredients.objects.filter(name__icontains=ingredient_name)
        for ing in searched_ingredients:

            recipeslist = set(chain(recipeslist,Recipe.objects.filter(ingredients = ing)))
        return render(request, 'recipe/mealplanner.html',{'recipes':recipeslist})

def my_cookbook(request, recipe_id=None):
    if request.method == 'GET':
        mycookbook = MyCookBook.objects.get(user=get_user_model().objects.get(email="lafna@gmail.com"))
        return render(request, 'recipe/mycookbook.html',{'mycookbook':mycookbook})
    else:
        recipe = Recipe.objects.get(id=recipe_id)
        mycookbook_user = MyCookBook.objects.get(user=get_user_model().objects.get(email="lafna@gmail.com"))
        mycookbook_user.recipe.add(recipe)
        mycookbook_user.save()
        return render(request, 'recipe/mycookbook.html',{'mycookbook':mycookbook_user})
        


def mycart(request, ingredient_id=None):
    if request.method == 'GET':
        totalprice = 0
        cart = Cart.objects.get(buyer=get_user_model().objects.get(email="lafna@gmail.com"))
        cartingredients = CartIngredient.objects.filter(cart=cart)
        for cartingredient in cartingredients:
            totalprice = totalprice + cartingredient.ingredients.price * cartingredient.quantity
   
        ing_count = 0
        cartingredients = CartIngredient.objects.all()
        all_ingredients = {}
        for cartingredient in cartingredients:
            ing_count += 1
            if cartingredient.ingredients in all_ingredients:
                all_ingredients[cartingredient.ingredients] += cartingredient.quantity
            else:
                all_ingredients[cartingredient.ingredients] = cartingredient.quantity
        show_remove_ing = False
        if ing_count > 1:
            show_remove_ing = True
 
        return render(request, 'recipe/cart.html',{'cartingredients':all_ingredients, 'totalprice':totalprice , 'show_remove_ing':show_remove_ing})

    else: # POST
        # recipe = Recipe.objects.get(id=recipe_id)
        cartingredient = CartIngredient()
        cart = Cart.objects.get(buyer=get_user_model().objects.get(email="lafna@gmail.com"))
        cartingredient.cart = cart
        cartingredient.ingredients = Ingredients.objects.get(id=ingredient_id)
        cartingredient.save()
        
        
        
        # cart.recipe.add(recipe)
        # for ing in recipe.ingredients.all():
        #     cartingredient = CartIngredient()
        #     cartingredient.cart = cart
        #     cartingredient.recipe = recipe
        #     cartingredient.ingredients = ing
        #     cartingredient.save()
        #     totalprice = 0
        cartingredients = CartIngredient.objects.all()
        all_ingredients = {}
        ing_count = 0
        for cartingredient in cartingredients:
            ing_count += 1
            if cartingredient.ingredients in all_ingredients:
                all_ingredients[cartingredient.ingredients] += cartingredient.quantity
            else:
                all_ingredients[cartingredient.ingredients] = cartingredient.quantity
        totalprice = 0
        
        cartingredients = CartIngredient.objects.filter(cart=cart)
        for cartingredient in cartingredients:
            totalprice = totalprice + cartingredient.ingredients.price * cartingredient.quantity
        return render(request, 'recipe/cart.html',{'carts':cart,'totalprice':totalprice,'cartingredients':all_ingredients})




def increment_decrement(request,cartingredient_id,action):
    cartingredient = CartIngredient.objects.filter(ingredients=cartingredient_id)[0]
    if action == "increment":
        cartingredient.quantity+=1
    else:
        cartingredient.quantity-=1
    cartingredient.save()

    return redirect("mycart")

def remove_ingredient(request,cartingredient_id):
    
    cartingredient = CartIngredient.objects.filter(ingredients=cartingredient_id)
    cartingredient.delete()

    return redirect("mycart")
    



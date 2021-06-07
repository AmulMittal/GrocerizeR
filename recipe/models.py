from django.db import models
from django.contrib.auth import get_user_model


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Ingredients(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    image = models.ImageField(upload_to='media/ingredient')
    price = models.FloatField()
    weight = models.FloatField()
    quantity = models.IntegerField()
    
    


    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    chef = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredients)
    image = models.ImageField(upload_to='media/recipe')
    method = models.TextField(blank=True, null=True)
    

    def __str__(self):
        return self.name

class Cart(models.Model):
    buyer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    # recipe = models.ManyToManyField(Recipe,blank=True,null=True)
    
    
    
    def __str__(self):
        return self.buyer.email

class CartIngredient(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    # recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    # ingredients = models.ManyToManyField(Ingredients)
    ingredients = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

   

class MyCookBook(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    recipe = models.ManyToManyField(Recipe, blank=True,null=True)

    










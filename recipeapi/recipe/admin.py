from django.contrib import admin
from recipe.models import Recipe
from recipe.models import Review
admin.site.register(Recipe)
admin.site.register(Review)
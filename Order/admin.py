from django.contrib import admin

from .models import *

admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Sub)
admin.site.register(Extra)
admin.site.register(SubWithExtra)
admin.site.register(Pasta)
admin.site.register(Serving)
admin.site.register(PastaWithServing)
admin.site.register(ExtraCheese)
admin.site.register(Salad)
admin.site.register(DinnerPlatter)
admin.site.register(UserInfo)
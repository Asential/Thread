from django.contrib import admin
from vanshaj.models import User, Individual

class IndividualAdmin(admin.ModelAdmin):
    filter_horizontal = ("children",)


# Register your models here.
admin.site.register(User)
admin.site.register(Individual, IndividualAdmin)

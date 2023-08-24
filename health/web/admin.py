from django.contrib import admin
from .models import Exercises

class ExercisesAdmin(admin.ModelAdmin):
    # list_display = ["id_name", "name_ko", "name_en", "dir", "part"]
    search_fields = ["name_ko"]

admin.site.register(Exercises, ExercisesAdmin)

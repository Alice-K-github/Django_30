from django.contrib import admin
from school.models import Kurs, Lesson


@admin.register(Kurs)
class KursAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "description",
        "preview",
    )


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "description",
        "preview",
        "video",
    )

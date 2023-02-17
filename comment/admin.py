from django.contrib import admin

# Register your models here.
from comment.models import Comment

@admin.register(Comment)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('text', 'date_posted')
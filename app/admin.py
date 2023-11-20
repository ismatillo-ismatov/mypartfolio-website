from django.contrib import admin
from .models import Post,Tag,Profile,Comment
# Register your models here.
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Tag)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','headline','image','body','created')

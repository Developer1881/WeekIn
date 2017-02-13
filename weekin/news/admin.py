from django.contrib import admin
from .models import Post, SubPost




class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish',
        'status', 'week_end')
    list_filter = ('status', 'created', 'publish', 'author', 'week_end')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'week_end'
    ordering = ['status', 'publish']


admin.site.register(Post, PostAdmin)

class SubPostAdmin(admin.ModelAdmin):
    list_display = ('headline', 'post', 'get_week_end')
    list_filter = ('post__week_end', 'post', 'post__author',)
    search_fields = ('headline', 'post__week_end',)
    ordering = ['-post__week_end', 'post']

admin.site.register(SubPost, SubPostAdmin)




# Register your models here.

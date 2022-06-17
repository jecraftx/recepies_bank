from django.contrib import admin
from app_student.models import IceCream, IceCreamCategory, IceCreamRating, IceCreamComment, IceCreamIngredient


class IceCreamAdmin(admin.ModelAdmin):
    """
    Настройки отображения, фильтрации и поиска модели:'Receipt' на панели администратора
    """

    list_display = (  # поля для отображения
        'title',
        'image',
        'description',
        'author',
        'time_to_cook',
    )
    filter_horizontal = ('ingredients', 'category',)  # только для полей формата many_to_many_field
    list_display_links = (  # поля-ссылка
        'title',
        'description',
    )
    list_editable = (  # поля для редактирования объекта на лету
        'author',
        'time_to_cook',
    )
    list_filter = (  # поля для фильтрации
        'title',
        'image',
        'description',
        'author',
        'time_to_cook',
    )
    fieldsets = (  # подзаголовки для визуального отделения блоков друг от друга
        ('Main', {'fields': (
            'title',
            'description',
            'ingredients',
        )}),
        ('Extra', {'fields': (
            'image',
            'category',
            'time_to_cook',
        )}),
        ('Helper', {'fields': (
            'author',
        )}),
    )
    search_fields = [  # поле для поиска
        'title',
        'image',
        'description',
        'author',
    ]

class IceCreamCategoryAdmin(admin.ModelAdmin):
    """
    Настройки отображения, фильтрации и поиска модели:'IceCreamCategory' на панели администратора
    """

    list_display = (  # поля для отображения
        'title',
    )
    list_display_links = (  # поля-ссылка
        'title',
    )
    list_editable = (  # поля для редактирования объекта на лету
    )
    list_filter = (  # поля для редактирования объекта на лету
        'title',
    )
    fieldsets = (  # подзаголовки для визуального отделения блоков друг от друга
        ('Main', {'fields': (
            'title',
        )}),
    )
    search_fields = [  # поле для поиска
        'title',
    ]

class IceCreamIngredientAdmin(admin.ModelAdmin):
    """
    Настройки отображения, фильтрации и поиска модели:'IceCreamIngredient' на панели администратора
    """
    list_display = (  # поля для отображения
        'name',
    )
    list_display_links = (  # поля-ссылка
        'name',
    )
    list_editable = (  # поля для редактирования объекта на лету
    )
    list_filter = (  # поля для редактирования объекта на лету
        'name',
    )
    fieldsets = (  # подзаголовки для визуального отделения блоков друг от друга
        ('Main', {'fields': (
            'name',
        )}),
    )
    search_fields = [  # поле для поиска
        'name',
    ]

class IceCreamCommentAdmin(admin.ModelAdmin):
    """
    Настройки отображения, фильтрации и поиска модели:'IceCreamIngredient' на панели администратора
    """

    list_display = (  # поля для отображения
        'comment_text',
        'user',
        'IceCream',
    )
    list_display_links = (  # поля-ссылка
        'comment_text',
    )
    list_editable = (  # поля для редактирования объекта на лету
    )
    list_filter = (  # поля для редактирования объекта на лету
        'comment_text',
        'user',
        'IceCream',
    )
    fieldsets = (  # подзаголовки для визуального отделения блоков друг от друга
        ('Основное', {'fields': (
            'comment_text',
            'user',
            'IceCream',
        )}),
    )
    search_fields = [  # поле для поиска
        'comment_text',
        'user',
        'IceCream',
    ]

class IceCreamRatingAdmin(admin.ModelAdmin):
    """
    Настройки отображения, фильтрации и поиска модели:'IceCreamIngredient' на панели администратора
    """

    list_display = (  # поля для отображения
        'is_liked',
        'rating_value',
        'user',
        'IceCream',
    )
    list_display_links = (  # поля-ссылка
        'is_liked',
    )
    list_editable = (  # поля для редактирования объекта на лету
        'is_liked',
    )
    list_filter = (  # поля для редактирования объекта на лету
        'is_liked',
        'rating_value',
        'user',
        'IceCream',
    )
    fieldsets = (  # подзаголовки для визуального отделения блоков друг от друга
        ('Основное', {'fields': (
            'is_liked',
            'rating_value',
            'user',
            'IceCream',
        )}),
    )
    search_fields = [  # поле для поиска
        'is_liked',
        'rating_value',
        'user',
        'IceCream',
    ]


admin.site.register(IceCreamCategory, IceCreamCategoryAdmin)
admin.site.register(IceCreamIngredient, IceCreamIngredientAdmin)
admin.site.register(IceCream, IceCreamAdmin)
admin.site.register(IceCreamRating)
admin.site.register(IceCreamComment, IceCreamCommentAdmin)
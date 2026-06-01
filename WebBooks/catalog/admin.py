from django.contrib import admin

# Register your models here.
from .models import Author,Book,Genre,Language,Status,BookInstance,Lecturer,Course,Student,Group

#admin.site.register(Author)
#admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Status)
#admin.site.register(BookInstance)
admin.site.register(Lecturer)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Group)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name','first_name')
    fields= (('first_name','last_name'),
             ('date_of_birth','date_of_death'))
admin.site.register(Author,AuthorAdmin)

class BookInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','genre','language','display_author')
    list_filter = ('genre','author')
    inlines = [BookInstanceInline]
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('book', 'status')
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    fieldsets = [
        ('Book', {
            'fields': ('book', 'imprint', 'inv_nom')
        }),
        ('Status', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    ]
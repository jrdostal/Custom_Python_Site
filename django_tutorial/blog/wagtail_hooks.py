import wagtail_modeladmin.options
from .models import BlogPage


class BlogPage_Admin(wagtail_modeladmin.options.ModelAdmin):
    model = BlogPage()
    menu_icon = 'pilcrow'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    list_display = ("author", "date", "intro", "text")
    list_filter = ("author", "date", "intro", "text")
    search_fields = ("author", "date", "intro", "text")

# Now you just need to register your customised ModelAdmin class with Wagtail
wagtail_modeladmin.options.modeladmin_register(BlogPage_Admin)
from django.contrib import admin
from .models import Category, Discovery, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # Shows category names clearly in the admin list.
    list_display = ('name',)

    # Helps us quickly find categories later.
    search_fields = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    # Shows tag names clearly in the admin list.
    list_display = ('name',)

    # Helps us quickly find reusable tags.
    search_fields = ('name',)


@admin.register(Discovery)
class DiscoveryAdmin(admin.ModelAdmin):
    # Shows the most useful discovery info at a glance.
    list_display = ('title', 'category', 'location', 'date_seen', 'user')

    # Helps us filter discoveries by category and date.
    list_filter = ('category', 'date_seen', 'tags')

    # Lets us edit tags from the discovery admin page.
    filter_horizontal = ('tags',)

    # Helps us search discoveries by meaningful content.
    search_fields = ('title', 'location', 'description')


# Gives Django admin a TrailTales-branded identity.
admin.site.site_header = 'TrailTales Admin'
admin.site.site_title = 'TrailTales Admin'
admin.site.index_title = 'Manage TrailTales'

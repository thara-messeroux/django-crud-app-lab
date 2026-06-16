from django.contrib import admin
from .models import Category, Discovery, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # Shows category names clearly in the admin list.
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    # Shows tag names clearly in the admin list.
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Discovery)
class DiscoveryAdmin(admin.ModelAdmin):
    # Shows the most useful discovery info at a glance.
    list_display = ('title', 'category', 'tag_list', 'location', 'date_seen', 'user')

    # Helps us filter discoveries by category, tags, and date.
    list_filter = ('category', 'tags', 'date_seen')

    # Lets us edit tags from the discovery admin page.
    filter_horizontal = ('tags',)

    # Helps us search discoveries by meaningful content.
    search_fields = ('title', 'location', 'description')

    def tag_list(self, obj):
        # Shows many-to-many tags as readable text in the admin list.
        return ', '.join(tag.name for tag in obj.tags.all())

    tag_list.short_description = 'Tags'


# Gives Django admin a TrailTales-branded identity.
admin.site.site_header = 'TrailTales Admin'
admin.site.site_title = 'TrailTales Admin'
admin.site.index_title = 'Manage TrailTales'

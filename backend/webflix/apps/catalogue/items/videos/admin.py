from django.contrib import admin
from .models import VideoAllProxy, VideoPublishedProxy


# Register your models here.


class VideoAllAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'state', 'embed_id', 'is_published']
    search_fields = ['title', 'description']
    list_filter = ['state', 'active']
    readonly_fields = ['id', 'slug', 'is_published', 'publish_timestamp']

    class Meta:
        model = VideoAllProxy


admin.site.register(VideoAllProxy, VideoAllAdmin)


class VideoPublishedProxyAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'embed_id']
    search_fields = ['title', 'description']
    readonly_fields = ['id', 'slug', 'is_published', 'publish_timestamp']

    class Meta:
        model = VideoPublishedProxy

    def get_queryset(self, request):
        return VideoAllProxy.objects.filter(active=True)


admin.site.register(VideoPublishedProxy, VideoPublishedProxyAdmin)

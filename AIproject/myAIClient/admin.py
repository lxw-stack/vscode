from django.contrib import admin
from myAIClient.models import NeedFiles, Contents

@admin.register(NeedFiles)
class NeedFilesAdmin(admin.ModelAdmin):
    list_display = ('project', 'requirement_doc', 'version')
    search_fields = ('project', 'requirement_doc')

@admin.register(Contents)
class ContentsAdmin(admin.ModelAdmin):
    list_display = ('title', 'needfile')
    list_filter = ('needfile',)
    raw_id_fields = ('needfile',)
from django.contrib import admin
from .models import Profile, Project, ProjectAttachment

class ProjectAttachmentInline(admin.TabularInline):
    model = ProjectAttachment
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'profile', 'is_visible', 'order')
    list_filter = ('is_visible',)
    inlines = [ProjectAttachmentInline]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(profile__user=request.user)

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        if not request.user.is_superuser:
            # Hide profile field for non-superusers, we'll set it automatically
            if 'profile' in fields:
                fields.remove('profile')
        return fields

    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            # Force the project to belong to the user's profile
            if not hasattr(obj, 'profile'):
                obj.profile = request.user.portfolio_profile
        super().save_model(request, obj, form, change)

    def has_add_permission(self, request):
        # Only allow adding if the user has a profile
        if request.user.is_superuser:
            return True
        return hasattr(request.user, 'portfolio_profile')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'slug')
    prepopulated_fields = {'slug': ('name',)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def get_fields(self, request, obj=None):
        fields = list(super().get_fields(request, obj))
        if not request.user.is_superuser:
            if 'user' in fields:
                fields.remove('user')
        return fields

    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            obj.user = request.user
        super().save_model(request, obj, form, change)

    def has_add_permission(self, request):
        # If superuser, can add profiles. 
        # If normal staff, can only add if they don't have one already.
        if request.user.is_superuser:
            return True
        return not hasattr(request.user, 'portfolio_profile')

    def has_delete_permission(self, request, obj=None):
        # Prevent non-superusers from deleting their own profile
        return request.user.is_superuser

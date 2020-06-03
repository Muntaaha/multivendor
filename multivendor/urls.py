from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from store.views import user_login, user_logout, user_register, user_profile, updateItem

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('login/', user_login, name='login'),
    path('register/', user_register, name='register'),
    path('logout/', user_logout, name='logout'),
    path('user/', user_profile, name='user_profile'),

	path('update_item/', updateItem, name="update_item")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
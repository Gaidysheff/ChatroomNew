from django.contrib import admin
from django.urls import path, include
from chat.views import index, chatPage


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('', index, name='home'),
    path('chat/', chatPage, name='chat'),
]

# '<str:username>/'

from django.contrib import admin
from django.urls import path,include
# from django.conf import settings
# from django.conf.urls.static import static
from django.views.i18n import JavaScriptCatalog

urlpatterns = [
    path('',include('orientacao.urls')),
    path('task/',include('tasks.urls'), name = 'task'),
    path('encontros/',include('encontros.urls')),
    path('jsi18n', JavaScriptCatalog.as_view, name = 'js-catalog'),
    path('admin/', admin.site.urls),
]

#if settings.DEBUG:
	#urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


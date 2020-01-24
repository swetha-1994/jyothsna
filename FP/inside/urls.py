from django.urls import path,include
from inside import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name= "index"),
    path('profile/', views.profiles, name="profile"),
    path('step1/', views.step1, name= "step1"),
    path('vp/<int:id>/',views.viewpro, name= "viewprofile"),
    path('sv/', views.save, name='save'),
    path('edit/<int:id>/', views.edit, name= "editor"),
    path('del/<int:id>/', views.delete, name= "del"),
    path('register/',views.register,name="register"),
    path('logout/',views.logout,name='log'),
    path('login/',views.login,name='login'),
    path('auth/', include('social_django.urls', namespace='social')),
    ] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
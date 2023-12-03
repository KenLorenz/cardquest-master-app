from django.urls import path
from cardquest.views import HomePageView, TrainerList
from cardquest import views

urlpatterns = [
        path('admin/', admin.site.urls),
        path('', views.HomePageView.as_view(), name='base'),
        path('trainer_list/', TrainerList.as_view(), name='trainer-list'),
        ]

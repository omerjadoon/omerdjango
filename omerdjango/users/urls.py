from django.urls import path

from .views import fruit_data_api, user_detail_view
from .views import user_redirect_view
from .views import user_update_view
from .views import chart_view
from .views import chart_data_api

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
    path("chart/", view=chart_view, name="chart_view"),
    path("api/chart-data/", view=chart_data_api, name="chart_data_api"),
    path('api/fruits/', fruit_data_api, name='fruit_data_api'),
]
import random
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import QuerySet
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView
from django.views.generic import RedirectView
from django.views.generic import UpdateView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import DataPoint

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import DataPoint
from .serializers import DataPointSerializer, FruitSerializer

from omerdjango.users.models import User
from .models import Fruit

from django.http import JsonResponse

class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    fields = ["name"]
    success_message = _("Information successfully updated")

    def get_success_url(self) -> str:
        assert self.request.user.is_authenticated  # type guard
        return self.request.user.get_absolute_url()

    def get_object(self, queryset: QuerySet | None=None) -> User:
        assert self.request.user.is_authenticated  # type guard
        return self.request.user


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self) -> str:
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()



@login_required
def chart_view(request):
    # Fetch data from the database
    fruits = Fruit.objects.all()
    xdata = [fruit.name for fruit in fruits]
    ydata = [fruit.calories for fruit in fruits]
    chart_data = [{"label": name, "value": calories} for name, calories in zip(xdata, ydata)]
    
    # Chart configuration
    charttype = "pieChart"
    chartcontainer = "piechart_container"
    data = {
        "charttype": charttype,
        "chartdata": {
            "x": xdata,
            "y": ydata
        },
        "chartcontainer": chartcontainer,
        "extra": {
            "x_is_date": False,
            "x_axis_format": "",
            "tag_script_js": True,
            "jquery_on_ready": True,
        },
    }
    
    return render(request, "chart.html", data)



@api_view(["GET"])
@permission_classes([IsAuthenticated])
def chart_data_api(request):
    data = DataPoint.objects.all()
    serializer = DataPointSerializer(data, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def fruit_data_api(request):
    # Fetch all fruit records
    fruits = Fruit.objects.all()
    # Serialize the data
    serializer = FruitSerializer(fruits, many=True)
    # Return the serialized data
    return Response(serializer.data)


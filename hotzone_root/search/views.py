from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Address
import json, requests


# Create your views here.
class ViewSearchBox(ListView):
    model = Address
    template_name = "searchPage.html"


class ConfirmResultPage(TemplateView):
    template_name = "resultPage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        address = self.request.GET.get('add')
        url = "https://geodata.gov.hk/gs/api/v1.0.0/locationSearch?q=" + address
        response_obj = requests.get(url)

        context['successful'] = 'true'
        if (response_obj.status_code == 200):
            response = json.loads(response_obj.text)
            address_obj = Address()
            context["zhname"] = response[0]["nameZH"]
            address_obj.nameZH = response[0]["nameZH"]
            address_obj.nameEN = response[0]["nameEN"]
            address_obj.addressZH = response[0]["addressZH"]
            address_obj.addressEN = response[0]["addressEN"]
            address_obj.x = response[0]["x"]
            address_obj.y = response[0]["y"]
            context["addresszh"] = address_obj.addressZH
            context["addressen"] = address_obj.addressEN
            context["namezh"] = address_obj.nameZH
            context["nameen"] = address_obj.nameEN
            context["x"] = address_obj.x
            context["y"] = address_obj.y
            address_obj.save()
            context['pk'] = address_obj.pk
        else:
            context['successful'] = 'false'
            context['code'] = int(response_obj.status_code)
            input_address = address
            if input_address=="":
                input_address = "nothing entered"
            context['address_input'] = input_address

        return context


class CancelInput(TemplateView):
    template_name = 'addCancel.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        apk = self.request.GET.get('key')
        try:
            address = Address.objects.get(pk=apk)
            address.delete()
            context['status'] = 'Successful'
        except:
            context['status'] = "Record don't exist"
        return context

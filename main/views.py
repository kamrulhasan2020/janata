from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from django.views.generic import TemplateView
from .load_data import load
from .serializers import TradeSerializer
from .models import Trade, TradeCode
from django.http import HttpResponse
from django.http import JsonResponse


def load_data_from_csv(request):
    status = load()
    context = {"status": status}
    return render(request, "main/load.html", context)


class LatestEntry(generics.RetrieveAPIView):
    serializer_class = TradeSerializer

    def get_object(self):
        return Trade.objects.latest()


class Trades(generics.ListCreateAPIView):
    serializer_class = TradeSerializer

    def get_queryset(self):
        code = self.kwargs['code']
        return Trade.objects.filter(trade_code=code).order_by('-date')


class HomeView(TemplateView):
    template_name = "main/main-home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["trade_codes"] = TradeCode.objects.all()
        return context


def update(request):
    pk = request.POST["pk"]
    attr = request.POST["attr"]
    val = request.POST["val"]
    obj = get_object_or_404(Trade, pk=pk)
    setattr(obj, attr, val)
    obj.save()
    return HttpResponse(200)


def delete(request):
    pk = request.POST["pk"]
    obj = get_object_or_404(Trade, pk=pk)
    obj.delete()
    return HttpResponse(200)


def chart(request):
    labels = []
    data = []
    data2 = []
    trade_code = request.POST["trade_code"]
    trades = Trade.objects.filter(trade_code=trade_code).order_by("date")
    for entry in trades:
        labels.append(entry.date)
        data.append(entry.close)
        data2.append(entry.volume)
    return JsonResponse(
        data={
            "labels": labels,
            "data": data,
            "data2": data2,
        }
    )




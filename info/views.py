from django.shortcuts import render, redirect, reverse
from .models import *
from django.views.generic import TemplateView, ListView, DeleteView, CreateView, UpdateView, DetailView
from django.http import HttpResponse
from .forms import OperatorModelForm


# Create your views here.

class LandingPageView(TemplateView):
	template_name = TemplateView()







def landing_page(request):
    return render(request, 'landing.html')


def antennas_list(request):
    antennas = Antenna.objects.all()
    context = {
        'antennas': antennas,
    }
    return render(request, 'info/antennas_list.html', context=context)


class OperatorsListView(ListView):
	template_name = "info/operators_list.html"
	queryset = Operator.objects.all()
	context_object_name = 'operators'


# # Операторы
# def operators(request):
#     operators = Operator.objects.all()
#     context = {
#         'operators': operators,
#     }
#     return render(request, 'info/operators_list.html', context=context)

class OperatorsDetailView(DetailView):
	template_name = "info/operators_details.html"
	queryset = Operator.objects.all()
	context_object_name = 'operator'


# def operator_details(request, pk):
#     operator = Operator.objects.get(id=pk)
#     context = {
#         'operator': operator,
#     }
#     return render(request, 'info/operators_details.html', context=context)

class OperatorsCreateView(CreateView):
	template_name = "info/operator_create.html"
	form_class = OperatorModelForm

	def get_success_url(self):
		# return redirect('/main_info/operators')
		return reverse("info:operators_list")



# def operator_create(request):
#     form = OperatorModelForm()
#     if request.method == 'POST':
#         print(request.POST)
#         form = OperatorModelForm(request.POST)
#         if form.is_valid():
#             # Если в файле forms.py указана ссылка на модель Operator, то можно просто form.save() без других указаний багодаря OperatorModelForm
#             form.save()
#             print('Создан новый оператор')
#             return redirect('/main_info/operators')
#     context = {
#         'form': form,
#     }
#     return render(request, 'info/operator_create.html', context=context)


class OperatorsUpdateView(UpdateView):
	template_name = "info/operators_update.html"
	queryset = Operator.objects.all()
	form_class = OperatorModelForm

	def get_success_url(self):
		# return redirect('/main_info/operators')
		return reverse("info:operators_list")


# def operator_update(request, pk):
#     operator = Operator.objects.get(id=pk)
#     #instance=operator говорит о том, что надо обновить багодаря OperatorModelForm
#     form = OperatorModelForm(instance=operator)
#     if request.method == 'POST':
#         print(request.POST)
#         form = OperatorModelForm(request.POST, instance=operator)
#         if form.is_valid():
#             # Если в файле forms.py указана ссылка на модель Operator, то можно просто form.save() без других указаний
#             form.save()
#             print('Создан новый оператор')
#             return redirect('../')
#     context = {
#         'form': form,
#         'operator': operator,
#     }

#     return render(request, 'info/operators_update.html', context=context)

class OperatorsDeleteView(DeleteView):
	template_name = "info/operator_delete.html"
	queryset = Operator.objects.all()


	def get_success_url(self):
		# return redirect('/main_info/operators')
		return reverse("info:operators_list")


# def operator_delete(request, pk):
#     operator = Operator.objects.get(id=pk)
#     operator.delete()
#     return redirect('/main_info/operators')
# def operator_create(request):
#     form = OperatorModelForm()
#     if request.method == 'POST':
#         print(request.POST)
#         form = OperatorModelForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             fullname = form.cleaned_data['fullname']
#             login = form.cleaned_data['login']
#             password = form.cleaned_data['password']
#             nds = form.cleaned_data['nds']
#             proc = form.cleaned_data['proc']
#             Operator.objects.create(
#                 fullname=fullname,
#                 login=login,
#                 password=password,
#                 nds=nds,
#                 proc=proc,
#             )
#             print('Создан новый оператор')
#             return redirect('/operators')
#     context = {
#         'form': form,
#     }
#     return render(request, 'info/operator_create.html', context=context)

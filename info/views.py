from django.shortcuts import render, redirect, reverse
from .models import *
from django.views.generic import TemplateView, ListView, DeleteView, CreateView, UpdateView, DetailView
from django.http import HttpResponse
from .forms import OperatorModelForm, CustomUserCreationForm
from django.views import generic
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
#! Создание квхода/выхода
class SignupView(generic.CreateView):
	template_name = 'registration/signup.html'
	form_class = CustomUserCreationForm

	def get_success_url(self):
			# return redirect('/main_info/operators')
			return reverse("login")



#! Создание главной страницы
class LandingPageView(generic.TemplateView):
	template_name = 'landing.html'


def landing_page(request):
    return render(request, 'landing.html')


def antennas_list(request):
    antennas = Antenna.objects.all()
    context = {
        'antennas': antennas,
    }
    return render(request, 'info/antennas_list.html', context=context)

#! Создание всего по ОПЕРАТОРАМ
class OperatorsListView(LoginRequiredMixin, generic.ListView):
	template_name = "info/operators/operators_list.html"
	queryset = Operator.objects.all()
	context_object_name = 'operators'


# # Операторы
# def operators(request):
#     operators = Operator.objects.all()
#     context = {
#         'operators': operators,
#     }
#     return render(request, 'info/operators_list.html', context=context)

class OperatorsDetailView(LoginRequiredMixin, generic.DetailView):
	template_name = "info/operators/operators_details.html"
	queryset = Operator.objects.all()
	context_object_name = 'operator'


# def operator_details(request, pk):
#     operator = Operator.objects.get(id=pk)
#     context = {
#         'operator': operator,
#     }
#     return render(request, 'info/operators_details.html', context=context)

class OperatorsCreateView(LoginRequiredMixin, generic.CreateView):
	template_name = "info/operators/operator_create.html"
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


class OperatorsUpdateView(LoginRequiredMixin, generic.UpdateView):
	template_name = "info/operators/operators_update.html"
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

class OperatorsDeleteView(LoginRequiredMixin, generic.DeleteView):
	template_name = "info/operators/operator_delete.html"
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


#! Создание классов для всех партнеров

class PartnersView(LoginRequiredMixin, generic.ListView):
	template_name = "info/partners/partners_list.html"
	queryset = Operator.objects.all()
	context_object_name = 'partners'

	def get_queryset(self):
		return Partner.objects.all()
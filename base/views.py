from django.shortcuts import render
from django.http import HttpResponseRedirect
from base.models import tbTodo
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here. 

class tbTodoListView(LoginRequiredMixin, ListView):
    model = tbTodo
    template_name = "task.html"
    context_object_name = 'data'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["data"] = context['data'].filter(tdUser=self.request.user)
        context['data'] = context['data'].filter(tdStatus = False)
        context['data'] = context['data'].filter(tdIsDeleted = False)
        return context
    

class tbTodoDetailView(LoginRequiredMixin, DetailView):
    model = tbTodo
    template_name = "detail.html"
    context_object_name = 'data'


class tbTodoCreateView(LoginRequiredMixin, CreateView):
    model = tbTodo
    template_name = "create.html"
    context_object_name = 'data'
    # define fields for the form
    fields = ['tdName','tdDes', 'tdStatus']
    success_url = reverse_lazy('task')

    def form_valid(self, form):
        form.instance.tdUser = self.request.user
        return super(tbTodoCreateView, self).form_valid(form)
    

    
class tbTodoUpdateView(LoginRequiredMixin, UpdateView):
    model = tbTodo
    template_name = "update.html"
    fields = '__all__'
    success_url = reverse_lazy('task')


# Delete Method
def tbTodoDeleteView(request, delId):
    data= {}
    data = tbTodo.objects.all().filter(id= delId)
    data={
        'data':data
    }

    if request.method == 'POST':
        but_val = request.POST.get('delete')
        if but_val == 'Delete':
            model = tbTodo.objects.get(id = delId)
            model.tdIsDeleted = True
            model.save()
            return render(request, 'task.html', data)
    return render(request, 'delete.html', data)

    

# code of logins 

class LoginView(LoginView):
    template_name = "login.html"
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('task')

def logouts(request):
    logout(request)
    return HttpResponseRedirect('/login/')




# Extra Methods 
# method for show deleted tasks

# show all completed tasks to user 
class completdTaskShow(ListView):
    model = tbTodo
    template_name = 'deleted.html'
    context_object_name = 'data'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["data"] = context["data"].filter(tdStatus=True) 
        context['data'] = context['data'].filter(tdIsDeleted = False)
        context["data"] = context["data"].filter(tdUser = self.request.user)
        return context
    

class DeletedTaskShow(ListView):
    model = tbTodo
    template_name = "deleted.html"
    context_object_name = 'data'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["data"] = context["data"].filter(tdUser = self.request.user)
        context["data"] = context["data"].filter(tdIsDeleted=True) 
        return context

        
    

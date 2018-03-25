

from rest_framework import viewsets, generics
from django.views import generic
from django.views.generic import View

from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import View
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView


from .forms import UserForm,JobForm,LoginForm
from django.contrib.auth.models import Permission,User
#for update
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.core.urlresolvers import reverse_lazy, reverse
from .models import Job,JobFinal
from .forms import JobFormFinal,JobFormFinalUpdate
##for user
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login


from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .permissions import IsAdminOrReadOnly

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from JobSchd.models import JobFinal
from JobSchd.serializers import JobSerializer, UserSerializer


#########################################

#### Rest API


#########################################
class JobFinalList(generics.ListCreateAPIView):
    queryset = JobFinal.objects.all()
    serializer_class = JobSerializer
    ##permission_classes = (IsAdminOrReadOnly,)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class JobFinalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobFinal.objects.all()
    serializer_class = JobSerializer
    ##permission_classes = (IsAdminOrReadOnly, )

#########################################
#########################################











class UserJob(generic.ListView):
    model = JobFinal
    paginate_by = 10

    template_name = 'JobSchd/Details.html'
    def get_queryset(self):
        user=self.request.user
        return user

class JobFinalCreate(CreateView):
    model = JobFinal
    #fields = '__all__'
    form_class = JobFormFinal
    #success_url = reverse_lazy('user_jobs')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(JobFinalCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('JobSchd:user_details',kwargs={'pk': self.request.user.id})


class JobFinalUpdate(UpdateView):
    model = JobFinal
    form_class = JobFormFinalUpdate
    def get_success_url(self):
        return reverse('JobSchd:user_details',kwargs={'pk': self.request.user.id})

class JobFinalDelete(DeleteView):
    model = JobFinal
    form_class = JobFormFinal

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(JobFinalCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('JobSchd:user_details',kwargs={'pk': self.request.user.id})

class DetailsView(generic.DetailView):
    model = User
    template_name = 'JobSchd/Details.html'

class UserCreate(CreateView):
    model = User
    fields = ['username','email','password','first_name','last_name']


class IndexView(generic.ListView):
    template_name = 'JobSchd/index.html'

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(username=user)

def team(request):
    return render(
        request,
        'JobSchd/team.html',
    )



class UserFormView(View):
    form_class=UserForm
    template_name='JobSchd/registration_form.html'

    #display blank form
    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})

    # process form data
    def post(self,request):
        form=self.form_class(request.POST)

        if form.is_valid():

            user=form.save(commit=False)
            # clean ,normalize the data
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # return User Objects if cred are correct

            user=authenticate(username=username,password=password)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('JobSchd:index')

        return render(request,self.template_name,{'form':form})






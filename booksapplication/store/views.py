from django.shortcuts import render,redirect
from django.views.generic import View
from store.forms import BooksCreateForm,BooksUpdateForm
from store.models import Books

# Create your views here.

class BooksCreateView(View):
    def get(self,request,*args,**kwargs):
        form=BooksCreateForm()
        return render(request,"books_add.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=BooksCreateForm(request.POST)
        if form.is_valid():
            Books.objects.create(**form.cleaned_data)
            return render(request,"books_add.html",{"form":form})
        else:
            return render(request,"books_add.html",{"form":form})
        
class BooksListView(View):
    def get(self,request,*args,**kwargs):
        # qs=Books.objects.all()
        qs=Books.objects.filter(price__gte=400,price__lte=500)
        return render(request,"books_list.html",{"books":qs})
    

class BookDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Books.objects.get(id=id)
        return render(request,"books_detail.html",{"book":qs})
    

class BookDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Books.objects.filter(id=id).delete()
        return redirect("books-list")


class BookUpdateView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Books.objects.get(id=id)
        form=BooksUpdateForm(instance=obj)
        return render(request,"books_edit.html",{'form':form})

    


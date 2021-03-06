from django.shortcuts import render, redirect

from lists.models import Item, List


def home_page(request):
    return render(request, 'lists/home.html')


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    items = Item.objects.filter(list=list_)
    return render(request, 'lists/list.html', {'list': list_})


def new_list(request):
    if request.method == 'POST':
        list_ = List.objects.create()
        new_item_text = request.POST['item_text']
        Item.objects.create(text=new_item_text, list=list_)
        return redirect('/lists/%d/' % list_.id)

    return redirect('/')


def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/%d/' % list_.id)

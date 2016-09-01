from django.core.urlresolvers import reverse
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from form import MenuCard, HotelDetails

from .models import Hotel, Menu
from django.http import HttpResponse


# Create your views here.

#
# def index(request):
#     return render(request, 'hotel/index.html')

# def login(request):
#     username = "not logged in"
#
#     if request.method == "POST":
#         # Get the posted form
#         MyLoginForm = LoginForm(request.POST)
#
#         if MyLoginForm.is_valid():
#             username = MyLoginForm.cleaned_data['username']
#     else:
#         MyLoginForm = Loginform()
#
#     return render(request, 'loggedin.html', {"username": username})
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)


def index(request):
    return render(request, 'hotel/index.html')
    # return render(request, 'hotel/index.html')


def menu_details(request):
    if request.method == 'GET':
        form1 = HotelDetails()
        form2 = MenuCard()

    else:
        form1 = HotelDetails(request.POST)
        form2 = MenuCard(request.POST)
        if form1.is_valid() & form2.is_valid():
            import ipdb;ipdb.set_trace()
            hotel_name = form1.cleaned_data['hotel_name']
            opening_time = form1.cleaned_data['opening_time']
            closing_time = form1.cleaned_data['closing_time']
            item_one = form2.cleaned_data['item_one']
            item_two = form2.cleaned_data['item_two']
            hotl_obj = Hotel.objects.create(hotel_name=hotel_name, opening_time=opening_time, closing_time=closing_time)
            Menu.objects.create(hotel=hotl_obj,item_one=item_one, item_two=item_two)
            return HttpResponseRedirect(reverse('view'))

    return render(request, 'hotel/menu_details.html', {'form1': form1, 'form2': form2})


def view_hotel(request):
    if request.method == 'GET':
        context = {'hotels_list': Hotel.objects.all()}
        return render(request, 'hotel/view.html', context)


def detail(request,hotel_id):
    import ipdb; ipdb.set_trace()
    get_object_or_404(Hotel, pk=hotel_id)
    get_object_or_404(Menu, hotel=hotel_id)
    # name = Hotel.objects.get(pk = hotel_id)
    context = {'hotel_details': Hotel.objects.get(pk = hotel_id), 'menu': Menu.objects.get(pk = hotel_id)}
    return render(request, 'hotel/detail.html', context)
    # return HttpResponse("You're looking for %s." %name.hotel_name)
    # try:
    #     Hotel.objects.get(pk=1)
    # except Hotel.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return HttpResponse("No Error")


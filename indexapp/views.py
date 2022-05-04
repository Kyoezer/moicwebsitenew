from django.shortcuts import redirect, render
from django.views.generic import DetailView
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from indexapp.models import post, event, vacancie, tender, IpModel
from django.core.mail import send_mail, BadHeaderError
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    popuplarPs = post.objects.all()
    events = event.objects.all().order_by('-id')
    # Events Pagination
    p = Paginator(event.objects.all(), 3)
    page = request.GET.get('page')
    events = p.get_page(page)

    vacancies = vacancie.objects.all().order_by('-id')
    # Vacancy Pagination
    # p1 = Paginator(vacancie.objects.all(), 1)
    # page = request.GET.get('page')
    # vacancies = p1.get_page(page)

    tenders = tender.objects.all().order_by('-id')
    # Tender Pagination
    # p3 = Paginator(tender.objects.all(), 1)
    # page = request.GET.get('page')
    # tenders = p3.get_page(page)

    #add when the pagination works
    # 'vacancy': vacancies, 'tender': tenders

    return render(request, 'home.html', {'post': popuplarPs, 'events': events, 'vacancies': vacancies, 'tenders': tenders, 'event': events})


def vacancy_detail(request, id):
    obj =get_object_or_404(vacancie, pk=id)
    return render(request, 'vacancy_detail.html', {'obj': obj})


def tender_detail(request, id):
    obj =get_object_or_404(tender, pk=id)
    return render(request, 'tender_detail.html', {'obj': obj})


def detail(request, id):
    print(id)
    obj =get_object_or_404(event, pk=id)
    return render(request, 'detail.html', {'obj': obj})

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class PostDetailView(DetailView):
    model = event
    context_object_name = 'obj'
    # context_object_name = 'post'
    template_name = 'detail.html'
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        ip = get_client_ip(self.request)

        if IpModel.objects.filter(ip=ip).exists():
            event_id = request.GET.get('event-id')
            Event = event.objects.get(pk=event_id)
            Event.views.add(IpModel.objects.get(ip=ip))
        else:
            IpModel.objects.create(ip=ip)
            event_id = request.GET.get('event-id')
            Event = event.objects.get(pk=event_id)
            Event.views.add(IpModel.objects.get(ip=ip))
            detail(request, event.objects.get(pk=event_id).id)
        return self.render_to_response(context)

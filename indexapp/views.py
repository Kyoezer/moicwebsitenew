from django.shortcuts import redirect, render
from django.views.generic import DetailView
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from indexapp.models import post, event, vacancie, tender, IpModel
from django.core.mail import send_mail, BadHeaderError
from django.core.paginator import Paginator
from django.db.models import Q
from itertools import chain


# Create your views here.
def home(request):
    popuplarPs = post.objects.all()
    # Events Pagination
    p = Paginator(event.objects.all().order_by('-id'), 3)
    page = request.GET.get('page')
    events = p.get_page(page)

    # Vacancy Pagination
    p1 = Paginator(vacancie.objects.all().order_by('-id'), 3)
    page1 = request.GET.get('page1')
    vacancies = p1.get_page(page1)

#     Tender Pagination
    p3 = Paginator(tender.objects.all().order_by('-id'), 3)
    page2 = request.GET.get('page2')
    tenders = p3.get_page(page2)

    # add when the pagination works
    # 'vacancy': vacancies, 'tender': tenders

    return render(request, 'home.html', {'post': popuplarPs, 'events': events, 'vacancies': vacancies, 'tenders': tenders, 'event': events})


def vacancy_detail(request, id):
    obj = get_object_or_404(vacancie, pk=id)
    return render(request, 'vacancy_detail.html', {'obj': obj})


def tender_detail(request, id):
    obj = get_object_or_404(tender, pk=id)
    return render(request, 'tender_detail.html', {'obj': obj})


def detail(request, id):
    print(id)
    obj = get_object_or_404(event, pk=id)
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


def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        events = event.objects.filter(
            Q(event_title__icontains=searched) |
            Q(category__icontains=searched)
        )
        event_count = events.count()

        vacancies = vacancie.objects.filter(
            Q(vacancy_title__icontains=searched)
        )
        vacancy_count = vacancies.count()

        tenders = tender.objects.filter(
            Q(tender_title__icontains=searched)
        )
        tender_count = tenders.count()

        total_count = event_count + vacancy_count + tender_count
        search_results = chain(events, vacancies)
        return render(request, 'search.html', {'searched': searched,
                                               'events': events,
                                               'vacancies': vacancies,
                                               'tenders': tenders,
                                               'total_count': total_count,
                                               })
    else:
        return render(request, 'search.html',)

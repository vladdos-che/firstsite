from django.db.models import Min, Max, Count, Q, Sum, IntegerField, Avg
from django.http import HttpResponseRedirect, HttpResponse, StreamingHttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.template.loader import get_template, render_to_string
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.urls import reverse

from bboard.forms import BbForm
from bboard.models import Bb, Rubric


def count_bb():
    result = dict()
    for r in Rubric.objects.annotate(num_bbs=Count('bb')):
        result.update({r.pk: r.num_bbs})

    return result


class BbCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        context['count_bb'] = count_bb()
        return context


def index_resp(request):
    resp = HttpResponse('Здесь будет', content_type='text/plain; charset=utf-8')
    resp.write(' главная')
    resp.writelines((' страница', ' сайта'))
    resp['keywords'] = 'Python, Django'

    return resp


# def index(request):
#     resp_content = ('Здесь будет', ' главная', ' страница', ' сайта')
#     resp = StreamingHttpResponse(resp_content,
#                                  content_type='text/plain; charset=utf-8')
#     return resp


def index(request):
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {
        'bbs': bbs,
        'rubrics': rubrics,
    }
    # template = get_template('bboard/index.html')

    # return HttpResponse(template.render(context=context, request=request))
    return HttpResponse(render_to_string('bboard/index.html', context, request))

    # data = {'title': 'Мотоцикл', 'content': 'Старый', 'price': 10_000.0}
    # return JsonResponse(data)

    # return redirect('by_rubric', rubric_id=|сюда какой-то объект|.cleaned_data['rubric'].pk)


def index_old(request):
    bbs = Bb.objects.order_by('-published')
    rubrics = Rubric.objects.all()

    # min_price = Bb.objects.aggregate(Min('price'))
    # max_price = Bb.objects.aggregate(mp=Max('price'))
    result = Bb.objects.aggregate(min_price=Min('price'),
                                  max_price=Max('price'),
                                  diff_price=Max('price') - Min('price'),)

    # for r in Rubric.objects.annotate(Count('bb')):
    #     print(f'{r.name}: {r.bb__count}')
    #
    # for r in Rubric.objects.annotate(num_bbs=Count('bb')):
    #     print(f'{r.name}: {r.num_bbs}')

    # for r in Rubric.objects.annotate(cnt=Count('bb',
    #                                            filter=Q(bb__price__gt=100_000)
    #                                            # min=Min('bb__price')).filter(cnt__gt=0)
    #                                            )):
    #     # print(f'{r.name}: {r.min}')
    #     print(f'{r.name}: {r.cnt}')

    # print(
    #     Bb.objects.aggregate(
    #         sum=Sum(
    #             'price',
    #             output_field=IntegerField(),
    #             filter=Q(rubric__name='Бытовая техника')
    #         )
    #     )
    # )

    # print(
    #     Bb.objects.aggregate(
    #         avg=Avg(
    #             'price',
    #             output_field=IntegerField(),
    #             filter=Q(rubric__name='Сельхозтехника'),
    #             distinct=False  # True = только уникальные
    #         )
    #     )
    # )

    context = {
        'bbs': bbs,
        'rubrics': rubrics,
        # 'min_price': min_price.get('price__min'),
        # 'max_price': max_price.get('mp'),
        'min_price': result.get('min_price'),
        'max_price': result.get('min_price'),
        'diff_price': result.get('diff_price'),
        'count_bb': count_bb(),
    }
    return render(request, 'bboard/index.html', context)


def by_rubric(request, rubric_id, **kwargs):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)

    context = {
        'bbs': bbs,
        'rubrics': rubrics,
        'current_rubric': current_rubric,
        'count_bb': count_bb(),
        # 'name': kwargs.get('name'),
        'kwargs': kwargs,
    }
    return render(request, 'bboard/by_rubric.html', context)


def login(request):
    rubrics = Rubric.objects.all()
    context = {
        'rubrics': rubrics,
        'count_bb': count_bb(),

    }
    return render(request, 'bboard/login.html', context)


def add(request):
    bbf = BbForm()
    context = {'form': bbf}
    return render(request, 'bboard/create.html', context)


def add_save(request):
    bbf = BbForm(request.POST)

    if bbf.is_valid():
        bbf.save()

        return HttpResponseRedirect(reverse('by_rubric',
                                            kwargs={'rubric_id': bbf.cleaned_data['rubric'].pk}
                                            ))
    else:
        context = {'form': bbf}
        return render(request, 'bboard/create.html', context)


def add_and_save(request):
    if request.method == 'POST':
        bbf = BbForm(request.POST)

        if bbf.is_valid():
            bbf.save()
            return HttpResponseRedirect(reverse('by_rubric',
                                                kwargs={'rubric_id': bbf.cleaned_data['rubric'].pk}
                                                ))
        else:
            context = {'form': bbf}
            return render(request, 'bboard/create.html', context)

    else:
        bbf = BbForm()
        context = {'form': bbf}
        return render(request, 'bboard/create.html', context)


def detail(request, rec_id):
    bb = get_object_or_404(Bb, pk=rec_id)
    bbs = get_list_or_404(Bb, rubric=bb.rubric.pk)
    context = {
        'bbs': bbs,
        'bb': bb
    }
    return HttpResponse(render_to_string('bboard/detail.html', context, request))

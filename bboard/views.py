from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Min, Max, Count, Q, Sum, IntegerField, Avg
from django.forms import modelformset_factory, inlineformset_factory
from django.http import HttpResponseRedirect, HttpResponse, StreamingHttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.template.loader import get_template, render_to_string
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import TemplateView, RedirectView
from django.views.generic.dates import ArchiveIndexView, MonthArchiveView
from django.views.generic.edit import CreateView, FormView, UpdateView, DeleteView
from django.urls import reverse
from precise_bbcode.bbcode import get_parser

from bboard.forms import BbForm, IceCreamForm, SearchForm, CaptchaLibraryForm
from bboard.models import Bb, Rubric

import logging  # lesson_16_hw


def count_bb():
    result = dict()
    for r in Rubric.objects.annotate(num_bbs=Count('bb')):
        result.update({r.pk: r.num_bbs})

    return result


# class BbCreateView(CreateView):
#     template_name = 'bboard/create.html'
#     form_class = BbForm
#     success_url = reverse_lazy('index')
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['rubrics'] = Rubric.objects.all()
#         context['count_bb'] = count_bb()
#         return context


class BbCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    success_url = '/bboard/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


# class BbAddView(FormView):
# class BbAddView(LoginRequiredMixin, FormView):
class BbAddView(UserPassesTestMixin, FormView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    initial = {'price': 0.0}

    # Start For UserPassesTestMixin
    def test_func(self):
        return self.request.user.is_staff

    # End For UserPassesTestMixin

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_form(self, form_class=None):
        self.object = super().get_form(form_class)
        return self.object

    def get_success_url(self):
        return reverse('by_rubric', kwargs={'rubric_id': self.object.cleaned_data['rubric'].pk})


# def index_resp(request):
#     resp = HttpResponse('Здесь будет', content_type='text/plain; charset=utf-8')
#     resp.write(' главная')
#     resp.writelines((' страница', ' сайта'))
#     resp['keywords'] = 'Python, Django'
#
#     return resp


# def index(request):
#     resp_content = ('Здесь будет', ' главная', ' страница', ' сайта')
#     resp = StreamingHttpResponse(resp_content,
#                                  content_type='text/plain; charset=utf-8')
#     return resp


# def index(request):
#     bbs = Bb.objects.all()
#     rubrics = Rubric.objects.all()
#     context = {
#         'bbs': bbs,
#         'rubrics': rubrics,
#     }
#     # template = get_template('bboard/index.html')
#
#     # return HttpResponse(template.render(context=context, request=request))
#     return HttpResponse(render_to_string('bboard/index.html', context, request))
#
#     # data = {'title': 'Мотоцикл', 'content': 'Старый', 'price': 10_000.0}
#     # return JsonResponse(data)
#
#     # return redirect('by_rubric', rubric_id=|сюда какой-то объект|.cleaned_data['rubric'].pk)


# def index_old(request):
#     bbs = Bb.objects.order_by('-published')
#     rubrics = Rubric.objects.all()
#
#     # min_price = Bb.objects.aggregate(Min('price'))
#     # max_price = Bb.objects.aggregate(mp=Max('price'))
#     result = Bb.objects.aggregate(min_price=Min('price'),
#                                   max_price=Max('price'),
#                                   diff_price=Max('price') - Min('price'),)
#
#     # for r in Rubric.objects.annotate(Count('bb')):
#     #     print(f'{r.name}: {r.bb__count}')
#     #
#     # for r in Rubric.objects.annotate(num_bbs=Count('bb')):
#     #     print(f'{r.name}: {r.num_bbs}')
#
#     # for r in Rubric.objects.annotate(cnt=Count('bb',
#     #                                            filter=Q(bb__price__gt=100_000)
#     #                                            # min=Min('bb__price')).filter(cnt__gt=0)
#     #                                            )):
#     #     # print(f'{r.name}: {r.min}')
#     #     print(f'{r.name}: {r.cnt}')
#
#     # print(
#     #     Bb.objects.aggregate(
#     #         sum=Sum(
#     #             'price',
#     #             output_field=IntegerField(),
#     #             filter=Q(rubric__name='Бытовая техника')
#     #         )
#     #     )
#     # )
#
#     # print(
#     #     Bb.objects.aggregate(
#     #         avg=Avg(
#     #             'price',
#     #             output_field=IntegerField(),
#     #             filter=Q(rubric__name='Сельхозтехника'),
#     #             distinct=False  # True = только уникальные
#     #         )
#     #     )
#     # )
#
#     context = {
#         'bbs': bbs,
#         'rubrics': rubrics,
#         # 'min_price': min_price.get('price__min'),
#         # 'max_price': max_price.get('mp'),
#         'min_price': result.get('min_price'),
#         'max_price': result.get('min_price'),
#         'diff_price': result.get('diff_price'),
#         'count_bb': count_bb(),
#     }
#     return render(request, 'bboard/index.html', context)


# class BbIndexView(TemplateView):
#     template_name = 'bboard/index.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['rubrics'] = Rubric.objects.all()
#         context['bbs'] = Bb.objects.order_by('-published')
#         context['count_bb'] = count_bb()
#         result = Bb.objects.aggregate(min_price=Min('price'),
#                                                  max_price=Max('price'),
#                                                  diff_price=Max('price') - Min('price'),
#                                                  )
#         context['min_price'] = result.get('min_price')
#         context['max_price'] = result.get('min_price')
#         context['diff_price'] = result.get('diff_price')
#
#         return context


class BbIndexView(ArchiveIndexView):
    model = Bb
    date_field = 'published'
    date_list_period = 'year'
    template_name = 'bboard/index.html'
    context_object_name = 'bbs'
    allow_empty = True

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # context['rubrics'] = Rubric.objects.all()
        context['rubrics'] = Rubric.objects.order_by_bb_count()
        return context


class BbIndexRedirectView(RedirectView):
    url = '/'


# def index(request):
#     rubrics = Rubric.objects.all()
#     bbs = Bb.objects.all()
#     paginator = Paginator(bbs, 5)
#
#     if 'page' in request.GET:
#         page_num = request.GET['page']
#     else:
#         page_num = 1
#
#     page = paginator.get_page(page_num)
#     context = {'rubrics': rubrics, 'page': page, 'bbs': page.object_list}
#
#     return render(request, 'bboard/index.html', context)


def index(request, page=1):
    # rubrics = Rubric.objects.all()
    # rubrics = Rubric.objects.order_by_bb_count()
    rubrics = Rubric.objects.order_by_bb_count()
    # bbs = Bb.objects.all()
    bbs = Bb.by_price.all()
    paginator = Paginator(bbs, 5)

    try:
        bbs_paginator = paginator.get_page(page)
    except EmptyPage:
        bbs_paginator = paginator.get_page(paginator.num_pages)
    except PageNotAnInteger:
        bbs_paginator = paginator.get_page(paginator.num_pages)

    context = {'rubrics': rubrics,
               'page': bbs_paginator,
               'bbs': bbs_paginator.object_list,
               'count_bb': count_bb()}

    return render(request, 'bboard/index.html', context)


def by_rubric(request, rubric_id, **kwargs):
    # bbs = Bb.objects.filter(rubric=rubric_id)
    bbs = Bb.by_price.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    paginator = Paginator(bbs, 1)

    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1

    page = paginator.get_page(page_num)

    context = {
        'bbs': page.object_list,
        'rubrics': rubrics,
        'current_rubric': current_rubric,
        'count_bb': count_bb(),
        'page': page,
        # 'name': kwargs.get('name'),
        # 'kwargs': kwargs,
    }
    return render(request, 'bboard/by_rubric.html', context)


class BbByRubricView(ListView):
    template_name = 'bboard/by_rubric.html'
    context_object_name = 'bbs'
    paginate_by = 2

    def get_queryset(self):
        return Bb.objects.filter(rubric=self.kwargs['rubric_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        context['current_rubric'] = Rubric.objects.get(pk=self.kwargs['rubric_id'])
        return context


class BbByRubricByDateView(ArchiveIndexView):  # lesson_20_hw
    template_name = 'bboard/by_rubric.html'
    context_object_name = 'bbs'
    paginate_by = 2
    model = Bb
    date_field = 'published'
    date_list_period = 'year'
    allow_empty = True

    def get_queryset(self):
        return Bb.objects.filter(rubric=self.kwargs['rubric_id'])

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['rubrics'] = Rubric.objects.all()
        context['current_rubric'] = Rubric.objects.get(pk=self.kwargs['rubric_id'])
        return context


# class BbByRubricView(TemplateView):
#     template_name = 'bboard/by_rubric.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['current_rubric'] = Rubric.objects.get(pk=context['rubric_id'])
#         context['bbs'] = Bb.objects.filter(rubric=context['rubric_id'])
#         context['rubrics'] = Rubric.objects.all()
#         return context


# class BbByRubricView(ListView):
#     template_name = 'bboard/by_rubric.html'
#     context_object_name = 'bbs'
#
#     def get_queryset(self):
#         return Bb.objects.filter(rubric=self.kwargs['rubric_id'])
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['rubrics'] = Rubric.objects.all()
#         context['current_rubric'] = Rubric.objects.get(pk=self.kwargs['rubric_id'])
#         return context


def login(request):  # Моё не нужное
    rubrics = Rubric.objects.all()
    context = {
        'rubrics': rubrics,
        'count_bb': count_bb(),

    }

    logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w", encoding='utf-8')  # lesson_16_hw
    logging.info(request)

    return render(request, 'bboard/login.html', context)


class BbLoginRedirectView(RedirectView):  # lesson_16_hw
    url = '/'


# def add(request):
#     bbf = BbForm()
#     context = {'form': bbf}
#     return render(request, 'bboard/create.html', context)


# def add_save(request):
#     bbf = BbForm(request.POST)
#
#     if bbf.is_valid():
#         bbf.save()
#
#         return HttpResponseRedirect(reverse('by_rubric',
#                                             kwargs={'rubric_id': bbf.cleaned_data['rubric'].pk}
#                                             ))
#     else:
#         context = {'form': bbf}
#         return render(request, 'bboard/create.html', context)


# def add_and_save(request):
#     if request.method == 'POST':
#         bbf = BbForm(request.POST)
#
#         if bbf.is_valid():
#             bbf.save()
#             return HttpResponseRedirect(reverse('by_rubric',
#                                                 kwargs={'rubric_id': bbf.cleaned_data['rubric'].pk}
#                                                 ))
#         else:
#             context = {'form': bbf}
#             return render(request, 'bboard/create.html', context)
#
#     else:
#         bbf = BbForm()
#         context = {'form': bbf}
#         return render(request, 'bboard/create.html', context)


# def detail(request, rec_id):
#     bb = get_object_or_404(Bb, pk=rec_id)
#     bbs = get_list_or_404(Bb, rubric=bb.rubric.pk)
#     context = {
#         'bbs': bbs,
#         'bb': bb
#     }
#     return HttpResponse(render_to_string('bboard/detail.html', context, request))


class BbDetailView(DetailView):
    model = Bb

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # parser = get_parser()
        # context['parsed_content'] = parser.render(context['bb'].content)

        context['rubrics'] = Rubric.objects.all()
        context['bbs'] = get_list_or_404(Bb, rubric=context['bb'].rubric)
        return context


class BbRedirectView(RedirectView):
    url = '/detail/%(pk)d/'


class BbEditView(UpdateView):
    model = Bb
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


class BbDeleteView(DeleteView):
    model = Bb
    success_url = reverse_lazy('index')


class BbMonthArchiveView(MonthArchiveView):
    model = Bb
    date_field = "published"
    month_format = '%m'
    context_object_name = 'bbs'


class IceCreamCreateView(CreateView):  # lesson_25_hw
    template_name = 'bboard/icecream_create.html'
    form_class = IceCreamForm
    success_url = '/'


@permission_required(('bboard.add_rubriс', 'bboard.change_rubric', 'bboard.delete_rubric'))
@user_passes_test(lambda user: user.is_staff)
@login_required
def rubrics(request):
    # RubricFromSet = modelformset_factory(Rubric, fields=('name',),
    #                                      can_order=True, can_delete=True)
    #
    # formset = RubricFromSet(initial=[{'name': 'Новая рубрика'}],
    #                         qweryset=Rubric.objects.all()[0:5])
    #
    # formset = RubricFromSet(request.POST)
    #
    # if formset.is_valid():
    #     # formset.save()
    #     formset.save(commit=False)
    #     for rubric in formset.deleted_objects:
    #         rubric.delete()

    RubricFormSet = modelformset_factory(Rubric, fields=('name',),
                                         can_delete=True, extra=3,  # extra=1 по умолчанию
                                         min_num=5, validate_min=True)  # lesson_27_hw

    if request.method == 'POST':
        formset = RubricFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('index')
    else:
        formset = RubricFormSet()

    context = {'formset': formset}
    return render(request, 'bboard/rubrics.html', context)


def bbs(request, rubric_id):
    # if request.user.has_perm('bboard.delete_bb'):  # request.user.has_perms  # lesson_28
    #     pass

    # request.user.get_user_permissions()  # lesson_28
    # request.user.get_group_permissions()  # lesson_28
    # request.user.get_all_permissions()  # lesson_28

    # User.objects.with_perm('bboard.add_bb', include_superusers=False)  # lesson_28

    BbsFormSet = inlineformset_factory(Rubric, Bb, form=BbForm, extra=1)  # extra=3 по умолчанию
    rubric = Rubric.objects.get(pk=rubric_id)

    if request.method == 'POST':
        formset = BbsFormSet(request.POST, instance=rubric)

        if formset.is_valid():
            formset.save()
            return redirect('index')
    else:
        formset = BbsFormSet(instance=rubric)

    context = {'formset': formset, 'current_rubric': rubric}
    return render(request, 'bboard/bbs.html', context)


def search(request):
    if request.method == 'POST':
        sf = SearchForm(request.POST)
        if sf.is_valid():
            keyword = sf.cleaned_data['keyword']
            rubric_id = sf.cleaned_data['rubric'].pk
            bbs = Bb.objects.filter(title__iregex=keyword,
                                    rubric=rubric_id)
            context = {'bbs': bbs, 'form': sf}
            return render(request, 'bboard/search.html', context)
    else:
        sf = SearchForm()
    context = {'form': sf}
    return render(request, 'bboard/search.html', context)


class CaptchaLibraryView(FormView):  # lesson_32_hw
    template_name = 'bboard/captcha_library.html'
    form_class = CaptchaLibraryForm

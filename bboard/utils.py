from .models import Rubric


class RubricMixin:  # lesson_47_hw
    def get_user_context(self, **kwargs):
        context = kwargs
        context['rubrics'] = Rubric.objects.all()
        return context

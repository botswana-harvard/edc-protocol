from django.apps import apps as django_apps
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView

from edc_base.view_mixins import EdcBaseViewMixin


class HomeView(EdcBaseViewMixin, TemplateView):

    template_name = 'edc_protocol/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        app_config = django_apps.get_app_config('edc_protocol')
        context.update({
            'protocol': app_config.protocol,
            'protocol_number': app_config.protocol_number,
            'protocol_name': app_config.protocol_name,
            'protocol_title': app_config.protocol_title,
            'study_open_datetime': app_config.study_open_datetime,
            'study_close_datetime': app_config.study_close_datetime,
            'enrollment_caps': app_config.caps})
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(HomeView, self).dispatch(*args, **kwargs)
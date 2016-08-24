import sys

from django.apps import AppConfig as DjangoAppConfig
from django.core.exceptions import ImproperlyConfigured


SUBJECT_TYPE = 0
COUNT = 1


class AppConfig(DjangoAppConfig):
    name = 'edc_protocol'
    verbose_name = 'Edc Protocol'

    protocol = 'BHP000'
    protocol_number = '000'
    protocol_name = 'My Protocol'
    protocol_title = 'My Protocol of Many Things'

    subject_types = {'subject': 'Subjects'}  # {key: verbose_name}
    enrollment_caps = {'example.enrollmentmodel': ('subject', -1)}  # {label_lower: (key, count)}

    def ready(self):
        sys.stdout.write('Loading {} ...\n'.format(self.verbose_name))
        sys.stdout.write(' * {}: {}.\n'.format(self.protocol, self.protocol_name))
        for label, cap in self.enrollment_caps.items():
            if cap[SUBJECT_TYPE] not in list(self.subject_types.keys()):
                raise ImproperlyConfigured(
                    'Enrollment cap refers to an undefined subject_type. See edc_protocol.AppConfig')
            sys.stdout.write(
                ' * enrollment cap set to {} for {} in \'{}\'.\n'.format(
                    cap[COUNT], self.subject_types[cap[SUBJECT_TYPE]], label))
        sys.stdout.write(' Done loading {}.\n'.format(self.verbose_name))
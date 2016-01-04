from autofixture import register, AutoFixture
from django.contrib.contenttypes.models import ContentType
from django.core.management import call_command

class GenericAutoFixture(AutoFixture):

    field_values = {
            'expired': False,
            'live': True,
            'has_unpublished_changes': False,
            'numchild': 0,
    }

    @classmethod
    def generate_page(cls, child_class, fields, number_childs):
        aux_dict = {'content_type': ContentType.objects.get_for_model(child_class)}
        cls.field_values = dict(cls.field_values, **aux_dict)
        cls.field_values = dict(cls.field_values, **fields)
        register(child_class, GenericAutoFixture, overwrite=True)
        call_command('loadtestdata', child_class._meta.__unicode__() + ':' + str(number_childs))
        call_command('fixtree')

    class Meta:
        abstract = True

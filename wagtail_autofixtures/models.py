from autofixture import register, AutoFixture
from django.contrib.contenttypes.models import ContentType
from django.core.management import call_command
from wagtail.wagtailcore.models import Page

class GenericAutoFixture(AutoFixture):

    field_values = {
            'expired': False,
            'live': True,
            'has_unpublished_changes': False,
            'numchild': 0,
    }

    @classmethod
    def generate_page(cls, child_class, parent_id, number_childs):
        aux_dict = {
            'content_type': ContentType.objects.get_for_model(child_class)
        }
        cls.field_values = dict(cls.field_values, **aux_dict)
        register(child_class, GenericAutoFixture, overwrite=True)

        parent_page = Page.objects.filter(pk=parent_id)[0]
        parent_path = parent_page.path
        child_depth = parent_page.depth + 1
        num_childs = parent_page.numchild
        for pos in range(0, number_childs):
            new_page_path = parent_path + str(num_childs + 1).zfill(4)
            fields = {
                'path': new_page_path,
                'depth': child_depth
            }
            cls.field_values = dict(cls.field_values, **fields)
            call_command('loadtestdata', child_class._meta.__unicode__() + ':1')
            call_command('fixtree')
            num_childs += 1

    class Meta:
        abstract = True

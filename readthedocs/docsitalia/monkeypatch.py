"""
This is a really nasty module which monkeypatches ``Project`` model to keep the size to 255 characters up
from 63 since RTD 2.8.1.

Migration projects.0030_change-max-length-project-slug is modified in a noop (code is commented to clarify the origina
scope of the migration).
"""

from django.core import validators

from readthedocs.projects.models import Project

def monkey_patch_project_model():
    """
    This revert changes in 8d2ee29de95690a9cd72d4f2a0b4131a44449928.

    They changed the original values as any domain part can't be longer than 63 chars but we don't have this limitation.
    """
    fields = ["name", "slug"]
    field_length = 255
    for field in fields:
        fieldobj = Project._meta.get_field(field)
        fieldobj.max_length = field_length
        for v in fieldobj.validators:
            if isinstance(v, validators.MaxLengthValidator):
                v.limit_value = field_length


monkey_patch_project_model()

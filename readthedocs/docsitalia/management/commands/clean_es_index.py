"""Removes projects without publisher from the ES index"""
from __future__ import (
    absolute_import, print_function)

from django.db.models import Q
from django.core.management.base import BaseCommand
from django.conf import settings

from elasticsearch import Elasticsearch
from readthedocs.projects.models import Project

from readthedocs.docsitalia.models import PublisherProject


class Command(BaseCommand):

    """
    Clean ES index:

    Removes projects without publisher or inactive publisher or
    inactive publisher project from the ES index.
    Delete projects not linked to a publisher project from the db.
    """

    def handle(self, *args, **options):
        """handle command"""
        e_s = Elasticsearch(settings.ES_HOSTS)
        inactive_pp = PublisherProject.objects.filter(
            Q(active=False) | Q(publisher__active=False)
        ).values_list('pk', flat=True)
        queryset = Project.objects.filter(
            Q(publisherproject__isnull=True) | Q(publisherproject__in=inactive_pp)
        )
        for p_o in queryset:
            print(p_o.name)
            print(p_o.get_absolute_url())
            print(p_o.pk)
            if e_s.exists(index='readthedocs', doc_type='project', id=p_o.pk):
                e_s.delete(index='readthedocs', doc_type='project', id=p_o.pk)
            if p_o.publisherproject_set.count() == 0:
                p_o.delete()
            print('')

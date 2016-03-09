from __future__ import absolute_import

from celery import shared_task
from celery.result import AsyncResult
from unlocode.csvimport import importUNLOCODE

@shared_task
def importVersion(version):
    result = importUNLOCODE(version)
    return result

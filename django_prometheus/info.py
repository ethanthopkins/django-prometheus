from django import get_version
from prometheus_client import Info
from django_prometheus.conf import NAMESPACE

django_info = Info("django", 
                   "Django version information", 
                   namespace=NAMESPACE)
django_info.info({"major": get_version().split('.')[0], 
                  "minor": get_version().split('.')[1], 
                  "patchlevel": get_version().split('.')[2], 
                  "version": get_version()})
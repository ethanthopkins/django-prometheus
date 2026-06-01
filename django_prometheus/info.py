from django import get_version
from prometheus_client import Info
from django_prometheus.conf import NAMESPACE

django_info = Info("django_info", 
                   "Django version information", 
                   namespace=NAMESPACE)
django_info.info({"version": get_version()})
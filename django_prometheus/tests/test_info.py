from django import get_version

def test_info_metric():
    from django_prometheus.info import django_info
    assert django_info._name == "django"
    assert django_info._documentation == "Django version information"
    assert django_info._value == {"major": get_version().split('.')[0], 
                                  "minor": get_version().split('.')[1], 
                                  "patchlevel": get_version().split('.')[2], 
                                  "version": get_version()}
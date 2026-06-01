from django import get_version

def test_info_metric():
    from django_prometheus.info import django_info
    assert django_info._name == "django_info"
    assert django_info._documentation == "Django version information"
    assert django_info._value == {"version": get_version()}
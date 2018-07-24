import pytest

from kiali_qe.tests import ServicesPageTest

@pytest.mark.group18
@pytest.mark.group38
def test_pagination_feature(kiali_client, openshift_client, browser):
    tests = ServicesPageTest(
        kiali_client=kiali_client, openshift_client=openshift_client, browser=browser)
    tests.assert_pagination_feature()

@pytest.mark.group19
@pytest.mark.group39
def test_namespaces(kiali_client, openshift_client, browser):
    tests = ServicesPageTest(
        kiali_client=kiali_client, openshift_client=openshift_client, browser=browser)
    tests.assert_namespaces()

@pytest.mark.group20
@pytest.mark.group40
def test_filter_options(kiali_client, openshift_client, browser):
    tests = ServicesPageTest(
        kiali_client=kiali_client, openshift_client=openshift_client, browser=browser)
    tests.assert_filter_options()


def test_filter_feature_random(kiali_client, openshift_client, browser):
    tests = ServicesPageTest(
        kiali_client=kiali_client, openshift_client=openshift_client, browser=browser)
    tests.assert_filter_feature_random()

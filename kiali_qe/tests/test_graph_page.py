import pytest
from kiali_qe.components.enums import (
    GraphPageBadgesFilter,
    GraphPageDisplayFilter,
    GraphPageLayout,
    EdgeLabelsFilter,
    GraphPageDuration,
    GraphRefreshInterval
)
from kiali_qe.pages import GraphPage
from kiali_qe.utils import is_equal
from kiali_qe.utils.log import logger

@pytest.mark.group1
@pytest.mark.group21
def test_duration(browser):
    # get page instance
    page = GraphPage(browser)
    # test options
    options_defined = [item.text for item in GraphPageDuration]
    duration = page.duration
    options_listed = duration.options
    logger.debug('Options[defined:{}, listed:{}]'.format(options_defined, options_listed))
    assert is_equal(options_defined, options_listed), \
        ('Options mismatch: defined:{}, listed:{}'.format(options_defined, options_listed))

@pytest.mark.group2
@pytest.mark.group22
def test_refresh_interval(browser):
    # get page instance
    page = GraphPage(browser)
    # test options
    options_defined = [item.text for item in GraphRefreshInterval]
    interval = page.interval
    options_listed = interval.options
    logger.debug('Options[defined:{}, listed:{}]'.format(options_defined, options_listed))
    assert is_equal(options_defined, options_listed), \
        ('Options mismatch: defined:{}, listed:{}'.format(options_defined, options_listed))

def test_layout(browser):
    # get page instance
    page = GraphPage(browser)
    # test options
    options_defined = [item.text for item in GraphPageLayout]
    layout = page.filter.layout
    options_listed = layout.options
    assert is_equal(options_defined, options_listed), \
        ('Options mismatch: defined:{}, listed:{}'.format(options_defined, options_listed))

@pytest.mark.group3
@pytest.mark.group23
def test_filter(browser):
    # get page instance
    page = GraphPage(browser)
    # test available filters
    options_defined = [item.text for item in GraphPageBadgesFilter]
    for item in GraphPageDisplayFilter:
        options_defined.append(item.text)
    edge_options_defined = [item.text for item in EdgeLabelsFilter]
    options_listed = page.filter.items
    edge_options_listed = page.filter.radio_items
    logger.debug('Filter options[defined:{}, listed:{}]'
                 .format(options_defined, options_listed))
    logger.debug('Radio options[defined:{}, listed:{}]'
                 .format(edge_options_defined, edge_options_listed))
    assert is_equal(options_defined, options_listed), \
        ('Filter Options mismatch: defined:{}, listed:{}'
         .format(options_defined, options_listed))
    assert is_equal(options_defined, options_listed), \
        ('Radio Options mismatch: defined:{}, listed:{}'
         .format(edge_options_defined, edge_options_listed))
    # enable disable each filter
    for filter_name in options_listed:
        _filter_test(page, filter_name)
    # select each filter in radio
    for filter_name in edge_options_listed:
        _filter_test(page, filter_name, uncheck=False)


def _filter_test(page, filter_name, uncheck=True):
    # test filter checked
    page.filter.check(filter_name)
    assert page.filter.is_checked(filter_name) is True
    if uncheck:
        # test filter unchecked
        page.filter.uncheck(filter_name)
        assert page.filter.is_checked(filter_name) is False

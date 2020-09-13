# Pytest It allows us to generate reports much easier to read than those of django

import pytest


@pytest.fixture(scope='session')
def data_dir(pytestconfig):
    return pytestconfig.rootdir.join(DJANGO_SETTINGS_MODULE=config.settings.test)

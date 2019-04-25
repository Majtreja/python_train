# -*- coding: utf-8 -*-
import pytest
from data import Data
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_login(app):
    app.open_page()
    app.fill_form(Data(user="QA_DB_superuser", password="roo6Piv2"))

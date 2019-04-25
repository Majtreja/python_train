# -*- coding: utf-8 -*-
import pytest
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_login(app):
    app.open_page()
    app.fill_form(user="QA_DB_superuser", password="roo6Piv2")


def test_empty_login(app):
    app.open_page()
    app.fill_form(user="", password="")

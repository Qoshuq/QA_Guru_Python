import pytest


@pytest.fixture
def browser():
    print("Выполняюсь перед тестом")

    yield

    print("Выполняюсь после теста")


@pytest.fixture
def main_page(browser):
    pass


def test_first(browser, user, main_page):
    pass

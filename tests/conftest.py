# Fixtures — это функции, выполняемые pytest до (а иногда и после) фактических тестовых функций.
# место где можем поместить fixtures, для использования всеми тестами в каталоге тестов
# scope='function' - Выполняется один раз для каждой функции теста
# scope='module' - Выполняется один раз для каждого модуля, независимо от того, сколько тестовых функций или методов или других фикстур при использовании модуля.

import pytest
from utils.api_client import ReqresApiClient

@pytest.fixture(scope="module")
def api_client():
    return ReqresApiClient()

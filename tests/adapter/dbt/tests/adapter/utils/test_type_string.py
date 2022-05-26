import pytest
from dbt.tests.adapter.utils.base_utils import BaseUtils
from dbt.tests.adapter.utils.fixture_type_string import (
    seeds__data_type_string_csv,
    models__test_type_string_sql,
    models__test_type_string_yml,
)


class BaseTypeString(BaseUtils):
    @pytest.fixture(scope="class")
    def seeds(self):
        return {"data_type_string.csv": seeds__data_type_string_csv}

    @pytest.fixture(scope="class")
    def models(self):
        return {
            "test_type_string.yml": models__test_type_string_yml,
            "test_type_string.sql": self.interpolate_macro_namespace(
                models__test_type_string_sql, "type_string"
            ),
        }


@pytest.mark.skip(reason="TODO - implement this test")
class TestTypeString(BaseTypeString):
    pass

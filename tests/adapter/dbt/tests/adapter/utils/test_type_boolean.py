import pytest
from dbt.tests.adapter.utils.base_utils import BaseUtils
from dbt.tests.adapter.utils.fixture_type_boolean import (
    seeds__data_type_boolean_csv,
    models__test_type_boolean_sql,
    models__test_type_boolean_yml,
)


class BaseTypeBoolean(BaseUtils):
    @pytest.fixture(scope="class")
    def seeds(self):
        return {"data_type_boolean.csv": seeds__data_type_boolean_csv}

    @pytest.fixture(scope="class")
    def models(self):
        return {
            "test_type_boolean.yml": models__test_type_boolean_yml,
            "test_type_boolean.sql": self.interpolate_macro_namespace(
                models__test_type_boolean_sql, "type_boolean"
            ),
        }


@pytest.mark.skip(reason="TODO - implement this test")
class TestTypeBoolean(BaseTypeBoolean):
    pass

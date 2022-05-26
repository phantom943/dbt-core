import pytest
from dbt.tests.adapter.utils.base_utils import BaseUtils
from dbt.tests.adapter.utils.fixture_type_float import (
    seeds__data_type_float_csv,
    models__test_type_float_sql,
    models__test_type_float_yml,
)


class BaseTypeFloat(BaseUtils):
    @pytest.fixture(scope="class")
    def seeds(self):
        return {"data_type_float.csv": seeds__data_type_float_csv}

    @pytest.fixture(scope="class")
    def models(self):
        return {
            "test_type_float.yml": models__test_type_float_yml,
            "test_type_float.sql": self.interpolate_macro_namespace(
                models__test_type_float_sql, "type_float"
            ),
        }


@pytest.mark.skip(reason="TODO - implement this test")
class TestTypeFloat(BaseTypeFloat):
    pass

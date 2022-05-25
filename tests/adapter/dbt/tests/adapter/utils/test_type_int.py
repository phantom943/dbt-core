import pytest
from dbt.tests.adapter.utils.base_utils import BaseUtils
from dbt.tests.adapter.utils.fixture_type_int import (
    seeds__data_type_int_csv,
    models__test_type_int_sql,
    models__test_type_int_yml,
)


class BaseTypeInt(BaseUtils):
    @pytest.fixture(scope="class")
    def seeds(self):
        return {"data_type_int.csv": seeds__data_type_int_csv}

    @pytest.fixture(scope="class")
    def models(self):
        return {
            "test_type_int.yml": models__test_type_int_yml,
            "test_type_int.sql": self.interpolate_macro_namespace(models__test_type_int_sql, "type_int"),
        }


@pytest.mark.skip(reason="TODO - implement this test")
class TestTypeInt(BaseTypeInt):
    pass

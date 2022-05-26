import pytest
from dbt.tests.adapter.utils.base_utils import BaseUtils
from dbt.tests.adapter.utils.fixture_type_numeric import (
    seeds__data_type_numeric_csv,
    models__test_type_numeric_sql,
    models__test_type_numeric_yml,
)


class BaseTypeNumeric(BaseUtils):
    @pytest.fixture(scope="class")
    def seeds(self):
        return {"data_type_numeric.csv": seeds__data_type_numeric_csv}

    @pytest.fixture(scope="class")
    def models(self):
        return {
            "test_type_numeric.yml": models__test_type_numeric_yml,
            "test_type_numeric.sql": self.interpolate_macro_namespace(
                models__test_type_numeric_sql, "type_numeric"
            ),
        }


@pytest.mark.skip(reason="TODO - implement this test")
class TestTypeNumeric(BaseTypeNumeric):
    pass

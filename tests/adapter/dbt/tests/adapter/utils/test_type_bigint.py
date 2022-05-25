import pytest
from dbt.tests.adapter.utils.base_utils import BaseUtils
from dbt.tests.adapter.utils.fixture_type_bigint import (
    seeds__data_type_bigint_csv,
    models__test_type_bigint_sql,
    models__test_type_bigint_yml,
)


class BaseTypeBigint(BaseUtils):
    @pytest.fixture(scope="class")
    def seeds(self):
        return {"data_type_bigint.csv": seeds__data_type_bigint_csv}

    @pytest.fixture(scope="class")
    def models(self):
        return {
            "test_type_bigint.yml": models__test_type_bigint_yml,
            "test_type_bigint.sql": self.interpolate_macro_namespace(models__test_type_bigint_sql, "type_bigint"),
        }


@pytest.mark.skip(reason="TODO - implement this test")
class TestTypeBigint(BaseTypeBigint):
    pass

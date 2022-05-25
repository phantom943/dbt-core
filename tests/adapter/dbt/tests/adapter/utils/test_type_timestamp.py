import pytest
from dbt.tests.adapter.utils.base_utils import BaseUtils
from dbt.tests.adapter.utils.fixture_type_timestamp import (
    seeds__data_type_timestamp_csv,
    models__test_type_timestamp_sql,
    models__test_type_timestamp_yml,
)


class BaseTypeTimestamp(BaseUtils):
    @pytest.fixture(scope="class")
    def seeds(self):
        return {"data_type_timestamp.csv": seeds__data_type_timestamp_csv}

    @pytest.fixture(scope="class")
    def models(self):
        return {
            "test_type_timestamp.yml": models__test_type_timestamp_yml,
            "test_type_timestamp.sql": self.interpolate_macro_namespace(models__test_type_timestamp_sql, "type_timestamp"),
        }


@pytest.mark.skip(reason="TODO - implement this test")
class TestTypeTimestamp(BaseTypeTimestamp):
    pass

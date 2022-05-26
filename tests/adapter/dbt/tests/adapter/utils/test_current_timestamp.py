import pytest
from dbt.tests.adapter.utils.base_utils import BaseUtils
from dbt.tests.adapter.utils.fixture_current_timestamp import (
    models__test_current_timestamp_sql,
    models__test_current_timestamp_yml,
)


class BaseCurrentTimestamp(BaseUtils):
    @pytest.fixture(scope="class")
    def models(self):
        return {
            "test_current_timestamp.yml": models__test_current_timestamp_yml,
            "test_current_timestamp.sql": self.interpolate_macro_namespace(
                models__test_current_timestamp_sql, "current_timestamp"
            ),
        }


class TestCurrentTimestamp(BaseCurrentTimestamp):
    pass

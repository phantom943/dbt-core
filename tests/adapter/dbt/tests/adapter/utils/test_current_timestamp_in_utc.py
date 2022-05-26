import pytest
from dbt.tests.adapter.utils.base_utils import BaseUtils
from dbt.tests.adapter.utils.fixture_current_timestamp_in_utc import (
    models__test_current_timestamp_in_utc_sql,
    models__test_current_timestamp_in_utc_yml,
)


class BaseCurrentTimestampInUtc(BaseUtils):
    @pytest.fixture(scope="class")
    def models(self):
        return {
            "test_current_timestamp_in_utc.yml": models__test_current_timestamp_in_utc_yml,
            "test_current_timestamp_in_utc.sql": self.interpolate_macro_namespace(
                models__test_current_timestamp_in_utc_sql, "current_timestamp_in_utc"
            ),
        }


class TestCurrentTimestampInUtc(BaseCurrentTimestampInUtc):
    pass

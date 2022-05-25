
# current_timestamp_in_utc

# TODO how can we test this better?
models__test_current_timestamp_in_utc_sql = """
select
    {{ current_timestamp_in_utc() }} as actual,
    {{ current_timestamp_in_utc() }} as expected
"""


models__test_current_timestamp_in_utc_yml = """
version: 2
models:
  - name: test_current_timestamp_in_utc
    tests:
      - assert_equal:
          actual: actual
          expected: expected
"""

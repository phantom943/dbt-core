{% macro postgres__current_timestamp_in_utc() %}
    (current_timestamp at time zone 'utc')::{{dbt.type_timestamp()}}
{% endmacro %}

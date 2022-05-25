{% macro current_timestamp_in_utc() -%}
  {{ return(adapter.dispatch('current_timestamp_in_utc', 'dbt')()) }}
{%- endmacro %}

{% macro default__current_timestamp_in_utc() %}
    {{dbt.current_timestamp()}}
{% endmacro %}

{% macro current_timestamp() -%}
  {{ return(adapter.dispatch('current_timestamp', 'dbt')()) }}
{%- endmacro %}

{% macro default__current_timestamp() %}
    current_timestamp::{{dbt_utils.type_timestamp()}}
{% endmacro %}

{% macro current_timestamp_in_utc() -%}
  {{ return(adapter.dispatch('current_timestamp_in_utc', 'dbt')()) }}
{%- endmacro %}

{% macro default__current_timestamp_in_utc() %}
    {{dbt_utils.current_timestamp()}}
{% endmacro %}

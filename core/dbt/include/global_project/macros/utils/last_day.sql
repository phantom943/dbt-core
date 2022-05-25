{% macro last_day(date, datepart) %}
  {{ return(adapter.dispatch('last_day', 'dbt') (date, datepart)) }}
{% endmacro %}

{%- macro default_last_day(date, datepart) -%}
    cast(
        {{dbt_utils.dateadd('day', '-1',
        dbt_utils.dateadd(datepart, '1', dbt_utils.date_trunc(datepart, date))
        )}}
        as date)
{%- endmacro -%}

{% macro default__last_day(date, datepart) -%}
    {{dbt_utils.default_last_day(date, datepart)}}
{%- endmacro %}

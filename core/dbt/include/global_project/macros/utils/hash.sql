{% macro hash(field) -%}
  {{ return(adapter.dispatch('hash', 'dbt') (field)) }}
{%- endmacro %}

{% macro default__hash(field) -%}
    md5(cast({{field}} as {{dbt_utils.type_string()}}))
{%- endmacro %}

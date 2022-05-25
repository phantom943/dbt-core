{% macro hash(field) -%}
  {{ return(adapter.dispatch('hash', 'dbt') (field)) }}
{%- endmacro %}

{% macro default__hash(field) -%}
    md5(cast({{field}} as {{dbt.type_string()}}))
{%- endmacro %}

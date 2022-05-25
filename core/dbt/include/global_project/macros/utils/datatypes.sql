{%- macro type_string() -%}
  {{ return(adapter.dispatch('type_string', 'dbt')()) }}
{%- endmacro -%}

{% macro default__type_string() %}
    string
{% endmacro %}

{%- macro type_timestamp() -%}
  {{ return(adapter.dispatch('type_timestamp', 'dbt')()) }}
{%- endmacro -%}

{% macro default__type_timestamp() %}
    timestamp
{% endmacro %}

{%- macro type_float() -%}
  {{ return(adapter.dispatch('type_float', 'dbt')()) }}
{%- endmacro -%}

{% macro default__type_float() %}
    float
{% endmacro %}

{%- macro type_numeric() -%}
  {{ return(adapter.dispatch('type_numeric', 'dbt')()) }}
{%- endmacro -%}

{% macro default__type_numeric() %}
    numeric(28, 6)
{% endmacro %}

{%- macro type_bigint() -%}
  {{ return(adapter.dispatch('type_bigint', 'dbt')()) }}
{%- endmacro -%}

{% macro default__type_bigint() %}
    bigint
{% endmacro %}

{%- macro type_int() -%}
  {{ return(adapter.dispatch('type_int', 'dbt')()) }}
{%- endmacro -%}

{% macro default__type_int() %}
    int
{% endmacro %}

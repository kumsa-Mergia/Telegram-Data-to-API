-- macros/test_no_negative_message_length.sql
{% test no_negative_message_length(model) %}
SELECT *
FROM {{ model }}
WHERE message_length < 0
{% endtest %}

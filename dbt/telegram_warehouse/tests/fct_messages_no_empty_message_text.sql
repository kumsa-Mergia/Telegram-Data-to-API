select
    message_id, 
    message_text
from {{ ref('fct_messages') }}
where trim(message_text) = '' or message_text is null
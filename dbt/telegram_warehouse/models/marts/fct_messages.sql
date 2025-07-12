select
    id as message_id,
    channel_name as channel_id,
    date::date as date_id,
    message_text,
    message_length,
    has_image
from {{ ref('stg_telegram_messages') }}

with raw as (
    select *
    from {{ source('raw', 'telegram_messages') }}
)
select
    id,
    date,
    channel_name,
    -- Modified: Add a fallback string if both 'text' and 'message' are empty/null
    coalesce(
        nullif(trim(text), ''),
        nullif(trim(message), ''),
        '[No Content Provided]' -- <--- ADDED THIS FALLBACK STRING
    ) as message_text,
    sender_id,
    media_type,
    downloaded_image_path,
    length(coalesce(
        text,
        message,
        '' -- Added for length calculation if both text/message are null
    )) as message_length,
    case
        when downloaded_image_path is not null then true
        else false
    end as has_image
from raw
select distinct channel_name as channel_id
from {{ ref('stg_telegram_messages') }}
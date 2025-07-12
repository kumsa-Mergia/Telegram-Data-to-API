select distinct cast(date as date) as date_id
from {{ ref('stg_telegram_messages') }}
{{ config(materialized='view') }}

with yolo as (
    select
        row_number() over () as detection_id,  -- ✅ generate a surrogate key
        message_id,
        detected_object_class,
        confidence_score
    from {{ ref('stg_yolo_detections') }}  -- ✅ use staging model instead of raw source
),

messages as (
    select
        message_id,
        channel_id,
        date_id as date,
        message_length
    from {{ ref('fct_messages') }}
)

select
    y.detection_id,
    y.message_id,
    y.detected_object_class,
    y.confidence_score,
    m.channel_id,
    m.date
from yolo y
join messages m on y.message_id = m.message_id

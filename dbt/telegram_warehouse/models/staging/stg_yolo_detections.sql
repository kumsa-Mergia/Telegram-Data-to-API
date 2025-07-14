{{ config(materialized='view') }}

with source as (

    select *
    from {{ source('external_sources', 'yolo_detections') }}

),

renamed as (

    select
        cast(message_id as bigint) as message_id,
        detected_object_class,
        round(confidence_score::numeric, 4) as confidence_score
    from source

)

select * from renamed

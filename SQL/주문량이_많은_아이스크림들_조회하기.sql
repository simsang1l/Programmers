with j as (
    select
        FLAVOR
        , sum(total_order) as total_order
    from
        JULY
    group by
        FLAVOR
)
, f as (
    select
        flavor
        , sum(total_order) as total_order
    from
        first_half
    group by
        flavor
)
select
    j.flavor
from 
    j
    inner join 
        f
        on j.flavor = f.flavor
group by 
    j.flavor
order by 
    sum(j.total_order + f.total_order) desc
limit 3
;
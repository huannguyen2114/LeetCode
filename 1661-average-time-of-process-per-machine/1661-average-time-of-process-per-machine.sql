# Write your MySQL query statement below
select s.machine_id, round(avg(e.timestamp - s.timestamp), 3) as processing_time from Activity e join Activity s where e.activity_type = "end" and s.activity_type = "start" and e.machine_id = s.machine_id GROUP BY s.machine_id;
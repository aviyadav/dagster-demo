import dagster as dg
from .jobs import car_price_job

car_price_schedule = dg.ScheduleDefinition(
    job=car_price_job,
    cron_schedule="* * * * *",  # Every minute
)

# This schedule will run the car_price_job every minute.
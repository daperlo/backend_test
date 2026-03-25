from datetime import datetime, timedelta, time

def generate_slots(start: time, end: time, duration_minutes: int = 30):
    slots = []

    current = datetime.combine(datetime.today(), start)
    end_dt = datetime.combine(datetime.today(), end)

    delta = timedelta(minutes=duration_minutes)

    while current + delta <= end_dt:
        slot_start = current.time()
        slot_end = (current + delta).time()

        slots.append({
            "start_time": slot_start,
            "end_time": slot_end
        })

        current += delta

    return slots
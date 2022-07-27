# Mars hours = h, minutes = m, work_time = k, work_schedule_periods_starts_at = m/2 (performs twice an hour)
# n = trains departure every day in their strict time schedule
# Goal: find t = time of end of 1st work in hour
# Inconvenient = Train that departures within work_time

error = 'Please enter correct integers: trains up to 10"5", hours in day up to 10^9, minutes in hour: evens ' \
        'up to 10^9; work time: up to half of the minutes in hour, departure hour and minutes:' \
        'up to hours in a day and minutes in an hour'
def inputter_int(input_descripton, arg_error, agr_not_less, agr_not_much, arg_is):
    while True:
        try:
            i = int(input(input_descripton))
            if i < agr_not_less or i > agr_not_much or i == arg_is or arg_is is True:
                print(arg_error)
                continue
            return i
            break
        except:
            print(arg_error)
            continue
n = inputter_int('How many trains: ', error, 1, 10000, 0)
h = inputter_int('How many hours in a day at Mars: ', error, 1, 1000000000, 0)
while True:
    try:
        m = inputter_int('How many minutes in an hour at Mars: ', error, 1, 1000000000, 0)
        if m %2 != 0:
            print(error)
            continue
        break
    except:
        print(error)
        continue
k = inputter_int('How many minutes required for the work: ', error, 1, m/2, 0)

trains = {}
i = 0
while i < n:
    dep_i = int(i+1)
    dep_h_desc = f"Train # {i + 1} departure hour: "
    dep_h = inputter_int(str(dep_h_desc), error, 0, h, h)
    dep_m_desc = f"Train # {i + 1} departure minute: "
    dep_m = inputter_int(str(dep_m_desc), error, 0, m, m)
    trains[dep_i] = [dep_h, dep_m]
    i = i + 1
print(trains)

def work_timing(i):
    work_time_start = {1: 0, 2: int(m / 2)}
    work_time_start[1] = (work_time_start[1] + i)
    work_time_start[2] = (work_time_start[2] + i)
    while work_time_start[1] >= m / 2:
        work_time_start[1] = int(work_time_start[1] - m / 2)
        work_time_start[2] = int(work_time_start[2] - m / 2)
    return work_time_start
def find_out_busy_munutes(j):
    corr_time_start = work_timing(j)
    busy_minutes = [x for x in range(corr_time_start[1] + 1, corr_time_start[1] + k, 1)] + \
                   [x for x in range(corr_time_start[2] + 1, corr_time_start[2] + k, 1)]
    for minute in busy_minutes:
        if minute >= m:
            busy_minutes[busy_minutes.index(minute)] = minute - m
    return busy_minutes

start_minute_to_inconvenient_hash = {}

for first_work_starts_minute in range(0,m+1,1):
    inconvenient_trains = []
    for i in range(1,n+1,1):
        for work_minute in find_out_busy_munutes(first_work_starts_minute):
            if trains.get(i)[1] == work_minute:
                inconvenient_trains.append(i)
    start_minute_to_inconvenient_hash[first_work_starts_minute] = [x for x in inconvenient_trains]

print(start_minute_to_inconvenient_hash)


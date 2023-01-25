def study_schedule(permanence_period: list, target_time: int):
    students_online = 0

    try:
        for period in permanence_period:
            login, logoff = period
            if login <= target_time and logoff >= target_time:
                students_online += 1
        return students_online
    except TypeError:
        return None

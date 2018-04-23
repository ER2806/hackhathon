def preparatory_computation(pt_duration, pt_number, fq):
    step_duration = float(1)/float(fq)
    start_time = step_duration - (pt_number * pt_duration % step_duration)
    return start_time, step_duration

def parse_pocket(learn_data, pt_number):
    fqs = [fq for fq in range(8, 31)]
    fq_amps = []
    pt_duration = 0.5
    for fq in fqs:
        start_time, step_duration = preparatory_computation(pt_duration, pt_number, fq)
        time_marks = []
        while start_time < pt_duration:
            time_marks.append(start_time)
            start_time += step_duration
        freq_response = []
        for time in time_marks:
            freq_response.append(learn_data[int((time/pt_duration)*len(learn_data))])
        #print freq_response
        fq_amps.append(freq_response)
    return fq_amps



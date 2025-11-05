def summarize_sensor_data(readings):
    if not readings:
        return []
    readings.sort()
    maximums = []
    curr_sensor_id = readings [0] [0] 
    for i in range (1, len(readings)):
        if readings[i] [0] != curr_sensor_id:
            maximums.append(readings [i-1])
            curr_sensor_id = readings[i] [0]
    maximums.append(readings[-1])

    return maximums



readings = [
	('SensorB', 25.4),
	('SensorA', 22.1),
	('SensorB', 26.1), 
	('SensorC', 30.5),
	('SensorA', 21.9),  
	('SensorB', 25.9)
]

result = summarize_sensor_data(readings)
print (result)
print(summarize_sensor_data([]))
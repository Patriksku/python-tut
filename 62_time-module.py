import time

# epoch = a date and time from which a computer measures system time
# -> when your computer thinks time began (reference point)

print(time.ctime(0))  # convert a time expressed in seconds since epoch to a readable string

print(time.time())  # return current seconds since epoch

print(time.ctime(time.time()))

time_object = time.localtime()
# time_object = time.gmtime()  # UTC
print(time_object)

local_time = time.strftime("%Y %B %d %H:%M:%S", time_object)  # To make the time-object readable
print(local_time)


time_string = "20 April, 2020"
time_object_from_string = time.strptime(time_string, "%d %B, %Y")  # Converts a string-representation of a time and/or date to a time-object
print(time_object_from_string)


# (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string_from_tuple = time.asctime(time_tuple)
print(time_string_from_tuple)


# (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string_from_tuple = time.mktime(time_tuple)  # Will convert the time from a tuple to seconds since epoch
print(time_string_from_tuple)




class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def addTime(self, other_time):
        total_hours = self.hours + other_time.hours
        total_minutes = self.minutes + other_time.minutes

        if total_minutes >= 60:
            total_hours += total_minutes // 60
            total_minutes %= 60

        return Time(total_hours, total_minutes)

    def displayTime(self):
        print(f"{self.hours} hr and {self.minutes} min")

    def displayMinute(self):
        total_minutes = (self.hours * 60) + self.minutes
        print(total_minutes, "minutes")

time1 = Time(2, 50)
time2 = Time(1, 20)

result_time = time1.addTime(time2)

print("Time 1:")
time1.displayTime()
time1.displayMinute()

print("Time 2:")
time2.displayTime()
time2.displayMinute()

print("Total Time:")
result_time.displayTime()
result_time.displayMinute()

class Time:

    def __init__(self,seconds):
        self.seconds = seconds

    def convert_to_minutes(self):
        if self.seconds < 60:
           return self.seconds
        else:
           minute = int(self.seconds/60)
           sec = self.seconds% 60
           return "{}min:{}sec".format(minute,sec)

    def convert_to_hours(self):
        if self.seconds < 60:
            h =0
            minute = 0
            sec = self.seconds
            return "{}:{}:{}".format(h,minute,sec)
        elif 60 < self.seconds < 3600:
            h = 0
            minute = int(self.seconds/60)
            sec = self.seconds % 60
            return "{}:{}:{}".format(h, minute, sec)
        elif self.seconds >= 3600:
            h = int(self.seconds/3600)
            if self.seconds - 3600 < 60:
               minute =0
            else:
                minute = int((self.seconds - 3600) / 60)
            sec = int(self.seconds-3600)%60
            return "{}:{}:{}".format(h, minute, sec)


result =Time(3850)
print(result.convert_to_minutes())
print(result.convert_to_hours())
from weather import *

weather_instance = Weather()
current_date = datetime.date.today()

print(weather_instance.get_season(current_date))
weather_instance.get_temp()

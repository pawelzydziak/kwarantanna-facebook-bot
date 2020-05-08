import requests
import facebook
import datetime
import json

week_days = ["poniedziałek", "wtorek", "środa", "czwartek", "piątek"]
with open('/home/pzydziak/PycharmProjects/kwarantannaBot/data.json') as json_file:
  data = json.load(json_file)

access_page = data["access_page"]
access_user = data["access_user"]
user_id = data["user_id"]
app_secret = data["app_secret"]
page_id = data["page_id"]

client = facebook.GraphAPI(access_token=access_page, version="3.0")

current_week_day = datetime.datetime.today().weekday()
# print(week_days[current_week_day])

how_many_days = datetime.date.today() - datetime.date(2020, 3, 13)
# print(how_many_days.days)

msg = "[CRON PYTHON BOT TEST] " + "#" + str(how_many_days.days) + ":" + " Dziś jest " + str(week_days[current_week_day]) + "."
# print(msg)

client.put_object(parent_object=page_id, connection_name="feed", message=msg)

import schedule
import time
from bot import InstagramEngagementBot

def job():
    bot = InstagramEngagementBot(instagram_api)
    bot.like_post('12345')
    bot.comment_on_post('12345', 'Great post!')

def run_scheduler():
    schedule.every(1).hour.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)
    
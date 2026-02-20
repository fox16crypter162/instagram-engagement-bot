
from bot import InstagramEngagementBot

class EngagementTask:
    def __init__(self, bot, post_id, comment=None):
        self.bot = bot
        self.post_id = post_id
        self.comment = comment

    def perform_task(self):
        self.bot.like_post(self.post_id)
        if self.comment:
            self.bot.comment_on_post(self.post_id, self.comment)
    
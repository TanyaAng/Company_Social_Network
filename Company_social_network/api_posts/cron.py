from django_cron import CronJobBase, Schedule

from datetime import timedelta
from django.utils import timezone

from Company_social_network.api_posts.models import Post


class MyCronJob(CronJobBase):
    RUN_EVERY_DAY = 24 * 60

    schedule = Schedule(run_every_mins=RUN_EVERY_DAY)
    code = 'Company_social_network.api_posts.my_cron_job'

    def do(self):
        ten_days_ago = timezone.now() - timedelta(hours=10)
        Post.objects.filter(deleted=True, date_deleted__lte=ten_days_ago).delete()

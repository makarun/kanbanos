from django.db import models
from django.utils import timezone

class Task(models.Model):
    TAKS_PRIORITY = (
            (1, 'Do First'),
            (2, 'Schedule'),
            (3, 'Delegate'),
            (4, 'Don’t Do'),
        )
    TASK_CATEGORY = (
            (1, 'To Do'),
            (2, 'Doing'),
            (3, 'Done'),
            (4, 'Aborted'),
        )
    author = models.ForeignKey('auth.User')
    date = models.DateTimeField(default=timezone.now, blank=True)
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    # Eisenhower Matrix Style
    priority = models.PositiveSmallIntegerField(choices=TAKS_PRIORITY)
    category = models.PositiveSmallIntegerField(choices=TASK_CATEGORY)

    def __str__(self):
        return self.title

class Stage(models.Model):

    task = models.ForeignKey('todo.Task', related_name='stages')
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    date = models.DateTimeField(default=timezone.now, blank=True)
    achieved = models.BooleanField(default=False)

    def change_achieved(self):
        # if self.achieved == True:
        #     self.achieved = False
        # else:
        #     self.achieved = True
        self.achieved = not self.achieved
        # = not achieved
        self.save()

    def __str__(self):
        return self.title
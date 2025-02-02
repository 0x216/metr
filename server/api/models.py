from django.db import models
from hashid_field import HashidAutoField
from api.utils import Counter


def display_option_validator(item):
    return item in DISPLAY_OPTIONS


class Room(models.Model):
    id = HashidAutoField(primary_key=True, salt='room.id')
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    use_color = models.BooleanField(default=True)

    def online_counter(self):
        return Client.objects.filter(room=self, time_destroyed=None).count()

    def is_online(self):
        return self.id in Counter.admin_counter


class Question(models.Model):
    id = HashidAutoField(primary_key=True, salt='question.id')
    time_created = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey(Room, models.CASCADE)
    # Name of widget to use when data is displayed
    display_option = models.CharField(max_length=100, validators=[display_option_validator])
    value = models.CharField(max_length=1000)

    @property
    def mode_rate(self):
        return 0

    @property
    def mean_rate(self):
        mean = 0
        clients = Client.objects.filter(room=self.room, time_destroyed=None).all()
        for client in clients:
            try:
                mean += NumericAnswer.objects.filter(client=client, question=self).latest('time_created').value
            except NumericAnswer.DoesNotExist:
                mean += DISPLAY_OPTIONS[self.display_option][1]
        return mean / len(clients) if len(clients) else DISPLAY_OPTIONS[self.display_option][1]

    @property
    def median_rate(self):
        return 0


class Client(models.Model):
    id = HashidAutoField(primary_key=True, salt='client.id')
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)
    time_destroyed = models.DateTimeField(null=True, default=None)


class Answer(models.Model):
    type: str = None

    id = HashidAutoField(primary_key=True, salt='answer.id')
    time_created = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    question = models.ForeignKey(Question, models.CASCADE)

    class Meta:
        abstract = True


class NumericAnswer(Answer):
    type = 'numeric_answers'
    value = models.FloatField()


# Option name: [valid answer type, default value]
DISPLAY_OPTIONS = {
    'numeric_range_maximum': [NumericAnswer, 100],
    'numeric_range_optimum': [NumericAnswer, 50],
}

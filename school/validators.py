
from rest_framework.exceptions import ValidationError
import re


class VideoCustomValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        reg = re.compile('^(https?://)?(www\.)?youtube\.com/.+$')
        tmp_val = dict(value).get(self.field)
        if tmp_val is not None:
            if not bool(reg.match(tmp_val)):
                raise ValidationError('Ссылки должны быть только на видео с сайта youtube.com.')


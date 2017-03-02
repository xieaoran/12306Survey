import re
import urllib2
from threading import Thread

import settings


class Grabber(Thread):

    @property
    def survey_number_re(self):
        return self._survey_number_re

    @property
    def survey_number_list(self):
        return self._survey_number_list

    def __init__(self):
        super(Grabber, self).__init__()
        self._survey_number_re = re.compile(settings.SURVEY_NUMBER_REGEX)
        self._survey_number_list = []

    def run(self):
        request = urllib2.Request(settings.SURVEY_LIST_URL)
        response = urllib2.urlopen(request)
        response_text = response.read()
        response.close()
        for survey_number_td in self.survey_number_re.finditer(response_text):
            self.survey_number_list.append(survey_number_td.group(1))

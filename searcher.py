import urllib
import urllib2
from threading import Thread

import settings


class Searcher(Thread):
    @property
    def id_number(self):
        return self._id_number

    @property
    def survey_numbers(self):
        return self._survey_numbers

    @property
    def failed_numbers(self):
        return self._failed_numbers

    def __init__(self, id_number, survey_numbers):
        super(Searcher, self).__init__()
        self._id_number = id_number
        self._survey_numbers = survey_numbers
        self._failed_numbers = []

    def run(self):
        for survey_number in self.survey_numbers:
            try:
                post_data = {
                    settings.ID_NUMBER_KEY: self.id_number,
                    settings.SURVEY_NUMBER_KEY: survey_number
                }
                request = urllib2.Request(settings.SURVEY_SEARCH_URL, urllib.urlencode(post_data))
                response = urllib2.urlopen(request)
                response_text = response.read()
                response.close()
                if settings.VALID_CRITERIA in response_text:
                    print "Survey %s Rewarded" % survey_number
            except:
                self.failed_numbers.append(survey_number)

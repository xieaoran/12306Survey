import sys

import grabber
import searcher
import settings

gr = grabber.Grabber()
gr.start()
gr.join()

thread_list = []

each = len(gr.survey_number_list) / settings.THREAD_COUNT

id_number = sys.argv[1]

for thread_index in xrange(settings.THREAD_COUNT):
    start_index = each * thread_index
    end_index = start_index + each - 1
    survey_numbers = gr.survey_number_list[start_index:end_index]
    sr = searcher.Searcher(id_number, survey_numbers)
    thread_list.append(sr)
    sr.start()

last_survey_numbers = gr.survey_number_list[each * settings.THREAD_COUNT:]
last_sr = searcher.Searcher(id_number, last_survey_numbers)
thread_list.append(last_sr)
last_sr.start()

failed_numbers = []
for thread in thread_list:
    thread.join()
    for failed_number in thread.failed_numbers:
        failed_numbers.append(failed_number)

while len(failed_numbers) != 0:
    failed_sr = searcher.Searcher(id_number, failed_numbers)
    failed_sr.start()
    failed_sr.join()
    failed_numbers = failed_sr.failed_numbers

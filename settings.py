# coding=utf-8

SURVEY_LIST_URL = "http://dynamic.12306.cn/surweb/rewardList/reward_list_11.jsp"

SURVEY_NUMBER_REGEX = r"<td>(\d{10})</td>"

SURVEY_SEARCH_URL = "http://dynamic.12306.cn/surweb/questionnaireAction.do?method=querySurveyListByFileNo"

ID_NUMBER_KEY = "idNO"

SURVEY_NUMBER_KEY = "surveyNo"

VALID_CRITERIA = "有效"

THREAD_COUNT = 10

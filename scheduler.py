#stucture: problems = {1: [question_title_slug, question_title_slug, ...], 2: [question_title_slug, question_title_slug, ...], 3: [question_title_slug, question_title_slug, ...]}

import requests

url_problem_prefix = "https://leetcode.com/problems/"

url_json = "https://leetcode.com/api/problems/algorithms/"
r = requests.get(url=url_json)

data = r.json()
dict_of_problems = {1: [], 2: [], 3: []}
for problem in data.get("stat_status_pairs", []):
    dict_of_problems[problem.get("difficulty", {}).get("level")].append(problem.get("stat", {}).get("question__title_slug"))

if __name__ == "__main__":
    print(data) #displays the json given by the url
    print(len(data.get("stat_status_pairs", [])))
    print(dict_of_problems) #grabs the title slugs (used for suffix of urls)

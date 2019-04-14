#stucture: problems = {1: [question_title_slug, question_title_slug, ...], 2: [question_title_slug, question_title_slug, ...], 3: [question_title_slug, question_title_slug, ...]}

#weekdays: 1 medium, 1 easy, 2 days work, 1 day break
#weekends: which ever
import requests
#import webbrowser

url_problem_prefix = "https://leetcode.com/problems/"

url_json = "https://leetcode.com/api/problems/algorithms/"
r = requests.get(url=url_json)

data = r.json()
dict_of_problems = {1: [], 2: [], 3: []}
for problem in data.get("stat_status_pairs", []):
    if problem.get("paid_only") == False:
        dict_of_problems[problem.get("difficulty", {}).get("level")].append(problem.get("stat", {}).get("question__title_slug"))

if __name__ == "__main__":
    print(data) #displays the json given by the url
    print(len(data.get("stat_status_pairs", [])))
    print(dict_of_problems) #grabs the title slugs (used for suffix of urls)
    print(len(dict_of_problems[1]), len(dict_of_problems[2]), len(dict_of_problems[3]))

    problem_url = f"{url_problem_prefix}{dict_of_problems[1][0]}"
    #webbrowser.open(problem_url)

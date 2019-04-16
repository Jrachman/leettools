#to grab new questions, we can create a new dict for is_new_question == True for every check

#stucture: problems = {1: [question_title_slug, question_title_slug, ...], 2: [question_title_slug, question_title_slug, ...], 3: [question_title_slug, question_title_slug, ...]}

# different parameters to customize study strategy:
#    - days till interview / expectec time to completion
#    - percent of time in day willing to devote to leetcode
#    - specific skills wanting to focus on
#    - weekly pattern (every day, every other day, work-work-break, etc.)
#    - difficulty selection (no hards, complete easys then meds, med-easy)
#    - target overall leetcode question coverage percentage
#    - bring already completed
#
# https://zapier.com/blog/smart-goals/
#    - the most achievable goals you can set: HARD mnemonic
#      - Heartfelt: enriching your own life and the lives of others. Who else is impacted positively by the achievement of this goal?
#      - Animated: and vivid in your imagination. What does my business, career, or life look like when I achieve this goal? (Visualize it!)
#      - Required: for personal or professional well-being. Why is this goal so necessary? What are the stakes (personal or professional)?
#      - Difficult: forcing you to leave your comfort zone and learn new skills. What will I have to learn to accomplish this? Where will I have to stretch myself? (Record this answer in great detail.)
#    - build a SMART plan
#      - Specific
#      - Measurable
#      - Achievable
#      - Realistic
#      - Time-bounded


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
    #print(data) #displays the json given by the url
    #print(len(data.get("stat_status_pairs", [])))
    #print(dict_of_problems) #grabs the title slugs (used for suffix of urls)
    print(len(dict_of_problems[1]), len(dict_of_problems[2]), len(dict_of_problems[3]))

    problem_url = f"{url_problem_prefix}{dict_of_problems[1][0]}"
    print(problem_url)
    #webbrowser.open(problem_url)

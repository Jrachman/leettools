#to grab new questions, we can create a new dict for is_new_question == True for every check

#stucture: problems = {1: [question_title_slug, question_title_slug, ...], 2: [question_title_slug, question_title_slug, ...], 3: [question_title_slug, question_title_slug, ...]}

# different parameters to customize study strategy:
#    - days till interview / expected time to completion
#    - percent of time in day willing to devote to leetcode
#    - specific skills wanting to focus on
#    - weekly pattern (every day, every other day, work-work-break, etc.)
#    - difficulty selection (no hards, complete easys then meds, med-easy)
#    - target overall leetcode question coverage percentage
#    - bring already completed

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

#compare min_len and time_range
#   - if min_len <= time_range, can complete pairings within time frame and can throw in single/double problems from the remaining problems
#   - if min_len > time_range, going to have to not be able to complete all of the pairings or choose a different pattern

#19 days/month for work-work-break method

#work strategies:
#   - weekend vs no weekend ask option
#   -
#   for pairs:
#      - 1-1 every day till pairs run out then go through whatever is left
#      - 2-1 every day till one runs out or they end up lining up
#      - (alternate 1 each day) (if really want to space out)
#   for singles:
#      - 1 question/day
#      - 2 questions/day
#      - (3 questions/day) (if you are really grinding)
#      -


import requests
import random
import math

url_problem_prefix = "https://leetcode.com/problems/"

def get_problems():
    url_json = "https://leetcode.com/api/problems/algorithms/"
    r_data = requests.get(url=url_json).json()
    num_to_str = {1: "e", 2: "m", 3: "h"}
    dict_of_problems = {"e": [], "m": [], "h": []}

    for problem in r_data.get("stat_status_pairs", []):
        if problem.get("paid_only") == False:
            dict_of_problems[num_to_str[problem.get("difficulty", {}).get("level")]].append(problem.get("stat", {}).get("question__title_slug"))

    for key in dict_of_problems.keys():
        random.shuffle(dict_of_problems[key])

    return dict_of_problems

def user_personalization_entries():
    problems = get_problems()

    while True: #difficulty range
        difficulty_range = input("Choose your difficulty range. [e/em/m/mh/h]: ")

        if difficulty_range in ["e", "em", "m", "mh", "h"]:
            break

        print("Please enter a valid answer.")

    while True: #amount of time for grinding
        try:
            time_range = int(input("How many days in grind period? [i.e., '120' = 120 days]: "))
            break
        except:
            print("Please enter a valid answer.")

    #below is just for experimentation
    len_of_problems = [len(problems[i]) for i in list(difficulty_range)]
    min_len = min(len_of_problems)
    sum_len = sum(len_of_problems)
    remaining_len = max(len_of_problems) - min(len_of_problems)

    print(len_of_problems, min_len, sum_len, remaining_len)
    print(min_len/time_range)


if __name__ == "__main__":
    #print(data) #displays the json given by the url
    #print(len(data.get("stat_status_pairs", [])))
    #print(dict_of_problems) #grabs the title slugs (used for suffix of urls)

    """
    dict_of_problems = get_problems()
    print(len(dict_of_problems[1]), len(dict_of_problems[2]), len(dict_of_problems[3]))
    print(len(dict_of_problems[1]) + len(dict_of_problems[2]) + len(dict_of_problems[3]), len(dict_of_problems[1]) + len(dict_of_problems[2]))

    problem_url = f"{url_problem_prefix}{dict_of_problems[1][0]}"
    print(problem_url)
    """

    user_personalization_entries()

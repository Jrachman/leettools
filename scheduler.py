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
#   for pairs:
#      - 1-1 every day till pairs run out then go through whatever is left
#      - 2-1 every day till one runs out or they end up lining up
#      - (alternate 1 each day) (if really want to space out)
#   for singles:
#      - 1 question/day
#      - 2 questions/day
#      - (3 questions/day) (if you are really grinding)

#for the future iterations:
#   - possibly look into dynamic question choosing like Connect with confidence scales and weighing problems

#example of ics for all day:
#   - BEGIN:VEVENT
#     DTSTART;VALUE=DATE:20190503
#     DTEND;VALUE=DATE:20190504
#     DTSTAMP:20190503T184637Z
#     UID:1stn8i34gpmp7vg0p06aamhren@google.com
#     CREATED:20190503T184611Z
#     DESCRIPTION:bitch<a href="http://www.google.com" id="ow736" __is_owner="true">hello world bitch</a>
#     LAST-MODIFIED:20190503T184611Z
#     LOCATION:
#     SEQUENCE:0
#     STATUS:CONFIRMED
#     SUMMARY:hello world
#     TRANSP:TRANSPARENT
#     END:VEVENT

#THING TO KEEP IN MIND: there are a lot of params that are just going down the pipeline like problems and start_date so just set as variable then grab
#   (look at all of the "here"'s)


import requests
import random
import math
from ics import Calendar, Event
import datetime

def get_problems():
    url_json = "https://leetcode.com/api/problems/algorithms/"
    r_data = requests.get(url=url_json).json()
    num_to_str = {1: "e", 2: "m", 3: "h"}
    dict_of_problems = {"e": [], "m": [], "h": []}

    for problem in r_data.get("stat_status_pairs", []):
        if problem.get("paid_only") == False:
            dict_of_problems[num_to_str[problem.get("difficulty", {}).get("level")]].append((problem.get("stat", {}).get("question__title"), problem.get("stat", {}).get("question__title_slug")))

    for key in dict_of_problems.keys():
        random.shuffle(dict_of_problems[key])

    return dict_of_problems

def user_personalization_entries():
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

    while True:
        try:
            date_start = datetime.datetime.strptime(input("Choose your start date. [format: yyyy-mm-dd]: "), "%Y-%m-%d").date()
            if date_start >= datetime.date.today():
                break
            print("Please enter a valid answer.")
        except:
            print("Please enter a valid answer.")

    """
    while True: #weekends?
        weekends = input("Will you practice on the weekends? [y/n]: ")

        if weekends in ["y", "n"]:
            break

        print("Please enter a valid answer.")
    """

    return difficulty_range, time_range, date_start#, weekends

def strat_key_to_name(strat_key):
    abbr_to_word = {"e": "easy", "m": "medium", "h": "hard"}
    diffs, num_of_prob = strat_key[0], strat_key[1]

    output_name =  ", ".join([f"{num_of_prob[i]} {abbr_to_word[diffs[i]]}" for i in range(len(diffs))])
    output_name += " problem(s) per day"

    return output_name

def analyze_strategies(problems, difficulty_range):
    #just ask for continuation (future implementation)
    strategies = dict()

    len_of_problems = [len(problems[i]) for i in difficulty_range]

    max_len = max(len_of_problems)
    min_len = min(len_of_problems)
    sum_len = sum(len_of_problems)
    remaining_len = max_len - min_len

    if len(len_of_problems) == 1: #for single difficulty
        strategies[(difficulty_range, (1,))] = min_len # "1 problem per day"

        for num in [2, 3]:
            strategies[(difficulty_range, (num,))] = int(min_len/num) + int(min_len%num) # f"{num} problems per day"

        #need to add 2 problems a day, 1 day break AND 3 problems a day, 1 day break

    else: #for 2 difficulties
        strategies[(difficulty_range, (1, 1))] = min_len # "1 pair of problems per day (without leftovers)"

        if len_of_problems[0]/2 > len_of_problems[1]:
            strategies[(difficulty_range, (2, 1))] = len_of_problems[0]/2 # f"2 {difficulty_range[0]} and 1 {difficulty_range[1]}"
        else:
            strategies[(difficulty_range, (2, 1))] = int(min_len/2) + int(min_len%2) # f"2 {difficulty_range[0]} and 1 {difficulty_range[1]} (without leftovers)"

        if len_of_problems[0] < len_of_problems[1]/2:
            strategies[(difficulty_range, (1, 2))] = len_of_problems[1]/2 # f"2 {difficulty_range[1]} and 1 {difficulty_range[0]}"
        else:
            strategies[(difficulty_range, (1, 2))] = int(max_len/2) + int(max_len%2) # f"2 {difficulty_range[1]} and 1 {difficulty_range[0]} (without leftovers)"

    return strategies

# need to add function to find strategy closest to the time frame and then also give the increasing order of the strategies by time
def strat_best_fit(strategies, time_range):

    best_fits = dict()

    best_fits["closest"] = []
    closest_abs_diff = -1

    for key, value in strategies.items():
        abs_diff = abs(time_range - value)
        print(closest_abs_diff, abs_diff, key, value)

        if closest_abs_diff == -1:
            closest_abs_diff = abs_diff

        if abs_diff == closest_abs_diff:
            best_fits["closest"].append(key)
        elif abs_diff < closest_abs_diff:
            best_fits["closest"] = [key]
            closest_abs_diff = abs_diff

    best_fits["incr"] = sorted(strategies.keys(), key=lambda x: strategies[x])

    return best_fits

def choose_strategy(best_fits, strategies, time_range):
    num = 0
    choices = f"Please choose one of the following strategies (time range selected: {time_range}):\n"

    list_of_ord_strats = []
    for cat, strats in best_fits.items():
        choices += f"   {cat.upper()}\n"

        for strat in strats:
            percent_complete = (sum(strat[1]) * strategies[strat])/sum([len(problems[i]) for i in strat[0]]) * 100
            choices += f"      [{num}] ({strategies[strat]} days, {100.0 if percent_complete > 100 else percent_complete:.1f}% complete) {strat_key_to_name(strat)}\n"
            list_of_ord_strats.append(strat)
            num += 1

    choices += "Enter number here: "

    while True:
        try:
            choice = int(input(choices))
            if 0 <= choice <= len(strategies)+1:
                return list_of_ord_strats[choice], strategies[list_of_ord_strats[choice]]
            print(f"Invalid entry not in range 0 to {len(strategies)+1}")
        except:
            print("Invalid entry not an integer")

def create_calendar(strat_choice, n_days, problems, date_start):
    #different ways of iterating (until days are up)
    #   - 1 difficulty
    #     - pop n problems from difficulty
    #     - add info to calendar then append
    #   - 2 difficulties
    #     - pop n problems and m problems from respective difficulties
    #     - add info to calendar then append

    c = Calendar(creator="LeetTools: created by Julian Rachman")
    t = "00:00:00"
    nl = "\n"
    curr_date = date_start #current format: yyyy-mm-dd
    diffs, num_of_prob = strat_choice[0], strat_choice[1]

    for i in range(n_days):
        e = Event() # create events through strat_best_fit
        problems_of_the_day = dict(problems[diff].pop() for diff in diffs)
        e.name = f"[LeetTools] Day {i+1}: {', '.join(problems_of_the_day)}"
        e.begin = f"{curr_date.strftime('%Y%m%d')} {t}"
        curr_date += + datetime.timedelta(days=1)
        e.end = f"{curr_date.strftime('%Y%m%d')} {t}"
        composition = [f'<a href=https://leetcode.com/problems/{problems_of_the_day[title]}>{title}</a>' for title in problems_of_the_day]
        comp_body = '\n   - '.join(composition)
        e.description = f"Problem(s) of the day:{nl}   - {comp_body}"
        e.make_all_day()
        c.events.add(e)

    with open('test.ics', 'w') as f:
        f.writelines(c)

    return c.events

if __name__ == "__main__":
    problems = get_problems()
    difficulty_range, time_range, date_start = user_personalization_entries()
    strategies = analyze_strategies(problems, difficulty_range)
    best_fits = strat_best_fit(strategies, time_range)
    strat_choice, n_days = choose_strategy(best_fits, strategies, time_range)

    cal = create_calendar(strat_choice, n_days, problems, date_start)
    print(cal)

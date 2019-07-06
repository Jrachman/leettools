from flask import Flask, render_template, request, flash, send_file
from forms import ChoiceForm, ResultForm
from flask_cors import CORS
import scheduler as sc
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'development key'
CORS(app)


@app.route('/', methods=['GET', 'POST'])
def contact():
    global strategies, problems, list_of_ord_strats, start_date

    choice_form = ChoiceForm()

    if request.method == 'GET':
        return render_template('index.html', form=choice_form)
    elif request.method == 'POST':
        if not choice_form.validate():
            flash('All fields are required.')
            return render_template('index.html', form=choice_form)
        else:
            problems = sc.get_problems()
            strategies = sc.analyze_strategies(problems, choice_form.diff_range.data)
            best_fits = sc.strat_best_fit(strategies, choice_form.grind_per.data)
            choices, list_of_ord_strats = sc.present_strategy(problems, best_fits, strategies, choice_form.grind_per.data)
            start_date = datetime(choice_form.start_year.data, choice_form.start_month.data, choice_form.start_day.data)
            result_form = ResultForm()
            result_form.strat_choice.choices = [(i, i) for i in range(len(list_of_ord_strats))]
            return render_template('result.html', form=result_form, data={"choices": choices, "time_range": choice_form.grind_per.data})


@app.route('/result.html', methods=['POST', 'GET'])
def result():
    choice = request.form["strat_choice"]
    strat_choice, n_days = sc.choose_strategy(int(choice), strategies, list_of_ord_strats)

    cal = sc.create_calendar(strat_choice, n_days, problems, start_date)
    print(cal)

    return render_template('success.html')


if __name__ == "__main__":
    app.run()

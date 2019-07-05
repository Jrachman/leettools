from flask import Flask, render_template, request, flash
from forms import ChoiceForm, ResultForm
from flask_cors import CORS
import scheduler as sc

app = Flask(__name__)
app.secret_key = 'development key'
CORS(app)


@app.route('/', methods=['GET', 'POST'])
def contact():
    choice_form = ChoiceForm()
    result_form = ResultForm()

    if request.method == 'GET':
        return render_template('index.html', form=choice_form)
    elif request.method == 'POST':
        print(choice_form.validate())
        if not choice_form.validate():
            flash('All fields are required.')
            return render_template('index.html', form=choice_form)
        else:
            problems = sc.get_problems()
            strategies = sc.analyze_strategies(problems, choice_form.diff_range.data)
            best_fits = sc.strat_best_fit(strategies, choice_form.grind_per.data)
            choices, list_of_ord_strats = sc.present_strategy(problems, best_fits, choice_form.grind_per.data)
            data = {
                "start_date": f"{choice_form.start_year.data}-{choice_form.start_month.data:02d}-{choice_form.start_day.data:02d}",
            }
            return render_template('result.html', form=result_form, data=data)


@app.route('/choices', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        req = request.json
        problems = sc.get_problems()
        strategies = sc.analyze_strategies(problems, req["diff_range"])
        best_fits = sc.strat_best_fit(strategies, int(req["grind_per"]))
        print(best_fits)
        choices, list_of_ord_strats = sc.present_strategy(problems, best_fits, strategies, int(req["grind_per"]))
        # list_of_ord_strats to be used later for better design
        # print(strat_choice, n_days)
        return f"<h2>{choices}<h2>"


if __name__ == "__main__":
    app.run()

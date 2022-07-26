import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def hello():
	return render_template('index.html')

get_plot = False

@app.route('/get_plot', methods=['GET', 'POST'])
def get_plot():
	if request.method == 'POST':
		year_1 = request.form['year_1']
		year_2 = request.form['year_2']
		year_3 = request.form['year_3']
		year_4 = request.form['year_4']
		year_1_capital = request.form['year_1_capital']
		year_2_capital = request.form['year_2_capital']
		year_3_capital = request.form['year_3_capital']
		year_4_capital = request.form['year_4_capital']
		desired_growth_rate = request.form['desired_growth_rate']
		years = [year_1, year_2, year_3, year_4]
		capitals = [year_1_capital, year_2_capital, year_3_capital, year_4_capital]
		for i in range(len(capitals)):
			capitals[i] = float(capitals[i])
		print(capitals)
		data = {}
		for i in range(len(years)):
			data[years[i]] = capitals[i]
		desired_growth = []
		desired_growth.append(float(year_1_capital))
		growth = float(year_1_capital)
		for i in range(len(capitals) - 1):
			growth *= float(desired_growth_rate)
			desired_growth.append(growth)
		plt.plot(years, capitals)
		plt.plot(years, desired_growth)
		plt.title("Trend")
		plt.xlabel("Years")
		plt.ylabel("Capital")
		plt.legend(["Actual growth", "Desired growth"])
		plt.savefig('static/my_plot.png')
		return render_template('index.html', get_plot = True, plot_url = 'static/my_plot.png', data = data)
	else:
		return render_template('index.html')

app.secret_key = 'some key that you will never guess'

#Run the app on localhost port 5000
if __name__ == "__main__":
    app.run('127.0.0.1', 5000, debug = True)



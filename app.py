from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Global variables to store data
expenses = []
salary = 0
financial_target = 0
target_date = None
normal_expenses_threshold = 0

@app.route('/', methods=['GET', 'POST'])
def index():
    global salary, financial_target, target_date, normal_expenses_threshold

    if request.method == 'POST':
        try:
            # Handling salary input
            if 'salary' in request.form:
                salary = float(request.form['salary'])

            # Handling expense input
            elif 'expense' in request.form:
                description = request.form['description']
                amount = float(request.form['amount'])
                category = request.form['category']
                date = request.form['date']
                
                # Add expense to the list
                expenses.append({'description': description, 'amount': amount, 'category': category, 'date': date})

            # Handling financial target input
            elif 'financial_target' in request.form:
                financial_target = float(request.form['financial_target'])
                target_date = request.form['target_date']

            # Handling normal expenses threshold input
            elif 'normal_expenses_threshold' in request.form:
                normal_expenses_threshold = float(request.form['normal_expenses_threshold'])
        except ValueError:
            pass  # Handle any invalid input gracefully

        # Redirect to clear form data after processing
        return redirect(url_for('index'))

    # Calculate total expenses and categorize them
    total_expenses = sum(exp['amount'] for exp in expenses)
    category_summary = {}
    for exp in expenses:
        if exp['category'] in category_summary:
            category_summary[exp['category']] += exp['amount']
        else:
            category_summary[exp['category']] = exp['amount']

    # Financial target savings suggestion
    savings_needed_per_day = 0
    savings_needed_per_month = 0
    savings_needed_per_year = 0
    if financial_target > 0 and target_date:
        target_date_obj = datetime.strptime(target_date, "%Y-%m-%d")
        today = datetime.today()
        days_left = (target_date_obj - today).days
        months_left = (target_date_obj.year - today.year) * 12 + target_date_obj.month - today.month
        years_left = target_date_obj.year - today.year

        savings_needed_per_day = financial_target / days_left if days_left > 0 else 0
        savings_needed_per_month = financial_target / months_left if months_left > 0 else 0
        savings_needed_per_year = financial_target / years_left if years_left > 0 else 0

    # Check if we are overspending
    overspending_alert = ""
    if total_expenses > salary and salary > 0:
        overspending_alert = "Warning: You are overspending. Please review your expenses."
    elif total_expenses > normal_expenses_threshold and normal_expenses_threshold > 0:
        overspending_alert = "Alert: Your expenses have exceeded the normal spending threshold!"

    # Render the page with the necessary data
    return render_template('index.html', expenses=expenses, salary=salary, total_expenses=total_expenses,
                           category_summary=category_summary, overspending_alert=overspending_alert,
                           financial_target=financial_target, savings_needed_per_day=savings_needed_per_day,
                           savings_needed_per_month=savings_needed_per_month, savings_needed_per_year=savings_needed_per_year,
                           target_date=target_date, normal_expenses_threshold=normal_expenses_threshold)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5002, debug=True)

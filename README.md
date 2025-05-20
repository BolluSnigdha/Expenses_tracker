 💸 Expense Tracker Web App

A simple yet effective expense tracking application built using Flask. This app helps you manage and categorize your daily expenses, track your salary, set financial goals, and monitor spending patterns with alerts when you exceed normal expense thresholds.


 🚀 Features

- Add, view, and categorize daily expenses
- Enter and update your monthly salary
- Set a financial target with a future date
- Get calculated savings needed per day/month/year
- Receive alerts for overspending
- Clean and interactive web interface


 🛠️ Tech Stack

- **Frontend**: HTML (via Jinja templates)
- **Backend**: Python (Flask)
- **Data Format**: JSON (`expenses.json`)
- **Server**: Localhost (Flask built-in server)

 📂 Project Structure
project-folder/
│
├── app.py # Main Flask application
├── expenses.json # Sample expenses data
├── templates/
│ └── index.html # HTML interface 



1. **Clone the repository**
```bash
git clone https://github.com/BolluSnigdha/Expenses-tracker.git
cd expense-tracker

2.Install dependencies
pip install flask
3.Run the app
python app.py
4.Open in browser
http://127.0.0.1:5002

📈 Calculations
Total Expenses: Sum of all entered expenses
Savings Suggestion:
Per Day / Month / Year required to meet your financial goal
Overspending Alert: Triggered when:
Total expenses > salary
Expenses exceed a user-defined threshold

👩‍💻 Author
Snigdha
Feel free to connect on https://github.com/BolluSnigdha

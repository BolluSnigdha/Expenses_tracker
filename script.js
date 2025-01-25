document.getElementById('salary-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const salary = document.getElementById('salary-input').value;
  
    const response = await fetch('/set_salary', {
      method: 'POST',
      body: new URLSearchParams({ salary }),
    });
    const data = await response.json();
  
    document.getElementById('salary-message').textContent = data.message;
    document.getElementById('expense-section').style.display = 'block';
    document.getElementById('target-section').style.display = 'block';
  });
  
  document.getElementById('expense-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const description = document.getElementById('description').value;
    const amount = document.getElementById('amount').value;
    const date = document.getElementById('date').value;
  
    const response = await fetch('/add_expense', {
      method: 'POST',
      body: new URLSearchParams({ description, amount, date }),
    });
    const data = await response.json();
  
    document.getElementById('expense-message').textContent = data.message;
    document.getElementById('total-expenses').textContent = `$${data.total_expenses.toFixed(2)}`;
    document.getElementById('remaining-balance').textContent = `$${data.remaining_balance.toFixed(2)}`;
  });
  
  document.getElementById('target-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const target = document.getElementById('target-amount').value;
    const end_date = document.getElementById('target-date').value;
  
    const response = await fetch('/financial_target', {
      method: 'POST',
      body: new URLSearchParams({ target, end_date }),
    });
    const data = await response.json();
  
    if (data.error) {
      document.getElementById('target-result').textContent = data.error;
    } else {
      document.getElementById('target-result').innerHTML = `
        <p>You need to earn:</p>
        <ul>
          <li>Daily: $${data.daily_earnings.toFixed(2)}</li>
          <li>Weekly: $${data.weekly_earnings.toFixed(2)}</li>
          <li>Monthly: $${data.monthly_earnings.toFixed(2)}</li>
        </ul>
      `;
    }
  });
  
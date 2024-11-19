# Stock Picker

- This basic app offers users a straightforward approach to gain familiarity with navigating a stock trading platform.
- Through current and historical stock data, users can assess a stock’s performance.
- Stock data, stock tickers and charts are in real time.  Historical data is presented in a 5-year chart.
- Buy and sell features allow users to pick stocks from among the following list which includes pre-populated sample data for price/quantity amounts via a dropdown selection menu:
  - Google
  - General Electric
  - Microsoft
  - Amazon

- A preset limit of $5,000 has been included to purchase stocks. 
-	A preset limit of $5,000 has been included to sell stocks.
-	A reset button has been placed on the transactions purchased and sold pages, so users can reset account back to $0.00.
-	As each transaction is submitted (bought/sold), the transaction page will be updated to reflect new balances.
-	Once the transactions (bought/sold) reach the $5,000 limit, all further transactions will not be processed.  An alert will appear on the screen and the transactions above the allowable limit will appear in “red” as a signal to show these transactions will not be processed.

# Technologies Used

-	Django
-	Python
-	CSS
-	HTML
-	JavaScript
-	Bootstrap
-	TradingView – For stock prices/graphs and stock ticker widgets

# Suggested Future Enhancements

- Expand access to all securities on all stock exchanges rather than limited to four preset stocks.
- Buy and sell pages could be expanded to allow for access to all securities on all stock exchanges.
- Set up stock price alerts allowing users to purchase or sell a stock at a predetermined price.
-	Show portfolio stock positions/cash balances on homepage.
-	Search box for users to enter ticker symbols to get instant quotes on all stock exchanges.
-	Add a login feature so users can save their portfolios.
-	Allow a single user to add more than one portfolio to their account.

# Cloning and Running App

-	Clone GitHub repository
-	cd to local directory where files will be stored
-	Activate virtual environment:
    -  venv/scripts/activate
-	To run app, enter:
    -  python manage.py runserver
-	Development server will be started:
    -  http://127.0.0.1:8000/




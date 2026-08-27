# 🐍 5 Python API Practice Projects

The goal with these projects is to practice the following workflow:

**Read documentation → make request → inspect response → extract data → use the data in your program**

---

## 1. 🌤️ Weather CLI


**API:** Open-Meteo
<br>
**API Key:** Not required
<br>
**Difficulty:** ⭐⭐

### Goal

Build a command-line weather program.

```bash
python weather.py Port_of_Spain
```

### Example output

```text
Port of Spain
Temperature: 29°C
Wind: 18 km/h
Weather: Partly cloudy
```

### Practice

* `requests.get()`
* Query parameters with `params=`
* JSON
* Dictionaries
* Lists
* Command-line arguments
* Reading API documentation

---

## 2. 💱 Currency Converter

**API:** Frankfurter or ExchangeRate API
<br>
**API Key:** Depends on API
<br>
**Difficulty:** ⭐⭐½

### Goal

Build a currency conversion program.

```bash
python convert.py USD TTD 100
```

### Example output

```text
100 USD = 678.42 TTD
```

Then support:

```bash
python convert.py USD EUR 100
python convert.py GBP TTD 50
```

### Practice

* URL parameters
* JSON
* Dictionaries
* Floats
* Command-line arguments
* Invalid currency handling
* API documentation

---

## 3. 🎬 Movie Search CLI

**API:** OMDb API
<br>
**API Key:** Required
<br>
**Difficulty:** ⭐⭐⭐

### Goal

Search for a movie and display information about it.

```bash
python movie.py "Inception"
```

### Example output

```text
Inception
Year: 2010
Director: Christopher Nolan
IMDb Rating: 8.8
```

Try:

```bash
python movie.py "The Dark Knight"
python movie.py "Interstellar"
```

### Practice

* API keys
* Query parameters
* JSON
* Nested dictionaries
* Error handling
* Command-line arguments
* Extracting specific information from API responses

---

## 4. 📈 Cryptocurrency Price Tracker

**API:** CoinCap
<br>
**API Key:** Required
<br>
**Difficulty:** ⭐⭐⭐

### Goal

Build a command-line cryptocurrency price tracker.

```bash
python crypto.py BTC
```

### Example output

```text
Bitcoin (BTC)
Price: $79,220.00
```

Then make it support multiple cryptocurrencies:

```bash
python crypto.py BTC ETH SOL
```

### Example output

```text
Bitcoin     $79,220.00
Ethereum     $3,421.20
Solana         $182.43
```

### Practice

* API authentication
* HTTP headers
* Multiple API requests
* Loops
* JSON
* Functions
* Exceptions
* API errors
* Command-line arguments

---

## 5. 💰 Stock / Portfolio Tracker

**API:** Alpha Vantage or another market-data API
<br>
**API Key:** Required
<<<<<<< HEAD
<br>
=======

>>>>>>> 2d5930fe2e1892784cce6a2d7ccdf8c202c9c0d6
**Difficulty:** ⭐⭐⭐½

### Goal

Build a command-line stock price tracker.

```bash
python stock.py AAPL
```

### Example output

```text
Apple Inc.
Price: $XXX.XX
Change: +1.42%
```

Then support multiple stocks:

```bash
python stock.py AAPL MSFT NVDA
```

### Final challenge

Allow the user to enter how many shares they own and calculate the portfolio value.

```text
AAPL
Shares: 10
Price: $XXX.XX
Value: $X,XXX.XX
```

### Practice

* API keys
* Headers
* Query parameters
* JSON
* Functions
* Loops
* Data validation
* Calculations
* Error handling
* Program decomposition

---

# 📚 Recommended Order

Do them in this order:

```text
1. Weather
      ↓
2. Currency Converter
      ↓
3. Movie Search
      ↓
4. Crypto Tracker
      ↓
5. Stock / Portfolio Tracker
```

Each project should introduce a little more complexity.

| Project      | Main Skill                         |
| ------------ | ----------------------------------- |
| 🌤️ Weather  | `requests` fundamentals            |
| 💱 Currency  | Parameters + JSON                  |
| 🎬 Movies    | API keys + nested JSON             |
| 📈 Crypto    | Authentication + multiple requests |
| 💰 Portfolio | Combining everything               |

---

# 🧠 Rules For Every Project

Before asking for help, spend **20–30 minutes** investigating the API yourself.

### Step 1 — Find the documentation

Find the official API documentation.

### Step 2 — Understand authentication

Ask:

* Do I need an API key?
* Where do I put the API key?
* Is it a header?
* Is it a query parameter?
* Do I need `Bearer`?

### Step 3 — Find the endpoint

Figure out which endpoint gives you the information you need.

### Step 4 — Identify the parameters

Figure out exactly what the API expects.

### Step 5 — Make ONE request

Start simple.

```python
response = requests.get(...)
```

### Step 6 — Inspect the response

```python
print(response.status_code)
print(response.text)
```

### Step 7 — Study the JSON

Ask yourself:

> What type of data did I get back?

Is it:

* A dictionary?
* A list?
* A dictionary containing a list?
* Nested dictionaries?

### Step 8 — Extract the information

Only after understanding the response should you start doing things like:

```python
data = response.json()
```

and extracting values.

### Step 9 — Build the program

Now connect the API data to your own program logic.

---

# 🎯 The Main Skill You're Practicing

Don't memorize API syntax.

Practice this process:

```text
I don't know how this works
            ↓
Read the documentation
            ↓
Find an example
            ↓
Try a small request
            ↓
Inspect what comes back
            ↓
Understand the data
            ↓
Build from there
```

That's the skill that will make working with APIs, libraries, frameworks, and eventually larger software systems much easier.
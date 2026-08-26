
## RANDOM LINKS
# documentation booklet
[requests-library-documentation-readthedocs-io-en-latest](<../../# books/requests-library-documentation-readthedocs-io-en-latest.pdf>)


<br>

# research paper on network based software architecture
<br>
https://ics.uci.edu/%7Efielding/pubs/dissertation/top.htm


<br>
# video courses
<br>
check description to get all videos
<br>
https://www.youtube.com/watch?v=WXsD0ZgxjRw#:~:text=This%20course%20provides%20an,their%20benefits.


freecodecamp's tutorial
<br>
https://www.youtube.com/watch?v=FOZtRzY5x8E&t=808s

<br>
<br>

# Python `requests` Library — Understanding HTTP Requests

## 🎯 The Big Idea

The `requests` library allows Python programs to communicate with web servers and APIs using HTTP.

The most important thing to understand is:

> `requests` is a Python tool for constructing and sending HTTP requests.

I don't need to memorize every option available in `requests.get()`.

I need to understand **what an HTTP request is** and then understand how `requests` lets me construct one.

---

## 1. The Basic GET Request

The simplest GET request looks like this:

```python
import requests

response = requests.get("https://api.example.com/data")
```

This means:

> "Python, send a GET request to this URL."

The server receives the request and sends back a response.

```text
Python program
     |
     | HTTP GET request
     v
   Server
     |
     | HTTP response
     v
Python program
```

---

## 2. What Does `requests.get()` Actually Do?

When I write:

```python
requests.get(url)
```

I'm asking the `requests` library to create and send an HTTP GET request.

There are additional things I can give it:

```python
requests.get(
    url,
    params=params,
    headers=headers,
    timeout=10
)
```

These aren't four completely different concepts.

They are different pieces of information that can be included in the HTTP request.

---

## 3. URL

The URL tells the program:

> "Which server/resource am I communicating with?"

Example:

```python
url = "https://api.example.com/weather"

response = requests.get(url)
```

Think:

```text
URL = WHERE am I going?
```

---

## 4. `params`

`params` are used for **query parameters**.

Suppose the API documentation says:

```text
GET /weather?city=Port-of-Spain
```

I can write:

```python
params = {
    "city": "Port-of-Spain"
}

response = requests.get(
    "https://api.example.com/weather",
    params=params
)
```

`requests` builds the query string for me.

Conceptually:

```text
params = WHAT INFORMATION AM I ASKING FOR?
```

For example:

```python
params = {
    "city": "Port-of-Spain",
    "units": "metric"
}
```

This produces something conceptually similar to:

```text
https://api.example.com/weather?city=Port-of-Spain&units=metric
```

---

## 5. `headers`

Headers contain additional information about the request.

Example:

```python
headers = {
    "Authorization": "Bearer MY_API_KEY",
    "Accept": "application/json"
}

response = requests.get(
    url,
    headers=headers
)
```

Conceptually:

```text
headers = ADDITIONAL INFORMATION ABOUT THE REQUEST
```

Headers can be used for things such as:

- Authentication
- API keys
- Authorization tokens
- Specifying accepted response formats
- Providing information about the client

---

## 6. Authentication Headers

A very common example is:

```python
headers = {
    "Authorization": "Bearer MY_API_KEY"
}
```

The server can inspect this header and determine whether I am authorized to access the API.

This is why API documentation might show something like:

```text
Authorization: Bearer <API_KEY>
```

I translate that into Python:

```python
headers = {
    "Authorization": "Bearer MY_API_KEY"
}
```

Then:

```python
response = requests.get(
    url,
    headers=headers
)
```

---

## 7. `timeout`

I can tell `requests` how long it should wait for a response.

```python
response = requests.get(
    url,
    timeout=10
)
```

This means:

> "Don't wait indefinitely for the server."

If the server doesn't respond within the specified time, the request can raise a timeout exception.

---

## 8. The Response

The server sends a response back to Python.

I store that response:

```python
response = requests.get(url)
```

The response object contains information about what happened.

For example:

```python
response.status_code
```

might return:

```text
200
```

A status code of `200` generally means the request was successful.

---

## 9. Status Codes

Some important HTTP status codes:

```text
200 → OK
201 → Created
400 → Bad Request
401 → Unauthorized
403 → Forbidden
404 → Not Found
500 → Internal Server Error
```

I can inspect the status:

```python
print(response.status_code)
```

---

## 10. Getting JSON Data

APIs commonly return JSON.

For example, the server might return:

```json
{
    "city": "Port-of-Spain",
    "temperature": 30,
    "condition": "Sunny"
}
```

I can convert the JSON response into Python data:

```python
data = response.json()
```

Now I can work with it like a Python dictionary:

```python
print(data["city"])
print(data["temperature"])
```

---

## 11. The Basic API Workflow

A very important workflow to remember:

```text
READ API DOCUMENTATION
        ↓
UNDERSTAND THE ENDPOINT
        ↓
BUILD THE URL
        ↓
ADD PARAMETERS IF NEEDED
        ↓
ADD HEADERS IF NEEDED
        ↓
SEND REQUEST
        ↓
CHECK RESPONSE
        ↓
READ JSON
        ↓
EXTRACT THE DATA
        ↓
USE THE DATA IN MY PROGRAM
```

In Python:

```python
import requests

url = "https://api.example.com/weather"

params = {
    "city": "Port-of-Spain"
}

headers = {
    "Authorization": "Bearer MY_API_KEY"
}

response = requests.get(
    url,
    params=params,
    headers=headers
)

print(response.status_code)

data = response.json()

print(data)
```

---

## 12. I Don't Need to Use Everything

This is important.

I don't always need:

```python
params
headers
timeout
json
```

For example, a simple API might only require:

```python
response = requests.get(url)
```

Another API might require:

```python
response = requests.get(
    url,
    params=params
)
```

Another might require:

```python
response = requests.get(
    url,
    headers=headers
)
```

Another might require both:

```python
response = requests.get(
    url,
    params=params,
    headers=headers
)
```

The **API documentation tells me what the server expects**.

---

## 13. Mental Model

Instead of trying to memorize all the arguments to `requests.get()`, think about the request in layers.

```text
REQUEST
│
├── URL
│   └── Where am I going?
│
├── PARAMS
│   └── What specifically am I asking for?
│
├── HEADERS
│   └── What additional information does the server need?
│
└── TIMEOUT
    └── How long should I wait?
```

Then the server sends:

```text
RESPONSE
│
├── STATUS CODE
│   └── Did the request succeed?
│
├── HEADERS
│   └── Information about the response
│
└── BODY
    └── The actual data
```

---

## 14. HTTP and `requests`

`requests` is not the HTTP protocol itself.

HTTP already exists.

`requests` gives Python a convenient way to work with HTTP.

Conceptually:

```text
HTTP
│
├── GET
├── POST
├── PUT
├── PATCH
└── DELETE
```

Python's `requests` library gives me methods such as:

```python
requests.get()
requests.post()
requests.put()
requests.patch()
requests.delete()
```

So:

```python
requests.get(url)
```

means:

> Use Python's `requests` library to construct and send an HTTP GET request.

---

## 15. GET vs POST

### GET

Usually used to **retrieve information**.

```python
response = requests.get(url)
```

Think:

> "Give me some data."

### POST

Usually used to **send data to the server**.

```python
data = {
    "name": "Lincia"
}

response = requests.post(
    url,
    json=data
)
```

Think:

> "Here is some data. Do something with it."

---

## 16. What I Should Learn First

I should learn these concepts in roughly this order:

### Level 1 — HTTP basics

Understand:

- Client
- Server
- Request
- Response
- URL
- HTTP
- GET
- POST
- Status codes

### Level 2 — Request components

Understand:

- Query parameters
- Headers
- Authentication
- Request body

### Level 3 — Python `requests`

Learn:

```python
requests.get()
requests.post()
response.status_code
response.json()
response.headers
```

Then learn:

```python
params=
headers=
json=
data=
timeout=
```

### Level 4 — API development

Practice:

```text
Read documentation
       ↓
Find endpoint
       ↓
Identify parameters
       ↓
Identify authentication
       ↓
Make request
       ↓
Inspect response
       ↓
Extract data
       ↓
Use data in application
```

---

## 🧠 Important Lesson

I don't need to memorize the entire `requests` library.

When working with a new API, I should ask:

1. What is the endpoint?
2. What HTTP method does it require?
3. Does it require query parameters?
4. Does it require headers?
5. Does it require authentication?
6. What does the response look like?
7. What status codes should I expect?
8. How do I extract the data I need?

The API documentation tells me the answers.

My job is to understand the concepts well enough to translate those requirements into Python.

---

## 🔑 Core Pattern to Remember

```python
import requests

response = requests.get(
    url,
    params=params,
    headers=headers
)

print(response.status_code)

data = response.json()
```

I don't need to use every argument.

I add them **only when the API requires them**.

> **Learn HTTP first. Learn `requests` second.**

Once HTTP makes sense, `requests` becomes much easier to understand.



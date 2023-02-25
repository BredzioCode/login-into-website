import requests
from bs4 import BeautifulSoup

# Set up session
session = requests.Session()

# Get login page and extract hidden form inputs
login_url = "https://example.com/login"
response = session.get(login_url)
soup = BeautifulSoup(response.content, "html.parser")
inputs = soup.find_all("input")
data = {}
for inp in inputs:
    name = inp.get("name")
    value = inp.get("value")
    if name:
        data[name] = value

# Add login credentials to form data
data["username"] = "your_username"
data["password"] = "your_password"

# Submit login form and follow redirect
response = session.post(login_url, data=data, allow_redirects=False)
while response.status_code in [301, 302]:
    redirect_url = response.headers["Location"]
    response = session.get(redirect_url, allow_redirects=False)

# Check if login was successful
if response.ok:
    print("Login successful!")
else:
    print("Login failed.")

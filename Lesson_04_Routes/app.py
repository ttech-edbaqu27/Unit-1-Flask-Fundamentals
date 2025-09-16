from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>Dynamic Routes Demo</h1>
<h2>Try: These URLs</h2>
<ul>
    <li><a href="/user/john">User Profile: john</a></li>
    <li><a href="/user/alice">User Profile: alice</a></li>
    <li><a href=""></a></li>
    <li><a href=""></a></li>
    <li><a href=""></a></li>
    <li><a href=""></a></li>
    <li><a href=""></a></li>
</ul>
'''


@app.route("/user/<username>", methods=["GET"])
def user_profile(username):
    return f"""
<h1>User Profile</h1>
<p><strong>{username}</strong></p>
<p>Profile Type: {type(username).__name__}</p>
<p>Welcome to {username}'s profile page!</p>
<nav>
    <a href="/">Back to Homepage</a>
    <a href="/user/alice">Alice's Profile</a>
    <a href="/user/bob">Bob's Profile</a>
</nav>
"""

@app.route("/calc/<int:num1>/operation/<int:num2>", methods=["GET"])
def calculator(num1, operation, num2):
    operations = {
        "+": num1 + num2,
        "-": num1 - num2,
        "*": num1 * num2,
        "/": num1 / num2 if num2 != 0 else "Div0 Error"
    }

    if operation in operations:
        result = operations[operation]
        return f"{num1} {operation} {num2} = {result}"
    
@app.route("/url/<int:temp>/<startUnit>", methods=["GET"])
def url(temp, startUnit):
    if startUnit == "F":
        return f"{temp} F is {(temp-32)/1.8} deg C"
    elif startUnit == "C":
        return f"{temp} C is {(temp*1.8+32)} deg F"


if __name__ == '__main__':
    app.run(debug=True)
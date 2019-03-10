<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ name }}</title>
  </head>

  <body>
    <main>
      <div class="card">
        <form class="form" action="{{ target }}" method="post">

          <h1>Login
            <span>Please Input Username and Password</span>
          </h1>
          <label>
            <span>Username: </span>
            <input type="text" name="username" placeholder="Username" autofocus />
          </label>
          <label>
            <span>Password: </span>
            <input type="password" name="password" placeholder="Password" />
          </label>
          <label>
            <span>&nbsp;</span>
            <input type="submit" class="button" value="Login" />
          </label>
        </form>

      </div>
    </main>
  </body>

</html>


<style>

.form {
  margin-left: auto;
  margin-right: auto;
  max-width: 500px;
  padding: 20px 30px 20px 30px;
  font-family:Arial;
  -webkit-border-radius: 5px;
  -moz-border-radius: 5px;
}
.form h1 {
  padding: 0px 0px 10px 40px;
  display: block;
  border-bottom: 1px solid # 444;
  margin: -10px -30px 30px -30px;
}
.form h1>span {
  display: block;
  font-size: 11px;
}
.form label {
  display: block;
  margin: 0px 0px 5px;
}
.form label>span {
  float: left;
  width: 20%;
  text-align: right;
  padding-right: 10px;
  margin-top: 10px;
  font-weight: bold;
}
.form input[type="text"], .form input[type="password"] {
  border: none;
  height: 25px;
  line-height: 15px;
  margin-bottom: 16px;
  margin-right: 24px;
  margin-top: 2px;
  outline: 0 none;
  padding: 5px 0px 5px 5px;
  width: 70%;
  -webkit-border-radius: 2px;
  -moz-border-radius: 2px;
  -moz-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}

.form .button {
  background-color:#44c767;
  -moz-border-radius:28px;
  -webkit-border-radius:28px;
  border-radius:28px;
  border:1px solid #18ab29;
  display:inline-block;
  cursor:pointer;
  color:#ffffff;
  font-family:Arial;
  font-size:12px;
  font-weight: bold;
  padding:16px 31px;
  text-decoration:none;
  text-shadow:0px 1px 0px #2f6627;
}
.from .button:hover {
  background-color:#5cbf2a;
}
.from .button:active {
  position:relative;
  top:1px;
}

.card {
  width: 80%;
  padding: 10px;
  border: 3px solid #ab15e380;
  border-radius: 10px;
}

main {
  height: 100%;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}

html, body {
  width: 100%;
  height: 100%;
  margin: 0;
  padding: 0;
}

body {
  background: repeating-linear-gradient(30deg, #ecea96, #4c90bd);
}
</style>

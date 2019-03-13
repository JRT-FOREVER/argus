<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="shortcut icon" href="assets/favicon.ico" type="image/x-icon">
    <link rel="stylesheet" href="assets/argus.css"/>
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


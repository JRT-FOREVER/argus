			<form class="form-horizontal" role="form" method="post" action="<?php echo $_SERVER['PHP_SELF'];?>?class=user&method=login">
				<div class="form-group">
					 <label for="username" class="col-sm-2 control-label">Username</label>
					<div class="col-sm-10">
						<input class="form-control" name="username" type="text" />
					</div>
				</div>
				<div class="form-group">
					 <label for="password" class="col-sm-2 control-label">Password</label>
					<div class="col-sm-10">
						<input class="form-control" name="password" type="password" />
					</div>
				</div>
				<div class="form-group">
					<div class="col-sm-offset-2 col-sm-10">
						 <button type="submit" class="btn btn-default">Sign in</button>
					</div>
				</div>
			</form>

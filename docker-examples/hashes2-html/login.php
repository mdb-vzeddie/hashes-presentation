<?php
    $dir = 'sqlite:/var/www/html/organization.db';
    $dbh = new PDO($dir) or die ("cannot open");

    $myusername = $_POST['user'];
    $mypassword = md5($_POST['pass']);

    $query = "SELECT COUNT(*) FROM CLIENTS WHERE username='$myusername' AND password='$mypassword'";
		$result = $dbh->query($query);
    $count = $result->fetchColumn();
	
    if($count == 0){
      print "Incorrect username or password!";
    }
    else {
      print "<p>Welcome $myusername! You are a valued client and we take security very seriously.</p>";
      if(strpos($myusername, "admin") !== false) {
        print "<p>It seems like you're some kind of admin.</p><p>Here's the local database for your perusal: <p>";
        print "<a href='organization.db'>organization.db</a>";
      }
    }
?>

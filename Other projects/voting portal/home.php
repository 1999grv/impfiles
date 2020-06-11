
	<?php
	session_start();
	$conn=mysqli_connect("localhost","root","","voting_system");
	?>
	<!DOCTYPE html>
	<html>
	<head>
		<meta charset="utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<title>Page Title</title>
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<link rel="stylesheet" type="text/css" media="screen" href="main.css">
		<script src="main.js"></script>
	</head>
	<body>
		
	</body>
	</html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>
registeration
</title>
<style type="text/css"> 
#main
{
background:url("register-to-vote-online.jpg");
background-size: cover;
width:100%;
height:120%;
}
#registeration
{
background-color:blue;
width:100%;
height:11%;
font-color:white;
font-size:200%;
}
#form
{
height:760px;
width:600px;
background-color:black;
opacity:0.6;
margin-left:500px;
font-size:25px;
color:white;
padding: 20px 20px;
}


</style>
</head>
<body>
<div id="registeration">

<h1><center>register here</center></h1>
</div>
<div id="main">

	<form tag="Create Logon" action="home.php" method="post">
		<div id="form" align="center">
			Username *: <input type="text" name="username" /><br /><br /><br />
			Password *: <input type="password" name="pwd" /><br /><br /><br />
			Full Name*: <input type="text" name="surname" /><br /><br /><br />
			
			Date of Birth *: <input type="text" name="dob" /><br /><br /><br />
			Email *: <input type="email" name="email" /><br /><br /><br />
			Telephone: <input type="text" name="tel" /><br /><br /><br />
			Address *: <input type="text" name="add" /><br /><br /><br />
			Post Code *: <input type="text" name="ptc" /><br /><br /><br />

		<input type="submit" name='submit' value="submit" />
		</div>
	</form>
</div>

<?php
if(isset($_POST['submit']))
{
    $username=$_POST['username'];
    $pwd=$_POST['pwd'];
    $surname=$_POST['surname'];
    $dob=$_POST['dob'];
    $email=$_POST['email'];
    $tel=$_POST['tel'];
    $add=$_POST['add'];
    $ptc=$_POST['ptc'];

    $query="INSERT INTO register VALUES('$username','$pwd','$surname','$dob','$email','$tel','$add','$ptc')";
    if(mysqli_query($conn,$query))
    {
        echo "<h3>YOU HAVE REGISTERED SUCCEDDFULY</h3>";
	} 
	else {
		echo "failed";
	}
}?>	
</body>
</html>
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

	<form tag="Create Logon" action="home.php" method="POST">
		<div id="form" align="center">
			Username *: <input type="text" name="username" /><br /><br /><br />
			Password *: <input type="password" name="pwd" /><br /><br /><br />
			Full Name*: <input type="text" name="surname" /><br /><br /><br />
			
			Date of Birth *: <input type="text" name="dob" /><br /><br /><br />
			Email *: <input type="email" name="email" /><br /><br /><br />
			Telephone: <input type="number" name="tel" /><br /><br /><br />
			Address *: <input type="text" name="add" /><br /><br /><br />
			Post Code *: <input type="number" name="ptc" /><br /><br /><br />

		<input type="submit" value="Submit" />
		</div>
	</form>
</div>	
</body>
</html>
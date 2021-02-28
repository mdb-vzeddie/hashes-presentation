<!DOCTYPE html>
<html>
  <head>

  <style>
	a:link {
		color: white;
}
    .title {
      font-family: 'Trebuchet MS', sans-serif;
        font-size: 400%;
    }
    
    .subtitle {
      font-family: 'Trebuchet MS', sans-serif;
        font-size: 150%;
    }
    
    .subnote {
      font-family: 'Trebuchet MS', sans-serif;
        font-size: 75%;
    }
    
    .outer {
        display: table;
        position: absolute;
        height: 100%;
        width: 100%;
    	background: url("barielle-mustapich-unsplash.jpg");
        background-position: center;
    }
    
    .middle {
        display: table-cell;
        vertical-align: middle;
    }
    
    .innie {
        text-align: center;
			background: rgba(0,0,0,0.5);
			padding: 15px;
		color: white;
    }
  </style>

  </head>

  <body>

	<div class="outer">
		<div class="middle">
			<div class="innie">
				<span class="title">Welcome to my website!</span>
<br />
<span class="subtitle">For my clients who love Keanu Reeves.</span>
<br />
<span class="subtitle">You can click the button below for fun facts about Keanu Reeves!</span>
<br />
<span>

<form action="index.php" method="get">
  <button name="view" value="1.html" type="submit">First fact</button>
  <button name="view" value="2.html" type="submit">Second fact</button>
  <button name="view" value="3.html" type="submit">Third fact</button>
</form>

<br />
<?php 

if(isset($_GET["view"])){
  include $_GET["view"];
}
?>

</span>

<br />
<br />

<footer><span class="subnote">Photo by <a href="https://unsplash.com/@gmustapich?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Gabrielle Mustapich</a> on <a href="https://unsplash.com/t/wallpapers?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Unsplash</a></span></footer>
</div>

  </body>

</html>

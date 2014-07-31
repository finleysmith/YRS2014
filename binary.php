<html>
<head>
<Title>BINERYED</title>
<style type="text/css">
    @import url('css/fonts/stylesheet.css');
    body{
        word-wrap: break-word;
        font-family: 'open_sanslight', sans-serif;
        color: #fff;
        background: #000;
        width:100%;
        height:100%;
        font-size:18px;
    
    }
    html{
        padding: 20px;
    }
    .hi{
        font-size: 11px;
    }
    h1{
        font-weight: 200;
    }
</style>
<!-- Bootstrap core CSS -->
<link href="css/bootstrap.min.css" rel="stylesheet">
<!-- Bootstrap theme -->
<link href="css/bootstrap-theme.min.css" rel="stylesheet">
</head>
<body>
<?php
$message = $_POST['message'];
str_replace(" ", "!", $message);
//echo($message);
$result = exec("python bin.py " . $message);
echo $result;
?>
</body>
</html>
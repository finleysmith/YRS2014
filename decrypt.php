<HTML>
<HEAD>
<TITLE>Decryted</title>
<meta tag="robots" value="noindex, nofollow">
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
<script type="text/javascript" src="https://openspace.ordnancesurvey.co.uk/osmapapi/openspace.js?key=FE260633012F4B86E0430B6CA40A6CB4"></script>
<script type= "text/javascript" src="https://openspace.ordnancesurvey.co.uk/osmapapi/script/mapbuilder/basicmap.js"></script>
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>




<?php
$key1 = $_POST['key1']; //get data from post(index.htm 186-234)
$key2 = $_POST['key2'];
$key3 = $_POST['key3'];
$key4 = $_POST['key4'];
$post = $_POST['post'];
$comp = $_POST['comp'];
$data = $_POST['data'];
//echo($key1 . $key2 . $key3 . $key4 . $post . $comp . $data);
function ernest_marples($postcode) {
    $postcode = str_replace(" ", "", $postcode); //remove space from postcode
    $url = "http://www.uk-postcodes.com/postcode/". urlencode($postcode) .".csv"; // Build the URL
    $file = file_get_contents($url); //get the csv
    if (strpos($file, "html") === FALSE) { // Some error checking - if the file contains html, then we've been redirected to the homepage and something has gone wrong
    $pieces = explode(",", $file); //explode the csv
    $result['postcode'] = $pieces[0]; //postcode
    $result['lat'] = $pieces[1]; //lat
    $result['lng'] = $pieces[2]; //lng
    $result['northing'] = $pieces[3]; //northing
    $result['easting'] = $pieces[4]; //easting
    } else {
        $result['error'] = TRUE; // If an error, return one
    }
    return $result;
}
$shit = ernest_marples($post);
echo('<script type="text/javascript">' . "function initmapbuilder()
{
var options = {resolutions: [2500, 1000, 500, 200, 100, 50, 25, 10, 5, 4, 2.5, 2, 1]};
osMap = new OpenSpace.Map('map', options);
setglobaloptions();
osMap.setCenter(new OpenSpace.MapPoint(" . $shit['easting'] . "," . $shit['northing'] . "),1);}</script>"); //make the make function, with correct northing and easting
echo("</head>"); //end header
echo('<body>'); //body tag with onload initmapbuilder
echo("<h1>Your Keys(keep them safe): </h1>"); //keys
echo("Key 1: " . $key1 . "<br>");
echo("Key 2: " . $key2 . "<br>");
echo("Key 3: " . $key3 . "<br>");
echo("Key 4: " . $key4 . "<br>");
echo("Postcode: " . $post);
//echo("DEBUG NOTRH EAST " . );



echo("<h1>Your decrypted data:</h1>");
//$shit = ernest_marples($post); //run function as shit
//echo("DEBUG NOTRH EAST " . $shit['northing'] . "     " . $shit['easting']);
//echo("Lan: " . $shit['lat'] . "  Lng: " . $shit['lng']);
$lat = $shit['lat'];
//$lat = str_replace(".", "", $lat); //get rid of dot
$lng = $shit['lng'];
//$lng = str_replace(".", "", $lng); //get rid of dot

//$result = exec("python to.py " . $data . ' ' . $comp . ' ' . $key1 . ' ' . $key2 . ' ' . $lat . ' ' . $lng . ' ' .  $key3 . ' ' . $key4);
//echo $result;
echo("DEBUG COMMAND: " . "python de.py " . $data . ' ' . $comp . ' ' . $key1 . ' ' . $key2 . ' ' . $lat . ' ' . $lng . ' ' .  $key3 . ' ' . $key4);
$lastline = system("python de.py " . $data . ' ' . $comp . ' ' . $key1 . ' ' . $key2 . ' ' . $lat . ' ' . $lng . ' ' .  $key3 . ' ' . $key4, $returnval); //run command
echo('<p class="hi">' . $lastline . '</p>');



echo("<br><h1>Latitude and Longitiude</h1>" . $lat . "             " . $lng);


?>


</body>
</html>
<?php 
    require_once('GoogleMapsGeocoder.php');
    
if (!empty($_POST)) {
  $address= strip_tags($_POST['search']);
}

echo '<form action="example.php" method="post">';
echo '<input type="text" name="search" />';
echo '<input type="submit" value="Get geographic data!" />';
echo '</form>';


if (!empty($address)) {
    
    $Geocoder = new GoogleMapsGeocoder($address);
    $response = $Geocoder->geocode();

?>

Formatted Address: <?php echo $response['results'][0]['formatted_address']; ?><br />
Lat: <?php echo $response['results'][0]['geometry']['location']['lat']; ?><br />
Lng: <?php echo $response['results'][0]['geometry']['location']['lng']; ?>

<pre>
    <?php echo $Geocoder->getAddress(); ?>
</pre>

<?php } ?>
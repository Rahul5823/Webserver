<?php
#Check if the 'name' query parameter is set or not
if (isset($_GET['name'])) {
    $name = $_GET['name'];
    echo "Hey, " . htmlspecialchars($name) . "! You've sent a GET request with a name parameter.";
#'htmlspecialchars()' is used to prevent XSS attacks, which is a good safety precaution
} 
else {
    echo "You got me into GET 200 without a name parameter.";
}
?>

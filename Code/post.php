<?php
$request_method = $_SERVER['REQUEST_METHOD'];

if ($request_method === 'POST') {
    #You can directly access the $_POST
    $name = isset($_POST["name"]) ? htmlspecialchars($_POST["name"]) : "undefined";
    #'htmlspecialchars()' is used to prevent XSS attacks, which is a good safety precaution
    $age = isset($_POST["age"]) ? intval($_POST["age"]) : "undefined";
    echo "Name: " . $name . "<br>";
    echo "Age: " . $age . "<br>";
    #if method is POST, it outputs both 'name' and 'age' values
} else {
    #if not, prompts to send POST request
    echo "Please send a POST request.";
}
?>

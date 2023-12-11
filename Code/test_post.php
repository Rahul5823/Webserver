<?php
    #Handling a POST request
    $input_data = file_get_contents("php://input");
    echo "Received a POST request with data: " . $input_data;
?>

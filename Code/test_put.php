<?php
    # Processing a PUT request
    $input_json = json_decode(file_get_contents('php://input'), true);
    $item_id = $input_json['id'];
    $updated_name = $input_json['newName'];
    echo "Record updated, ID: $item_id, New Name: $updated_name";
?>

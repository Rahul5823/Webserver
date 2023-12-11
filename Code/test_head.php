<?php
    #Responding to a HEAD request
    header("Content-Type: text/plain");
    header("Custom-Header: Demo");
    #No body content is sent in HEAD response
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Information</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f4f4f4;
        }
        .content {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        a {
            color: #007bff;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        footer {
            margin-top: 20px;
            text-align: center;
            background-color: #f1f1f1;
            padding: 10px;
            border-radius: 8px;
        }
    </style>
</head>
<body>

<div class="content">
    <p>Welcome <?php echo htmlspecialchars($_GET["name"]); ?> from <?php echo htmlspecialchars(getenv("REMOTE_HOST")); ?></p>

    <p>Your email address is: <?php echo htmlspecialchars($_GET["email"]); ?></p>

    <p>GET variable data - <br />
        <?php
        foreach ($_GET as $param_name => $param_val) {
            echo "Param: " . htmlspecialchars($param_name) . "; Value: " . htmlspecialchars($param_val) . "<br />\n";
        }
        ?>
    </p>
</div>

<footer>
    <p><a href="welcome.html">Welcome/GET page</a></p>
    <p><a href="index.html">Home Page</a></p>
</footer>

</body>
</html>

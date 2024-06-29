<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $gate_code = $_POST['gate_code'];

    
    file_put_contents('gate_config.php', $gate_code);

    echo "Gate updated successfully.";
} else {
    echo "Invalid request method.";
}
?>
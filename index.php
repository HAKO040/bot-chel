<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Visa Checker</title>
    <link href="https://cdn.jsdelivr.net/npm/daisyui@2.51.5/dist/full.css" rel="stylesheet" type="text/css" />
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gradient-to-r from-blue-400 to-purple-500 min-h-screen flex flex-col items-center justify-center">
    <div class="bg-white rounded-lg shadow-lg p-8 max-w-md w-full">
        <h1 class="text-3xl font-bold text-center mb-6 text-gray-800">Visa Checker</h1>
        <form action="gates.php" method="post" class="space-y-4">
            <div>
                <label for="combo" class="block text-gray-700 font-bold mb-2">Combo (Card|Month|Year|CVV):</label>
                <textarea id="combo" name="combo" rows="10" cols="50" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"></textarea>
            </div>
            <div>
                <label for="telegram_token" class="block text-gray-700 font-bold mb-2">Telegram Bot Token (optional):</label>
                <input type="text" id="telegram_token" name="telegram_token" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
            </div>
            <div>
                <label for="telegram_chat_id" class="block text-gray-700 font-bold mb-2">Telegram Chat ID (optional):</label>
                <input type="text" id="telegram_chat_id" name="telegram_chat_id" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
            </div>
            <div class="flex items-center justify-between">
                <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" type="submit">Check</button>
            </div>
        </form>
    </div>
    <div class="bg-white rounded-lg shadow-lg p-8 max-w-md w-full mt-8">
        <h2 class="text-2xl font-bold text-center mb-6 text-gray-800">Update Gate</h2>
        <form action="update_gate.php" method="post" class="space-y-4">
            <div>
                <label for="gate_code" class="block text-gray-700 font-bold mb-2">Gate Code:</label>
                <textarea id="gate_code" name="gate_code" rows="10" cols="50" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"></textarea>
            </div>
            <div class="flex items-center justify-between">
                <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" type="submit">Update Gate</button>
            </div>
        </form>
    </div>
</body>
</html>
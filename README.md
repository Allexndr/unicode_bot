# README

## English Version

### Telegram Bot with Language Detection and Message Modification

This project is a simple Telegram bot built with the `telebot` library that detects the language of incoming messages and modifies them by inserting special Unicode characters. The bot also responds with a sticker when a specific command is received.

### Features

1. **Language Detection:** The bot uses the `langdetect` library to identify the language of the incoming message.
2. **Message Modification:** Depending on the detected language, the bot modifies the message by inserting special Unicode characters.
3. **Sticker Response:** The bot sends a specific sticker when the `/hohol` command is received.

### Prerequisites

- Python 3.x
- `pyTelegramBotAPI` library
- `langdetect` library

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/yourproject.git
    cd yourproject
    ```

2. Install the required libraries:
    ```bash
    pip install pyTelegramBotAPI langdetect
    ```

3. Add your Telegram bot token in the script:
    ```python
    bot = telebot.TeleBot("YOUR_TELEGRAM_BOT_TOKEN")
    ```

### Usage

1. Run the bot:
    ```bash
    python bot.py
    ```

2. Send a message with the `/t` prefix to see the modified message.
3. Send the `/hohol` command to receive a sticker.

### Code Explanation

- The bot listens for text messages and detects their language.
- Depending on the language, it modifies the message by adding special Unicode characters.
- The modified message is then sent back to the user.
- If the `/hohol` command is received, the bot sends a sticker.

### Example

- Sending the message: `/t Hello World!`
- Receiving the message: `H​e​l​l​o​ ​W​o​r​l​d​!`

### License

This project is licensed under the MIT License.

---

## Версия на русском языке

### Телеграм-бот с обнаружением языка и модификацией сообщений

Этот проект представляет собой простой телеграм-бот, созданный с использованием библиотеки `telebot`, который определяет язык входящих сообщений и модифицирует их, вставляя специальные символы Unicode. Бот также отправляет стикер при получении определенной команды.

### Особенности

1. **Обнаружение языка:** Бот использует библиотеку `langdetect` для определения языка входящего сообщения.
2. **Модификация сообщения:** В зависимости от обнаруженного языка бот модифицирует сообщение, вставляя специальные символы Unicode.
3. **Ответ со стикером:** Бот отправляет определенный стикер при получении команды `/hohol`.

### Необходимые компоненты

- Python 3.x
- Библиотека `pyTelegramBotAPI`
- Библиотека `langdetect`

### Установка

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/yourusername/yourproject.git
    cd yourproject
    ```

2. Установите необходимые библиотеки:
    ```bash
    pip install pyTelegramBotAPI langdetect
    ```

3. Добавьте токен вашего телеграм-бота в скрипт:
    ```python
    bot = telebot.TeleBot("YOUR_TELEGRAM_BOT_TOKEN")
    ```

### Использование

1. Запустите бота:
    ```bash
    python bot.py
    ```

2. Отправьте сообщение с префиксом `/t`, чтобы увидеть модифицированное сообщение.
3. Отправьте команду `/hohol`, чтобы получить стикер.

### Объяснение кода

- Бот прослушивает текстовые сообщения и определяет их язык.
- В зависимости от языка, он модифицирует сообщение, добавляя специальные символы Unicode.
- Модифицированное сообщение отправляется обратно пользователю.
- При получении команды `/hohol`, бот отправляет стикер.

### Пример

- Отправка сообщения: `/t Привет, мир!`
- Получение сообщения: `П​р​и​в​е​т​,​ ​м​и​р​!`

### Лицензия

Этот проект лицензирован по лицензии MIT.

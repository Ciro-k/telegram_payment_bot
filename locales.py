# locales.py - все переводы для бота

LANGUAGES = {
    "ru": {
        "name": "Русский",
        "flag": "🇷🇺",
        "select_language": "🌍 Выберите язык:",
        "language_set": "✅ Язык установлен: Русский",
        "main_menu": "🏦 Главное меню\n\nВыберите действие:",
        "create_invoice": "💰 Создать счёт",
        "pay_invoice": "💳 Оплатить счёт",
        "my_balance": "📊 Мой баланс",
        "withdraw": "💸 Вывод средств",
        "help": "ℹ️ Помощь",
        "admin_stats": "📈 Статистика",
        "admin_users": "👥 Пользователи",
        "help_admin": "👑 Админ-команды",
        "back": "🔙 Назад",
        "help_text": "ℹ️ Помощь\n\n"
                     "💰 Создать счёт — создайте счет для оплаты\n"
                     "💳 Оплатить счёт — оплатите существующий счет\n"
                     "📊 Баланс — проверьте свой баланс\n"
                     "💸 Вывод — выведите средства\n\n"
                     "⏳ Счета действительны 15 минут\n"
                     "💱 Комиссия: {commission}% (0.01 € с каждого €)\n"
                     "🔒 Все платежи анонимны\n"
                     "💰 Минимальная сумма: 1 €",
        "create_invoice_text": "💰 Создание счета\n\n"
                               "Введите сумму в евро:\n"
                               "Минимум: 1 €\n"
                               "Максимум: 5000 €\n\n"
                               "Пример: 50 или 100.50",
        "min_amount_error": "❌ Минимальная сумма: 1 €",
        "max_amount_error": "❌ Максимальная сумма: 5000 €",
        "invalid_number": "❌ Введите корректное число!",
        "create_error": "❌ Ошибка создания счета!",
        "invoice_created": "✅ Счет создан!\n\n"
                           "💵 Сумма: {amount}\n"
                           "🔑 Код: {code}\n"
                           "⏳ Счет действителен 15 минут\n"
                           "💱 Комиссия: {commission}%\n\n"
                           "Выберите способ оплаты:",
        "pay_invoice_text": "💳 Оплата счета\n\nВведите код счета (8 символов):",
        "invoice_not_found": "❌ Счет не найден или уже оплачен!",
        "invoice_expired": "❌ Счет истек (15 минут)!",
        "payment_methods": "💳 Выберите способ оплаты\n\n"
                           "💵 Сумма: {amount}\n"
                           "🔑 Код: {code}\n"
                           "⏳ Осталось: {time_left}",
        "payment_confirmed_user": "✅ Оплата получена!\n\n"
                                  "💵 Сумма: {amount}\n"
                                  "💸 Комиссия: {commission} ({percent}%)\n"
                                  "💳 Зачислено: {earned}\n"
                                  "🔑 Код: {code}",
        "payment_confirmed_buyer": "✅ Оплата подтверждена!\n\n"
                                   "💵 Сумма: {amount}\n"
                                   "🔑 Код: {code}\n\n"
                                   "Спасибо за использование! 🙌",
        "balance_text": "📊 Ваш баланс\n\n"
                        "💰 Баланс: {balance}\n\n"
                        "💸 Минимальная сумма вывода: {min_withdraw}\n"
                        "💱 Комиссия при оплате: {commission}%",
        "withdraw_text": "💸 Вывод средств\n\n"
                         "Введите сумму для вывода:\n"
                         "Минимум: 10 €\n\n"
                         "Пример: 50 или 100.50",
        "withdraw_min_error": "❌ Минимальная сумма вывода: 10 €",
        "insufficient_balance": "❌ Недостаточно средств!",
        "withdraw_create_error": "❌ Ошибка создания заявки!",
        "withdraw_success": "✅ Заявка #{id} создана!\nСумма: {amount}\nОжидайте подтверждения.",
        "admin_withdraw_request": "💰 Запрос на вывод!\n\n"
                                  "👤 Пользователь: ID {user_id}\n"
                                  "💵 Сумма: {amount}\n"
                                  "🆔 Заявка #{id}\n\n"
                                  "Подтвердите вывод:\n/withdraw_admin {user_id} {amount}",
        "no_rights": "❌ Нет прав!",
        "stats_text": "📈 Статистика за неделю\n\n",
        "stats_day": "📅 {day}:\n"
                     "   Счетов: {total} | Оплачено: {paid}\n"
                     "   Сумма: {amount} | Комиссия: {commission}\n\n",
        "stats_total": "📊 Итого:\n"
                       "👥 Пользователей: {users}\n"
                       "💳 Оплат: {payments}\n"
                       "💰 Сумма: {amount}\n"
                       "💸 Комиссий: {commission}\n"
                       "⚙️ Комиссия: {percent}%",
        "users_list": "👥 Пользователи\n\n",
        "user_item": "• ID: {id} | Баланс: {balance}\n",
        "users_more": "\n... и еще {count} пользователей",
        "admin_help": "👑 Админ-команды\n\n"
                      "📊 Статистика и пользователи:\n"
                      "/stats — общая статистика\n"
                      "/users — список всех пользователей\n"
                      "/userinfo <id> — полная инфо о пользователе\n"
                      "/getid <username> — найти ID по username\n\n"
                      "💳 Управление платежами:\n"
                      "/view <код_счета> — создать одноразовый код просмотра\n"
                      "/check <код> — проверить сделку (для всех)\n"
                      "/withdraw_admin <id> <сумма> — подтвердить вывод\n\n"
                      "📋 Команды для обычных пользователей:\n"
                      "/start — главное меню\n"
                      "/language — сменить язык\n"
                      "/help — помощь\n"
                      "/create <сумма> — создать счет\n"
                      "/pay <код> — оплатить счет\n"
                      "/balance — мой баланс\n"
                      "/withdraw <сумма> — вывод средств\n"
                      "/check <код> — проверить сделку",
        "view_code_created": "✅ Код просмотра создан!\n\n"
                             "🔑 Код: {view_code}\n"
                             "📋 Счет: {invoice_code}\n"
                             "⚠️ Одноразовый, после просмотра удаляется",
        "invoice_not_paid": "❌ Счет еще не оплачен!",
        "check_invoice": "📋 Информация о сделке\n\n"
                         "🔑 Код счета: {code}\n"
                         "💵 Сумма: {amount}\n"
                         "📊 Статус: {status}\n"
                         "📅 Создан: {created}\n"
                         "💳 Комиссия: {commission}\n"
                         "👤 Получатель: ID {creator}",
        "user_info": "👤 Информация о пользователе\n\n"
                     "🆔 ID: {id}\n"
                     "👤 Username: @{username}\n"
                     "📅 Зарегистрирован: {registered}\n"
                     "💰 Баланс: {balance}\n\n"
                     "📊 Статистика:\n"
                     "📤 Создано счетов: {created}\n"
                     "📥 Оплачено (как покупатель): {paid_count} на {paid_sum}\n"
                     "💵 Заработано (как продавец): {earned}\n"
                     "💸 Комиссии заплачено: {commission_paid}\n\n"
                     "📋 Последние счета (созданные):\n"
                     "  {invoices}\n\n"
                     "💳 Последние оплаты (как покупатель):\n"
                     "  {payments}",
        "user_not_found": "❌ Пользователь не найден!",
        "invalid_id": "❌ Введи корректный ID!",
        "user_not_in_db": "❌ Пользователь @{username} не найден в базе!\n\n"
                          "Попросите его написать /start боту.",
        "invoice_status_paid": "✅ оплачен",
        "invoice_status_pending": "⏳ ожидает",
        "status": "статус",
        "expired": "Истек",
        "time_left": "{minutes} мин {seconds} сек",
        "payment_method_paypal": "👤 PayPal\n\nОплатите на PayPal:\nexample@paypal.com\n\n"
                                  "💵 Сумма: {amount}\n📝 Комментарий: {code}\n\n"
                                  "⚠️ После оплаты нажмите \"Я оплатил(а)\"",
        "payment_method_usdt": "₿ USDT (TRC20)\n\nОтправьте USDT на адрес:\nTRC20_ADDRESS_HERE\n\n"
                               "🌐 Сеть: TRC20\n💵 Сумма: {amount} USDT\n\n"
                               "⚠️ После отправки нажмите \"Я оплатил(а)\"",
        "payment_method_btc": "₿ Bitcoin\n\nОтправьте BTC на адрес:\nBTC_ADDRESS_HERE\n\n"
                              "💵 Сумма: {amount} BTC (по курсу)\n\n"
                              "⚠️ После отправки нажмите \"Я оплатил(а)\"",
        "payment_method_p2p": "🏦 P2P (Binance)\n\nСвяжитесь с продавцом:\n👤 @P2P_Manager\n\n"
                              "💵 Сумма: {amount} EUR\n\n"
                              "⚠️ После оплаты нажмите \"Я оплатил(а)\"",
        "payment_method_card": "💳 Банковская карта\n\nОплатите по ссылке:\n🔗 https://payment.link/{code}\n\n"
                               "💵 Сумма: {amount}\n\n"
                               "⚠️ После оплаты нажмите \"Я оплатил(а)\"",
        "i_paid": "✅ Я оплатил(а)",
        "back_to_methods": "🔙 Назад к способам",
        "main_menu_btn": "🏠 Главное меню",
        "use_buttons": "Используйте кнопки меню 👇",
        "language_command": "🌍 Смена языка\n\nВыберите язык:",
        "language_changed": "✅ Язык изменен на {language}",
        "paypal": "💳 PayPal",
        "usdt": "₿ USDT (TRC20)",
        "btc": "₿ Bitcoin (BTC)",
        "p2p": "🏦 P2P (Binance)",
        "card": "💳 Банковская карта",
        "confirm_payment": "✅ Я оплатил(а)",
        "min_withdraw_amount": "10",
    },
    "en": {
        "name": "English",
        "flag": "🇬🇧",
        "select_language": "🌍 Select language:",
        "language_set": "✅ Language set: English",
        "main_menu": "🏦 Main menu\n\nSelect an action:",
        "create_invoice": "💰 Create invoice",
        "pay_invoice": "💳 Pay invoice",
        "my_balance": "📊 My balance",
        "withdraw": "💸 Withdraw funds",
        "help": "ℹ️ Help",
        "admin_stats": "📈 Statistics",
        "admin_users": "👥 Users",
        "help_admin": "👑 Admin commands",
        "back": "🔙 Back",
        "help_text": "ℹ️ Help\n\n"
                     "💰 Create invoice — create a payment invoice\n"
                     "💳 Pay invoice — pay an existing invoice\n"
                     "📊 Balance — check your balance\n"
                     "💸 Withdraw — withdraw funds\n\n"
                     "⏳ Invoices valid for 15 minutes\n"
                     "💱 Commission: {commission}% (0.01 € per €)\n"
                     "🔒 All payments are anonymous\n"
                     "💰 Minimum amount: 1 €",
        "create_invoice_text": "💰 Create invoice\n\n"
                               "Enter amount in euros:\n"
                               "Minimum: 1 €\n"
                               "Maximum: 5000 €\n\n"
                               "Example: 50 or 100.50",
        "min_amount_error": "❌ Minimum amount: 1 €",
        "max_amount_error": "❌ Maximum amount: 5000 €",
        "invalid_number": "❌ Enter a valid number!",
        "create_error": "❌ Error creating invoice!",
        "invoice_created": "✅ Invoice created!\n\n"
                           "💵 Amount: {amount}\n"
                           "🔑 Code: {code}\n"
                           "⏳ Invoice valid for 15 minutes\n"
                           "💱 Commission: {commission}%\n\n"
                           "Select payment method:",
        "pay_invoice_text": "💳 Pay invoice\n\nEnter invoice code (8 characters):",
        "invoice_not_found": "❌ Invoice not found or already paid!",
        "invoice_expired": "❌ Invoice expired (15 minutes)!",
        "payment_methods": "💳 Select payment method\n\n"
                           "💵 Amount: {amount}\n"
                           "🔑 Code: {code}\n"
                           "⏳ Time left: {time_left}",
        "payment_confirmed_user": "✅ Payment received!\n\n"
                                  "💵 Amount: {amount}\n"
                                  "💸 Commission: {commission} ({percent}%)\n"
                                  "💳 Credited: {earned}\n"
                                  "🔑 Code: {code}",
        "payment_confirmed_buyer": "✅ Payment confirmed!\n\n"
                                   "💵 Amount: {amount}\n"
                                   "🔑 Code: {code}\n\n"
                                   "Thank you for using! 🙌",
        "balance_text": "📊 Your balance\n\n"
                        "💰 Balance: {balance}\n\n"
                        "💸 Minimum withdrawal: {min_withdraw}\n"
                        "💱 Payment commission: {commission}%",
        "withdraw_text": "💸 Withdraw funds\n\n"
                         "Enter amount to withdraw:\n"
                         "Minimum: 10 €\n\n"
                         "Example: 50 or 100.50",
        "withdraw_min_error": "❌ Minimum withdrawal: 10 €",
        "insufficient_balance": "❌ Insufficient balance!",
        "withdraw_create_error": "❌ Error creating request!",
        "withdraw_success": "✅ Request #{id} created!\nAmount: {amount}\nWait for confirmation.",
        "admin_withdraw_request": "💰 Withdrawal request!\n\n"
                                  "👤 User: ID {user_id}\n"
                                  "💵 Amount: {amount}\n"
                                  "🆔 Request #{id}\n\n"
                                  "Confirm withdrawal:\n/withdraw_admin {user_id} {amount}",
        "no_rights": "❌ No rights!",
        "stats_text": "📈 Weekly statistics\n\n",
        "stats_day": "📅 {day}:\n"
                     "   Invoices: {total} | Paid: {paid}\n"
                     "   Amount: {amount} | Commission: {commission}\n\n",
        "stats_total": "📊 Total:\n"
                       "👥 Users: {users}\n"
                       "💳 Payments: {payments}\n"
                       "💰 Amount: {amount}\n"
                       "💸 Commissions: {commission}\n"
                       "⚙️ Commission: {percent}%",
        "users_list": "👥 Users\n\n",
        "user_item": "• ID: {id} | Balance: {balance}\n",
        "users_more": "\n... and {count} more users",
        "admin_help": "👑 Admin commands\n\n"
                      "📊 Statistics and users:\n"
                      "/stats — general statistics\n"
                      "/users — list all users\n"
                      "/userinfo <id> — full user info\n"
                      "/getid <username> — find ID by username\n\n"
                      "💳 Payment management:\n"
                      "/view <invoice_code> — create one-time view code\n"
                      "/check <code> — check transaction (for all)\n"
                      "/withdraw_admin <id> <amount> — confirm withdrawal\n\n"
                      "📋 Commands for regular users:\n"
                      "/start — main menu\n"
                      "/language — change language\n"
                      "/help — help\n"
                      "/create <amount> — create invoice\n"
                      "/pay <code> — pay invoice\n"
                      "/balance — my balance\n"
                      "/withdraw <amount> — withdraw funds\n"
                      "/check <code> — check transaction",
        "view_code_created": "✅ View code created!\n\n"
                             "🔑 Code: {view_code}\n"
                             "📋 Invoice: {invoice_code}\n"
                             "⚠️ One-time, deleted after viewing",
        "invoice_not_paid": "❌ Invoice not paid yet!",
        "check_invoice": "📋 Transaction info\n\n"
                         "🔑 Invoice code: {code}\n"
                         "💵 Amount: {amount}\n"
                         "📊 Status: {status}\n"
                         "📅 Created: {created}\n"
                         "💳 Commission: {commission}\n"
                         "👤 Recipient: ID {creator}",
        "user_info": "👤 User info\n\n"
                     "🆔 ID: {id}\n"
                     "👤 Username: @{username}\n"
                     "📅 Registered: {registered}\n"
                     "💰 Balance: {balance}\n\n"
                     "📊 Statistics:\n"
                     "📤 Invoices created: {created}\n"
                     "📥 Paid (as buyer): {paid_count} for {paid_sum}\n"
                     "💵 Earned (as seller): {earned}\n"
                     "💸 Commissions paid: {commission_paid}\n\n"
                     "📋 Recent invoices (created):\n"
                     "  {invoices}\n\n"
                     "💳 Recent payments (as buyer):\n"
                     "  {payments}",
        "user_not_found": "❌ User not found!",
        "invalid_id": "❌ Enter valid ID!",
        "user_not_in_db": "❌ User @{username} not found in database!\n\n"
                          "Ask them to write /start to the bot.",
        "invoice_status_paid": "✅ paid",
        "invoice_status_pending": "⏳ pending",
        "status": "status",
        "expired": "Expired",
        "time_left": "{minutes} min {seconds} sec",
        "payment_method_paypal": "👤 PayPal\n\nPay via PayPal:\nexample@paypal.com\n\n"
                                  "💵 Amount: {amount}\n📝 Comment: {code}\n\n"
                                  "⚠️ After payment click \"I paid\"",
        "payment_method_usdt": "₿ USDT (TRC20)\n\nSend USDT to address:\nTRC20_ADDRESS_HERE\n\n"
                               "🌐 Network: TRC20\n💵 Amount: {amount} USDT\n\n"
                               "⚠️ After sending click \"I paid\"",
        "payment_method_btc": "₿ Bitcoin\n\nSend BTC to address:\nBTC_ADDRESS_HERE\n\n"
                              "💵 Amount: {amount} BTC (at current rate)\n\n"
                              "⚠️ After sending click \"I paid\"",
        "payment_method_p2p": "🏦 P2P (Binance)\n\nContact seller:\n👤 @P2P_Manager\n\n"
                              "💵 Amount: {amount} EUR\n\n"
                              "⚠️ After payment click \"I paid\"",
        "payment_method_card": "💳 Bank card\n\nPay via link:\n🔗 https://payment.link/{code}\n\n"
                               "💵 Amount: {amount}\n\n"
                               "⚠️ After payment click \"I paid\"",
        "i_paid": "✅ I paid",
        "back_to_methods": "🔙 Back to methods",
        "main_menu_btn": "🏠 Main menu",
        "use_buttons": "Use menu buttons 👇",
        "language_command": "🌍 Change language\n\nSelect language:",
        "language_changed": "✅ Language changed to {language}",
        "paypal": "💳 PayPal",
        "usdt": "₿ USDT (TRC20)",
        "btc": "₿ Bitcoin (BTC)",
        "p2p": "🏦 P2P (Binance)",
        "card": "💳 Bank card",
        "confirm_payment": "✅ I paid",
        "min_withdraw_amount": "10",
    },
    "fr": {
        "name": "Français",
        "flag": "🇫🇷",
        "select_language": "🌍 Choisissez la langue :",
        "language_set": "✅ Langue définie : Français",
        "main_menu": "🏦 Menu principal\n\nChoisissez une action :",
        "create_invoice": "💰 Créer une facture",
        "pay_invoice": "💳 Payer une facture",
        "my_balance": "📊 Mon solde",
        "withdraw": "💸 Retirer des fonds",
        "help": "ℹ️ Aide",
        "admin_stats": "📈 Statistiques",
        "admin_users": "👥 Utilisateurs",
        "help_admin": "👑 Commandes admin",
        "back": "🔙 Retour",
        "help_text": "ℹ️ Aide\n\n"
                     "💰 Créer une facture — créez une facture de paiement\n"
                     "💳 Payer une facture — payez une facture existante\n"
                     "📊 Solde — vérifiez votre solde\n"
                     "💸 Retirer — retirez des fonds\n\n"
                     "⏳ Factures valables 15 minutes\n"
                     "💱 Commission : {commission}% (0.01 € par €)\n"
                     "🔒 Tous les paiements sont anonymes\n"
                     "💰 Montant minimum : 1 €",
        "create_invoice_text": "💰 Création d'une facture\n\n"
                               "Entrez le montant en euros :\n"
                               "Minimum : 1 €\n"
                               "Maximum : 5000 €\n\n"
                               "Exemple : 50 ou 100.50",
        "min_amount_error": "❌ Montant minimum : 1 €",
        "max_amount_error": "❌ Montant maximum : 5000 €",
        "invalid_number": "❌ Entrez un nombre valide !",
        "create_error": "❌ Erreur de création de la facture !",
        "invoice_created": "✅ Facture créée !\n\n"
                           "💵 Montant : {amount}\n"
                           "🔑 Code : {code}\n"
                           "⏳ Facture valable 15 minutes\n"
                           "💱 Commission : {commission}%\n\n"
                           "Choisissez le mode de paiement :",
        "pay_invoice_text": "💳 Payer une facture\n\nEntrez le code de la facture (8 caractères) :",
        "invoice_not_found": "❌ Facture non trouvée ou déjà payée !",
        "invoice_expired": "❌ Facture expirée (15 minutes) !",
        "payment_methods": "💳 Choisissez le mode de paiement\n\n"
                           "💵 Montant : {amount}\n"
                           "🔑 Code : {code}\n"
                           "⏳ Temps restant : {time_left}",
        "payment_confirmed_user": "✅ Paiement reçu !\n\n"
                                  "💵 Montant : {amount}\n"
                                  "💸 Commission : {commission} ({percent}%)\n"
                                  "💳 Crédité : {earned}\n"
                                  "🔑 Code : {code}",
        "payment_confirmed_buyer": "✅ Paiement confirmé !\n\n"
                                   "💵 Montant : {amount}\n"
                                   "🔑 Code : {code}\n\n"
                                   "Merci pour votre utilisation ! 🙌",
        "balance_text": "📊 Votre solde\n\n"
                        "💰 Solde : {balance}\n\n"
                        "💸 Retrait minimum : {min_withdraw}\n"
                        "💱 Commission de paiement : {commission}%",
        "withdraw_text": "💸 Retirer des fonds\n\n"
                         "Entrez le montant à retirer :\n"
                         "Minimum : 10 €\n\n"
                         "Exemple : 50 ou 100.50",
        "withdraw_min_error": "❌ Retrait minimum : 10 €",
        "insufficient_balance": "❌ Solde insuffisant !",
        "withdraw_create_error": "❌ Erreur de création de la demande !",
        "withdraw_success": "✅ Demande #{id} créée !\nMontant : {amount}\nEn attente de confirmation.",
        "admin_withdraw_request": "💰 Demande de retrait !\n\n"
                                  "👤 Utilisateur : ID {user_id}\n"
                                  "💵 Montant : {amount}\n"
                                  "🆔 Demande #{id}\n\n"
                                  "Confirmer le retrait :\n/withdraw_admin {user_id} {amount}",
        "no_rights": "❌ Pas de droits !",
        "stats_text": "📈 Statistiques hebdomadaires\n\n",
        "stats_day": "📅 {day} :\n"
                     "   Factures : {total} | Payées : {paid}\n"
                     "   Montant : {amount} | Commission : {commission}\n\n",
        "stats_total": "📊 Total :\n"
                       "👥 Utilisateurs : {users}\n"
                       "💳 Paiements : {payments}\n"
                       "💰 Montant : {amount}\n"
                       "💸 Commissions : {commission}\n"
                       "⚙️ Commission : {percent}%",
        "users_list": "👥 Utilisateurs\n\n",
        "user_item": "• ID : {id} | Solde : {balance}\n",
        "users_more": "\n... et {count} autres utilisateurs",
        "admin_help": "👑 Commandes admin\n\n"
                      "📊 Statistiques et utilisateurs :\n"
                      "/stats — statistiques générales\n"
                      "/users — liste de tous les utilisateurs\n"
                      "/userinfo <id> — infos complètes sur l'utilisateur\n"
                      "/getid <username> — trouver l'ID par nom d'utilisateur\n\n"
                      "💳 Gestion des paiements :\n"
                      "/view <code_facture> — créer un code de visualisation unique\n"
                      "/check <code> — vérifier la transaction (pour tous)\n"
                      "/withdraw_admin <id> <montant> — confirmer le retrait\n\n"
                      "📋 Commandes pour les utilisateurs réguliers :\n"
                      "/start — menu principal\n"
                      "/language — changer la langue\n"
                      "/help — aide\n"
                      "/create <montant> — créer une facture\n"
                      "/pay <code> — payer une facture\n"
                      "/balance — mon solde\n"
                      "/withdraw <montant> — retirer des fonds\n"
                      "/check <code> — vérifier une transaction",
        "view_code_created": "✅ Code de visualisation créé !\n\n"
                             "🔑 Code : {view_code}\n"
                             "📋 Facture : {invoice_code}\n"
                             "⚠️ Unique, supprimé après visualisation",
        "invoice_not_paid": "❌ Facture pas encore payée !",
        "check_invoice": "📋 Informations sur la transaction\n\n"
                         "🔑 Code facture : {code}\n"
                         "💵 Montant : {amount}\n"
                         "📊 Statut : {status}\n"
                         "📅 Créé : {created}\n"
                         "💳 Commission : {commission}\n"
                         "👤 Destinataire : ID {creator}",
        "user_info": "👤 Informations sur l'utilisateur\n\n"
                     "🆔 ID : {id}\n"
                     "👤 Nom d'utilisateur : @{username}\n"
                     "📅 Inscrit : {registered}\n"
                     "💰 Solde : {balance}\n\n"
                     "📊 Statistiques :\n"
                     "📤 Factures créées : {created}\n"
                     "📥 Payé (en tant qu'acheteur) : {paid_count} pour {paid_sum}\n"
                     "💵 Gagné (en tant que vendeur) : {earned}\n"
                     "💸 Commissions payées : {commission_paid}\n\n"
                     "📋 Dernières factures (créées) :\n"
                     "  {invoices}\n\n"
                     "💳 Derniers paiements (en tant qu'acheteur) :\n"
                     "  {payments}",
        "user_not_found": "❌ Utilisateur non trouvé !",
        "invalid_id": "❌ Entrez un ID valide !",
        "user_not_in_db": "❌ Utilisateur @{username} non trouvé dans la base de données !\n\n"
                          "Demandez-lui d'écrire /start au bot.",
        "invoice_status_paid": "✅ payée",
        "invoice_status_pending": "⏳ en attente",
        "status": "statut",
        "expired": "Expirée",
        "time_left": "{minutes} min {seconds} sec",
        "payment_method_paypal": "👤 PayPal\n\nPayez via PayPal :\nexample@paypal.com\n\n"
                                  "💵 Montant : {amount}\n📝 Commentaire : {code}\n\n"
                                  "⚠️ Après le paiement, cliquez sur \"J'ai payé\"",
        "payment_method_usdt": "₿ USDT (TRC20)\n\nEnvoyez USDT à l'adresse :\nTRC20_ADDRESS_HERE\n\n"
                               "🌐 Réseau : TRC20\n💵 Montant : {amount} USDT\n\n"
                               "⚠️ Après l'envoi, cliquez sur \"J'ai payé\"",
        "payment_method_btc": "₿ Bitcoin\n\nEnvoyez BTC à l'adresse :\nBTC_ADDRESS_HERE\n\n"
                              "💵 Montant : {amount} BTC (au taux actuel)\n\n"
                              "⚠️ Après l'envoi, cliquez sur \"J'ai payé\"",
        "payment_method_p2p": "🏦 P2P (Binance)\n\nContactez le vendeur :\n👤 @P2P_Manager\n\n"
                              "💵 Montant : {amount} EUR\n\n"
                              "⚠️ Après le paiement, cliquez sur \"J'ai payé\"",
        "payment_method_card": "💳 Carte bancaire\n\nPayez via le lien :\n🔗 https://payment.link/{code}\n\n"
                               "💵 Montant : {amount}\n\n"
                               "⚠️ Après le paiement, cliquez sur \"J'ai payé\"",
        "i_paid": "✅ J'ai payé",
        "back_to_methods": "🔙 Retour aux méthodes",
        "main_menu_btn": "🏠 Menu principal",
        "use_buttons": "Utilisez les boutons du menu 👇",
        "language_command": "🌍 Changer la langue\n\nChoisissez la langue :",
        "language_changed": "✅ Langue changée en {language}",
        "paypal": "💳 PayPal",
        "usdt": "₿ USDT (TRC20)",
        "btc": "₿ Bitcoin (BTC)",
        "p2p": "🏦 P2P (Binance)",
        "card": "💳 Carte bancaire",
        "confirm_payment": "✅ J'ai payé",
        "min_withdraw_amount": "10",
    },
    "es": {
        "name": "Español",
        "flag": "🇪🇸",
        "select_language": "🌍 Seleccione el idioma:",
        "language_set": "✅ Idioma establecido: Español",
        "main_menu": "🏦 Menú principal\n\nSeleccione una acción:",
        "create_invoice": "💰 Crear factura",
        "pay_invoice": "💳 Pagar factura",
        "my_balance": "📊 Mi saldo",
        "withdraw": "💸 Retirar fondos",
        "help": "ℹ️ Ayuda",
        "admin_stats": "📈 Estadísticas",
        "admin_users": "👥 Usuarios",
        "help_admin": "👑 Comandos admin",
        "back": "🔙 Volver",
        "help_text": "ℹ️ Ayuda\n\n"
                     "💰 Crear factura — cree una factura de pago\n"
                     "💳 Pagar factura — pague una factura existente\n"
                     "📊 Saldo — verifique su saldo\n"
                     "💸 Retirar — retire fondos\n\n"
                     "⏳ Facturas válidas por 15 minutos\n"
                     "💱 Comisión: {commission}% (0.01 € por €)\n"
                     "🔒 Todos los pagos son anónimos\n"
                     "💰 Monto mínimo: 1 €",
        "create_invoice_text": "💰 Creación de factura\n\n"
                               "Ingrese el monto en euros:\n"
                               "Mínimo: 1 €\n"
                               "Máximo: 5000 €\n\n"
                               "Ejemplo: 50 o 100.50",
        "min_amount_error": "❌ Monto mínimo: 1 €",
        "max_amount_error": "❌ Monto máximo: 5000 €",
        "invalid_number": "❌ ¡Ingrese un número válido!",
        "create_error": "❌ ¡Error al crear la factura!",
        "invoice_created": "✅ ¡Factura creada!\n\n"
                           "💵 Monto: {amount}\n"
                           "🔑 Código: {code}\n"
                           "⏳ Factura válida por 15 minutos\n"
                           "💱 Comisión: {commission}%\n\n"
                           "Seleccione el método de pago:",
        "pay_invoice_text": "💳 Pagar factura\n\nIngrese el código de la factura (8 caracteres):",
        "invoice_not_found": "❌ ¡Factura no encontrada o ya pagada!",
        "invoice_expired": "❌ ¡Factura expirada (15 minutos)!",
        "payment_methods": "💳 Seleccione el método de pago\n\n"
                           "💵 Monto: {amount}\n"
                           "🔑 Código: {code}\n"
                           "⏳ Tiempo restante: {time_left}",
        "payment_confirmed_user": "✅ ¡Pago recibido!\n\n"
                                  "💵 Monto: {amount}\n"
                                  "💸 Comisión: {commission} ({percent}%)\n"
                                  "💳 Acreditado: {earned}\n"
                                  "🔑 Código: {code}",
        "payment_confirmed_buyer": "✅ ¡Pago confirmado!\n\n"
                                   "💵 Monto: {amount}\n"
                                   "🔑 Código: {code}\n\n"
                                   "¡Gracias por usar! 🙌",
        "balance_text": "📊 Su saldo\n\n"
                        "💰 Saldo: {balance}\n\n"
                        "💸 Retiro mínimo: {min_withdraw}\n"
                        "💱 Comisión de pago: {commission}%",
        "withdraw_text": "💸 Retirar fondos\n\n"
                         "Ingrese el monto a retirar:\n"
                         "Mínimo: 10 €\n\n"
                         "Ejemplo: 50 o 100.50",
        "withdraw_min_error": "❌ Retiro mínimo: 10 €",
        "insufficient_balance": "❌ ¡Saldo insuficiente!",
        "withdraw_create_error": "❌ ¡Error al crear la solicitud!",
        "withdraw_success": "✅ ¡Solicitud #{id} creada!\nMonto: {amount}\nEspere confirmación.",
        "admin_withdraw_request": "💰 ¡Solicitud de retiro!\n\n"
                                  "👤 Usuario: ID {user_id}\n"
                                  "💵 Monto: {amount}\n"
                                  "🆔 Solicitud #{id}\n\n"
                                  "Confirmar retiro:\n/withdraw_admin {user_id} {amount}",
        "no_rights": "❌ ¡Sin derechos!",
        "stats_text": "📈 Estadísticas semanales\n\n",
        "stats_day": "📅 {day}:\n"
                     "   Facturas: {total} | Pagadas: {paid}\n"
                     "   Monto: {amount} | Comisión: {commission}\n\n",
        "stats_total": "📊 Total:\n"
                       "👥 Usuarios: {users}\n"
                       "💳 Pagos: {payments}\n"
                       "💰 Monto: {amount}\n"
                       "💸 Comisiones: {commission}\n"
                       "⚙️ Comisión: {percent}%",
        "users_list": "👥 Usuarios\n\n",
        "user_item": "• ID: {id} | Saldo: {balance}\n",
        "users_more": "\n... y {count} usuarios más",
        "admin_help": "👑 Comandos admin\n\n"
                      "📊 Estadísticas y usuarios:\n"
                      "/stats — estadísticas generales\n"
                      "/users — lista de todos los usuarios\n"
                      "/userinfo <id> — información completa del usuario\n"
                      "/getid <username> — encontrar ID por nombre de usuario\n\n"
                      "💳 Gestión de pagos:\n"
                      "/view <código_factura> — crear código de visualización único\n"
                      "/check <código> — verificar transacción (para todos)\n"
                      "/withdraw_admin <id> <monto> — confirmar retiro\n\n"
                      "📋 Comandos para usuarios regulares:\n"
                      "/start — menú principal\n"
                      "/language — cambiar idioma\n"
                      "/help — ayuda\n"
                      "/create <monto> — crear factura\n"
                      "/pay <código> — pagar factura\n"
                      "/balance — mi saldo\n"
                      "/withdraw <monto> — retirar fondos\n"
                      "/check <código> — verificar transacción",
        "view_code_created": "✅ ¡Código de visualización creado!\n\n"
                             "🔑 Código: {view_code}\n"
                             "📋 Factura: {invoice_code}\n"
                             "⚠️ Único, eliminado después de la visualización",
        "invoice_not_paid": "❌ ¡Factura aún no pagada!",
        "check_invoice": "📋 Información de la transacción\n\n"
                         "🔑 Código de factura: {code}\n"
                         "💵 Monto: {amount}\n"
                         "📊 Estado: {status}\n"
                         "📅 Creado: {created}\n"
                         "💳 Comisión: {commission}\n"
                         "👤 Destinatario: ID {creator}",
        "user_info": "👤 Información del usuario\n\n"
                     "🆔 ID: {id}\n"
                     "👤 Usuario: @{username}\n"
                     "📅 Registrado: {registered}\n"
                     "💰 Saldo: {balance}\n\n"
                     "📊 Estadísticas:\n"
                     "📤 Facturas creadas: {created}\n"
                     "📥 Pagado (como comprador): {paid_count} por {paid_sum}\n"
                     "💵 Ganado (como vendedor): {earned}\n"
                     "💸 Comisiones pagadas: {commission_paid}\n\n"
                     "📋 Últimas facturas (creadas):\n"
                     "  {invoices}\n\n"
                     "💳 Últimos pagos (como comprador):\n"
                     "  {payments}",
        "user_not_found": "❌ ¡Usuario no encontrado!",
        "invalid_id": "❌ ¡Ingrese un ID válido!",
        "user_not_in_db": "❌ ¡Usuario @{username} no encontrado en la base de datos!\n\n"
                          "Pídale que escriba /start al bot.",
        "invoice_status_paid": "✅ pagada",
        "invoice_status_pending": "⏳ pendiente",
        "status": "estado",
        "expired": "Expirada",
        "time_left": "{minutes} min {seconds} seg",
        "payment_method_paypal": "👤 PayPal\n\nPague vía PayPal:\nexample@paypal.com\n\n"
                                  "💵 Monto: {amount}\n📝 Comentario: {code}\n\n"
                                  "⚠️ Después del pago, haga clic en \"He pagado\"",
        "payment_method_usdt": "₿ USDT (TRC20)\n\nEnvie USDT a la dirección:\nTRC20_ADDRESS_HERE\n\n"
                               "🌐 Red: TRC20\n💵 Monto: {amount} USDT\n\n"
                               "⚠️ Después del envío, haga clic en \"He pagado\"",
        "payment_method_btc": "₿ Bitcoin\n\nEnvie BTC a la dirección:\nBTC_ADDRESS_HERE\n\n"
                              "💵 Monto: {amount} BTC (según tasa actual)\n\n"
                              "⚠️ Después del envío, haga clic en \"He pagado\"",
        "payment_method_p2p": "🏦 P2P (Binance)\n\nContacte al vendedor:\n👤 @P2P_Manager\n\n"
                              "💵 Monto: {amount} EUR\n\n"
                              "⚠️ Después del pago, haga clic en \"He pagado\"",
        "payment_method_card": "💳 Tarjeta bancaria\n\nPague a través del enlace:\n🔗 https://payment.link/{code}\n\n"
                               "💵 Monto: {amount}\n\n"
                               "⚠️ Después del pago, haga clic en \"He pagado\"",
        "i_paid": "✅ He pagado",
        "back_to_methods": "🔙 Volver a métodos",
        "main_menu_btn": "🏠 Menú principal",
        "use_buttons": "Use los botones del menú 👇",
        "language_command": "🌍 Cambiar idioma\n\nSeleccione el idioma:",
        "language_changed": "✅ Idioma cambiado a {language}",
        "paypal": "💳 PayPal",
        "usdt": "₿ USDT (TRC20)",
        "btc": "₿ Bitcoin (BTC)",
        "p2p": "🏦 P2P (Binance)",
        "card": "💳 Tarjeta bancaria",
        "confirm_payment": "✅ He pagado",
        "min_withdraw_amount": "10",
    },
    "pt": {
        "name": "Português",
        "flag": "🇵🇹",
        "select_language": "🌍 Selecione o idioma:",
        "language_set": "✅ Idioma definido: Português",
        "main_menu": "🏦 Menu principal\n\nSelecione uma ação:",
        "create_invoice": "💰 Criar fatura",
        "pay_invoice": "💳 Pagar fatura",
        "my_balance": "📊 Meu saldo",
        "withdraw": "💸 Sacar fundos",
        "help": "ℹ️ Ajuda",
        "admin_stats": "📈 Estatísticas",
        "admin_users": "👥 Utilizadores",
        "help_admin": "👑 Comandos admin",
        "back": "🔙 Voltar",
        "help_text": "ℹ️ Ajuda\n\n"
                     "💰 Criar fatura — crie uma fatura de pagamento\n"
                     "💳 Pagar fatura — pague uma fatura existente\n"
                     "📊 Saldo — verifique seu saldo\n"
                     "💸 Sacar — retire fundos\n\n"
                     "⏳ Faturas válidas por 15 minutos\n"
                     "💱 Comissão: {commission}% (0.01 € por €)\n"
                     "🔒 Todos os pagamentos são anônimos\n"
                     "💰 Valor mínimo: 1 €",
        "create_invoice_text": "💰 Criação de fatura\n\n"
                               "Digite o valor em euros:\n"
                               "Mínimo: 1 €\n"
                               "Máximo: 5000 €\n\n"
                               "Exemplo: 50 ou 100.50",
        "min_amount_error": "❌ Valor mínimo: 1 €",
        "max_amount_error": "❌ Valor máximo: 5000 €",
        "invalid_number": "❌ Digite um número válido!",
        "create_error": "❌ Erro ao criar fatura!",
        "invoice_created": "✅ Fatura criada!\n\n"
                           "💵 Valor: {amount}\n"
                           "🔑 Código: {code}\n"
                           "⏳ Fatura válida por 15 minutos\n"
                           "💱 Comissão: {commission}%\n\n"
                           "Selecione o método de pagamento:",
        "pay_invoice_text": "💳 Pagar fatura\n\nDigite o código da fatura (8 caracteres):",
        "invoice_not_found": "❌ Fatura não encontrada ou já paga!",
        "invoice_expired": "❌ Fatura expirada (15 minutos)!",
        "payment_methods": "💳 Selecione o método de pagamento\n\n"
                           "💵 Valor: {amount}\n"
                           "🔑 Código: {code}\n"
                           "⏳ Tempo restante: {time_left}",
        "payment_confirmed_user": "✅ Pagamento recebido!\n\n"
                                  "💵 Valor: {amount}\n"
                                  "💸 Comissão: {commission} ({percent}%)\n"
                                  "💳 Creditado: {earned}\n"
                                  "🔑 Código: {code}",
        "payment_confirmed_buyer": "✅ Pagamento confirmado!\n\n"
                                   "💵 Valor: {amount}\n"
                                   "🔑 Código: {code}\n\n"
                                   "Obrigado por usar! 🙌",
        "balance_text": "📊 Seu saldo\n\n"
                        "💰 Saldo: {balance}\n\n"
                        "💸 Saque mínimo: {min_withdraw}\n"
                        "💱 Comissão de pagamento: {commission}%",
        "withdraw_text": "💸 Sacar fundos\n\n"
                         "Digite o valor para sacar:\n"
                         "Mínimo: 10 €\n\n"
                         "Exemplo: 50 ou 100.50",
        "withdraw_min_error": "❌ Saque mínimo: 10 €",
        "insufficient_balance": "❌ Saldo insuficiente!",
        "withdraw_create_error": "❌ Erro ao criar solicitação!",
        "withdraw_success": "✅ Solicitação #{id} criada!\nValor: {amount}\nAguarde confirmação.",
        "admin_withdraw_request": "💰 Solicitação de saque!\n\n"
                                  "👤 Usuário: ID {user_id}\n"
                                  "💵 Valor: {amount}\n"
                                  "🆔 Solicitação #{id}\n\n"
                                  "Confirmar saque:\n/withdraw_admin {user_id} {amount}",
        "no_rights": "❌ Sem direitos!",
        "stats_text": "📈 Estatísticas semanais\n\n",
        "stats_day": "📅 {day}:\n"
                     "   Faturas: {total} | Pagas: {paid}\n"
                     "   Valor: {amount} | Comissão: {commission}\n\n",
        "stats_total": "📊 Total:\n"
                       "👥 Utilizadores: {users}\n"
                       "💳 Pagamentos: {payments}\n"
                       "💰 Valor: {amount}\n"
                       "💸 Comissões: {commission}\n"
                       "⚙️ Comissão: {percent}%",
        "users_list": "👥 Utilizadores\n\n",
        "user_item": "• ID: {id} | Saldo: {balance}\n",
        "users_more": "\n... e mais {count} utilizadores",
        "admin_help": "👑 Comandos admin\n\n"
                      "📊 Estatísticas e utilizadores:\n"
                      "/stats — estatísticas gerais\n"
                      "/users — lista de todos os utilizadores\n"
                      "/userinfo <id> — informações completas do utilizador\n"
                      "/getid <username> — encontrar ID por nome de utilizador\n\n"
                      "💳 Gestão de pagamentos:\n"
                      "/view <código_fatura> — criar código de visualização único\n"
                      "/check <código> — verificar transação (para todos)\n"
                      "/withdraw_admin <id> <valor> — confirmar saque\n\n"
                      "📋 Comandos para utilizadores regulares:\n"
                      "/start — menu principal\n"
                      "/language — mudar idioma\n"
                      "/help — ajuda\n"
                      "/create <valor> — criar fatura\n"
                      "/pay <código> — pagar fatura\n"
                      "/balance — meu saldo\n"
                      "/withdraw <valor> — sacar fundos\n"
                      "/check <código> — verificar transação",
        "view_code_created": "✅ Código de visualização criado!\n\n"
                             "🔑 Código: {view_code}\n"
                             "📋 Fatura: {invoice_code}\n"
                             "⚠️ Único, excluído após visualização",
        "invoice_not_paid": "❌ Fatura ainda não paga!",
        "check_invoice": "📋 Informações da transação\n\n"
                         "🔑 Código da fatura: {code}\n"
                         "💵 Valor: {amount}\n"
                         "📊 Status: {status}\n"
                         "📅 Criado: {created}\n"
                         "💳 Comissão: {commission}\n"
                         "👤 Destinatário: ID {creator}",
        "user_info": "👤 Informações do utilizador\n\n"
                     "🆔 ID: {id}\n"
                     "👤 Nome de utilizador: @{username}\n"
                     "📅 Registrado: {registered}\n"
                     "💰 Saldo: {balance}\n\n"
                     "📊 Estatísticas:\n"
                     "📤 Faturas criadas: {created}\n"
                     "📥 Pago (como comprador): {paid_count} por {paid_sum}\n"
                     "💵 Ganho (como vendedor): {earned}\n"
                     "💸 Comissões pagas: {commission_paid}\n\n"
                     "📋 Últimas faturas (criadas):\n"
                     "  {invoices}\n\n"
                     "💳 Últimos pagamentos (como comprador):\n"
                     "  {payments}",
        "user_not_found": "❌ Utilizador não encontrado!",
        "invalid_id": "❌ Digite um ID válido!",
        "user_not_in_db": "❌ Utilizador @{username} não encontrado no banco de dados!\n\n"
                          "Peça para ele escrever /start para o bot.",
        "invoice_status_paid": "✅ paga",
        "invoice_status_pending": "⏳ pendente",
        "status": "status",
        "expired": "Expirada",
        "time_left": "{minutes} min {seconds} seg",
        "payment_method_paypal": "👤 PayPal\n\nPague via PayPal:\nexample@paypal.com\n\n"
                                  "💵 Valor: {amount}\n📝 Comentário: {code}\n\n"
                                  "⚠️ Após o pagamento, clique em \"Eu paguei\"",
        "payment_method_usdt": "₿ USDT (TRC20)\n\nEnvie USDT para o endereço:\nTRC20_ADDRESS_HERE\n\n"
                               "🌐 Rede: TRC20\n💵 Valor: {amount} USDT\n\n"
                               "⚠️ Após o envio, clique em \"Eu paguei\"",
        "payment_method_btc": "₿ Bitcoin\n\nEnvie BTC para o endereço:\nBTC_ADDRESS_HERE\n\n"
                              "💵 Valor: {amount} BTC (na taxa atual)\n\n"
                              "⚠️ Após o envio, clique em \"Eu paguei\"",
        "payment_method_p2p": "🏦 P2P (Binance)\n\nContacte o vendedor:\n👤 @P2P_Manager\n\n"
                              "💵 Valor: {amount} EUR\n\n"
                              "⚠️ Após o pagamento, clique em \"Eu paguei\"",
        "payment_method_card": "💳 Cartão bancário\n\nPague através do link:\n🔗 https://payment.link/{code}\n\n"
                               "💵 Valor: {amount}\n\n"
                               "⚠️ Após o pagamento, clique em \"Eu paguei\"",
        "i_paid": "✅ Eu paguei",
        "back_to_methods": "🔙 Voltar aos métodos",
        "main_menu_btn": "🏠 Menu principal",
        "use_buttons": "Use os botões do menu 👇",
        "language_command": "🌍 Mudar idioma\n\nSelecione o idioma:",
        "language_changed": "✅ Idioma alterado para {language}",
        "paypal": "💳 PayPal",
        "usdt": "₿ USDT (TRC20)",
        "btc": "₿ Bitcoin (BTC)",
        "p2p": "🏦 P2P (Binance)",
        "card": "💳 Cartão bancário",
        "confirm_payment": "✅ Eu paguei",
        "min_withdraw_amount": "10",
    },
    "it": {
        "name": "Italiano",
        "flag": "🇮🇹",
        "select_language": "🌍 Seleziona la lingua:",
        "language_set": "✅ Lingua impostata: Italiano",
        "main_menu": "🏦 Menu principale\n\nSeleziona un'azione:",
        "create_invoice": "💰 Crea fattura",
        "pay_invoice": "💳 Paga fattura",
        "my_balance": "📊 Il mio saldo",
        "withdraw": "💸 Preleva fondi",
        "help": "ℹ️ Aiuto",
        "admin_stats": "📈 Statistiche",
        "admin_users": "👥 Utenti",
        "help_admin": "👑 Comandi admin",
        "back": "🔙 Indietro",
        "help_text": "ℹ️ Aiuto\n\n"
                     "💰 Crea fattura — crea una fattura di pagamento\n"
                     "💳 Paga fattura — paga una fattura esistente\n"
                     "📊 Saldo — verifica il tuo saldo\n"
                     "💸 Preleva — preleva fondi\n\n"
                     "⏳ Fatture valide 15 minuti\n"
                     "💱 Commissione: {commission}% (0.01 € per €)\n"
                     "🔒 Tutti i pagamenti sono anonimi\n"
                     "💰 Importo minimo: 1 €",
        "create_invoice_text": "💰 Creazione fattura\n\n"
                               "Inserisci l'importo in euro:\n"
                               "Minimo: 1 €\n"
                               "Massimo: 5000 €\n\n"
                               "Esempio: 50 o 100.50",
        "min_amount_error": "❌ Importo minimo: 1 €",
        "max_amount_error": "❌ Importo massimo: 5000 €",
        "invalid_number": "❌ Inserisci un numero valido!",
        "create_error": "❌ Errore nella creazione della fattura!",
        "invoice_created": "✅ Fattura creata!\n\n"
                           "💵 Importo: {amount}\n"
                           "🔑 Codice: {code}\n"
                           "⏳ Fattura valida 15 minuti\n"
                           "💱 Commissione: {commission}%\n\n"
                           "Seleziona il metodo di pagamento:",
        "pay_invoice_text": "💳 Paga fattura\n\nInserisci il codice della fattura (8 caratteri):",
        "invoice_not_found": "❌ Fattura non trovata o già pagata!",
        "invoice_expired": "❌ Fattura scaduta (15 minuti)!",
        "payment_methods": "💳 Seleziona il metodo di pagamento\n\n"
                           "💵 Importo: {amount}\n"
                           "🔑 Codice: {code}\n"
                           "⏳ Tempo rimanente: {time_left}",
        "payment_confirmed_user": "✅ Pagamento ricevuto!\n\n"
                                  "💵 Importo: {amount}\n"
                                  "💸 Commissione: {commission} ({percent}%)\n"
                                  "💳 Accreditato: {earned}\n"
                                  "🔑 Codice: {code}",
        "payment_confirmed_buyer": "✅ Pagamento confermato!\n\n"
                                   "💵 Importo: {amount}\n"
                                   "🔑 Codice: {code}\n\n"
                                   "Grazie per aver utilizzato! 🙌",
        "balance_text": "📊 Il tuo saldo\n\n"
                        "💰 Saldo: {balance}\n\n"
                        "💸 Prelievo minimo: {min_withdraw}\n"
                        "💱 Commissione di pagamento: {commission}%",
        "withdraw_text": "💸 Preleva fondi\n\n"
                         "Inserisci l'importo da prelevare:\n"
                         "Minimo: 10 €\n\n"
                         "Esempio: 50 o 100.50",
        "withdraw_min_error": "❌ Prelievo minimo: 10 €",
        "insufficient_balance": "❌ Saldo insufficiente!",
        "withdraw_create_error": "❌ Errore nella creazione della richiesta!",
        "withdraw_success": "✅ Richiesta #{id} creata!\nImporto: {amount}\nAttendi conferma.",
        "admin_withdraw_request": "💰 Richiesta di prelievo!\n\n"
                                  "👤 Utente: ID {user_id}\n"
                                  "💵 Importo: {amount}\n"
                                  "🆔 Richiesta #{id}\n\n"
                                  "Conferma prelievo:\n/withdraw_admin {user_id} {amount}",
        "no_rights": "❌ Nessun diritto!",
        "stats_text": "📈 Statistiche settimanali\n\n",
        "stats_day": "📅 {day}:\n"
                     "   Fatture: {total} | Pagate: {paid}\n"
                     "   Importo: {amount} | Commissione: {commission}\n\n",
        "stats_total": "📊 Totale:\n"
                       "👥 Utenti: {users}\n"
                       "💳 Pagamenti: {payments}\n"
                       "💰 Importo: {amount}\n"
                       "💸 Commissioni: {commission}\n"
                       "⚙️ Commissione: {percent}%",
        "users_list": "👥 Utenti\n\n",
        "user_item": "• ID: {id} | Saldo: {balance}\n",
        "users_more": "\n... e altri {count} utenti",
        "admin_help": "👑 Comandi admin\n\n"
                      "📊 Statistiche e utenti:\n"
                      "/stats — statistiche generali\n"
                      "/users — elenco di tutti gli utenti\n"
                      "/userinfo <id> — informazioni complete dell'utente\n"
                      "/getid <username> — trovare ID per nome utente\n\n"
                      "💳 Gestione pagamenti:\n"
                      "/view <codice_fattura> — crea codice di visualizzazione unico\n"
                      "/check <codice> — verifica transazione (per tutti)\n"
                      "/withdraw_admin <id> <importo> — conferma prelievo\n\n"
                      "📋 Comandi per utenti regolari:\n"
                      "/start — menu principale\n"
                      "/language — cambia lingua\n"
                      "/help — aiuto\n"
                      "/create <importo> — crea fattura\n"
                      "/pay <codice> — paga fattura\n"
                      "/balance — il mio saldo\n"
                      "/withdraw <importo> — preleva fondi\n"
                      "/check <codice> — verifica transazione",
        "view_code_created": "✅ Codice di visualizzazione creato!\n\n"
                             "🔑 Codice: {view_code}\n"
                             "📋 Fattura: {invoice_code}\n"
                             "⚠️ Unico, eliminato dopo la visualizzazione",
        "invoice_not_paid": "❌ Fattura non ancora pagata!",
        "check_invoice": "📋 Informazioni sulla transazione\n\n"
                         "🔑 Codice fattura: {code}\n"
                         "💵 Importo: {amount}\n"
                         "📊 Stato: {status}\n"
                         "📅 Creato: {created}\n"
                         "💳 Commissione: {commission}\n"
                         "👤 Destinatario: ID {creator}",
        "user_info": "👤 Informazioni utente\n\n"
                     "🆔 ID: {id}\n"
                     "👤 Nome utente: @{username}\n"
                     "📅 Registrato: {registered}\n"
                     "💰 Saldo: {balance}\n\n"
                     "📊 Statistiche:\n"
                     "📤 Fatture create: {created}\n"
                     "📥 Pagato (come acquirente): {paid_count} per {paid_sum}\n"
                     "💵 Guadagnato (come venditore): {earned}\n"
                     "💸 Commissioni pagate: {commission_paid}\n\n"
                     "📋 Ultime fatture (create):\n"
                     "  {invoices}\n\n"
                     "💳 Ultimi pagamenti (come acquirente):\n"
                     "  {payments}",
        "user_not_found": "❌ Utente non trovato!",
        "invalid_id": "❌ Inserisci un ID valido!",
        "user_not_in_db": "❌ Utente @{username} non trovato nel database!\n\n"
                          "Chiedigli di scrivere /start al bot.",
        "invoice_status_paid": "✅ pagata",
        "invoice_status_pending": "⏳ in attesa",
        "status": "stato",
        "expired": "Scaduta",
        "time_left": "{minutes} min {seconds} sec",
        "payment_method_paypal": "👤 PayPal\n\nPaga tramite PayPal:\nexample@paypal.com\n\n"
                                  "💵 Importo: {amount}\n📝 Commento: {code}\n\n"
                                  "⚠️ Dopo il pagamento, clicca su \"Ho pagato\"",
        "payment_method_usdt": "₿ USDT (TRC20)\n\nInvia USDT all'indirizzo:\nTRC20_ADDRESS_HERE\n\n"
                               "🌐 Rete: TRC20\n💵 Importo: {amount} USDT\n\n"
                               "⚠️ Dopo l'invio, clicca su \"Ho pagato\"",
        "payment_method_btc": "₿ Bitcoin\n\nInvia BTC all'indirizzo:\nBTC_ADDRESS_HERE\n\n"
                              "💵 Importo: {amount} BTC (al tasso attuale)\n\n"
                              "⚠️ Dopo l'invio, clicca su \"Ho pagato\"",
        "payment_method_p2p": "🏦 P2P (Binance)\n\nContatta il venditore:\n👤 @P2P_Manager\n\n"
                              "💵 Importo: {amount} EUR\n\n"
                              "⚠️ Dopo il pagamento, clicca su \"Ho pagato\"",
        "payment_method_card": "💳 Carta bancaria\n\nPaga tramite link:\n🔗 https://payment.link/{code}\n\n"
                               "💵 Importo: {amount}\n\n"
                               "⚠️ Dopo il pagamento, clicca su \"Ho pagato\"",
        "i_paid": "✅ Ho pagato",
        "back_to_methods": "🔙 Torna ai metodi",
        "main_menu_btn": "🏠 Menu principale",
        "use_buttons": "Usa i pulsanti del menu 👇",
        "language_command": "🌍 Cambia lingua\n\nSeleziona la lingua:",
        "language_changed": "✅ Lingua cambiata in {language}",
        "paypal": "💳 PayPal",
        "usdt": "₿ USDT (TRC20)",
        "btc": "₿ Bitcoin (BTC)",
        "p2p": "🏦 P2P (Binance)",
        "card": "💳 Carta bancaria",
        "confirm_payment": "✅ Ho pagato",
        "min_withdraw_amount": "10",
    },
    "de": {
        "name": "Deutsch",
        "flag": "🇩🇪",
        "select_language": "🌍 Sprache wählen:",
        "language_set": "✅ Sprache eingestellt: Deutsch",
        "main_menu": "🏦 Hauptmenü\n\nWählen Sie eine Aktion:",
        "create_invoice": "💰 Rechnung erstellen",
        "pay_invoice": "💳 Rechnung bezahlen",
        "my_balance": "📊 Mein Guthaben",
        "withdraw": "💸 Geld abheben",
        "help": "ℹ️ Hilfe",
        "admin_stats": "📈 Statistiken",
        "admin_users": "👥 Benutzer",
        "help_admin": "👑 Admin-Befehle",
        "back": "🔙 Zurück",
        "help_text": "ℹ️ Hilfe\n\n"
                     "💰 Rechnung erstellen — Zahlungsrechnung erstellen\n"
                     "💳 Rechnung bezahlen — vorhandene Rechnung bezahlen\n"
                     "📊 Guthaben — Ihr Guthaben prüfen\n"
                     "💸 Abheben — Geld abheben\n\n"
                     "⏳ Rechnungen 15 Minuten gültig\n"
                     "💱 Provision: {commission}% (0.01 € pro €)\n"
                     "🔒 Alle Zahlungen sind anonym\n"
                     "💰 Mindestbetrag: 1 €",
        "create_invoice_text": "💰 Rechnung erstellen\n\n"
                               "Betrag in Euro eingeben:\n"
                               "Minimum: 1 €\n"
                               "Maximum: 5000 €\n\n"
                               "Beispiel: 50 oder 100.50",
        "min_amount_error": "❌ Mindestbetrag: 1 €",
        "max_amount_error": "❌ Höchstbetrag: 5000 €",
        "invalid_number": "❌ Geben Sie eine gültige Zahl ein!",
        "create_error": "❌ Fehler beim Erstellen der Rechnung!",
        "invoice_created": "✅ Rechnung erstellt!\n\n"
                           "💵 Betrag: {amount}\n"
                           "🔑 Code: {code}\n"
                           "⏳ Rechnung 15 Minuten gültig\n"
                           "💱 Provision: {commission}%\n\n"
                           "Zahlungsmethode wählen:",
        "pay_invoice_text": "💳 Rechnung bezahlen\n\nRechnungscode eingeben (8 Zeichen):",
        "invoice_not_found": "❌ Rechnung nicht gefunden oder bereits bezahlt!",
        "invoice_expired": "❌ Rechnung abgelaufen (15 Minuten)!",
        "payment_methods": "💳 Zahlungsmethode wählen\n\n"
                           "💵 Betrag: {amount}\n"
                           "🔑 Code: {code}\n"
                           "⏳ Verbleibende Zeit: {time_left}",
        "payment_confirmed_user": "✅ Zahlung erhalten!\n\n"
                                  "💵 Betrag: {amount}\n"
                                  "💸 Provision: {commission} ({percent}%)\n"
                                  "💳 Gutgeschrieben: {earned}\n"
                                  "🔑 Code: {code}",
        "payment_confirmed_buyer": "✅ Zahlung bestätigt!\n\n"
                                   "💵 Betrag: {amount}\n"
                                   "🔑 Code: {code}\n\n"
                                   "Danke für die Nutzung! 🙌",
        "balance_text": "📊 Ihr Guthaben\n\n"
                        "💰 Guthaben: {balance}\n\n"
                        "💸 Mindestabhebung: {min_withdraw}\n"
                        "💱 Zahlungsprovision: {commission}%",
        "withdraw_text": "💸 Geld abheben\n\n"
                         "Betrag zum Abheben eingeben:\n"
                         "Minimum: 10 €\n\n"
                         "Beispiel: 50 oder 100.50",
        "withdraw_min_error": "❌ Mindestabhebung: 10 €",
        "insufficient_balance": "❌ Nicht genügend Guthaben!",
        "withdraw_create_error": "❌ Fehler beim Erstellen der Anfrage!",
        "withdraw_success": "✅ Anfrage #{id} erstellt!\nBetrag: {amount}\nWarten auf Bestätigung.",
        "admin_withdraw_request": "💰 Abhebungsanfrage!\n\n"
                                  "👤 Benutzer: ID {user_id}\n"
                                  "💵 Betrag: {amount}\n"
                                  "🆔 Anfrage #{id}\n\n"
                                  "Abhebung bestätigen:\n/withdraw_admin {user_id} {amount}",
        "no_rights": "❌ Keine Rechte!",
        "stats_text": "📈 Wochenstatistiken\n\n",
        "stats_day": "📅 {day}:\n"
                     "   Rechnungen: {total} | Bezahlt: {paid}\n"
                     "   Betrag: {amount} | Provision: {commission}\n\n",
        "stats_total": "📊 Gesamt:\n"
                       "👥 Benutzer: {users}\n"
                       "💳 Zahlungen: {payments}\n"
                       "💰 Betrag: {amount}\n"
                       "💸 Provisionen: {commission}\n"
                       "⚙️ Provision: {percent}%",
        "users_list": "👥 Benutzer\n\n",
        "user_item": "• ID: {id} | Guthaben: {balance}\n",
        "users_more": "\n... und {count} weitere Benutzer",
        "admin_help": "👑 Admin-Befehle\n\n"
                      "📊 Statistiken und Benutzer:\n"
                      "/stats — allgemeine Statistiken\n"
                      "/users — alle Benutzer auflisten\n"
                      "/userinfo <id> — vollständige Benutzerinfo\n"
                      "/getid <username> — ID per Benutzername finden\n\n"
                      "💳 Zahlungsverwaltung:\n"
                      "/view <rechnungscode> — einmaligen Ansichtscode erstellen\n"
                      "/check <code> — Transaktion prüfen (für alle)\n"
                      "/withdraw_admin <id> <betrag> — Abhebung bestätigen\n\n"
                      "📋 Befehle für normale Benutzer:\n"
                      "/start — Hauptmenü\n"
                      "/language — Sprache ändern\n"
                      "/help — Hilfe\n"
                      "/create <betrag> — Rechnung erstellen\n"
                      "/pay <code> — Rechnung bezahlen\n"
                      "/balance — mein Guthaben\n"
                      "/withdraw <betrag> — Geld abheben\n"
                      "/check <code> — Transaktion prüfen",
        "view_code_created": "✅ Ansichtscode erstellt!\n\n"
                             "🔑 Code: {view_code}\n"
                             "📋 Rechnung: {invoice_code}\n"
                             "⚠️ Einmalig, nach Ansicht gelöscht",
        "invoice_not_paid": "❌ Rechnung noch nicht bezahlt!",
        "check_invoice": "📋 Transaktionsinformationen\n\n"
                         "🔑 Rechnungscode: {code}\n"
                         "💵 Betrag: {amount}\n"
                         "📊 Status: {status}\n"
                         "📅 Erstellt: {created}\n"
                         "💳 Provision: {commission}\n"
                         "👤 Empfänger: ID {creator}",
        "user_info": "👤 Benutzerinfo\n\n"
                     "🆔 ID: {id}\n"
                     "👤 Benutzername: @{username}\n"
                     "📅 Registriert: {registered}\n"
                     "💰 Guthaben: {balance}\n\n"
                     "📊 Statistiken:\n"
                     "📤 Rechnungen erstellt: {created}\n"
                     "📥 Bezahlt (als Käufer): {paid_count} für {paid_sum}\n"
                     "💵 Verdient (als Verkäufer): {earned}\n"
                     "💸 Provisionen gezahlt: {commission_paid}\n\n"
                     "📋 Letzte Rechnungen (erstellt):\n"
                     "  {invoices}\n\n"
                     "💳 Letzte Zahlungen (als Käufer):\n"
                     "  {payments}",
        "user_not_found": "❌ Benutzer nicht gefunden!",
        "invalid_id": "❌ Geben Sie eine gültige ID ein!",
        "user_not_in_db": "❌ Benutzer @{username} nicht in der Datenbank gefunden!\n\n"
                          "Bitten Sie ihn, /start an den Bot zu schreiben.",
        "invoice_status_paid": "✅ bezahlt",
        "invoice_status_pending": "⏳ ausstehend",
        "status": "Status",
        "expired": "Abgelaufen",
        "time_left": "{minutes} min {seconds} sek",
        "payment_method_paypal": "👤 PayPal\n\nZahlen Sie über PayPal:\nexample@paypal.com\n\n"
                                  "💵 Betrag: {amount}\n📝 Kommentar: {code}\n\n"
                                  "⚠️ Nach der Zahlung auf \"Ich habe bezahlt\" klicken",
        "payment_method_usdt": "₿ USDT (TRC20)\n\nSenden Sie USDT an die Adresse:\nTRC20_ADDRESS_HERE\n\n"
                               "🌐 Netzwerk: TRC20\n💵 Betrag: {amount} USDT\n\n"
                               "⚠️ Nach dem Senden auf \"Ich habe bezahlt\" klicken",
        "payment_method_btc": "₿ Bitcoin\n\nSenden Sie BTC an die Adresse:\nBTC_ADDRESS_HERE\n\n"
                              "💵 Betrag: {amount} BTC (zum aktuellen Kurs)\n\n"
                              "⚠️ Nach dem Senden auf \"Ich habe bezahlt\" klicken",
        "payment_method_p2p": "🏦 P2P (Binance)\n\nKontaktieren Sie den Verkäufer:\n👤 @P2P_Manager\n\n"
                              "💵 Betrag: {amount} EUR\n\n"
                              "⚠️ Nach der Zahlung auf \"Ich habe bezahlt\" klicken",
        "payment_method_card": "💳 Bankkarte\n\nZahlen Sie über den Link:\n🔗 https://payment.link/{code}\n\n"
                               "💵 Betrag: {amount}\n\n"
                               "⚠️ Nach der Zahlung auf \"Ich habe bezahlt\" klicken",
        "i_paid": "✅ Ich habe bezahlt",
        "back_to_methods": "🔙 Zurück zu den Methoden",
        "main_menu_btn": "🏠 Hauptmenü",
        "use_buttons": "Verwenden Sie die Menü-Buttons 👇",
        "language_command": "🌍 Sprache ändern\n\nSprache wählen:",
        "language_changed": "✅ Sprache geändert auf {language}",
        "paypal": "💳 PayPal",
        "usdt": "₿ USDT (TRC20)",
        "btc": "₿ Bitcoin (BTC)",
        "p2p": "🏦 P2P (Binance)",
        "card": "💳 Bankkarte",
        "confirm_payment": "✅ Ich habe bezahlt",
        "min_withdraw_amount": "10",
    },
    "pl": {
        "name": "Polski",
        "flag": "🇵🇱",
        "select_language": "🌍 Wybierz język:",
        "language_set": "✅ Język ustawiony: Polski",
        "main_menu": "🏦 Menu główne\n\nWybierz akcję:",
        "create_invoice": "💰 Utwórz fakturę",
        "pay_invoice": "💳 Zapłać fakturę",
        "my_balance": "📊 Moje saldo",
        "withdraw": "💸 Wypłać środki",
        "help": "ℹ️ Pomoc",
        "admin_stats": "📈 Statystyki",
        "admin_users": "👥 Użytkownicy",
        "help_admin": "👑 Polecenia admina",
        "back": "🔙 Wstecz",
        "help_text": "ℹ️ Pomoc\n\n"
                     "💰 Utwórz fakturę — utwórz fakturę płatności\n"
                     "💳 Zapłać fakturę — zapłać istniejącą fakturę\n"
                     "📊 Saldo — sprawdź swoje saldo\n"
                     "💸 Wypłać — wypłać środki\n\n"
                     "⏳ Faktury ważne 15 minut\n"
                     "💱 Prowizja: {commission}% (0.01 € za każdy €)\n"
                     "🔒 Wszystkie płatności są anonimowe\n"
                     "💰 Minimalna kwota: 1 €",
        "create_invoice_text": "💰 Tworzenie faktury\n\n"
                               "Wprowadź kwotę w euro:\n"
                               "Minimum: 1 €\n"
                               "Maksimum: 5000 €\n\n"
                               "Przykład: 50 lub 100.50",
        "min_amount_error": "❌ Minimalna kwota: 1 €",
        "max_amount_error": "❌ Maksymalna kwota: 5000 €",
        "invalid_number": "❌ Wprowadź poprawną liczbę!",
        "create_error": "❌ Błąd tworzenia faktury!",
        "invoice_created": "✅ Faktura utworzona!\n\n"
                           "💵 Kwota: {amount}\n"
                           "🔑 Kod: {code}\n"
                           "⏳ Faktura ważna 15 minut\n"
                           "💱 Prowizja: {commission}%\n\n"
                           "Wybierz metodę płatności:",
        "pay_invoice_text": "💳 Zapłać fakturę\n\nWprowadź kod faktury (8 znaków):",
        "invoice_not_found": "❌ Faktura nie znaleziona lub już opłacona!",
        "invoice_expired": "❌ Faktura wygasła (15 minut)!",
        "payment_methods": "💳 Wybierz metodę płatności\n\n"
                           "💵 Kwota: {amount}\n"
                           "🔑 Kod: {code}\n"
                           "⏳ Pozostały czas: {time_left}",
        "payment_confirmed_user": "✅ Płatność otrzymana!\n\n"
                                  "💵 Kwota: {amount}\n"
                                  "💸 Prowizja: {commission} ({percent}%)\n"
                                  "💳 Zaksięgowano: {earned}\n"
                                  "🔑 Kod: {code}",
        "payment_confirmed_buyer": "✅ Płatność potwierdzona!\n\n"
                                   "💵 Kwota: {amount}\n"
                                   "🔑 Kod: {code}\n\n"
                                   "Dziękujemy za skorzystanie! 🙌",
        "balance_text": "📊 Twoje saldo\n\n"
                        "💰 Saldo: {balance}\n\n"
                        "💸 Minimalna wypłata: {min_withdraw}\n"
                        "💱 Prowizja od płatności: {commission}%",
        "withdraw_text": "💸 Wypłać środki\n\n"
                         "Wprowadź kwotę do wypłaty:\n"
                         "Minimum: 10 €\n\n"
                         "Przykład: 50 lub 100.50",
        "withdraw_min_error": "❌ Minimalna wypłata: 10 €",
        "insufficient_balance": "❌ Niewystarczające środki!",
        "withdraw_create_error": "❌ Błąd tworzenia zgłoszenia!",
        "withdraw_success": "✅ Zgłoszenie #{id} utworzone!\nKwota: {amount}\nOczekuj na potwierdzenie.",
        "admin_withdraw_request": "💰 Zgłoszenie wypłaty!\n\n"
                                  "👤 Użytkownik: ID {user_id}\n"
                                  "💵 Kwota: {amount}\n"
                                  "🆔 Zgłoszenie #{id}\n\n"
                                  "Potwierdź wypłatę:\n/withdraw_admin {user_id} {amount}",
        "no_rights": "❌ Brak uprawnień!",
        "stats_text": "📈 Statystyki tygodniowe\n\n",
        "stats_day": "📅 {day}:\n"
                     "   Faktur: {total} | Opłaconych: {paid}\n"
                     "   Kwota: {amount} | Prowizja: {commission}\n\n",
        "stats_total": "📊 Razem:\n"
                       "👥 Użytkowników: {users}\n"
                       "💳 Płatności: {payments}\n"
                       "💰 Kwota: {amount}\n"
                       "💸 Prowizje: {commission}\n"
                       "⚙️ Prowizja: {percent}%",
        "users_list": "👥 Użytkownicy\n\n",
        "user_item": "• ID: {id} | Saldo: {balance}\n",
        "users_more": "\n... i {count} innych użytkowników",
        "admin_help": "👑 Polecenia admina\n\n"
                      "📊 Statystyki i użytkownicy:\n"
                      "/stats — ogólne statystyki\n"
                      "/users — lista wszystkich użytkowników\n"
                      "/userinfo <id> — pełne informacje o użytkowniku\n"
                      "/getid <username> — znajdź ID po nazwie użytkownika\n\n"
                      "💳 Zarządzanie płatnościami:\n"
                      "/view <kod_faktury> — utwórz jednorazowy kod podglądu\n"
                      "/check <kod> — sprawdź transakcję (dla wszystkich)\n"
                      "/withdraw_admin <id> <kwota> — potwierdź wypłatę\n\n"
                      "📋 Polecenia dla zwykłych użytkowników:\n"
                      "/start — menu główne\n"
                      "/language — zmień język\n"
                      "/help — pomoc\n"
                      "/create <kwota> — utwórz fakturę\n"
                      "/pay <kod> — zapłać fakturę\n"
                      "/balance — moje saldo\n"
                      "/withdraw <kwota> — wypłać środki\n"
                      "/check <kod> — sprawdź transakcję",
        "view_code_created": "✅ Kod podglądu utworzony!\n\n"
                             "🔑 Kod: {view_code}\n"
                             "📋 Faktura: {invoice_code}\n"
                             "⚠️ Jednorazowy, usuwany po wyświetleniu",
        "invoice_not_paid": "❌ Faktura jeszcze nie opłacona!",
        "check_invoice": "📋 Informacje o transakcji\n\n"
                         "🔑 Kod faktury: {code}\n"
                         "💵 Kwota: {amount}\n"
                         "📊 Status: {status}\n"
                         "📅 Utworzono: {created}\n"
                         "💳 Prowizja: {commission}\n"
                         "👤 Odbiorca: ID {creator}",
        "user_info": "👤 Informacje o użytkowniku\n\n"
                     "🆔 ID: {id}\n"
                     "👤 Nazwa użytkownika: @{username}\n"
                     "📅 Zarejestrowany: {registered}\n"
                     "💰 Saldo: {balance}\n\n"
                     "📊 Statystyki:\n"
                     "📤 Faktur utworzonych: {created}\n"
                     "📥 Zapłaconych (jako kupujący): {paid_count} za {paid_sum}\n"
                     "💵 Zarobionych (jako sprzedający): {earned}\n"
                     "💸 Prowizji zapłaconych: {commission_paid}\n\n"
                     "📋 Ostatnie faktury (utworzone):\n"
                     "  {invoices}\n\n"
                     "💳 Ostatnie płatności (jako kupujący):\n"
                     "  {payments}",
        "user_not_found": "❌ Użytkownik nie znaleziony!",
        "invalid_id": "❌ Wprowadź poprawny ID!",
        "user_not_in_db": "❌ Użytkownik @{username} nie znaleziony w bazie danych!\n\n"
                          "Poproś go, aby napisał /start do bota.",
        "invoice_status_paid": "✅ opłacona",
        "invoice_status_pending": "⏳ oczekująca",
        "status": "status",
        "expired": "Wygasła",
        "time_left": "{minutes} min {seconds} sek",
        "payment_method_paypal": "👤 PayPal\n\nZapłać przez PayPal:\nexample@paypal.com\n\n"
                                  "💵 Kwota: {amount}\n📝 Komentarz: {code}\n\n"
                                  "⚠️ Po płatności kliknij \"Zapłaciłem\"",
        "payment_method_usdt": "₿ USDT (TRC20)\n\nWyślij USDT na adres:\nTRC20_ADDRESS_HERE\n\n"
                               "🌐 Sieć: TRC20\n💵 Kwota: {amount} USDT\n\n"
                               "⚠️ Po wysłaniu kliknij \"Zapłaciłem\"",
        "payment_method_btc": "₿ Bitcoin\n\nWyślij BTC na adres:\nBTC_ADDRESS_HERE\n\n"
                              "💵 Kwota: {amount} BTC (według aktualnego kursu)\n\n"
                              "⚠️ Po wysłaniu kliknij \"Zapłaciłem\"",
        "payment_method_p2p": "🏦 P2P (Binance)\n\nSkontaktuj się ze sprzedawcą:\n👤 @P2P_Manager\n\n"
                              "💵 Kwota: {amount} EUR\n\n"
                              "⚠️ Po płatności kliknij \"Zapłaciłem\"",
        "payment_method_card": "💳 Karta bankowa\n\nZapłać przez link:\n🔗 https://payment.link/{code}\n\n"
                               "💵 Kwota: {amount}\n\n"
                               "⚠️ Po płatności kliknij \"Zapłaciłem\"",
        "i_paid": "✅ Zapłaciłem",
        "back_to_methods": "🔙 Wróć do metod",
        "main_menu_btn": "🏠 Menu główne",
        "use_buttons": "Użyj przycisków menu 👇",
        "language_command": "🌍 Zmień język\n\nWybierz język:",
        "language_changed": "✅ Język zmieniony na {language}",
        "paypal": "💳 PayPal",
        "usdt": "₿ USDT (TRC20)",
        "btc": "₿ Bitcoin (BTC)",
        "p2p": "🏦 P2P (Binance)",
        "card": "💳 Karta bankowa",
        "confirm_payment": "✅ Zapłaciłem",
        "min_withdraw_amount": "10",
    },
    "ro": {
        "name": "Română",
        "flag": "🇷🇴",
        "select_language": "🌍 Selectați limba:",
        "language_set": "✅ Limba setată: Română",
        "main_menu": "🏦 Meniu principal\n\nSelectați o acțiune:",
        "create_invoice": "💰 Creează factură",
        "pay_invoice": "💳 Plătește factura",
        "my_balance": "📊 Soldul meu",
        "withdraw": "💸 Retrage fonduri",
        "help": "ℹ️ Ajutor",
        "admin_stats": "📈 Statistici",
        "admin_users": "👥 Utilizatori",
        "help_admin": "👑 Comenzi admin",
        "back": "🔙 Înapoi",
        "help_text": "ℹ️ Ajutor\n\n"
                     "💰 Creează factură — creați o factură de plată\n"
                     "💳 Plătește factura — plătiți o factură existentă\n"
                     "📊 Sold — verificați soldul\n"
                     "💸 Retrage — retrageți fonduri\n\n"
                     "⏳ Facturi valabile 15 minute\n"
                     "💱 Comision: {commission}% (0.01 € pentru fiecare €)\n"
                     "🔒 Toate plățile sunt anonime\n"
                     "💰 Suma minimă: 1 €",
        "create_invoice_text": "💰 Creare factură\n\n"
                               "Introduceți suma în euro:\n"
                               "Minim: 1 €\n"
                               "Maxim: 5000 €\n\n"
                               "Exemplu: 50 sau 100.50",
        "min_amount_error": "❌ Suma minimă: 1 €",
        "max_amount_error": "❌ Suma maximă: 5000 €",
        "invalid_number": "❌ Introduceți un număr valid!",
        "create_error": "❌ Eroare la crearea facturii!",
        "invoice_created": "✅ Factură creată!\n\n"
                           "💵 Suma: {amount}\n"
                           "🔑 Cod: {code}\n"
                           "⏳ Factură valabilă 15 minute\n"
                           "💱 Comision: {commission}%\n\n"
                           "Selectați metoda de plată:",
        "pay_invoice_text": "💳 Plătește factura\n\nIntroduceți codul facturii (8 caractere):",
        "invoice_not_found": "❌ Factură negăsită sau deja plătită!",
        "invoice_expired": "❌ Factură expirată (15 minute)!",
        "payment_methods": "💳 Selectați metoda de plată\n\n"
                           "💵 Suma: {amount}\n"
                           "🔑 Cod: {code}\n"
                           "⏳ Timp rămas: {time_left}",
        "payment_confirmed_user": "✅ Plată primită!\n\n"
                                  "💵 Suma: {amount}\n"
                                  "💸 Comision: {commission} ({percent}%)\n"
                                  "💳 Creditat: {earned}\n"
                                  "🔑 Cod: {code}",
        "payment_confirmed_buyer": "✅ Plată confirmată!\n\n"
                                   "💵 Suma: {amount}\n"
                                   "🔑 Cod: {code}\n\n"
                                   "Vă mulțumim pentru utilizare! 🙌",
        "balance_text": "📊 Soldul dvs.\n\n"
                        "💰 Sold: {balance}\n\n"
                        "💸 Retragere minimă: {min_withdraw}\n"
                        "💱 Comision de plată: {commission}%",
        "withdraw_text": "💸 Retrage fonduri\n\n"
                         "Introduceți suma de retras:\n"
                         "Minim: 10 €\n\n"
                         "Exemplu: 50 sau 100.50",
        "withdraw_min_error": "❌ Retragere minimă: 10 €",
        "insufficient_balance": "❌ Sold insuficient!",
        "withdraw_create_error": "❌ Eroare la crearea cererii!",
        "withdraw_success": "✅ Cerere #{id} creată!\nSuma: {amount}\nAșteptați confirmarea.",
        "admin_withdraw_request": "💰 Cerere de retragere!\n\n"
                                  "👤 Utilizator: ID {user_id}\n"
                                  "💵 Suma: {amount}\n"
                                  "🆔 Cerere #{id}\n\n"
                                  "Confirmați retragerea:\n/withdraw_admin {user_id} {amount}",
        "no_rights": "❌ Fără drepturi!",
        "stats_text": "📈 Statistici săptămânale\n\n",
        "stats_day": "📅 {day}:\n"
                     "   Facturi: {total} | Plătite: {paid}\n"
                     "   Suma: {amount} | Comision: {commission}\n\n",
        "stats_total": "📊 Total:\n"
                       "👥 Utilizatori: {users}\n"
                       "💳 Plăți: {payments}\n"
                       "💰 Suma: {amount}\n"
                       "💸 Comisioane: {commission}\n"
                       "⚙️ Comision: {percent}%",
        "users_list": "👥 Utilizatori\n\n",
        "user_item": "• ID: {id} | Sold: {balance}\n",
        "users_more": "\n... și încă {count} utilizatori",
        "admin_help": "👑 Comenzi admin\n\n"
                      "📊 Statistici și utilizatori:\n"
                      "/stats — statistici generale\n"
                      "/users — lista tuturor utilizatorilor\n"
                      "/userinfo <id> — informații complete despre utilizator\n"
                      "/getid <username> — găsiți ID după numele de utilizator\n\n"
                      "💳 Gestionarea plăților:\n"
                      "/view <cod_factură> — creați cod de vizualizare unic\n"
                      "/check <cod> — verificați tranzacția (pentru toți)\n"
                      "/withdraw_admin <id> <suma> — confirmați retragerea\n\n"
                      "📋 Comenzi pentru utilizatorii obișnuiți:\n"
                      "/start — meniu principal\n"
                      "/language — schimbă limba\n"
                      "/help — ajutor\n"
                      "/create <suma> — creează factură\n"
                      "/pay <cod> — plătește factura\n"
                      "/balance — soldul meu\n"
                      "/withdraw <suma> — retrage fonduri\n"
                      "/check <cod> — verifică tranzacția",
        "view_code_created": "✅ Cod de vizualizare creat!\n\n"
                             "🔑 Cod: {view_code}\n"
                             "📋 Factură: {invoice_code}\n"
                             "⚠️ Unic, șters după vizualizare",
        "invoice_not_paid": "❌ Factura nu a fost încă plătită!",
        "check_invoice": "📋 Informații despre tranzacție\n\n"
                         "🔑 Cod factură: {code}\n"
                         "💵 Suma: {amount}\n"
                         "📊 Status: {status}\n"
                         "📅 Creată: {created}\n"
                         "💳 Comision: {commission}\n"
                         "👤 Destinatar: ID {creator}",
        "user_info": "👤 Informații utilizator\n\n"
                     "🆔 ID: {id}\n"
                     "👤 Nume utilizator: @{username}\n"
                     "📅 Înregistrat: {registered}\n"
                     "💰 Sold: {balance}\n\n"
                     "📊 Statistici:\n"
                     "📤 Facturi create: {created}\n"
                     "📥 Plătit (ca cumpărător): {paid_count} pentru {paid_sum}\n"
                     "💵 Câștigat (ca vânzător): {earned}\n"
                     "💸 Comisioane plătite: {commission_paid}\n\n"
                     "📋 Ultimele facturi (create):\n"
                     "  {invoices}\n\n"
                     "💳 Ultimele plăți (ca cumpărător):\n"
                     "  {payments}",
        "user_not_found": "❌ Utilizator negăsit!",
        "invalid_id": "❌ Introduceți un ID valid!",
        "user_not_in_db": "❌ Utilizatorul @{username} nu a fost găsit în baza de date!\n\n"
                          "Cereți-i să scrie /start botului.",
        "invoice_status_paid": "✅ plătită",
        "invoice_status_pending": "⏳ în așteptare",
        "status": "status",
        "expired": "Expirată",
        "time_left": "{minutes} min {seconds} sec",
        "payment_method_paypal": "👤 PayPal\n\nPlătiți prin PayPal:\nexample@paypal.com\n\n"
                                  "💵 Suma: {amount}\n📝 Comentariu: {code}\n\n"
                                  "⚠️ După plată, faceți clic pe \"Am plătit\"",
        "payment_method_usdt": "₿ USDT (TRC20)\n\nTrimiteți USDT la adresa:\nTRC20_ADDRESS_HERE\n\n"
                               "🌐 Rețea: TRC20\n💵 Suma: {amount} USDT\n\n"
                               "⚠️ După trimitere, faceți clic pe \"Am plătit\"",
        "payment_method_btc": "₿ Bitcoin\n\nTrimiteți BTC la adresa:\nBTC_ADDRESS_HERE\n\n"
                              "💵 Suma: {amount} BTC (la cursul actual)\n\n"
                              "⚠️ După trimitere, faceți clic pe \"Am plătit\"",
        "payment_method_p2p": "🏦 P2P (Binance)\n\nContactați vânzătorul:\n👤 @P2P_Manager\n\n"
                              "💵 Suma: {amount} EUR\n\n"
                              "⚠️ După plată, faceți clic pe \"Am plătit\"",
        "payment_method_card": "💳 Card bancar\n\nPlătiți prin link:\n🔗 https://payment.link/{code}\n\n"
                               "💵 Suma: {amount}\n\n"
                               "⚠️ După plată, faceți clic pe \"Am plătit\"",
        "i_paid": "✅ Am plătit",
        "back_to_methods": "🔙 Înapoi la metode",
        "main_menu_btn": "🏠 Meniu principal",
        "use_buttons": "Folosiți butoanele din meniu 👇",
        "language_command": "🌍 Schimbă limba\n\nSelectați limba:",
        "language_changed": "✅ Limba schimbată în {language}",
        "paypal": "💳 PayPal",
        "usdt": "₿ USDT (TRC20)",
        "btc": "₿ Bitcoin (BTC)",
        "p2p": "🏦 P2P (Binance)",
        "card": "💳 Card bancar",
        "confirm_payment": "✅ Am plătit",
        "min_withdraw_amount": "10",
    },
    "zh": {
        "name": "中文",
        "flag": "🇨🇳",
        "select_language": "🌍 选择语言：",
        "language_set": "✅ 语言已设置：中文",
        "main_menu": "🏦 主菜单\n\n选择操作：",
        "create_invoice": "💰 创建账单",
        "pay_invoice": "💳 支付账单",
        "my_balance": "📊 我的余额",
        "withdraw": "💸 提现",
        "help": "ℹ️ 帮助",
        "admin_stats": "📈 统计",
        "admin_users": "👥 用户",
        "help_admin": "👑 管理员命令",
        "back": "🔙 返回",
        "help_text": "ℹ️ 帮助\n\n"
                     "💰 创建账单 — 创建支付账单\n"
                     "💳 支付账单 — 支付已有账单\n"
                     "📊 余额 — 查看您的余额\n"
                     "💸 提现 — 提现资金\n\n"
                     "⏳ 账单有效期为15分钟\n"
                     "💱 佣金：{commission}%（每€收取0.01€）\n"
                     "🔒 所有支付都是匿名的\n"
                     "💰 最低金额：1 €",
        "create_invoice_text": "💰 创建账单\n\n"
                               "输入欧元金额：\n"
                               "最低：1 €\n"
                               "最高：5000 €\n\n"
                               "示例：50 或 100.50",
        "min_amount_error": "❌ 最低金额：1 €",
        "max_amount_error": "❌ 最高金额：5000 €",
        "invalid_number": "❌ 请输入有效数字！",
        "create_error": "❌ 创建账单失败！",
        "invoice_created": "✅ 账单已创建！\n\n"
                           "💵 金额：{amount}\n"
                           "🔑 代码：{code}\n"
                           "⏳ 账单有效期15分钟\n"
                           "💱 佣金：{commission}%\n\n"
                           "选择支付方式：",
        "pay_invoice_text": "💳 支付账单\n\n输入账单代码（8位）：",
        "invoice_not_found": "❌ 账单未找到或已支付！",
        "invoice_expired": "❌ 账单已过期（15分钟）！",
        "payment_methods": "💳 选择支付方式\n\n"
                           "💵 金额：{amount}\n"
                           "🔑 代码：{code}\n"
                           "⏳ 剩余时间：{time_left}",
        "payment_confirmed_user": "✅ 已收到付款！\n\n"
                                  "💵 金额：{amount}\n"
                                  "💸 佣金：{commission}（{percent}%）\n"
                                  "💳 入账：{earned}\n"
                                  "🔑 代码：{code}",
        "payment_confirmed_buyer": "✅ 支付已确认！\n\n"
                                   "💵 金额：{amount}\n"
                                   "🔑 代码：{code}\n\n"
                                   "感谢使用！🙌",
        "balance_text": "📊 您的余额\n\n"
                        "💰 余额：{balance}\n\n"
                        "💸 最低提现金额：{min_withdraw}\n"
                        "💱 支付佣金：{commission}%",
        "withdraw_text": "💸 提现\n\n"
                         "输入提现金额：\n"
                         "最低：10 €\n\n"
                         "示例：50 或 100.50",
        "withdraw_min_error": "❌ 最低提现金额：10 €",
        "insufficient_balance": "❌ 余额不足！",
        "withdraw_create_error": "❌ 创建提现申请失败！",
        "withdraw_success": "✅ 申请 #{id} 已创建！\n金额：{amount}\n请等待确认。",
        "admin_withdraw_request": "💰 提现申请！\n\n"
                                  "👤 用户：ID {user_id}\n"
                                  "💵 金额：{amount}\n"
                                  "🆔 申请 #{id}\n\n"
                                  "确认提现：\n/withdraw_admin {user_id} {amount}",
        "no_rights": "❌ 无权限！",
        "stats_text": "📈 周统计\n\n",
        "stats_day": "📅 {day}：\n"
                     "   账单：{total} | 已付：{paid}\n"
                     "   金额：{amount} | 佣金：{commission}\n\n",
        "stats_total": "📊 总计：\n"
                       "👥 用户：{users}\n"
                       "💳 支付：{payments}\n"
                       "💰 金额：{amount}\n"
                       "💸 佣金：{commission}\n"
                       "⚙️ 佣金率：{percent}%",
        "users_list": "👥 用户列表\n\n",
        "user_item": "• ID：{id} | 余额：{balance}\n",
        "users_more": "\n...还有 {count} 个用户",
        "admin_help": "👑 管理员命令\n\n"
                      "📊 统计和用户：\n"
                      "/stats — 总体统计\n"
                      "/users — 所有用户列表\n"
                      "/userinfo <id> — 完整用户信息\n"
                      "/getid <用户名> — 通过用户名查找ID\n\n"
                      "💳 支付管理：\n"
                      "/view <账单代码> — 创建一次性查看代码\n"
                      "/check <代码> — 查看交易（所有人可用）\n"
                      "/withdraw_admin <id> <金额> — 确认提现\n\n"
                      "📋 普通用户命令：\n"
                      "/start — 主菜单\n"
                      "/language — 切换语言\n"
                      "/help — 帮助\n"
                      "/create <金额> — 创建账单\n"
                      "/pay <代码> — 支付账单\n"
                      "/balance — 我的余额\n"
                      "/withdraw <金额> — 提现\n"
                      "/check <代码> — 查看交易",
        "view_code_created": "✅ 查看代码已创建！\n\n"
                             "🔑 代码：{view_code}\n"
                             "📋 账单：{invoice_code}\n"
                             "⚠️ 一次性，查看后删除",
        "invoice_not_paid": "❌ 账单尚未支付！",
        "check_invoice": "📋 交易信息\n\n"
                         "🔑 账单代码：{code}\n"
                         "💵 金额：{amount}\n"
                         "📊 状态：{status}\n"
                         "📅 创建时间：{created}\n"
                         "💳 佣金：{commission}\n"
                         "👤 收款人：ID {creator}",
        "user_info": "👤 用户信息\n\n"
                     "🆔 ID：{id}\n"
                     "👤 用户名：@{username}\n"
                     "📅 注册时间：{registered}\n"
                     "💰 余额：{balance}\n\n"
                     "📊 统计：\n"
                     "📤 创建的账单：{created}\n"
                     "📥 支付的（作为买家）：{paid_count} 共 {paid_sum}\n"
                     "💵 赚取的（作为卖家）：{earned}\n"
                     "💸 支付的佣金：{commission_paid}\n\n"
                     "📋 最近的账单（创建的）：\n"
                     "  {invoices}\n\n"
                     "💳 最近的付款（作为买家）：\n"
                     "  {payments}",
        "user_not_found": "❌ 用户未找到！",
        "invalid_id": "❌ 请输入有效ID！",
        "user_not_in_db": "❌ 在数据库中未找到用户 @{username}！\n\n"
                          "请让他向机器人发送 /start。",
        "invoice_status_paid": "✅ 已支付",
        "invoice_status_pending": "⏳ 待支付",
        "status": "状态",
        "expired": "已过期",
        "time_left": "{minutes}分{seconds}秒",
        "payment_method_paypal": "👤 PayPal\n\n通过PayPal支付：\nexample@paypal.com\n\n"
                                  "💵 金额：{amount}\n📝 备注：{code}\n\n"
                                  "⚠️ 支付后点击\"我已支付\"",
        "payment_method_usdt": "₿ USDT（TRC20）\n\n将USDT发送到地址：\nTRC20_ADDRESS_HERE\n\n"
                               "🌐 网络：TRC20\n💵 金额：{amount} USDT\n\n"
                               "⚠️ 发送后点击\"我已支付\"",
        "payment_method_btc": "₿ Bitcoin\n\n将BTC发送到地址：\nBTC_ADDRESS_HERE\n\n"
                              "💵 金额：{amount} BTC（按当前汇率）\n\n"
                              "⚠️ 发送后点击\"我已支付\"",
        "payment_method_p2p": "🏦 P2P（Binance）\n\n联系卖家：\n👤 @P2P_Manager\n\n"
                              "💵 金额：{amount} EUR\n\n"
                              "⚠️ 支付后点击\"我已支付\"",
        "payment_method_card": "💳 银行卡\n\n通过链接支付：\n🔗 https://payment.link/{code}\n\n"
                               "💵 金额：{amount}\n\n"
                               "⚠️ 支付后点击\"我已支付\"",
        "i_paid": "✅ 我已支付",
        "back_to_methods": "🔙 返回支付方式",
        "main_menu_btn": "🏠 主菜单",
        "use_buttons": "使用菜单按钮 👇",
        "language_command": "🌍 切换语言\n\n选择语言：",
        "language_changed": "✅ 已切换至 {language}",
        "paypal": "💳 PayPal",
        "usdt": "₿ USDT（TRC20）",
        "btc": "₿ Bitcoin（BTC）",
        "p2p": "🏦 P2P（Binance）",
        "card": "💳 银行卡",
        "confirm_payment": "✅ 我已支付",
        "min_withdraw_amount": "10",
    }
}

# Список доступных языков для клавиатуры
LANGUAGE_LIST = [
    ("ru", "Русский", "🇷🇺"),
    ("en", "English", "🇬🇧"),
    ("fr", "Français", "🇫🇷"),
    ("es", "Español", "🇪🇸"),
    ("pt", "Português", "🇵🇹"),
    ("it", "Italiano", "🇮🇹"),
    ("de", "Deutsch", "🇩🇪"),
    ("pl", "Polski", "🇵🇱"),
    ("ro", "Română", "🇷🇴"),
    ("zh", "中文", "🇨🇳"),
]

def get_text(user_id, key, lang_code=None, **kwargs):
    """Получить текст на языке пользователя"""
    from database import Database
    db = Database()
    
    if lang_code is None:
        user = db.get_user(user_id)
        lang_code = user.get('language', 'ru') if user else 'ru'
    
    # Если языка нет в словаре - используем русский
    if lang_code not in LANGUAGES:
        lang_code = 'ru'
    
    text = LANGUAGES[lang_code].get(key, LANGUAGES['ru'].get(key, key))
    
    # Подставляем параметры
    if kwargs:
        try:
            text = text.format(**kwargs)
        except KeyError:
            # Если какой-то параметр не подставился - возвращаем как есть
            pass
    
    return text

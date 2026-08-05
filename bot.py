import logging
import random
import string
import time
from datetime import datetime, timedelta
from threading import Timer

from telegram.ext import Update
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    filters,
    ContextTypes,
)
from telegram.constants import ParseMode

from config import Config
from database import Database
from locales import get_text, LANGUAGE_LIST

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

db = Database()
active_invoices = {}

# ========== НАСТРОЙКИ ==========
ADMINS = [Config.ADMIN_ID, 6115925216]

# ========== ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ ==========
def generate_invoice_code() -> str:
    return "".join(random.choices(string.digits + string.ascii_uppercase, k=8))

def generate_view_code() -> str:
    return "".join(random.choices(string.digits + string.ascii_uppercase, k=6))

def format_eur(amount: float) -> str:
    return f"{amount:.2f} €"

def is_admin(user_id: int) -> bool:
    return user_id in ADMINS

def calculate_time_left(code: str) -> str:
    if code not in active_invoices:
        return "Истек"
    expiry = active_invoices[code]["expiry"]
    diff = expiry - datetime.now()
    if diff.total_seconds() <= 0:
        return "Истек"
    minutes = int(diff.total_seconds() // 60)
    seconds = int(diff.total_seconds() % 60)
    return f"{minutes} мин {seconds} сек"

def expire_invoice(code: str):
    if code in active_invoices:
        del active_invoices[code]
        db.update_payment_status(code, "expired")
        logger.info(f"Счет {code} истек")

# ========== ГЛАВНОЕ МЕНЮ ==========
async def main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE, message_text: str = None):
    user_id = update.effective_user.id
    lang = db.get_user_language(user_id)
    
    keyboard = [
        [InlineKeyboardButton(get_text(user_id, "create_invoice", lang), callback_data="create_invoice")],
        [InlineKeyboardButton(get_text(user_id, "pay_invoice", lang), callback_data="pay_invoice")],
        [InlineKeyboardButton(get_text(user_id, "my_balance", lang), callback_data="my_balance")],
        [InlineKeyboardButton(get_text(user_id, "withdraw", lang), callback_data="withdraw")],
        [InlineKeyboardButton(get_text(user_id, "help", lang), callback_data="help")],
        [InlineKeyboardButton("🌍 Language", callback_data="change_language")],
    ]
    if is_admin(user_id):
        keyboard.append([InlineKeyboardButton(get_text(user_id, "admin_stats", lang), callback_data="admin_stats")])
        keyboard.append([InlineKeyboardButton(get_text(user_id, "admin_users", lang), callback_data="admin_users")])
        keyboard.append([InlineKeyboardButton(get_text(user_id, "help_admin", lang), callback_data="help_admin")])
    reply_markup = InlineKeyboardMarkup(keyboard)
    text = message_text or get_text(user_id, "main_menu", lang)
    if update.callback_query:
        await update.callback_query.edit_message_text(text, reply_markup=reply_markup)
    else:
        await update.message.reply_text(text, reply_markup=reply_markup)

# ========== СМЕНА ЯЗЫКА ==========
async def change_language(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    lang = db.get_user_language(user_id)
    
    keyboard = []
    row = []
    for i, (code, name, flag) in enumerate(LANGUAGE_LIST):
        row.append(InlineKeyboardButton(f"{flag} {name}", callback_data=f"set_lang_{code}"))
        if len(row) == 2:
            keyboard.append(row)
            row = []
    if row:
        keyboard.append(row)
    
    keyboard.append([InlineKeyboardButton(get_text(user_id, "back", lang), callback_data="main_menu")])
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(
        get_text(user_id, "language_command", lang),
        reply_markup=reply_markup
    )

async def set_language(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    lang_code = query.data.replace("set_lang_", "")
    
    db.set_user_language(user_id, lang_code)
    
    # Получаем название языка на выбранном языке
    lang_name = None
    for code, name, flag in LANGUAGE_LIST:
        if code == lang_code:
            lang_name = f"{flag} {name}"
            break
    
    await query.edit_message_text(
        get_text(user_id, "language_changed", lang_code, language=lang_name or lang_code)
    )
    
    # Показываем главное меню на новом языке
    await main_menu(update, context)

# ========== ПОМОЩЬ ==========
async def help_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    lang = db.get_user_language(user_id)
    commission = db.get_commission_percent()
    
    keyboard = [[InlineKeyboardButton(get_text(user_id, "back", lang), callback_data="main_menu")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(
        get_text(user_id, "help_text", lang, commission=commission),
        reply_markup=reply_markup,
    )

# ========== HELP_ADMIN (только для админов) ==========
async def help_admin_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    lang = db.get_user_language(user_id)
    
    if not is_admin(user_id):
        await query.edit_message_text(get_text(user_id, "no_rights", lang))
        return
    
    keyboard = [[InlineKeyboardButton(get_text(user_id, "back", lang), callback_data="main_menu")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        get_text(user_id, "admin_help", lang),
        reply_markup=reply_markup,
    )

async def help_admin_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    lang = db.get_user_language(user_id)
    
    if not is_admin(user_id):
        await update.message.reply_text(get_text(user_id, "no_rights", lang))
        return
    
    await update.message.reply_text(get_text(user_id, "admin_help", lang))

# ========== СОЗДАНИЕ СЧЕТА ==========
async def create_invoice_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    lang = db.get_user_language(user_id)
    
    keyboard = [[InlineKeyboardButton(get_text(user_id, "back", lang), callback_data="main_menu")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        get_text(user_id, "create_invoice_text", lang),
        reply_markup=reply_markup,
    )
    context.user_data["state"] = "waiting_amount"

async def create_invoice_amount(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    lang = db.get_user_language(user_id)
    
    try:
        amount = float(update.message.text.replace(",", "."))
        if amount < 1:
            await update.message.reply_text(get_text(user_id, "min_amount_error", lang))
            return
        if amount > 5000:
            await update.message.reply_text(get_text(user_id, "max_amount_error", lang))
            return
    except ValueError:
        await update.message.reply_text(get_text(user_id, "invalid_number", lang))
        return
    
    code = generate_invoice_code()
    invoice_id = db.create_payment(user_id, amount, code)
    if not invoice_id:
        await update.message.reply_text(get_text(user_id, "create_error", lang))
        return
    
    expiry_time = datetime.now() + timedelta(minutes=15)
    timer = Timer(900, lambda: expire_invoice(code))
    timer.start()
    active_invoices[code] = {
        "timer": timer,
        "expiry": expiry_time,
        "amount": amount,
        "creator": user_id,
    }
    
    commission = db.get_commission_percent()
    keyboard = [
        [InlineKeyboardButton(get_text(user_id, "paypal", lang), callback_data=f"pay_method_paypal_{code}")],
        [InlineKeyboardButton(get_text(user_id, "usdt", lang), callback_data=f"pay_method_usdt_{code}")],
        [InlineKeyboardButton(get_text(user_id, "btc", lang), callback_data=f"pay_method_btc_{code}")],
        [InlineKeyboardButton(get_text(user_id, "p2p", lang), callback_data=f"pay_method_p2p_{code}")],
        [InlineKeyboardButton(get_text(user_id, "card", lang), callback_data=f"pay_method_card_{code}")],
        [InlineKeyboardButton(get_text(user_id, "back", lang), callback_data="main_menu")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        get_text(user_id, "invoice_created", lang, amount=format_eur(amount), code=code, commission=commission),
        reply_markup=reply_markup,
    )

# ========== ОПЛАТА СЧЕТА ==========
async def pay_invoice_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    lang = db.get_user_language(user_id)
    
    keyboard = [[InlineKeyboardButton(get_text(user_id, "back", lang), callback_data="main_menu")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        get_text(user_id, "pay_invoice_text", lang),
        reply_markup=reply_markup,
    )
    context.user_data["state"] = "waiting_pay_code"

async def pay_invoice_code(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    lang = db.get_user_language(user_id)
    code = update.message.text.strip().upper()
    
    payment = db.get_payment_by_code(code)
    if not payment or payment["status"] != "pending":
        await update.message.reply_text(get_text(user_id, "invoice_not_found", lang))
        return
    if code not in active_invoices:
        await update.message.reply_text(get_text(user_id, "invoice_expired", lang))
        return
    
    keyboard = [
        [InlineKeyboardButton(get_text(user_id, "paypal", lang), callback_data=f"pay_method_paypal_{code}")],
        [InlineKeyboardButton(get_text(user_id, "usdt", lang), callback_data=f"pay_method_usdt_{code}")],
        [InlineKeyboardButton(get_text(user_id, "btc", lang), callback_data=f"pay_method_btc_{code}")],
        [InlineKeyboardButton(get_text(user_id, "p2p", lang), callback_data=f"pay_method_p2p_{code}")],
        [InlineKeyboardButton(get_text(user_id, "card", lang), callback_data=f"pay_method_card_{code}")],
        [InlineKeyboardButton(get_text(user_id, "back", lang), callback_data="main_menu")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        get_text(user_id, "payment_methods", lang, 
                amount=format_eur(payment['amount']), 
                code=code, 
                time_left=calculate_time_left(code)),
        reply_markup=reply_markup,
    )

# ========== СПОСОБЫ ОПЛАТЫ ==========
async def payment_method_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    lang = db.get_user_language(user_id)
    data = query.data.split("_")
    method = data[2]
    code = data[3]
    
    payment = db.get_payment_by_code(code)
    if not payment or payment["status"] != "pending":
        await query.edit_message_text(get_text(user_id, "invoice_not_found", lang))
        return
    
    method_key = f"payment_method_{method}"
    text = get_text(user_id, method_key, lang, amount=format_eur(payment['amount']), code=code)
    
    keyboard = [
        [InlineKeyboardButton(get_text(user_id, "i_paid", lang), callback_data=f"confirm_payment_{code}")],
        [InlineKeyboardButton(get_text(user_id, "back_to_methods", lang), callback_data=f"back_to_payment_{code}")],
        [InlineKeyboardButton(get_text(user_id, "main_menu_btn", lang), callback_data="main_menu")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text, reply_markup=reply_markup)

async def back_to_payment_methods(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    lang = db.get_user_language(user_id)
    code = query.data.replace("back_to_payment_", "")
    
    payment = db.get_payment_by_code(code)
    if not payment or payment["status"] != "pending":
        await query.edit_message_text(get_text(user_id, "invoice_not_found", lang))
        return
    
    keyboard = [
        [InlineKeyboardButton(get_text(user_id, "paypal", lang), callback_data=f"pay_method_paypal_{code}")],
        [InlineKeyboardButton(get_text(user_id, "usdt", lang), callback_data=f"pay_method_usdt_{code}")],
        [InlineKeyboardButton(get_text(user_id, "btc", lang), callback_data=f"pay_method_btc_{code}")],
        [InlineKeyboardButton(get_text(user_id, "p2p", lang), callback_data=f"pay_method_p2p_{code}")],
        [InlineKeyboardButton(get_text(user_id, "card", lang), callback_data=f"pay_method_card_{code}")],
        [InlineKeyboardButton(get_text(user_id, "back", lang), callback_data="main_menu")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        get_text(user_id, "payment_methods", lang,
                amount=format_eur(payment['amount']),
                code=code,
                time_left=calculate_time_left(code)),
        reply_markup=reply_markup,
    )

# ========== ПОДТВЕРЖДЕНИЕ ОПЛАТЫ ==========
async def confirm_payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    lang = db.get_user_language(user_id)
    code = query.data.replace("confirm_payment_", "")
    
    payment = db.get_payment_by_code(code)
    if not payment or payment["status"] != "pending":
        await query.edit_message_text(get_text(user_id, "invoice_not_found", lang))
        return
    if code not in active_invoices:
        await query.edit_message_text(get_text(user_id, "invoice_expired", lang))
        return
    
    commission_percent = db.get_commission_percent()
    success = db.confirm_payment(code, user_id, commission_percent)
    if not success:
        await query.edit_message_text(get_text(user_id, "create_error", lang))
        return
    
    if code in active_invoices:
        del active_invoices[code]
    
    payment = db.get_payment_by_code(code)
    
    # Уведомление создателю счета
    try:
        creator_lang = db.get_user_language(payment["creator_id"])
        await context.bot.send_message(
            chat_id=payment["creator_id"],
            text=get_text(payment["creator_id"], "payment_confirmed_user", creator_lang,
                         amount=format_eur(payment['amount']),
                         commission=format_eur(payment['commission']),
                         percent=commission_percent,
                         earned=format_eur(payment['creator_earned']),
                         code=code),
        )
    except Exception:
        pass
    
    keyboard = [[InlineKeyboardButton(get_text(user_id, "main_menu_btn", lang), callback_data="main_menu")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        get_text(user_id, "payment_confirmed_buyer", lang, amount=format_eur(payment['amount']), code=code),
        reply_markup=reply_markup,
    )

# ========== БАЛАНС И ВЫВОД ==========
async def my_balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    lang = db.get_user_language(user_id)
    
    user = db.get_user(user_id)
    if not user:
        keyboard = [[InlineKeyboardButton(get_text(user_id, "back", lang), callback_data="main_menu")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(get_text(user_id, "user_not_found", lang), reply_markup=reply_markup)
        return
    
    commission = db.get_commission_percent()
    min_withdraw = get_text(user_id, "min_withdraw_amount", lang)
    
    keyboard = [
        [InlineKeyboardButton(get_text(user_id, "withdraw", lang), callback_data="withdraw")],
        [InlineKeyboardButton(get_text(user_id, "back", lang), callback_data="main_menu")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        get_text(user_id, "balance_text", lang,
                balance=format_eur(user['balance']),
                min_withdraw=min_withdraw,
                commission=commission),
        reply_markup=reply_markup,
    )

async def withdraw_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    lang = db.get_user_language(user_id)
    
    keyboard = [[InlineKeyboardButton(get_text(user_id, "back", lang), callback_data="main_menu")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        get_text(user_id, "withdraw_text", lang),
        reply_markup=reply_markup,
    )
    context.user_data["state"] = "waiting_withdraw_amount"

async def withdraw_amount(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    lang = db.get_user_language(user_id)
    
    try:
        amount = float(update.message.text.replace(",", "."))
        if amount < 10:
            await update.message.reply_text(get_text(user_id, "withdraw_min_error", lang))
            return
    except ValueError:
        await update.message.reply_text(get_text(user_id, "invalid_number", lang))
        return
    
    user = db.get_user(user_id)
    if not user or user["balance"] < amount:
        await update.message.reply_text(get_text(user_id, "insufficient_balance", lang))
        return
    
    withdraw_id = db.create_withdraw_request(user_id, amount)
    if not withdraw_id:
        await update.message.reply_text(get_text(user_id, "withdraw_create_error", lang))
        return
    
    # Уведомление админам
    for admin_id in ADMINS:
        try:
            admin_lang = db.get_user_language(admin_id)
            await context.bot.send_message(
                chat_id=admin_id,
                text=get_text(admin_id, "admin_withdraw_request", admin_lang,
                             user_id=user_id,
                             amount=format_eur(amount),
                             id=withdraw_id),
            )
        except Exception:
            pass
    
    keyboard = [[InlineKeyboardButton(get_text(user_id, "main_menu_btn", lang), callback_data="main_menu")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        get_text(user_id, "withdraw_success", lang, id=withdraw_id, amount=format_eur(amount)),
        reply_markup=reply_markup,
    )

# ========== АДМИНСКИЕ ФУНКЦИИ ==========
async def admin_stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    lang = db.get_user_language(user_id)
    
    if not is_admin(user_id):
        if update.callback_query:
            await update.callback_query.answer()
            await update.callback_query.edit_message_text(get_text(user_id, "no_rights", lang))
        else:
            await update.message.reply_text(get_text(user_id, "no_rights", lang))
        return
    
    if update.callback_query:
        query = update.callback_query
        await query.answer()
        message = query.message
    else:
        message = update.message
    
    stats = db.get_weekly_stats()
    total_stats = db.get_payment_stats()
    users = db.get_all_users()
    
    text = get_text(user_id, "stats_text", lang)
    for day, data in stats.items():
        text += get_text(user_id, "stats_day", lang,
                        day=day,
                        total=data['total'],
                        paid=data['paid'],
                        amount=format_eur(data['amount']),
                        commission=format_eur(data['commission']))
    
    text += get_text(user_id, "stats_total", lang,
                    users=len(users),
                    payments=total_stats['total_payments'],
                    amount=format_eur(total_stats['total_amount']),
                    commission=format_eur(total_stats['total_commission']),
                    percent=db.get_commission_percent())
    
    keyboard = [[InlineKeyboardButton(get_text(user_id, "back", lang), callback_data="main_menu")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    if update.callback_query:
        await query.edit_message_text(text, reply_markup=reply_markup)
    else:
        await message.reply_text(text, reply_markup=reply_markup)

async def admin_users(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    lang = db.get_user_language(user_id)
    
    if not is_admin(user_id):
        if update.callback_query:
            await update.callback_query.answer()
            await update.callback_query.edit_message_text(get_text(user_id, "no_rights", lang))
        else:
            await update.message.reply_text(get_text(user_id, "no_rights", lang))
        return
    
    if update.callback_query:
        query = update.callback_query
        await query.answer()
        message = query.message
    else:
        message = update.message
    
    users = db.get_all_users()
    text = get_text(user_id, "users_list", lang)
    for u in users[:20]:
        text += get_text(user_id, "user_item", lang, id=u['user_id'], balance=format_eur(u['balance']))
    if len(users) > 20:
        text += get_text(user_id, "users_more", lang, count=len(users) - 20)
    
    keyboard = [[InlineKeyboardButton(get_text(user_id, "back", lang), callback_data="main_menu")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    if update.callback_query:
        await query.edit_message_text(text, reply_markup=reply_markup)
    else:
        await message.reply_text(text, reply_markup=reply_markup)

# ========== ВЫВОД ДЛЯ АДМИНА (команда) ==========
async def withdraw_admin_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    lang = db.get_user_language(user_id)
    
    if not is_admin(user_id):
        await update.message.reply_text(get_text(user_id, "no_rights", lang))
        return
    
    args = context.args
    if len(args) != 2:
        await update.message.reply_text("❌ /withdraw_admin <user_id> <сумма>\nПример: /withdraw_admin 123456789 50")
        return
    
    try:
        target_user_id = int(args[0])
        amount = float(args[1])
        if amount <= 0:
            await update.message.reply_text("❌ Сумма > 0!")
            return
    except ValueError:
        await update.message.reply_text("❌ Введи числа!")
        return
    
    pending = db.get_pending_withdraws()
    target = None
    for w in pending:
        if w["user_id"] == target_user_id and abs(w["amount"] - amount) < 0.01:
            target = w
            break
    
    if not target:
        await update.message.reply_text(f"❌ Нет заявки от {target_user_id} на {format_eur(amount)}")
        return
    
    success = db.confirm_withdraw(target["id"])
    if not success:
        await update.message.reply_text("❌ Ошибка подтверждения вывода!")
        return
    
    try:
        target_lang = db.get_user_language(target_user_id)
        await context.bot.send_message(
            chat_id=target_user_id,
            text=get_text(target_user_id, "withdraw_success", target_lang, 
                         id=target["id"], amount=format_eur(amount)),
        )
    except Exception:
        pass
    
    await update.message.reply_text(f"✅ Вывод #{target['id']} подтвержден!")

# ========== ПРОСМОТР СДЕЛКИ ==========
async def generate_view_code(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    lang = db.get_user_language(user_id)
    
    if not is_admin(user_id):
        await update.message.reply_text(get_text(user_id, "no_rights", lang))
        return
    
    args = context.args
    if not args:
        await update.message.reply_text("❌ /view <код_счета>\nПример: /view A1B2C3D4")
        return
    
    invoice_code = args[0].strip().upper()
    payment = db.get_payment_by_code(invoice_code)
    if not payment:
        await update.message.reply_text(get_text(user_id, "invoice_not_found", lang))
        return
    if payment["status"] != "paid":
        await update.message.reply_text(get_text(user_id, "invoice_not_paid", lang))
        return
    
    view_code = generate_view_code()
    db.save_view_code(view_code, invoice_code)
    await update.message.reply_text(
        get_text(user_id, "view_code_created", lang, view_code=view_code, invoice_code=invoice_code)
    )

async def check_invoice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    lang = db.get_user_language(user_id)
    
    args = context.args
    if not args:
        await update.message.reply_text("❌ /check <код_просмотра>\nПример: /check A1B2C3")
        return
    
    view_code = args[0].strip().upper()
    invoice_code = db.get_invoice_by_view_code(view_code)
    if not invoice_code:
        await update.message.reply_text("❌ Неверный или уже использованный код!")
        return
    
    payment = db.get_payment_by_code(invoice_code)
    db.mark_view_code_used(view_code)
    if not payment:
        await update.message.reply_text(get_text(user_id, "invoice_not_found", lang))
        return
    
    status = get_text(user_id, "invoice_status_paid" if payment["status"] == "paid" else "invoice_status_pending", lang)
    
    await update.message.reply_text(
        get_text(user_id, "check_invoice", lang,
                code=payment['payment_code'],
                amount=format_eur(payment['amount']),
                status=status,
                created=payment['created_at'][:16],
                commission=format_eur(payment['commission']),
                creator=payment['creator_id'])
    )

# ========== ИНФА О ПОЛЬЗОВАТЕЛЕ ==========
async def userinfo_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    lang = db.get_user_language(user_id)
    
    if not is_admin(user_id):
        await update.message.reply_text(get_text(user_id, "no_rights", lang))
        return
    
    args = context.args
    if not args:
        await update.message.reply_text("❌ /userinfo <user_id>\nПример: /userinfo 6115925216")
        return
    
    try:
        target_id = int(args[0])
    except ValueError:
        await update.message.reply_text(get_text(user_id, "invalid_id", lang))
        return
    
    stats = db.get_user_full_stats(target_id)
    if not stats:
        await update.message.reply_text(get_text(user_id, "user_not_found", lang))
        return
    
    user = stats['user']
    
    invoices_text = ""
    for inv in stats['invoices'][:5]:
        status_emoji = "✅" if inv['status'] == 'paid' else "⏳"
        invoices_text += f"  {status_emoji} {inv['payment_code']} | {format_eur(inv['amount'])} | {inv['created_at'][:16]}\n"
    if not invoices_text:
        invoices_text = "  Нет данных\n"
    
    payments_text = ""
    for pm in stats['payments_made'][:5]:
        payments_text += f"  💳 {pm['payment_code']} | {format_eur(pm['amount'])} | {pm['created_at'][:16]}\n"
    if not payments_text:
        payments_text = "  Нет данных\n"
    
    await update.message.reply_text(
        get_text(user_id, "user_info", lang,
                id=user['user_id'],
                username=user.get('username', 'нет'),
                registered=user['registered_at'][:16],
                balance=format_eur(user['balance']),
                created=stats['total_created'],
                paid_count=stats['total_paid_count'],
                paid_sum=format_eur(stats['total_paid_sum']),
                earned=format_eur(stats['total_earned']),
                commission_paid=format_eur(stats['total_commission_paid']),
                invoices=invoices_text.strip(),
                payments=payments_text.strip())
    )

# ========== ПОЛУЧИТЬ ID ПО USERNAME ==========
async def get_user_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    lang = db.get_user_language(user_id)
    
    if not is_admin(user_id):
        await update.message.reply_text(get_text(user_id, "no_rights", lang))
        return
    
    args = context.args
    if not args:
        await update.message.reply_text("❌ /getid <username>\nПример: /getid @username")
        return
    
    username = args[0].strip().replace('@', '')
    user = db.get_user_by_username(username)
    
    if user:
        await update.message.reply_text(
            f"👤 Найден в базе:\n"
            f"🆔 ID: {user['user_id']}\n"
            f"👤 Username: @{user.get('username', 'нет')}\n"
            f"💰 Баланс: {format_eur(user['balance'])}"
        )
    else:
        await update.message.reply_text(
            get_text(user_id, "user_not_in_db", lang, username=username)
        )

# ========== START ==========
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    db.get_or_create_user(
        user_id=user.id,
        username=user.username,
        first_name=user.first_name,
        last_name=user.last_name,
    )
    await main_menu(update, context)

# ========== ОБРАБОТЧИК ТЕКСТА ==========
async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    lang = db.get_user_language(user_id)
    state = context.user_data.get("state")
    
    if state == "waiting_amount":
        await create_invoice_amount(update, context)
        context.user_data["state"] = None
        return
    if state == "waiting_pay_code":
        await pay_invoice_code(update, context)
        context.user_data["state"] = None
        return
    if state == "waiting_withdraw_amount":
        await withdraw_amount(update, context)
        context.user_data["state"] = None
        return
    
    await update.message.reply_text(get_text(user_id, "use_buttons", lang))

# ========== CALLBACK HANDLER ==========
async def callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    data = query.data
    
    if data == "main_menu":
        await main_menu(update, context)
    elif data == "create_invoice":
        await create_invoice_start(update, context)
    elif data == "pay_invoice":
        await pay_invoice_start(update, context)
    elif data == "my_balance":
        await my_balance(update, context)
    elif data == "withdraw":
        await withdraw_start(update, context)
    elif data == "admin_stats":
        await admin_stats(update, context)
    elif data == "admin_users":
        await admin_users(update, context)
    elif data == "help":
        await help_menu(update, context)
    elif data == "help_admin":
        await help_admin_callback(update, context)
    elif data == "change_language":
        await change_language(update, context)
    elif data.startswith("set_lang_"):
        await set_language(update, context)
    elif data.startswith("pay_method_"):
        await payment_method_handler(update, context)
    elif data.startswith("confirm_payment_"):
        await confirm_payment(update, context)
    elif data.startswith("back_to_payment_"):
        await back_to_payment_methods(update, context)

# ========== MAIN ==========
def main():
    application = Application.builder().token(Config.BOT_TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help_admin", help_admin_command))
    application.add_handler(CommandHandler("withdraw_admin", withdraw_admin_command))
    application.add_handler(CommandHandler("view", generate_view_code))
    application.add_handler(CommandHandler("check", check_invoice))
    application.add_handler(CommandHandler("userinfo", userinfo_command))
    application.add_handler(CommandHandler("getid", get_user_id))
    application.add_handler(CommandHandler("stats", admin_stats))
    application.add_handler(CommandHandler("users", admin_users))
    
    application.add_handler(CallbackQueryHandler(callback_handler))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    
    logger.info("🚀 Бот запущен и готов к работе!")
    application.run_polling()

if __name__ == "__main__":
    main()

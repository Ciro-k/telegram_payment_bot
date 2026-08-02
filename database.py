import sqlite3
import logging
from datetime import datetime, timedelta
from typing import Optional, List, Dict, Any

logger = logging.getLogger(__name__)

class Database:
    def __init__(self, db_path: str = 'payments.db'):
        self.db_path = db_path
        self._init_tables()
    
    def _get_connection(self):
        conn = sqlite3.connect(self.db_path)
        conn.execute("PRAGMA foreign_keys = ON")
        conn.row_factory = sqlite3.Row
        return conn
    
    def _init_tables(self):
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS users (
                        user_id INTEGER PRIMARY KEY,
                        username TEXT,
                        first_name TEXT,
                        last_name TEXT,
                        balance REAL DEFAULT 0,
                        is_admin INTEGER DEFAULT 0,
                        language TEXT DEFAULT 'ru',
                        registered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                ''')
                
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS payments (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        payment_code TEXT UNIQUE NOT NULL,
                        creator_id INTEGER NOT NULL,
                        amount REAL NOT NULL,
                        status TEXT DEFAULT 'pending',
                        commission REAL DEFAULT 0,
                        creator_earned REAL DEFAULT 0,
                        payer_id INTEGER,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        paid_at TIMESTAMP,
                        FOREIGN KEY (creator_id) REFERENCES users(user_id),
                        FOREIGN KEY (payer_id) REFERENCES users(user_id)
                    )
                ''')
                
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS withdraws (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER NOT NULL,
                        amount REAL NOT NULL,
                        status TEXT DEFAULT 'pending',
                        requested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        completed_at TIMESTAMP,
                        FOREIGN KEY (user_id) REFERENCES users(user_id)
                    )
                ''')
                
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS logs (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        action TEXT NOT NULL,
                        user_id INTEGER,
                        details TEXT,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                ''')
                
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS settings (
                        key TEXT PRIMARY KEY,
                        value TEXT NOT NULL
                    )
                ''')
                
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS view_codes (
                        view_code TEXT PRIMARY KEY,
                        invoice_code TEXT NOT NULL,
                        used INTEGER DEFAULT 0,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                ''')
                
                cursor.execute('''
                    INSERT OR IGNORE INTO settings (key, value) 
                    VALUES ('commission_percent', '1.0')
                ''')
                
                # Добавляем главного админа (который указан в .env)
                from config import Config
                cursor.execute('''
                    INSERT OR IGNORE INTO users (user_id, is_admin, balance, language)
                    VALUES (?, 1, 0, 'ru')
                ''', (Config.ADMIN_ID,))
                
                conn.commit()
                logger.info("Таблицы инициализированы успешно")
        except Exception as e:
            logger.error(f"Ошибка инициализации БД: {e}")
            raise
    
    def get_or_create_user(self, user_id: int, username: str = None, 
                           first_name: str = None, last_name: str = None) -> Dict:
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
                user = cursor.fetchone()
                if not user:
                    is_admin = 0
                    cursor.execute('''
                        INSERT INTO users (user_id, username, first_name, last_name, is_admin, language)
                        VALUES (?, ?, ?, ?, ?, 'ru')
                    ''', (user_id, username, first_name, last_name, is_admin))
                    conn.commit()
                    self.add_log('register', user_id, f"Зарегистрирован новый пользователь")
                    cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
                    user = cursor.fetchone()
                return dict(user)
        except Exception as e:
            logger.error(f"Ошибка get_or_create_user: {e}")
            return None
    
    def get_user(self, user_id: int) -> Optional[Dict]:
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
                user = cursor.fetchone()
                return dict(user) if user else None
        except Exception as e:
            logger.error(f"Ошибка get_user: {e}")
            return None
    
    def update_balance(self, user_id: int, amount: float) -> bool:
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('UPDATE users SET balance = balance + ? WHERE user_id = ?', (amount, user_id))
                conn.commit()
                return True
        except Exception as e:
            logger.error(f"Ошибка update_balance: {e}")
            return False
    
    def get_all_users(self) -> List[Dict]:
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM users ORDER BY registered_at DESC')
                return [dict(row) for row in cursor.fetchall()]
        except Exception as e:
            logger.error(f"Ошибка get_all_users: {e}")
            return []
    
    def create_payment(self, creator_id: int, amount: float, payment_code: str) -> Optional[int]:
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO payments (creator_id, amount, payment_code, status)
                    VALUES (?, ?, ?, 'pending')
                ''', (creator_id, amount, payment_code))
                conn.commit()
                payment_id = cursor.lastrowid
                self.add_log('create_payment', creator_id, 
                            f"Создан платеж #{payment_id} на {amount} евро, код {payment_code}")
                return payment_id
        except Exception as e:
            logger.error(f"Ошибка create_payment: {e}")
            return None
    
    def get_payment_by_code(self, code: str) -> Optional[Dict]:
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM payments WHERE payment_code = ?', (code,))
                payment = cursor.fetchone()
                return dict(payment) if payment else None
        except Exception as e:
            logger.error(f"Ошибка get_payment_by_code: {e}")
            return None
    
    def update_payment_status(self, code: str, status: str) -> bool:
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('UPDATE payments SET status = ? WHERE payment_code = ?', (status, code))
                conn.commit()
                return True
        except Exception as e:
            logger.error(f"Ошибка update_payment_status: {e}")
            return False
    
    def confirm_payment(self, payment_code: str, payer_id: int, commission_percent: float) -> bool:
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM payments WHERE payment_code = ? AND status = "pending"', 
                              (payment_code,))
                payment = cursor.fetchone()
                if not payment:
                    return False
                payment = dict(payment)
                amount = payment['amount']
                creator_id = payment['creator_id']
                commission = round(amount * (commission_percent / 100), 2)
                creator_earned = round(amount - commission, 2)
                cursor.execute('''
                    UPDATE payments 
                    SET status = 'paid', payer_id = ?, paid_at = CURRENT_TIMESTAMP,
                        commission = ?, creator_earned = ?
                    WHERE payment_code = ?
                ''', (payer_id, commission, creator_earned, payment_code))
                cursor.execute('UPDATE users SET balance = balance + ? WHERE user_id = ?', (creator_earned, creator_id))
                
                # Начисляем комиссию админам (поровну)
                admins = self.get_admins()
                if admins:
                    admin_share = commission / len(admins)
                    for admin in admins:
                        cursor.execute('UPDATE users SET balance = balance + ? WHERE user_id = ?', (admin_share, admin['user_id']))
                
                conn.commit()
                self.add_log('payment_confirmed', payer_id, 
                            f"Оплачен код {payment_code}, сумма {amount}, комиссия {commission}")
                return True
        except Exception as e:
            logger.error(f"Ошибка confirm_payment: {e}")
            return False
    
    def get_payment_stats(self) -> Dict:
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT COUNT(*) as total_payments FROM payments WHERE status = "paid"')
                total_payments = cursor.fetchone()['total_payments']
                cursor.execute('SELECT SUM(amount) as total_amount FROM payments WHERE status = "paid"')
                total_amount = cursor.fetchone()['total_amount'] or 0
                cursor.execute('SELECT SUM(commission) as total_commission FROM payments WHERE status = "paid"')
                total_commission = cursor.fetchone()['total_commission'] or 0
                return {'total_payments': total_payments, 'total_amount': total_amount, 'total_commission': total_commission}
        except Exception as e:
            logger.error(f"Ошибка get_payment_stats: {e}")
            return {'total_payments': 0, 'total_amount': 0, 'total_commission': 0}
    
    def get_weekly_stats(self) -> Dict:
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                stats = {}
                for i in range(7):
                    day = (datetime.now() - timedelta(days=i)).strftime('%Y-%m-%d')
                    cursor.execute('''
                        SELECT 
                            COUNT(*) as total,
                            SUM(CASE WHEN status = 'paid' THEN 1 ELSE 0 END) as paid,
                            SUM(CASE WHEN status = 'paid' THEN amount ELSE 0 END) as amount,
                            SUM(CASE WHEN status = 'paid' THEN commission ELSE 0 END) as commission
                        FROM payments 
                        WHERE DATE(created_at) = ?
                    ''', (day,))
                    row = cursor.fetchone()
                    stats[day] = {
                        'total': row['total'] or 0,
                        'paid': row['paid'] or 0,
                        'amount': row['amount'] or 0,
                        'commission': row['commission'] or 0
                    }
                return stats
        except Exception as e:
            logger.error(f"Ошибка get_weekly_stats: {e}")
            return {}
    
    def create_withdraw_request(self, user_id: int, amount: float) -> Optional[int]:
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT balance FROM users WHERE user_id = ?', (user_id,))
                user = cursor.fetchone()
                if not user or user['balance'] < amount:
                    return None
                cursor.execute('''
                    INSERT INTO withdraws (user_id, amount, status)
                    VALUES (?, ?, 'pending')
                ''', (user_id, amount))
                withdraw_id = cursor.lastrowid
                self.add_log('withdraw_request', user_id, f"Запрос на вывод #{withdraw_id}, сумма {amount}")
                conn.commit()
                return withdraw_id
        except Exception as e:
            logger.error(f"Ошибка create_withdraw_request: {e}")
            return None
    
    def confirm_withdraw(self, withdraw_id: int) -> bool:
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM withdraws WHERE id = ? AND status = "pending"', (withdraw_id,))
                withdraw = cursor.fetchone()
                if not withdraw:
                    return False
                withdraw = dict(withdraw)
                user_id = withdraw['user_id']
                amount = withdraw['amount']
                cursor.execute('SELECT balance FROM users WHERE user_id = ?', (user_id,))
                user = cursor.fetchone()
                if not user or user['balance'] < amount:
                    return False
                cursor.execute('UPDATE users SET balance = balance - ? WHERE user_id = ?', (amount, user_id))
                cursor.execute('''
                    UPDATE withdraws 
                    SET status = 'completed', completed_at = CURRENT_TIMESTAMP
                    WHERE id = ?
                ''', (withdraw_id,))
                conn.commit()
                self.add_log('withdraw_completed', user_id, f"Вывод #{withdraw_id} подтвержден, сумма {amount}")
                return True
        except Exception as e:
            logger.error(f"Ошибка confirm_withdraw: {e}")
            return False
    
    def get_pending_withdraws(self) -> List[Dict]:
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT w.*, u.username, u.first_name, u.last_name 
                    FROM withdraws w
                    JOIN users u ON w.user_id = u.user_id
                    WHERE w.status = 'pending'
                    ORDER BY w.requested_at ASC
                ''')
                return [dict(row) for row in cursor.fetchall()]
        except Exception as e:
            logger.error(f"Ошибка get_pending_withdraws: {e}")
            return []
    
    def get_commission_percent(self) -> float:
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT value FROM settings WHERE key = "commission_percent"')
                result = cursor.fetchone()
                return float(result['value']) if result else 1.0
        except Exception as e:
            logger.error(f"Ошибка get_commission_percent: {e}")
            return 1.0
    
    def set_commission_percent(self, percent: float) -> bool:
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('UPDATE settings SET value = ? WHERE key = "commission_percent"', (str(percent),))
                conn.commit()
                self.add_log('settings_change', None, f"Изменена комиссия на {percent}%")
                return True
        except Exception as e:
            logger.error(f"Ошибка set_commission_percent: {e}")
            return False
    
    def add_log(self, action: str, user_id: int = None, details: str = None):
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('INSERT INTO logs (action, user_id, details) VALUES (?, ?, ?)', (action, user_id, details))
                conn.commit()
        except Exception as e:
            logger.error(f"Ошибка add_log: {e}")
    
    def get_recent_logs(self, limit: int = 20) -> List[Dict]:
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM logs ORDER BY created_at DESC LIMIT ?', (limit,))
                return [dict(row) for row in cursor.fetchall()]
        except Exception as e:
            logger.error(f"Ошибка get_recent_logs: {e}")
            return []
    
    def make_admin(self, user_id: int) -> bool:
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('UPDATE users SET is_admin = 1 WHERE user_id = ?', (user_id,))
                conn.commit()
                self.add_log('make_admin', user_id, f"Пользователь {user_id} стал админом")
                return True
        except Exception as e:
            logger.error(f"Ошибка make_admin: {e}")
            return False
    
    def remove_admin(self, user_id: int) -> bool:
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('UPDATE users SET is_admin = 0 WHERE user_id = ?', (user_id,))
                conn.commit()
                self.add_log('remove_admin', user_id, f"Пользователь {user_id} удален из админов")
                return True
        except Exception as e:
            logger.error(f"Ошибка remove_admin: {e}")
            return False
    
    def get_admins(self) -> List[Dict]:
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM users WHERE is_admin = 1')
                return [dict(row) for row in cursor.fetchall()]
        except Exception as e:
            logger.error(f"Ошибка get_admins: {e}")
            return []
    
    # ========== МЕТОДЫ ДЛЯ РАБОТЫ С ЯЗЫКОМ ==========
    def set_user_language(self, user_id: int, language: str) -> bool:
        """Установить язык пользователя"""
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                # Проверяем, есть ли колонка language
                cursor.execute("PRAGMA table_info(users)")
                columns = [col[1] for col in cursor.fetchall()]
                if 'language' not in columns:
                    cursor.execute('ALTER TABLE users ADD COLUMN language TEXT DEFAULT "ru"')
                    conn.commit()
                
                cursor.execute('UPDATE users SET language = ? WHERE user_id = ?', (language, user_id))
                conn.commit()
                return True
        except Exception as e:
            logger.error(f"Ошибка set_user_language: {e}")
            return False
    
    def get_user_language(self, user_id: int) -> str:
        """Получить язык пользователя"""
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT language FROM users WHERE user_id = ?', (user_id,))
                result = cursor.fetchone()
                if result and result['language']:
                    return result['language']
                return 'ru'
        except Exception as e:
            logger.error(f"Ошибка get_user_language: {e}")
            return 'ru'
    
    # ========== МЕТОДЫ ДЛЯ VIEW_CODES ==========
    def save_view_code(self, view_code: str, invoice_code: str) -> bool:
        """Сохранить одноразовый код просмотра"""
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                # Создаем таблицу если её нет
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS view_codes (
                        view_code TEXT PRIMARY KEY,
                        invoice_code TEXT NOT NULL,
                        used INTEGER DEFAULT 0,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                ''')
                conn.commit()
                cursor.execute('INSERT INTO view_codes (view_code, invoice_code) VALUES (?, ?)', 
                              (view_code, invoice_code))
                conn.commit()
                return True
        except Exception as e:
            logger.error(f"Ошибка save_view_code: {e}")
            return False
    
    def get_invoice_by_view_code(self, view_code: str) -> Optional[str]:
        """Получить код счета по коду просмотра"""
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT invoice_code, used FROM view_codes WHERE view_code = ?', (view_code,))
                result = cursor.fetchone()
                if result and result['used'] == 0:
                    return result['invoice_code']
                return None
        except Exception as e:
            logger.error(f"Ошибка get_invoice_by_view_code: {e}")
            return None
    
    def mark_view_code_used(self, view_code: str) -> bool:
        """Отметить код просмотра как использованный"""
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('UPDATE view_codes SET used = 1 WHERE view_code = ?', (view_code,))
                conn.commit()
                return True
        except Exception as e:
            logger.error(f"Ошибка mark_view_code_used: {e}")
            return False
    
    # ========== МЕТОДЫ ДЛЯ USER INFO ==========
    def get_user_by_username(self, username: str) -> Optional[Dict]:
        """Найти пользователя по username"""
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
                user = cursor.fetchone()
                return dict(user) if user else None
        except Exception as e:
            logger.error(f"Ошибка get_user_by_username: {e}")
            return None
    
    def get_user_full_stats(self, user_id: int) -> Optional[Dict]:
        """Полная статистика пользователя"""
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                
                # Получаем пользователя
                cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
                user = cursor.fetchone()
                if not user:
                    return None
                user = dict(user)
                
                # Созданные счета
                cursor.execute('SELECT COUNT(*) as count FROM payments WHERE creator_id = ?', (user_id,))
                total_created = cursor.fetchone()['count'] or 0
                
                # Оплаченные как покупатель
                cursor.execute('SELECT COUNT(*) as count, SUM(amount) as sum FROM payments WHERE payer_id = ? AND status = "paid"', (user_id,))
                paid_data = cursor.fetchone()
                total_paid_count = paid_data['count'] or 0
                total_paid_sum = paid_data['sum'] or 0
                
                # Заработано как продавец
                cursor.execute('SELECT SUM(creator_earned) as earned FROM payments WHERE creator_id = ? AND status = "paid"', (user_id,))
                total_earned = cursor.fetchone()['earned'] or 0
                
                # Комиссии заплачено
                cursor.execute('SELECT SUM(commission) as commission FROM payments WHERE payer_id = ? AND status = "paid"', (user_id,))
                total_commission = cursor.fetchone()['commission'] or 0
                
                # Последние созданные счета
                cursor.execute('SELECT * FROM payments WHERE creator_id = ? ORDER BY created_at DESC LIMIT 5', (user_id,))
                invoices = [dict(row) for row in cursor.fetchall()]
                
                # Последние оплаты
                cursor.execute('SELECT * FROM payments WHERE payer_id = ? AND status = "paid" ORDER BY paid_at DESC LIMIT 5', (user_id,))
                payments_made = [dict(row) for row in cursor.fetchall()]
                
                return {
                    'user': user,
                    'total_created': total_created,
                    'total_paid_count': total_paid_count,
                    'total_paid_sum': total_paid_sum,
                    'total_earned': total_earned,
                    'total_commission_paid': total_commission,
                    'invoices': invoices,
                    'payments_made': payments_made
                }
        except Exception as e:
            logger.error(f"Ошибка get_user_full_stats: {e}")
            return None

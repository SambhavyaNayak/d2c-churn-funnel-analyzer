from faker import Faker
import pandas as pd
import random
from datetime import timedelta
import os

# Setup
fake = Faker()
random.seed(42)

# Create data folder
os.makedirs('data', exist_ok=True)

# =========================
# 1. USERS DATA
# =========================
users = []

for i in range(10000):
    users.append({
        'user_id': f'U{i:05d}',
        'signup_date': fake.date_between(start_date='-12M', end_date='today'),
        'country': random.choice(['India', 'USA', 'UK', 'UAE', 'Singapore']),
        'device_type': random.choice(['Mobile', 'Desktop', 'Tablet'])
    })

users_df = pd.DataFrame(users)
users_df.to_csv('data/users.csv', index=False)

# =========================
# 2. SESSIONS DATA
# =========================
sessions = []

for i in range(25000):
    user = random.choice(users)

    session_time = fake.date_time_between(start_date='-6M', end_date='now')

    sessions.append({
        'session_id': f'S{i:06d}',
        'user_id': user['user_id'],
        'session_start': session_time,
        'pages_viewed': random.randint(1, 15),
        'session_duration_sec': random.randint(20, 1800)
    })

sessions_df = pd.DataFrame(sessions)
sessions_df.to_csv('data/sessions.csv', index=False)

# =========================
# 3. FUNNEL EVENTS
# =========================
funnel_events = []

for session in sessions:
    base_time = pd.to_datetime(session['session_start'])

    # Everyone views product
    funnel_events.append({
        'session_id': session['session_id'],
        'event_type': 'product_view',
        'event_time': base_time
    })

    # 45% add to cart
    if random.random() < 0.45:
        funnel_events.append({
            'session_id': session['session_id'],
            'event_type': 'add_to_cart',
            'event_time': base_time + timedelta(minutes=2)
        })

        # 60% start checkout
        if random.random() < 0.60:
            funnel_events.append({
                'session_id': session['session_id'],
                'event_type': 'checkout_start',
                'event_time': base_time + timedelta(minutes=5)
            })

            # 70% complete payment
            if random.random() < 0.70:
                funnel_events.append({
                    'session_id': session['session_id'],
                    'event_type': 'payment_success',
                    'event_time': base_time + timedelta(minutes=8)
                })

funnel_df = pd.DataFrame(funnel_events)
funnel_df.to_csv('data/funnel_events.csv', index=False)

# =========================
# 4. ORDERS DATA
# =========================
successful_sessions = funnel_df[
    funnel_df['event_type'] == 'payment_success'
]['session_id'].unique()

orders = []

for i, session_id in enumerate(successful_sessions):
    session_row = sessions_df[
        sessions_df['session_id'] == session_id
    ].iloc[0]

    orders.append({
        'order_id': f'O{i:05d}',
        'user_id': session_row['user_id'],
        'order_date': pd.to_datetime(
            session_row['session_start']
        ).date(),
        'order_value': round(random.uniform(299, 9999), 2)
    })

orders_df = pd.DataFrame(orders)
orders_df.to_csv('data/orders.csv', index=False)

# =========================
# SUMMARY
# =========================
print('\\n✅ DATASETS GENERATED SUCCESSFULLY')
print('-' * 40)
print(f'Users: {len(users_df):,}')
print(f'Sessions: {len(sessions_df):,}')
print(f'Funnel Events: {len(funnel_df):,}')
print(f'Orders: {len(orders_df):,}')
print('\\nFiles saved in the data folder.')
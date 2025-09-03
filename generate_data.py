
import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta
import numpy as np

fake = Faker()
Faker.seed(42)
random.seed(42)
np.random.seed(42)

# Parameters
num_users = 10000
groups = ['A', 'B']
locations = ['Dubai', 'Abu Dhabi', 'Sharjah', 'Ajman']
loyalty_tiers = ['Basic', 'Silver', 'Gold']

data = []

for i in range(1, num_users + 1):
    user_id = f"U{i:05d}"
    group = random.choice(groups)
    signup_date = fake.date_between(start_date='-60d', end_date='-30d')

    # Simulate behavior
    if group == 'A':
        repeat = np.random.binomial(1, 0.22)  # ~22% repeat purchase
        revenue = np.random.normal(140, 60) if repeat else np.random.normal(70, 30)
    else:
        repeat = np.random.binomial(1, 0.30)  # ~30% repeat purchase with cashback
        revenue = np.random.normal(160, 65) if repeat else np.random.normal(80, 35)

    location = random.choice(locations)
    loyalty_tier = random.choices(loyalty_tiers, weights=[0.6, 0.3, 0.1])[0]

    data.append({
        'user_id': user_id,
        'group': group,
        'signup_date': signup_date,
        'repeat_purchase': repeat,
        'location': location,
        'loyalty_tier': loyalty_tier,
        'revenue': round(max(revenue, 0), 2)  # No negative revenue
    })

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("./data/loyalty_users.csv", index=False)
print("✅ Dataset 'loyalty_users.csv' generated with", len(df), "records.")
df.head()

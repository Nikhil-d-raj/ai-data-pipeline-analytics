from faker import Faker
import pandas as pd
import random

fake = Faker()

data = []

for _ in range(1000):
    data.append({
        "customer_id": random.randint(1000, 9999),
        "name": fake.name(),
        "email": fake.email(),
        "country": fake.country(),
        "purchase_amount": round(random.uniform(100, 10000), 2)
    })

df = pd.DataFrame(data)
df.to_csv("customer_data.csv", index=False)

print("Sample data generated!")

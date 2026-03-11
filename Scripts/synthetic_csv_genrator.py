import pandas as pd
import random
from faker import Faker

fake = Faker()

# -----------------------
# CRM DOMAIN
# -----------------------

def generate_crm():
    customers = []
    for i in range(1, 51):
        customers.append({
            "customer_id": i,
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "email": fake.email(),
            "status": random.choice(["Active", "Inactive"]),
            "created_date": fake.date_between(start_date='-2y', end_date='today')
        })

    pd.DataFrame(customers).to_csv("crm_customers.csv", index=False)

    leads = []
    for i in range(1, 31):
        leads.append({
            "lead_id": i,
            "lead_name": fake.name(),
            "email": fake.email(),
            "source": random.choice(["Website", "LinkedIn", "Referral"]),
            "created_date": fake.date_between(start_date='-1y', end_date='today')
        })

    pd.DataFrame(leads).to_csv("crm_leads.csv", index=False)

    interactions = []
    for i in range(1, 101):
        interactions.append({
            "interaction_id": i,
            "customer_id": random.randint(1, 50),
            "interaction_type": random.choice(["Call", "Email", "Meeting"]),
            "interaction_date": fake.date_between(start_date='-1y', end_date='today')
        })

    pd.DataFrame(interactions).to_csv("crm_interactions.csv", index=False)


# -----------------------
# RETAIL DOMAIN
# -----------------------

def generate_retail():
    customers = []
    for i in range(1, 201):
        customers.append({
            "customer_id": i,
            "name": fake.name(),
            "email": fake.email(),
            "country": fake.country(),
            "created_date": fake.date_between(start_date='-3y', end_date='today')
        })

    pd.DataFrame(customers).to_csv("retail_customers.csv", index=False)

    products = []
    for i in range(1, 101):
        products.append({
            "product_id": i,
            "product_name": fake.word(),
            "category": random.choice(["Electronics", "Clothing", "Home"]),
            "price": round(random.uniform(10, 500), 2)
        })

    pd.DataFrame(products).to_csv("retail_products.csv", index=False)

    orders = []
    for i in range(1, 501):
        orders.append({
            "order_id": i,
            "customer_id": random.randint(1, 200),
            "order_date": fake.date_between(start_date='-1y', end_date='today'),
            "status": random.choice(["Completed", "Pending", "Cancelled"])
        })

    pd.DataFrame(orders).to_csv("retail_orders.csv", index=False)

    order_items = []
    for i in range(1, 1201):
        order_items.append({
            "order_item_id": i,
            "order_id": random.randint(1, 500),
            "product_id": random.randint(1, 100),
            "quantity": random.randint(1, 5)
        })

    pd.DataFrame(order_items).to_csv("retail_order_items.csv", index=False)


# -----------------------
# INSURANCE DOMAIN
# -----------------------

def generate_insurance():
    holders = []
    for i in range(1, 301):
        holders.append({
            "policy_holder_id": i,
            "name": fake.name(),
            "email": fake.email(),
            "city": fake.city()
        })

    pd.DataFrame(holders).to_csv("insurance_policy_holders.csv", index=False)

    policies = []
    for i in range(1, 501):
        policies.append({
            "policy_id": i,
            "policy_holder_id": random.randint(1, 300),
            "policy_type": random.choice(["Health", "Vehicle", "Life"]),
            "start_date": fake.date_between(start_date='-3y', end_date='-1y'),
            "premium_amount": round(random.uniform(200, 2000), 2)
        })

    pd.DataFrame(policies).to_csv("insurance_policies.csv", index=False)

    claims = []
    for i in range(1, 1501):
        claims.append({
            "claim_id": i,
            "policy_id": random.randint(1, 500),
            "claim_amount": round(random.uniform(100, 10000), 2),
            "claim_status": random.choice(["Approved", "Rejected", "Pending"])
        })

    pd.DataFrame(claims).to_csv("insurance_claims.csv", index=False)

    payments = []
    for i in range(1, 2001):
        payments.append({
            "payment_id": i,
            "policy_id": random.randint(1, 500),
            "payment_date": fake.date_between(start_date='-1y', end_date='today'),
            "amount": round(random.uniform(100, 2000), 2)
        })

    pd.DataFrame(payments).to_csv("insurance_payments.csv", index=False)


# -----------------------
# RUN ALL GENERATORS
# -----------------------

generate_crm()
generate_retail()
generate_insurance()

print("All CSV files generated successfully.")

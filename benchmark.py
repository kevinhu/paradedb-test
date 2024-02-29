# %%
import multiprocessing
import random
import time
import faker
from tqdm import tqdm
import uuid
import psycopg


# %%
def insert_person(person):
    try:
        with psycopg.connect(
            "host=localhost dbname=dev user=dev password=test port=2345"
        ) as conn:
            with conn.cursor() as cur:
                time.sleep(random.random())
                cur.execute(
                    "INSERT INTO global.people (id, name, description) VALUES (%s, %s, %s)",
                    (str(uuid.uuid4()), person["name"], person["description"]),
                )
    except Exception as e:
        print(e)


if __name__ == "__main__":
    num_docs = 1000

    people = []

    fake = faker.Faker()

    for _ in tqdm(range(num_docs)):
        doc = {"name": fake.name(), "description": fake.text()}
        people.append(doc)

    with multiprocessing.Pool(128) as pool:
        for _ in tqdm(pool.imap_unordered(insert_person, people)):
            pass

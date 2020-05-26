from sqlalchemy import create_engine
import pandas
import matplotlib.pyplot as plt

engine = create_engine("sqlite:///sample.db")

query = """select products.prod_name as product_name, count(products.prod_id) as frequency
        from transactions
        join products
        on transactions.prod_id = products.prod_id
        group by transactions.prod_id
        order by frequency desc limit 10"""

with engine.connect() as conn, conn.begin():
    data = pandas.read_sql_query(query, conn)
    print(data)
    data.plot(x="product_name", y="frequency", kind="pie", use_index=False)
    plt.show()

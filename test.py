import sqlite3
from datetime import datetime

connection = sqlite3.connect("sample.db")
c = connection.cursor()
c.execute(
    """
        SELECT segments.cust_id, segments.seg_name, segments.update_at
        FROM segments WHERE segments.active_flag = 'Y'
        group by cust_id having max(update_at)
    """
)
customer_list = []
for cust_id, _, _, in c.fetchall():
    if cust_id in customer_list:
        raise ValueError(cust_id)
    else:
        customer_list.append(cust_id)
c.close()

c = connection.cursor()
c.execute(
    """
        SELECT trans_dt
        from transactions
        join products
        on transactions.prod_id = products.prod_id
        where transactions.trans_dt >= datetime('2016-01-01 00:00:00') and transactions.trans_dt <= datetime('2016-05-31 23:59:59')
        group by transactions.prod_id
    """
)
customer_list = []
date_format = "%Y-%m-%d %H:%M:%S"
start_date = datetime.strptime("2016-01-01 00:00:00", date_format)
end_date = datetime.strptime("2016-05-31 23:59:59", date_format)
for record in c.fetchall():
    trans_date = datetime.strptime(record[0], date_format)
    if trans_date >= start_date and trans_date <= end_date:
        continue
    else:
        raise ValueError(trans_date)
c.close()

c = connection.cursor()
c.execute(
    """
       select cust_id, update_at, seg_name
       from segments
       where update_at <= datetime("2016-03-01 23:59:59")
       group by cust_id having max(update_at);
    """
)
customer_list = []
date_format = "%Y-%m-%d %H:%M:%S"
end_date_1 = datetime.strptime("2016-03-01 23:59:59", date_format)
for record in c.fetchall():
    trans_date = datetime.strptime(record[1], date_format)
    if trans_date > end_date_1 or record[0] in customer_list:
        ValueError(f"{record[0]} -- {record[1]}")
c.close()

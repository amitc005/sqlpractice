## Comments:
1. From the README.md, there are several occurrences about the active segment </br>
   means `active='Y'` for each customers, But I have found some inconsistent </br>
   about that statement, because If we execute this SQL line </br>
   `select cust_id from segments where active_flag = 'Y' and group by cust_id having count(cust_id) > 1` </br>
   We see the customers who have the multiple active records. Such as customer number '12064'

## Answers:

1. Find the current active segment for each customer sorted by the segment
   update date.  The output should contain three columns: `cust_id`,
   `seg_name`, `updated_at`.  Here is some sample output:

        cust_id     seg_name        updated_at
        4402        LAPSED          2014-06-01 00:00:00
        11248       ONE-OFFS        2015-10-01 00:00:00

    Answer: `SELECT segments.cust_id, segments.seg_name, segments.update_at FROM segments WHERE segments.active_flag = 'Y' group by cust_id having max(update_at)`

2. For each product purchased between Jan 2016 and May 2016 (inclusive), find
   the number of distinct transactions.  The output should contain `prod_id`,
   `prod_name` and distinct transaction columns.  Here is some sample output:

        prod_id     prod_name       count
        199922      Product 199922  1
        207344      Product 207344  1
        209732      Product 209732  1

    Answer: ```SELECT transactions.prod_id, prod_name, count(distinct(trans_id)) as count
        from transactions
        join products
        on transactions.prod_id = products.prod_id
        where transactions.trans_dt >= datetime('2016-01-01 00:00:00') and transactions.trans_dt <= datetime('2016-05-31 23:59:59')
        group by transactions.prod_id```

3. Find the most recent segment of each customer as of 2016-03-01.
   *Hint*: You cannot simply use `active_flag` since that is as of the current
   date *not* 2016-03-01.  The output should contain the `cust_id`, `seg_name`
   and `update_at`  columns and should have at most one row per customer.  Here
   is some sample output:

       cust_id  seg_name    update_at
       4402     ONE-OFFS    2016-02-01 00:00:00
       11248    LOYAL       2016-02-01 00:00:00
       126169   ONE-OFFS    2015-03-01 00:00:00

    Answer: ```select cust_id, seg_name, update_at
       from segments
       where update_at <= datetime("2016-03-01 23:59:59")
       group by cust_id having max(update_at)```
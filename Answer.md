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

    * Answer:
    ```
        SELECT segments.cust_id, segments.seg_name, segments.update_at
        FROM segments
        WHERE segments.active_flag = 'Y'
        group by cust_id having max(update_at)
        order by update_at
    ```
    * Comment: From my comment no. 1, I can not use just active_flag = 'Y', because of multiple active rows for each customers. Therefore I used group by cust and bring
    up the latest one by using having clause(PS: Sqllite viewer is brining the latest record without having clause, need to check with other vendors, MySQL, Postgres)

2. For each product purchased between Jan 2016 and May 2016 (inclusive), find
   the number of distinct transactions.  The output should contain `prod_id`,
   `prod_name` and distinct transaction columns.  Here is some sample output:

        prod_id     prod_name       count
        199922      Product 199922  1
        207344      Product 207344  1
        209732      Product 209732  1

    * Answer:
        ```
            SELECT transactions.prod_id, prod_name, count(distinct(trans_id)) as count
            from transactions
            join products
            on transactions.prod_id = products.prod_id
            where transactions.trans_dt >= datetime('2016-01-01 00:00:00') and transactions.trans_dt <= datetime('2016-05-31 23:59:59')
            group by transactions.prod_id
        ```

3. Find the most recent segment of each customer as of 2016-03-01.
   *Hint*: You cannot simply use `active_flag` since that is as of the current
   date *not* 2016-03-01.  The output should contain the `cust_id`, `seg_name`
   and `update_at`  columns and should have at most one row per customer.  Here
   is some sample output:

       cust_id  seg_name    update_at
       4402     ONE-OFFS    2016-02-01 00:00:00
       11248    LOYAL       2016-02-01 00:00:00
       126169   ONE-OFFS    2015-03-01 00:00:00

    * Answer:
        ```
            select cust_id, seg_name, update_at
            from segments
            where update_at <= datetime("2016-03-01 23:59:59")
            group by cust_id having max(update_at)
        ```

4. Find the most popular category (by revenue) for each active segment.
   *Hint*: The current (most up to date) active segment is specified by `active_flag = 'Y'` column in the segments table.
   Here is the some sample output:

  	seg_name    category    revenue
	INFREQUENT  Women       20264

    Answer: `select products.category, sum(item_price) as revenue from transactions join products on transactions.prod_id = products.prod_id group by products.category` </br>
    Result:

        category    revenue
        Accessories 1706.15
        Make Up     26296.9200000004
        Men         15791.9
        Sun         1195.57
        Women       55936.9399999995

    Comment: </br>
        I have successfully determined which is the most popular category according to the customer expenditure. </br>
        But, I have faced a problem to join the segment table, because I can not determine products where were involved
        in segmentation changes.


## Testing Answer 1, 2, and 3
* I have added test.py file to verify answer 1 to 3, checked Sql clauses which could go wrong if we use them in a wrong way.
* To run the test script, please make sure you have python 3.6+
* Run on your terminal ( make sure you are inside the directory.)
    ```
        $ python test.py
    ```

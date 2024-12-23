This code selects the total amount (quantity * price) for each product, groups the results by product_id, and orders the results from highest total amount to lowest.
table called sales
id | product_id | customer_id | sales_date |quantity | price |


SELECT 
    product_id,
    SUM(price * quantity) as total_amount
FROM sales
GROUP BY product_id

______
select (quantity * price) as totalamount
from sales
group by product_id
order by totalamount desc // from highest to lowest


for each costumer which product buy most
______
select customer_id,product_id
group by customer_id 
order by quantity desc



data install csv 

user_id col_a col_b col_c col_new
1  2 3 4

filea
from pandas 
lines = filea.split("\n")
freq_cola = {}
for i in lines:
    col_a_val = i.split(",")[1]
    col_b_val = i.split(",")[2]
    col_c_val = float(col_a_val) * float*(col_b_val)

fix
from pandas import DataFrame

def process_file(filea: str) -> dict:
    lines = filea.split("\n")
    freq_cola = {}
    
    for line in lines:
        columns = line.split(",")
        if len(columns) >= 3:
            try:
                col_a_val = columns[1]
                col_b_val = columns[2]
                col_c_val = float(col_a_val) * float(col_b_val)
                freq_cola[col_c_val] = freq_cola.get(col_c_val, 0) + 1
            except ValueError:
                continue
            
    return freq_cola



game logs -> login keywords 
elastic search to extract these  -> merge them base on timestamp location 
transfer them into login players -> mysql - > grafana dashboard 
on jenkins using python





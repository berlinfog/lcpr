This code selects the total amount (quantity * price) for each product, groups the results by product_id, and orders the results from highest total amount to lowest.
table called sales
id | product_id | customer_id | sales_date |quantity | price |

//turn into sql
SELECT 
    product_id,
    SUM(price * quantity) as total_amount
FROM sales
GROUP BY product_id
//在 SQL 中，GROUP BY 和带 PARTITION BY 的窗口函数是两种不同的操作方式，主要区别在于结果的维度和是否保留行的详细信息
______________________________________________
// from highest to lowest
SELECT 
    product_id,
    SUM(price * quantity) as total_amount
FROM sales
GROUP BY product_id
ORDER BY total_amount DESC


——————————————————————————————————————————————
//for each costumer which product buy most

select customer_id, product_id, total_quantity
from(
    select customer_id, product_id,sum(quantity) as total_quantity,
    rank() over(partition by customer_id order by sum(quantity) desc) as rank
    from sales
    group by customer_id,product_id
) as customer_product_rank
where rank = 1
order by customer_id;


————————————————————————————————————————————————
data install csv 

there is a file called a.csv , the col like : user_id col_a col_b col_c 
how to get the col_new based on col_a+ col_b+ col_c group by user_id and save to the origin file

import pandas as pd

# Read the CSV file
df = pd.read_csv('a.csv')

# Calculate new column as sum of col_a, col_b, col_c grouped by user_id
df['col_new'] = df.groupby('user_id')[['col_a', 'col_b', 'col_c']].transform('sum')

# Save back to the original file
df.to_csv('a.csv', index=False)

.transform() vs .apply()
.transform() 返回的结果与原始数据形状相同，可以直接添加到原始 DataFrame。
.apply() 的结果通常是分组后的缩小数据（类似 SQL 聚合的结果）。
_______________________________________________

calculate the frequency of col_c

import pandas as pd

# Read the CSV file
df = pd.read_csv('a.csv')

# Calculate frequency of col_c values
frequency = df['col_c'].value_counts()

# Optional: Convert to DataFrame for better formatting
frequency_df = frequency.reset_index()
frequency_df.columns = ['col_c', 'frequency']

# Save to a new CSV file
frequency_df.to_csv('col_c_frequency.csv', index=False)



import pandas as pd

# Read the CSV file
df = pd.read_csv('a.csv')

# Calculate frequency of col_c values
frequency = df['col_c'].value_counts()

# Map the frequency back to the original DataFrame
df['col_c_frequency'] = df['col_c'].map(frequency)

# Save the DataFrame with the additional frequency column to a new CSV file
df.to_csv('a_with_col_c_frequency.csv', index=False)

https://juejin.cn/post/7079761909624340493
_______________________________________________



game logs -> login keywords 
elastic search to extract these  -> merge them base on timestamp location 
transfer them into login players -> mysql - > grafana dashboard 
on jenkins using python


import pandas as pd

# 读取 JSON 数据
df = pd.read_json('data.json')

# 删除缺失值
df = df.dropna()

# 用指定的值填充缺失值
df = df.fillna({'age': 0, 'score': 0})

# 重命名列名
df = df.rename(columns={'name': '姓名', 'age': '年龄', 'gender': '性别', 'score': '成绩'})

# 按成绩排序
df = df.sort_values(by='成绩', ascending=False)

# 按性别分组并计算平均年龄和成绩
grouped = df.groupby('性别').agg({'年龄': 'mean', '成绩': 'mean'})

# 选择成绩大于等于90的行，并只保留姓名和成绩两列
df = df.loc[df['成绩'] >= 90, ['姓名', '成绩']]

# 计算每列的基本统计信息
stats = df.describe()

# 计算每列的平均值
mean = df.mean()

# 计算每列的中位数
median = df.median()

# 计算每列的众数
mode = df.mode()

# 计算每列非缺失值的数量
count = df.count()




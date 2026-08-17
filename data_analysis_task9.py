# IMPORTING LIBRARIES
import pandas as pd
import matplotlib.pyplot as mat
import seaborn as sea

# LOADING CSV
data = pd.read_csv(r"C:\Users\91783\OneDrive\Desktop\superstore.csv")

# INSIGHT 1 -> CHECKING WHICH PRODUCT CATEGORY HAS HIGHEST SALES?
df= data.groupby('Category')['Sales'].sum().reset_index()
print(df)
sea.barplot(data=df , x = 'Category',y='Sales')
mat.title('Category Wise Sales')
mat.xlabel('Categories')
mat.ylabel('Sales')
mat.savefig("Category_Wise_Sales.png")
mat.show()

#INSIGHT 2 -> WHICH SUBCATEGORY HAS THE HIGHEST SALES ?
mat.figure()
sub = data.groupby('Sub-Category')['Sales'].sum().sort_values(ascending=False).reset_index()
print(sub)
sea.barplot(data=sub,x='Sales',y='Sub-Category')
mat.title('Subcategory wise sales')
mat.xlabel('Sales')
mat.ylabel('Subcategory')
mat.savefig("Subcategory_wise_sales.png")
mat.show()

#INSIGHT 3 -> WHICH REGION GENERSTEs THE HIGHEST SALES ?
mat.figure()
reg = data.groupby('Region')['Sales'].sum().sort_values(ascending=False).reset_index()
print(reg)
sea.barplot(data=reg , x='Sales' , y='Region')
mat.title('Region wise sales')
mat.xlabel('Sales')
mat.ylabel('Region')
mat.savefig("Region_wise_sales.png")
mat.show()

#INSIGHT 4 -> WHICH CUSTOMER SEGMENT GENERATES HIGHEST SALES
mat.figure()
seg = data.groupby('Segment')['Sales'].sum().sort_values(ascending=False).reset_index()
print(seg)
sea.barplot(data=seg , x='Sales' , y='Segment')
mat.title('customer segment wise sales')
mat.xlabel('Sales')
mat.ylabel('Segment')
mat.savefig("customer_segment__wise_sales.png")
mat.show()

#INSIGHT 5 -> Which Category has the most orders?
mat.figure()
uni = data.groupby('Category')['Order ID'].nunique().sort_values(ascending=False).reset_index()
print(uni)
sea.barplot(data=uni , x='Category',y='Order ID')
mat.title('Highest number of orders per category')
mat.xlabel('Category')
mat.ylabel('Unique Order IDs')
mat.savefig("Highest_number_of_orders_per_category.png")
mat.show()


# INSIGHT 6 -> HOW DO SALES CHANGE OVERTIME?
mat.figure()
print(data['Order Date'].dtype)
data['Order Date'] = pd.to_datetime(data['Order Date'], dayfirst=True)
print(data['Order Date'].dtype)
yearly_sales = data.groupby(data['Order Date'].dt.year)['Sales'].sum().reset_index()
print(yearly_sales)
sea.barplot(data=yearly_sales , x='Order Date',y='Sales')
mat.title('Yearly sales')
mat.xlabel('Year')
mat.ylabel('Sales')
mat.savefig("Yearly_sales.png")
mat.show()
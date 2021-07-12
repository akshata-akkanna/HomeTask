import pandas as pd
from datetime import datetime, timedelta, timezone
from flask import Flask,request ,jsonify

app = Flask(__name__)

@app.route('/')
def index():
	return "Welcome to the Assignment"

#reading the parquet file using the pandas read function
with open(r'data.parquet.gzip', 'rb') as file_name:
	df_file = pd.read_parquet(file_name,engine='pyarrow')

	#creating the dataframe to fetch only Country Peru values
	value_peru = (df_file.loc[df_file['country_code'] == 'Peru']) 

	#defining index values as customer_id column
	value_peru['customer_id'] = value_peru.index

	#chanding the datatype od total_orders and removing NaN values from voucher_amount
	value_peru['total_orders'] = pd.to_numeric(value_peru['total_orders'], errors='coerce') 
	value_peru['voucher_amount'] = value_peru['voucher_amount'].fillna(0.0)


#creating post method to call the API
@app.route('/customer_object',methods=['POST'])
def customer():
	# input for customer object
	customer_id = request.args.get('customer_id')
	country_code = request.args.get('country_code')
	last_order_ts = request.args.get('last_order_ts')
	first_order_ts = request.args.get('first_order_ts')
	total_orders = float(request.args.get('total_orders'))
	segment_name = request.args.get('segment_name')

	#calling the test function to fetch the response
	value = test(customer_id,country_code,last_order_ts,first_order_ts,total_orders,segment_name)
	voucher_amount={'voucher_amount':value}
	return jsonify(voucher_amount)

#creating function to define the custome_object input
def test(customer_id,country_code,last_order_ts,first_order_ts,total_orders,segment_name):
	#creating if-else condtion for segment_name i.e frequent_segment and recency_segment
    if(segment_name == 'frequent_segment'):
        value_peru1 = value_peru[value_peru['customer_id'] == int(customer_id)]
        if((total_orders >= 0.0) & (total_orders <= 4.0)):
        	temp = value_peru1[value_peru1['total_orders'] == total_orders]
        elif ((total_orders >= 5.0) & (total_orders <= 13.0)):
        	temp = value_peru1[value_peru1['total_orders'] == total_orders]
        elif ((total_orders >= 14.0) & (total_orders <= 37.0)):
        	temp = value_peru1[value_peru1['total_orders'] == total_orders]
        temp1 = str(temp.iloc[0]['voucher_amount'])
    elif(segment_name == 'recency_segment'):
        value_peru1 = value_peru[value_peru['customer_id']== int(customer_id)]
        last_order_ts = pd.to_datetime(last_order_ts)
        now = pd.Timestamp.now()
        if(
        	((((now-last_order_ts).days) >= 30) & (((now-last_order_ts).days) <= 60) &
        	(((now-last_order_ts).days) >= 61) & (((now-last_order_ts).days) <= 90) &
        	(((now-last_order_ts).days) >= 91) & (((now-last_order_ts).days) <=120) &
        	(((now-last_order_ts).days) >= 121) & (((now-last_order_ts).days) <= 180) &
        	(((now-last_order_ts).days) >= 180)) == last_order_ts):
        	temp = value_peru1[value_peru1['last_order_ts'] == last_order_ts] 
        temp1 = str(temp.iloc[0]['voucher_amount'])
    else:
        temp1 = 'no values'
    return(temp1)

if __name__ == "__main__":
    app.run(debug=True)


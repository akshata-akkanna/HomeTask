Assignent


1. Keeping in mind that I am creating POC for the requirement I have not added any of the exceptional conditions for the input data. As, validating the imput columns.

2. I have read the input parquet file and used it as datadrame for the requirements, did not write it to the table schema as need to connect to the external database or need to create own local database.

3. There are NaN values in the input file, I have converted voucher amount NaN value into zero but total_orders I have kept as is because the first varient of the frequent_segment is for the total_orders zero so if I convert NaN into zero then that customer belongs to the frequent_segment.

4. Keeping in my of the segment and there varient I have wrote the conditions, for the total_orders more then 37 will not return any value as there is not segment_name provided for that in the document.

5. I have not added any try and catch exceptional for handing the errors so you may end up seeing internal error or error code 500 when conditions will not satisfied.

RUN THE CODE

#without docker 
1 . run this cmd FLASK_APP=task.py flask run
2 . Paste the URL in the postman or web to see the respective results

    For example : http://127.0.0.1:5000/customer_object?customer_id=63&country_code=Peru&last_order_ts=2020-04-19 00:00:00+00:00&first_order_ts=2017-07-24 00:00:00+00:00&total_orders=20&segment_name=recency_segment
 
#with docker

1. Build the image
  docker build -t heroapp .
2. List docker images
  docker images
3. tag the image
   docker tag heroapp app
4. Run the python code
  docker run -it heroapp python task.py
  
  and you will find docker id and run the URL http://127.0.0.1:5000


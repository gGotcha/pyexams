echo '-----------------MATCH TRUE------------'
curl -i -H "Content-Type: application/json" -X POST -d "order_date=''" http://localhost:5000/get_form
curl -i -H "Content-Type: application/json" -X POST -d "order_date=''&user_tel=''" http://localhost:5000/get_form
curl -i -H "Content-Type: application/json" -X POST -d "order_date=''&user_tel=''&user_email=''" http://localhost:5000/get_form
curl -i -H "Content-Type: application/json" -X POST -d "order_date=''&user_tel=''&user_email=''&user_info=''" http://localhost:5000/get_form
echo ''
echo '------------------MATCH FALSE-------------'
curl -i -H "Content-Type: application/json" -X POST -d "date_false=''&tel_false=''&email_false=''&text=''" http://localhost:5000/get_form
curl -i -H "Content-Type: application/json" -X POST -d "1212-12-12=1212-12-12&12.12.1212'.'=12.12.1212&+7 123 123 45 67=+7 123 123 45 67&aaa@bbb.ccc=aaa@bbb.ccc&smth=smth" http://localhost:5000/get_form



1) Install Prequisite libraries:
   pip install django
   pip rest
   pip psycopg2
   pip install djangorestframework

2) Local Database Connection: PostgreSQL is used
   Database Name: Vender_Management
   put below field accordingly in settings.py in 'DATABASES'
   'USER':'postgres',   //your root name
   'PASSWORD':'root123',  //yout database password

3) in cmd 3 commands needs to run 
  1. python manage.py makemigrations
  2. python manage.py migrate
  3. python manage.py runserver

4) paste below url in your browser
   http://127.0.0.1:8000/api/
   welcome page should be open

5) Vender List: here you can crete venders in this I did't used token based Authentication
6) Purchase Order List: Here I have used Tokenbased Authentication
   tip: for cheaking purpose you can comment this line "permission_classes=[IsAuthenticated]"
   from views.py

7)Index based operation can be perform in vender Details
  For this first create a vendor having vendor code example: 1
  then check this in browser:  http://127.0.0.1:8000/api/vender/1

8)For Purchase order you can create a purchase order by :  http://127.0.0.1:8000/api/PO

9)Token based Authentication is automatically performed in this code while creating user, Token automatically gets created
  1.First create a superuser
    in cmd type: python manage.py createsuperuser
    username:
    password:
    note down name and password
    now open : http://127.0.0.1:8000/admin/
    here put above username and password

  2.Now under Authentication and authorization tab click on add user
    give username and password
    and token will automatically generated which can be seen in tokens tab

  3.Check the Token based authentication in POSTMAN
    in cmd: python manage.py runserver
    open POSTMAN and paste : http://127.0.0.1:8000/api/PO/
    and send a GET requsest , you will get error as Authentication is requered
    how click on header tab in POSTMAN in placeholder of Key and Value write below
    Key: Authorization
    Value: Token {paste token which can be seen from token tab, http://127.0.0.1:8000/admin/}
    now send request now you can see the expected result.

10) http://127.0.0.1:8000/api/vender/1/performance
    here can see the calculated values from the logic
    we can see the data of 1st vender performance accouding to the purchase order list updation

    
    
    


   
   

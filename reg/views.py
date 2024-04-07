import mysql.connector as sql
from django.shortcuts import render, redirect


def signup(request):

    error_message = ""
    message = ""

    if request.method == "POST":
        connection = sql.connect(host="localhost", user="root", password="yogesh", database="cem")
        cursor= connection.cursor()

        for key, value in request.POST.items():
            if key == "email":
                email = value
            if key == "username":
                username = value
            if key == "password":
                password = value

        # Check if the email already exists in the database
        check_email_query = f"SELECT * FROM reg_signup WHERE email = {repr(email)}"
        cursor.execute(check_email_query)
        existing_user = cursor.fetchone()

        if existing_user:
            error_message = "Email is already registered. Try with a different email."
        else:
            # Insert a new record if the email doesn't exist
            message = "Account created successfully."
            insert_query = f"INSERT INTO reg_signup (email, username, password) VALUES ({repr(email)}, {repr(username)}, {repr(password)})"
            cursor.execute(insert_query)
            connection.commit()
            return redirect('/login')
    return render(request, "signup.html", {"error_message": error_message, "message": message})

def login(request):

    if request.method == "POST":
        connection = sql.connect(host="localhost", user="root", password="yogesh", database="cem")
        cursor = connection.cursor()
        
        for key, value in request.POST.items():
            if key == "email":
                email = value
            if key == "password":
                password = value

        
        # Using parameterized query to prevent SQL injection
        c = "SELECT * FROM reg_signup WHERE email=%s AND password=%s"
        # print("SQL Query:", c)

        cursor.execute(c, (email, password))
        t = tuple(cursor.fetchall())
        if t == ():
            return render(request, 'InvalidCredentials.html')
        else:
            request.session['email'] = email
            return redirect('home/')
        
    return render(request, "login.html")

def InvalidCredentials(request):
    return render(request, "InvalidCredentials.html")

def home(request):
    return render(request, "home.html")
# Todo API (Django REST Framework)

### ✏ Description
- This API is for record todo list
  - provide CRUD function
- implemented using Django REST Framework
- todo list have comments
<br>

### ⚙ Envirionments (python 3.8.0)
> pip install django==3.1.7

> pip install djangorestframework==3.12.4

> pip install django-dotenv==1.4.2

❗ And, you have to create `.env` file in root.
then, please insert secret key (you can get at https://djskgen.herokuapp.com/)
```
(in .env file)

SECRET_KEY="value"
DEBUG=True
```
<br>

### 📃 API Descriptions

<b>Todo</b>
- GET "todos/" - Todo list read
- POST "todos/" - Todo create
- GET "todos/<int:todo_id>" -Todo detail read
- PATCH "todos/<int:todo_id>" - Todo update
- DELETE "todos/<int:todo_id>" - Todo delete

<b>Comment</b>
- GET "todos/<int:todo_id>/comments/" - Comment list read
- POST "todos/<int:todo_id>/comments/" - Comment create
- PATCH "todos/<int:todo_id>/comments/<int:comment_id>" - Comment update
- DELETE "todos/<int:todo_id>/comments/<int:comment_id>" - Comment delete
<br>

### ▶ Execution
> pip install httpie
```python
python manage.py makemigrations

python manage.py migrate

# execute django web server
python manage.py runserver

# if you see error "No such table Todo", 
## python manage.py makemigrations todo
## python manage.py migrate
## python manage.py runserver

""" in another cmd """
# (GET) Todo list read
http http://127.0.0.1:8000/todos/

# (POST) Todo create
http post http://127.0.0.1:8000/todos/ title="write a todo title" description="write a todo description"

# (GET) Todo detail read
http http://127.0.0.1:8000/todos/<int:todo_id>/

# (PATCH) Todo update
http patch http://127.0.0.1:8000/todos/<int:todo_id>/ title="write a todo title" description="write a todo description"

# (DELETE) Todo delete
http delete http://127.0.0.1:8000/todos/<int:todo_id>/

# (GET) Comment list read
http todos/<int:todo_id>/comments/

# (POST) Comment create
http post todos/<int:todo_id>/comments/ contents="write a comment contents"

# (PATCH) Comment update
http patch todos/<int:todo_id>/comments/<int:comment_id>/ contents="write a comment contents"

# (DELETE) Comment delete
http delete todos/<int:todo_id>/comments/<int:comment_id>/

```
<br>

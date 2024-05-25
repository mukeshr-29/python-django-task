# python-django-task

Prerequisites                                                                                                                             
pip install django djangorestframework requests                                                                                           
python -m venv env                                                                                                                        
env\Scripts\activate                                                                                                                      
                                                                                                                                          
django-admin startproject webhook_app #anything as project name                                                                           
cd webhook_app                                                                                                                            
python manage.py startapp core                                                                                                            
python manage.py makemigrations                                                                                                           
python manage.py migrate                                                                                                                  
python manage.py runserver                                                                                                                
                                                                                                                                          
Project Structure
webhook_app/
├── core/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
├── webhook_app/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
├── manage.py


![Screenshot 2024-05-24 190022](https://github.com/mukeshr-29/python-django-task/assets/137137629/45606243-4f74-4032-9089-d4a76bb36f8f)




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

![Screenshot 2024-05-24 190119](https://github.com/mukeshr-29/python-django-task/assets/137137629/a913d71a-948b-41f0-b7df-54a1e7eb6591)

![Screenshot 2024-05-24 190022](https://github.com/mukeshr-29/python-django-task/assets/137137629/a415f3ff-b65f-4def-a2fd-910e38bc600e)

![Screenshot 2024-05-24 185932](https://github.com/mukeshr-29/python-django-task/assets/137137629/ee3037c6-c611-476e-a5f9-327af8b86414)



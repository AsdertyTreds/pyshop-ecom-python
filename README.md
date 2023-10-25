# PyShop

PyShop is an online Python Ecommerce website built with Django, SQLite and Bootstrap. A simple and lightweight ecommerce app easily deployable anywhere anytime with modules developed upon the inbuilt django admin.

# Get Started
To setup the PyShop project, here is the following guidelines:
* Clone the repository <code>https://github.com/AsdertyTreds/pyshop-ecom-python.git</code>
* Open Project folder on terminal 
* Prepare your virtual environment <code>python3 -m venv venv</code> 
* Add export SERVERNAMES to env
* Activate your virtual environment <code>source env/bin/activate</code>
* Install your requirements.txt file <code>pip install -r requirements.txt</code>
* Create migrations using <code>python3 manage.py makemigrations</code> 
* Run migrations <code>python3 manage.py migrate</code>
* Start your dev server with <code>python3 manage.py runserver</code>
* Visit your App using <code>http://127.0.0.1:8000/</code>
* Create super user to access admin dashboard using <code> python3 manage.py createsuperuser</code>
* Follow the prompts after <code>Username: , Email address: , Password: , Password (again): </code>
* Visit Admin Page using <code>http://127.0.0.1:8000/admin</code> and login with the credentials created above.
* Add Products under the <b>Products</b> Menu, Add Offers also.
* Visit Products Page using <code>http://127.0.0.1:8000/products/</code>
* Visit New Arrival (Products) Page using <code>http://127.0.0.1:8000/products/new</code>
* Testing <code>python3 manage.py test</code>
* Make lang ru (or your) <code>django-admin makemessages -l ru --ignore=venv</code>
* Compile lang <code>django-admin compilemessages --ignore=venv</code>


## Contributing
Thank you for considering contributing to this small python project! For contribution discuss, please email to Asderty Treds [asdertytreds@gmail.com](mailto:asdertytreds@gmail.com).


## Security Vulnerabilities
If you discover a vulnerability or bugs within this project, please send an e-mail to (mailto:asdertytreds@gmail.com). All bugs and vulnerabilities will be promptly addressed.


## License
The PyShop Project is free open-sourced project, yet to be licensed under the [MIT license](https://opensource.org/licenses/MIT).
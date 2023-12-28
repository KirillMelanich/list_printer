### Kirill Melanich test task for SolidWay

# List Printer
This Django application allows user to view football clubs and football coaches in list and detail mode. User also can create, update and delete any club or coach.

## Installation 
1. Clone the repository:
   ```shell
   git clone https://github.com/KirillMelanich/list_printer
   
2. Navigate to the project directory and activate virtual environment:
   ```shell
   cd list_printer
   python -m venv venv
   venv\Scripts\activate (on Windows)
   source venv/bin/activate (on macOS)
   
3. Install dependencies:
   ```shell
    pip install -r requirements.txt

4. Run migrations
   ```shell
   python manage.py makemigrations
   python manage.py migrate

5. Create superuser
   ```shell
   python manage.py createsuperuser

6. Load data from football.json file
   ```shell
   python manage.py loaddata football.json
   
7. Run server:
   ```shell
   python manage.py runserver
   
8. Enjoy your time with list_printer app!!!
FestShare
FestShare is a Django-based social platform designed to help international students reduce isolation through event-based connections. Users can create, join, and manage events to meet people with similar interests and experiences.

Features
User Profiles: Personalized profiles for each user to showcase their interests, events, and connections.
Event Management: Users can create, view, and join events.
Event Memeber Management : A user who create an event can see who are the participants and also see who are offering to sponser the program. 
CRUD Operations: Full Create, Read, Update, and Delete functionality for events and profiles.
Social Connectivity: Users can connect with others through event participation and share experiences.
Sponsership : This is mostly target to wholeseller, if someone likes some event and want to contribute they also have ability to sponser the program.The sponser message would include their name, email(or way to reach them ) and what are they offering . 


Installation
Clone this repository:

bash
Copy code
git clone https://github.com/yourusername/festshare.git
Navigate to the project directory:

bash
Copy code
cd festshare
Set up a virtual environment:

bash
Copy code
python3 -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows
Install required dependencies:

bash
Copy code
pip install -r requirements.txt
Apply migrations:

bash
Copy code
python manage.py migrate
Run the development server:

bash
Copy code
python manage.py runserver
Visit the app at http://localhost:8000.

Technologies Used
Django: Web framework for building the app.
SQLite: Database for storing user profiles and events (can be swapped for other databases).
HTML/CSS/JS: Frontend design and interactions.

License
This project is licensed under the MIT License - see the LICENSE file for details.

<br />
<p align="center">
  <h3 align="center">Exam-Portal</h3>

  <p align="center">
    A complete Exam Portal System built using Django and Bootstrap
    <br />
    <br />



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li>
      <a href="#usage">Usage</a>
      <ul>
        <li><a href="#local">Local</a></li>
        <li><a href="#deployment">Deployment</a></li>
      </ul>
    </li>
    <li><a href="#to-do">TO-DO</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
A complete Exam Portal System built using Django and Bootstrap. Currently, the portal has login system(with authentication) for admin(the top level supervisor), professors and students with their respective homepage; MCQ questions, question papers, student groups and exams can be created/edited by professors; students can appear for exams allotted to them within the time constraints set by the professor and then view their marks and solutions after completing the exam.

### Built With

Frameworks used to build the project:
* [Django](https://www.djangoproject.com/)
* [Bootstrap](https://getbootstrap.com)


<!-- GETTING STARTED -->
## Getting Started
To setup the project locally, follow the given steps:

### Prerequisites
Following software needs to be setup in the system
* [git](https://git-scm.com/downloads)
* [python](https://www.python.org/downloads/)
* [pip](https://pip.pypa.io/en/stable/installing/)
* [virtual environment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
* [github-cli](https://github.com/cli/cli) (optional)

### Installation

1. Clone the repo by
   ```sh
   git clone https://github.com/JasrajUchiha/exam-management.git
   ```
   or (if [github-cli](https://github.com/cli/cli) is installed)
   ```sh
   gh repo clone JasrajUchiha/exam-management
   ```
2. Open the project in any source code editor.
3. Activate python virtual environment.
4. Inside the virtual environment, run
   ```sh
   pip install -r requirements.txt
   ```



<!-- USAGE EXAMPLES -->
## Usage
### Local
For running the project, navigate to the project directory and follow the following instructions:

* Type the following in the command line(inside the virtual environment):
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    # this will ask for username, email(optional) and password. Enter some credentials to be used later for django admin functionality.
    python manage.py runserver
  ```

* Log on to [django admin site](http://127.0.0.1:8000/admin) using the superuser credentials
    * Click on **Groups** section and create 2 groups - ***Professor*** and ***Student***
    * Click on **Users** section and create some users, and also make each user belong to one of the groups- Professor/Student as per role
    * Logout of the admin site and go to http://127.0.0.1:8000/ where the home page of the project will be rendered.

* Now any student/professor can login using their own credentials.


##### Credentials:
| User Type      | Username | Password |
| ----------- | ----------- | -----------|
| admin      | admin       | admin |
| student   | student_1        | password_student_1 |
| prof   | prof_1        | password_prof_1 |

The admin can create more users(professors/students) from the django admin panel and can add them to corresponding groups, after which they can login through the site.

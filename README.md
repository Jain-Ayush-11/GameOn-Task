# GameOn-Task
This is a DRF based seller application APIs for the task of GameOn Internship.
<br>
# Enviornment Set-Up
Clone the Repo and create a virtual enviornment as,
 ```sh
  $ virtualenv env
 ```
Start the Virtual Env by activating it.
Once activated, install the requirements by:
 ```sh
  $ pip install -r requirements.txt
 ```
Now inside the directory, execute
 ```sh
  $ python manage.py runserver
 ```
Once the server starts, the project is running.
<br>
# Project Set-Up
Log In to the admin pannel using admin credentials either created by executing
 ```sh
  $ python manage.py createsuperuser
 ```
Enter the details asked for.
<br>
An Admin/SuperUser is already created, Log-In using
- username: admin
- password: admin1234
<br>
<img src="images/admin-login.png">
<br>
<imt src="images/admin-panel.png">
<h3> Creating Users </h3>
Once Logged Into the admin pannel, Create some users by going into the users tab.
<br><br>
<img src="images/user-panel.png">
<br>
<img src="images/create-user.png">
Two Users are already created, user1 and user2. User1 credentials:
- username: user1
- password: abcdefg12345678
<br>
<h3> Creating Auctions </h3>
Similar to creating users, create auctions.
 - No need to provide <b>Winner</b> and <b>bid</b>.
<br><br>
<img src="images/auction-panel.png">
<br>
<img src="images/auction-create.png">
An Auction is already created named Auction 1 with id=1.

# APIs

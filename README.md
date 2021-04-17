





Best brute forcing tool in python
An awsome tool to brute force any website! 

Report Bug · Request Feature

Table of ContentsAbout The ProjectFeatures
Built With
Getting StartedDependencies
Installation
Usage
Roadmap
Contributing
License
Contact
About The ProjectThis is one of my python projects which I've been working on. It is able to brute force any website and is fully customizable.

If you have any issues, head to issues.

If you have a improvement, head to Contributing

A list of commonly used resources that I find helpful are listed in the acknowledgements.

FeaturesTest if it can connect to the URL

Doesn't use the same generated password for faster results

Fully customizable

Chose different kinds of generations

A simple GUI

Counts how many times it tried

Prints out every password that was used

Built WithThis project was built with the packages below.

PySimpleGUI

Requests

Secrets

Getting StartedTo start brute forcing, you must first install the dependencies.

Dependenciespython -m pip install requests PySimpleGUI

InstallationFork the repository

git clone https://github.com/asimo10/pyforce.git

Cd to the directory

cd C://cd/to/the/clone

Run pyforce.py in python

python pyforce.py

After that, a GUI like this should pop up

UsageTo start using PyForce I recommend using XAMPP to test it. After setting up XAMPP, copy the PHP code below.

<?php

if ($_POST[usr] == "admin" and $_POST[psw] == "69"){
  print "true";
}
else{
  print "false";
}

?>
<form method="post">
  <input name="usr" type="text">
  <input name="psw" type="text">
  <button type="submit">Submit</button>
</form>

Now, all you have to do is add each info into the input boxes.

Now, all you have to do is click on the Brute Force! button to start.

After you click it passwords will start printing on the console. Now all you have to do is sit back and wait while the program is guessing the password.

If a password match, a message like below should appear and the PyForce program should stop.

69

Success!
Found password after 61 times
Username: admin 
Password: 69

Process finished with exit code 0

RoadmapSee the open issues for a list of proposed features (and known issues).

ContributingContributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are greatly appreciated.

Fork the Project

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git push origin feature/AmazingFeature)

Open a Pull Request

LicenseDistributed under the MIT License. See LICENSE for more information.

ContactYour Name - portaltree - tahirmurata83@gmail.com

Project Link: https://github.com/asimo10/pyforce

[forks-shield]    https://img.shields.io/github/forks/asimo10/pyforce.svg?style=for-the-badge 
[forks-url]    https://github.com/asimo10/pyforce/network/members 
[stars-shield]    https://img.shields.io/github/stars/asimo10/pyforce.svg?style=for-the-badge 
[stars-url]    https://github.com/asimo10/pyforce/stargazers 
[issues-shield]    https://img.shields.io/github/issues/asimo10/pyforce.svg?style=for-the-badge 
[issues-url]    https://github.com/asimo10/pyforce/issues 
[license-shield]    https://img.shields.io/github/license/asimo10/pyforce.svg?style=for-the-badge 
[license-url]    https://github.com/asimo10/pyforce/blob/master/LICENSE 
[product-screenshot]    images/image.png 

[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<p align="center">
  <a href="https://github.com/asimo10/pyforce">
    <img src="images/logo.png"/>
  </a>
</p>

  <h3 align="center">PyForce</h3>

  <p align="center">
    An awsome tool to brute force any website!
    <br />
    <br />
    <a href="https://github.com/asimo10/pyforce/issues">Report Bug</a>
    ·
    <a href="https://github.com/asimo10/pyforce/issues">Request Feature</a>
  </p>

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#features">Features</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#dependencies">Dependencies</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

## About The Project

![ScreenShot][product-screenshot]

This is one of my python projects which I've been working on. It is able to brute force any website and is fully customizable.

If you have any issues, head to [issues](https://github.com/asimo10/pyforce/issues).

If you have a improvement, head to [Contributing](#Contributing)

### Features

* Test if it can connect to the URL
* Doesn't use the same generated password for faster results
* Fully customizable
* Chose different kinds of generations
* A simple GUI
* Counts how many times it tried
* Prints out every password that was used

### Built With

This project was built with the packages below.

* [PySimpleGUI](https://pysimplegui.readthedocs.io/)
* [Requests](https://docs.python-requests.org/)
* [Secrets](https://docs.python.org/3/library/secrets.html)

## Getting Started

To start brute forcing, you must first install the dependencies.

### Dependencies

```sh
python -m pip install requests PySimpleGUI
```

### Installation

1. Clone the repository

   ```sh
   git clone https://github.com/asimo10/pyforce.git
   ```

2. Cd to the directory

   ```sh
   cd C://cd/to/the/clone
   ```

3. Run `pyforce.py` in python

   ```sh
   python pyforce.py
   ```

After that, a GUI like this should pop up

![GUI](images\gui.png)

## Usage

To start using PyForce I recommend using [XAMPP](https://www.apachefriends.org/) to test it. After setting up XAMPP, copy the PHP code below.

```php
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
```

Now, all you have to do is add each info into the input boxes.

![DemoGUI](images\demogui.png)

Now, all you have to do is click on the Brute Force! button to start.

After you click it passwords will start printing on the console. Now all you have to do is sit back and wait while the program is guessing the password.

If a password match, a message like below should appear and the PyForce program should stop.

```sh
69

Success!
Found password after 61 times
Username: admin 
Password: 69

Process finished with exit code 0
```

## Roadmap

See the [open issues](https://github.com/asimo10/pyforce/issues) for a list of proposed features (and known issues).

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Portaltree - [GitHub Profile](https://github.com/asimo10) - <tahirmurata83@gmail.com>

Project Link: [https://github.com/asimo10/pyforce](https://github.com/asimo10/pyforce)



[forks-shield]: https://img.shields.io/github/forks/asimo10/pyforce.svg?style=for-the-badge
[forks-url]: https://github.com/asimo10/pyforce/network/members
[stars-shield]: https://img.shields.io/github/stars/asimo10/pyforce.svg?style=for-the-badge
[stars-url]: https://github.com/asimo10/pyforce/stargazers
[issues-shield]: https://img.shields.io/github/issues/asimo10/pyforce.svg?style=for-the-badge
[issues-url]: https://github.com/asimo10/pyforce/issues
[license-shield]: https://img.shields.io/github/license/asimo10/pyforce.svg?style=for-the-badge
[license-url]: https://github.com/asimo10/pyforce/blob/master/LICENSE
[product-screenshot]: images/image.png

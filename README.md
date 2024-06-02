# Admin Crawler v1

Admin Crawler v1 is a Python script designed to search for admin panels on a website using a predefined wordlist.

## Table of Contents

- [About the Project](#about-the-project)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## About the Project

This script is designed to crawl a website and search for admin panel URLs based on a given wordlist. The script prints the results to the console, indicating whether an admin panel is found or not.

## Prerequisites

Before running this script, ensure you have Python and `pip` installed on your system. Also, make sure to install the `requests` and `colorama` libraries by running the following command:

```bash
pip install requests colorama

Installation

	1.	Clone this repository:

git clone https://github.com/username/admin-crawler.git
cd admin-crawler

	2.	Ensure you have a wordlist.txt file in the same directory as the script. This file should contain a list of paths to search for the admin panel, one per line. Example:

admin/
admin/login/
admin/index.php
admin/panel/

Usage

To run the script, use the following command in the terminal:

python admin_crawler.py

Then, enter the URL of the website you want to crawl when prompted. The script will attempt each path from the wordlist as part of the URL and print the results to the console.

Contributing

If you would like to contribute to this project, please follow these steps:

	1.	Fork this repository
	2.	Create a new branch (git checkout -b your-feature)
	3.	Commit your changes (git commit -m 'Add your feature')
	4.	Push to the branch (git push origin your-feature)
	5.	Create a Pull Request

License

This project is licensed under the MIT License - see the LICENSE file for details.

Contact

Created by solos - solos@tutamail.com

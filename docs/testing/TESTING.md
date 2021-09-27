# Testing

View live version of the website [here](https://f1-weather-v2.herokuapp.com/).

Milestone Project 4: Full Stack Frameworks with Django – [Code Institute](https://codeinstitute.net/)

In this document you will find information about the testing procedures that I have used to make sure the website displays and functions correctly on most browsers and devices.

---

## Contents

- [**Browser compatibility**](#browser-compatibility)

  - Tested browsers and devices
  - What I tested
  - Browser compatibility testing results

- [**Mobile responsiveness**](#mobile-responsiveness)

- [**Code validators**](#code-validators)

  - W3C - Markup Validation Service
  - W3C - CSS Validation Service
  - JSHint - JavaScript code quality checker
  - Python checker - Python code syntax checker
  - PEP8 online - Python code style checker

- [**Test cases**](#test-cases)

- [**Testing user stories**](#testing-user-stories)

- [**Bugs**](#bugs)

  - Solved bugs
  - Known bugs

---

## Browser compatibility

### Tested browsers and devices

I tested these browser versions on these devices:

**Desktop PC (64-bit, Windows 10):**

- Google Chrome Version 94.0.4606.61 (Official Build) (64-bit)
- Firefox Version 92.0.1 (64-bit)
- Microsoft Edge Version 94.0.992.31 (Official build) (64-bit)

**Dell E7240 laptop (64-bit, Windows 10):**

- Opera Version 79.0.4143.66 (64-bit)

**Samsung Galaxy S7 (Android Version 8.0.0):**

- Samsung internet Version 13.2.2.4
- Brave Browser Version 1.23.76

### What I tested

List of things that I tested:

- If elements display correctly in size and order
- If images display correctly
- If all the (internal) links work
- If hover effects work
- If the JavaScript functionality works
- If the Python functionality works
- In general I tested the entire website, to see if it displayed and worked as intended.

### Browser compatibility testing results

**Google Chrome Version 94.0.4606.61 (Official Build) (64-bit):**

Everything is working and displaying as intended. [(screenshot)](testing-img/chrome.png)

**Firefox Version 92.0.1 (64-bit):**

Everything is working and displaying as intended. [(screenshot)](testing-img/firefox.png)

**Microsoft Edge Version 94.0.992.31 (Official build) (64-bit):**

Everything is working and displaying as intended. [(screenshot)](testing-img/edge.png)

**Opera Version 79.0.4143.66 (64-bit):**

Everything is working and displaying as intended. [(screenshot)](testing-img/opera.png)

**Samsung internet Version 13.2.2.4:**

Everything is working and displaying as intended. [(screenshot)](testing-img/samsung.jpg)

**Brave Browser Version 1.23.76:**

Everything is working and displaying as intended. [(screenshot)](testing-img/brave.jpg)

**_[Back to top](#contents)_**

---

## Mobile responsiveness

I've applied completely custom media queries throughout the website to achieve mobile responsiveness. To test the website for mobile responsiveness I've been using the Google Chrome devtools throughout the coding of the media queries. I manually used the sliders to adjust for different screen sizes, and I've also used all the pre-configured screen sizes in the devtools to test if things looked okay, both in vertical and horizontal directions. Another thing I usually do is use [responsive design checker](https://responsivedesignchecker.com/) and [ami responsive design](http://ami.responsivedesign.is/) for some additional mobile responsiveness testing throughout the building of the website, but for some reason I couldn't display the website on there. My guess is that the HTTPS protocol prevents this, while previous projects used the HTTP protocol which has less security built in.

**_[Back to top](#contents)_**

---

## Code validators

### W3C - Markup Validation Service

I've put the HTML code through the [W3C markup validator](https://validator.w3.org/), and I only got Django syntax related errors that should be ignored. There were also two errors or so in the stripe payment element code, but I'm not going to mess around with that and risk breaking the functionality.

### W3C - CSS Validation Service

I've put my base.css file through the [W3C CSS validator](https://jigsaw.w3.org/css-validator/) and it passed without errors on the second try, after removing some unnecessary text-justify styling.

### JSHint - JavaScript code quality checker

I've put my main.js file through the [JSHint validator](https://jshint.com/) and it gave no warnings or errors.

### Python checker - Python code syntax checker

I've checked my Python code syntax on the [extendsclass website](https://extendsclass.com/python-tester.html), and I got no errors at all.

### PEP8 online - Python code style checker

I've checked my Python code style to fit the PEP8 guidelines with the Visual Studio Code built in flake8 checker, and on the [PEP8online website](http://pep8online.com/). I'm getting some errors/warning about standard Django imports being unused like `from django.contrib.auth import get_user_model`, but I'm leaving them in because it's probably there for a reason. I'm also getting some warnings for trailing whitespace in multi-line comments which can be ignored, it's just a preference thing. In settings.py there are some 'line too long' errors in the `AUTH_PASSWORD_VALIDATORS` array, which can't be fixed because pushing them down the line is still too long and you can't break them up in smaller lines. In premium/views.py there is an error about unused variable 'charge' but that one is necessary for Stripe payments functionality.

**_[Back to top](#contents)_**

---

## Test cases

placeholder

**_[Back to top](#contents)_**

---

## Testing user stories

placeholder

**_[Back to top](#contents)_**

---

## Bugs

### Solved bugs

placeholder

### Known bugs

placeholder

**_[Back to top](#contents)_**

---

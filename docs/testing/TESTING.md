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

### General features

1. Header:

   1.1 The header will be visible at the top of the page.

   1.2 The header should be sticky.

   1.3 The header should have text/logo in the center.

   1.4 The header should have a hamburger menu icon on the left that turns into a cross and opens the sidenav when clicked.

---

2. Sidenav:

   2.1 The sidenav should have a cross in the top left when opened, clicking it will close the sidenav.

   2.2 The sidenav should have internal links to the home page, calendar, profile, premium, login, or logout pages dependent on whether a user is logged in or not.

---

3. Footer:

   3.1 The footer will be visible at the bottom of the page.

   3.2 The footer should have an external link to the weather API provider.

---

### Homepage

4. Homepage:

   4.1 The homepage should have a div with a welcome message and a button with an internal link to the calendar page.

   4.2 The homepage should have a div telling the visitor to register and mentions buying premium membership to access additional weather data. This div also has a button with an internal link to the register page.

---

### Calendar page

5. Calendar page:

   5.1 The calendar page should have cards for each of the (remaining) Formula 1 calendar events.

   5.2 Each card shows the event date and location.

   5.3 Clicking on active cards takes you to the single event page for the selected event.

---

### Single event page

6. Single event page:

    6.1 The single event page should have a wide div that displays the country flag for the selected event and the track name.

    6.2 The single event page should have a card with an internal link to the hourly forecast page.

    6.3 The single event page should have a card with an internal link to the daily forecast page.

---

### Hourly forecast page

7. Hourly forecast page:

    7.1 The hourly forecast page should only be accessible for users with a premium membership.

    7.2 The hourly forecast page should have a wide div that displays the country flag for the selected event and the track name.

    7.3 The hourly forecast page should have a wide div that could in the future display the local time of the event location.

    7.4 The hourly forecast page should have a div with the event schedule which includes all the local starting times for each session.

    7.5 The hourly forecast page should have twenty-four cards that could in the future display weather data for the selected event, one card for each hour of the day.

---

### Daily forecast page

8. Daily forecast page:

    8.1 The daily forecast page should have a wide div that displays the country flag for the selected event and the track name.

    8.2 The daily forecast page should have a wide div that could in the future display the local time of the event location.

    8.3 The daily forecast page should have a div with the event schedule which includes all the local starting times for each session.

    8.4 The daily forecast page should have five cards that could in the future display weather data for the selected event, one card for each of the next five days.

---

### Premium page

9. Premium page:

    9.1 The premium page should only be accessible for logged in users who don't have a premium membership yet.

    9.2 The premium page should display the logged in user their email address.

    9.3 The premium page should have an element for executing a Stripe payment to purchase premium membership.

---

### Profile page

10. Profile page:

    10.1 The profile page should only be accessible for logged in users.

    10.2 The profile page should display the logged in user their email address.

    10.3 The profile page should display the logged in user their premium membership status.

---

### Error pages

11. Error pages:

    11.1 The error pages should display the error HTTP status code.

    11.2 The error pages should have text saying "Back to home page", with an internal link to the home page.

---

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

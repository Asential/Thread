# THREAD

A news-discussion website.

I decided to create a forum based website, which only focuses on the current headlines for my final project. The idea is to provide a place where people can discuss whats going on & get informed as well. To do so, the website needs to stay updated constantly and focus only on the current news, hence the users are limited to a certain amount of posts.

------------------------------
## Work-Flow

You will find my general work-flow as follows:

1. I used newsapi.org's API to get the information for Indian news, which I then display after converting it. The api.py file is used for this purpose which returns JSON encoded data. I then display the data properly using HTML & CSS as the index.html of the website. Up to here, the work was relatively simple.

2. To create threads unique to the news headlines, I needed to store & filter them when needed. The problem here was that the API did not provide any unique identification for the headlines which leads to them being hard to distinguish when storing in models. I thought about storing the headlines themselves but there could be a case where two headlines are very similar. To overcome this problem, I passed the URL of each of the headlines, along with their topics to create separate objects for them. These URLs are the ones linking to the Article of the topic, so they have to be unique. So whenever a user clicks on a headline in the index page, the views.py file checks the headline's URL to the ones in the models, gets the comments if there are any & then displays them on the topic.html . This was not the tidiest of work, but it took me quite a bit to figure it out & it worked well in the end.

3. Next I implemented discussion forms and comments. The main problem here was to create nested discussions so as to allow people to have proper debates. I tried to implement this through my view.py file but later found out that it would be much cleaner to do so using Django's Template Language only, through recursion. First I made my Comment Model, which would store all the usual data, along with the parent Foreign Key which would be used for nesting. Then, I made the comments.html file which calls itself after passing different parameters for the parent comments. This was basically the heart of the project. Once I had managed to get it to display the comments without repetition, I polished the forums for a clearer view as to who is replying to whom.

4. I added forms through JavaScript which are displayed if the user clicks on the Reply button & hidden if they Cancel it. I then focused on making the website mobile responsive, for which I used the @media query. I changed the nav-bar style for mobile users to make it cleaner along with removing pictures and changing font size.

5. The Django's Login/Register system was also used for the user management. I also added the Admin Interface to moderate comments & topics.


------------------------------
## File Details


### PYTHON FILES (With any kind of modification other than defaults)

- **api.py** - Contains the function for returning JSON encoded data from the API request. It is called each time the website's Index page is loaded.
- **views.py** - Contains the following functions
   - index: Loads the index page with the headlines.
   - login_view, logout_view, register_view: Django's Login/Register feature.
   - topic: Called whenver a user clicks on a headline. It checks if the headline exists as an object by comparing the URLs. If it finds a model, it loads the previous comments on the topic, if any. Otherwise it creates the object
   - comment: It gets the topic and comment data & creates a comment object.
   - reply: It does the same function as comment, but for replies.

- **urls.py** - It contains the various routes for transferring information.

- **admin.py** - It contains the admin registration for the models.


### TEMPLATE FILES (HTML)

- **layout.html** - The layout file which is extended to other html files. It contains two navigation divisions for mobile responsiveness.
- **login.html** - It is the Login page.
- **register.html** - It is the Register page.
- **index.html** - It contains the API's headlines which contain the discussions.
- **topic.html** - It contains the link to the article in reference along with all the comments made on the topic.
- **comments.html** - It is used to display comments & is called recursively to display nested comments.


### STATIC FILES (CSS & JS)

- **main.css** - Contains all the CSS settings for the website, save a few, including the mobile responsiveness settings.
- **mobilemenu.css** - It contains the CSS for the Interactive menu for the mobile navigation bar.
- **hover.css** - It contains the CSS for the hover effect on the links.
- **mobile.js** - It contains the JS for the navigation bar on mobile.
- **reply.js** - It stores the JS for the form effects on topic.html page.


------------------------------
## The Reasoning for My Choice of Project

My main goal was to try and include everything I was taught during the course into a single project. I believe that the attempt to make all the different things taught, work together would be difficult & complex enough for me as well as the project. From basic CSS & HTML taught in the first project to recursion in HTML & JavaScript front-end, everything has been covered in this project, where the previous projects would be around a single topic only. I am hoping that this will be good enough to satisfy the requirements for the projects & be a good demonstration of my learning, even though my creativity is somewhat limited when thinking of ideas for websites.

------------------------------

Thank you for your time & this course.
I hope you have a wonderful day!

Dhruv

# **GEMS OF PARIS**

## **Introduction**

Gemsofparis is an E-commerce web application that ticks every single boxes of a fully functional E-commerce application criteria. This application was developed based on the fundamentals of a digital business strategy with the use of a powerful and advance web application frame work Django to build a scalable, responsive and powerful web application. However, the aim and objective of Gemsofparis is to serve web owners and web users with a digital marketing platform and ease of doing businesses online, also to build strong business relationships between consumers and e-commerce service providers, an e-commerce application is categorized into two  namely: 
  - 1. Business to Business B2B. 
  - 2. Business to Consumer B2C.

  ### **More About the application**

This  web application is an e-commerce web application which provides services digitally to consumers or users of the application, so it is  categorized a B2C web application in the sense that it’s services is based on a business to customer relationship, it’s a fully functional E-commerce web application  that deals in varieties of gemstones accessible accross the globe making it possible for purchasing a gemstone of your choice online and get it delivered to your doorstep with a fast and secure delivery system, some of the available gemstones are  Diamonds, Emeralds, Sapphires to name a few. To gemstone lovers who are keen about the originality and detailed history of what their customized jewellry is made of this E-commerce application is user friendly and with a functional , secure, with an accessible, easy to use and  responsive user interface.


![](/README_DOC/responsiveness.jpg)
**NB: Please Note**: The data on the website is for educational purposes only.

[Here is the link to the live version](https://gemsofparis.herokuapp.com/)

## Table of Contents

- [**Introduction**](#introduction)
  - [**About the application**](#about-the-application)
- [**UX (User Experience)**](#ux-user-experience)
  - [**User Stories**](#user-stories)
- [**Design Choices**](#design-choices)
  - [**Typography**](#typography)
  - [**Colour Scheme**](#colour-scheme)
  - [**Wireframes**](#wireframes)
- [**Features**](#features)
  - [**Site Navigation**](#site-navigation)
  - [**Customized Error Handling**](#customized-error-handling)
  - [**Responsive Design**](#responsive-design)
  - [**Defensive Design**](#defensive-design)
- [**Database Schema**](#database-schema)
- [**Technologies**](#technologies)
  - [**Languages**](#languages)
  - [**Frameworks**](#frameworks)
  - [**Libraries**](#libraries)
  - [**Tools**](#tools)
- [**Manual Testing**](#manual-testing)
- [**Bugs**](#bugs)
  - [**Bugs fixed**](#bugs-fixed)
  - [**Known Bugs**](#known-bugs)
- [**Deployment**](#deployment)
  - [**Running Locally**](#forking-the-gitHub-repository)
- [**Web Marketing & Business**](#web-marketing-&-business)
- [**Credits**](#credits)
  - [**Media**](#media)
  - [**Acknowledgements**](#acknowledgements)


## **User Stories**

#### **View products and Navigation**
*****************************

- As a user I can be able to view a list of products so that I can choose what to buy.

- As a user I can be able to view each product details so that I can See the price, item description, item images, item rating and sizes.

- As a user I can be able to see deals and special offers so that I can have the chance to save on items I of my interest to buy.

- As a user I can be able to view my purchase total with ease at any given time so that I do not overspend.

- As a user I can be able to like products so that I can view them later in my wishlist.

- As a user I can be able to navigate around the website with ease.

- The Website homepage is equiped with different functionlity which allows a user to navigate around the website right from the homepage , the presence of the shop now button on the carousel gives a direct access into the list of products available for sale. 

#### **Registrations and Authentications**
*****************************************

- As a/an Site User I can be able to register an account with ease so that I can have an account that allows me to have a private profile.

- As a Site User I can be able to signin and signout easily so that I can **my personal account informations and update my profile.

- As a Site User I can be able to **recover my forgotten password with ease so that I can gain access to my account.

- As a Site User I can be able to receive a confirmation email after registration so that I can be rest assured my registration was successful.

- As a Site User I can be able to customize my user profile so that I can view my order history,confirmation and able to securely save my payment information and addresses on my profile.


#### **Search and Filter**
*********************************

- As a  user I can search for products through the help of the search bar located at top of the navigation system. To view product information, users only click on the product and every detailed information about the product will be displayed for readablitiy. A Users can search for  products by name or by keyword using the search functionality provided at the top of the page. The product display page can be further narrowed down by searching products by category, Price, Alphabetically or by product rating.

- As a user I can be able to filter through available products so that I can identify best rated, best priced and filter products categorically.

- As a user I can be able to filter through products categorically so that I can **find the best priced, highly rated product in a specific category or filter products in that category by name.

- As a user I can be able to filter numerous categories of products simultaneously so that I can find the best priced or highly rated product across broad categories, such as "apparel" or "homeware".

- As a user I can be able to search for item by name or description so that I can locate the item I want to buy.

- As a user I can be able to view my searh results and what I have searched for so that I can easily see if the search product is available.

#### **Shopping Bag**
*********************
- As a user I want to add product to shopping bag So that I can can complete my purchase.

#### **Favorite**
******************
- As a user I want to add product to my wish list so that I can save items of my interest for later purchases.

#### **Purchase Quantity**
*************************
- As a user I want to increase or decrease the quantity of product to be purchased So that I can I do not under buy or over buy what I need.

- As a user I can be able to **choose the size and quantity of a product when making a order so that I can carefully select item size or quantity without mistake.

#### **Checkout**
*****************
- As a user I can be able to view the content of my shopping bag so that I can keep track of the total cost of my order and what to receive.

- As a user I can be able to modify the contents of my shopping cart so that I can make changes before final checkout.

- As a user I can be able to enter my payment information with ease so that I can checkout easily without delay.

- As a user I can be able to have a sense of security that my personal data is well protected and secure so that I can feel at ease to enter my information without feeling insecure.

- As a user I can be able to **view an order confirmation after checkout so that I can be sure that no mistake was made on my order.

- As a user I can be able to get an email confirmation of my order after checkout so that I can keep track my order record and purchases.

#### **Payment**
****************

- As a user I can be able to complete my order with a friendly payment system.

- As a user I want to make payment So that I can successfully complete my order.

#### **Security**.

- As a user I can be rest assured that I can feel secure  when putting my informations on the website.
- As a user I want to feel protect So that I can feel a sense of security.

#### **Management**
*******************

- As a/an Store Owner** I can be able to Add, Edit/Update and Delete products/items so that I can Add new Items, Change/Edit product prices, modify product descriptions, edit images, Remove/Delete items/Products that are out of stock.

- As a admin or product owner I want to keep track of activities So that I can manage the website.

#### **Newsletter**
*******************

- As a user I can subscribe to the website news letter so that I can have a first hand information and updates on products, deals, news and special offers.

- As a user I want to be able to subscribe to email newsletter So that I can read about the news and offer from the website.
#### **Support**
*****************
- As a User I want to have access to customer support So that I can contact the support team for swift assistance on different scenarios that could occur.


## **UX (User Experience)**

[Back to contents](#table-of-contents)


## **Design Choices**

### **Typography**

- The website has a user friendly navigation system with colors and contrast well thought to give the user a friendly color ,font and contrast experience.


- The website logo was personally designed to suite the website purposes.

![](/README_DOC/website_logo_white.png)

### **Colour Scheme**

The colors used in this project are:
- (#FFFFFF) - White
- (#000000) - Black
- (#FFEA00) - Yellow
- (#96DED1) - Robin Egg Blue
- (#F33A6A) - Red

  - The choice of color combination used provided a unique, warm and beautiful outlook to the website.

### **Wireframes**

![](/README_DOC/Wireframe.jpg)

  - The application wireframe using Figma:
  

[Back to contents](#table-of-contents)
## **Features**

### **Site Navigation**

  - The web application has numerous ease of access functionality for easy navigation through
    the navigation bar.
  ![](/README_DOC/navigation_bar.jpg)

#### Registertion
  - Users can register/Signup to make a personalized account by clicking on the user icon located on the top right of the navigation bar, there is a drop down menu which instructing the user of either login as an existing user or register as a new user by filling up the registration form with neccessary details i.e username, email address and password.

  ![](/README_DOC/Registration.jpg)

#### Log In, Log Out to and from Account
  - As stated above registered users can securely log in and out using the login/logout buttons on the navigation bar.

  ![](/README_DOC/login_link.jpg)

#### View, Search and Sort Products 
  - Located on the main page i.e application home page is a carousel picture slider which displays some products that are on sale , under the carousel capiton you can find a SHOP NOW button in yellow color  which when clicked navigates to the products list. On clicking on a product image, a detailed information about the product will be displayed to the user, the detail information contains Product name, Category, Rating, prices.

  - with the help of the navigation search box positioned at the middle of the navigation bar,a user can search for products by name or by keyword. 

  - Users can filter or narrow their search by filtering results by category, sort by price, sort in alphabetical order i.e A-Z, or filter prices by Low to High or vice versa.

![](/README_DOC/view_search_sort.jpg)


#### Product details Update
  - Products can be added to bag either a registered or non-registered user once a user navigates to the product details page. Item quantity increase and decrease button can help the user edit the quantity of items to be added to the shopping bag.

![](/README_DOC/product_detail.jpg)

#### User information, Email confirmation and Payment
  - Either a User is registered or not, the user can still checkout regardless of status, user can choose to store their information on their profile or not, generally orders can be completed regardless of the user status, the user will be directed to the appropriate payment page where the order can be completed, if successful an email confirmation is automatically sent to the provided user email address.

  ![](/README_DOC/user_info.jpg)

  ![](/README_DOC/email_confirmation.jpg)

  ![](/README_DOC/payment.jpg)

#### Profiles 
  - A user can Create, Modify, Edit or Update the informations or previously stored data on their personal profile.

#### Admin or Superuser
  - only an authorized personel can have access to the Admin page, as the web application security could be breached from an un-authorized access by infiltrators. However, to gain access to the Admin area an back slash is added to the URL of the web application, which will prompt an authorized login details.

  If the Admin login was successful:
  -  A Superuser can Create, Read, Update and Delete product.
  -  A SuperUser can manage orders and authorize orders and restric suspicious users or cancel a suspicious order.
  - SuperUser can maintain the website and make sure everything is up and running.

    ![](/README_DOC/admin_1.jpg)
    ![](/README_DOC/admin_2.jpg)
    ![](/README_DOC/admin_3.jpg)

### Customized Error Handling

 - To handle the 404 error, a 404 error handling page was created incase there was a 404 error
 which the soul purpose is to direct the user back to the homepage or product page.

  ![](/README_DOC/404error_test.jpg)

 - In case of a server error , a 500 error page was created to handle the error and redirect users back to the homepage.

### Newsletter

  - The Newsletter app allows user to subscribe and unsubscribe to newsletter, mailchimp marketing API was integrated to handle the subscription email contacts on the mailchimp server.

  - As a user I can be able to

  - subscribe to newsletter

  - unsubscribe from newsletter

  ![](/README_DOC/subscribe.jpg)

  ![](/README_DOC/unsubscribe.jpg)

### Shipping

  - Information about the shipping , delivery and return policies.

  ![](/README_DOC/shipping.jpg)


### Responsive Design

- This application was tested on all modern available devices, redering perfectly and adjusting to different screen sizes of each and every device it was tested on.

### Defensive Design

 - @login_required

   -  Addition of the login required decorator to separate a user from some of the website functionality i.e a user cannot use the favorite function if not logged in, also a user cannot modify any details in his or her profile without login in and finally a user cannot access a superuser section of the website or superuser features.

 - Form Validation

   - Forms can only be submitted if the required information is supplied correctly.

 - Unauthorised Attempts

    - Any unauthorized attempt on the web application environment will raise a 404 error.

 - For security reasons an env.py file was created to enable environment consent and chose what environmental variables, api keys should be ignored in the github commits.



[Back to contents](#contents)
 
### Database Schema

  - AWS: A cloud-based database that stores fields for products, users, orders.

  - PostgreSQL: PostgreSQL was used for fixtures categories.json and products.json  
  

  Below is the ER Diagram:

![](/README_DOC/DatabaseER.png)

  

[Back to contents](#table-of-contents)
## Technologies
    
## **Languages

  - HTML5
  - CSS3
  - JavaScript
### **Frameworks**

- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)

[Back to contents](#table-of-contents)

### **Tools**
  - [Canva](https://canva.com/)

  - [GitHub](https://github.com/)
  
  - [Gitpod](https://www.gitpod.io/)
  
  - [Heroku](https://www.heroku.com/home)

  - [AWS](https://aws.amazon.com/)

  - [Stripe](https://stripe.com/)

  - [Google fonts](https://fonts.google.com/)

  - [Htmlcolorcodes](https://htmlcolorcodes.com/)
  
  - [Lighthouse](https://developers.google.com/web/tools/lighthouse)

  - [Website Mockup Generator](https://websitemockupgenerator.com/)

  - [JSHint](https://jshint.com/)

  -  [Figma](https://figma.com/)
  
  -  [Mailchimp](https://mailchimp.com/)

  - [PEP8 Online](http://pep8online.com/)

  - [W3C Markup Validator](https://validator.w3.org/)

  - [Jigsaw Validator](https://jigsaw.w3.org/css-validator/)

  - [web page mobile friendly ](https://www.google.com/search?q=mobile+friendly+test/)

  - [Lucidchart](https://www.lucidchart.com/pages/)

[Back to contents](#table-of-contents)

## Manual Testing

  ## Home Page

  ![](/README_DOC/home.jpg)

  - The web application homepage header consist of the following.
    - Navigation bar located at the top-most part of the page, spanning from left to right.

      ![](/README_DOC/Navigation.jpg)

    - Company logo and logo font located at the left-most part of the navbar.

      ![](/README_DOC/company_logo_and_logo_font.jpg)

    - Search box situated at the middle of the navigation bar, The user can utilise the search bar in the header area to look up products. By entering different keywords, brand or sku, the search bar will provide a filtered list of results for those that do.

      ![](/README_DOC/search.jpg)

    - The User, Favorite and shopping bag icons can be found at the right-most part of the navigation bar. The User can login and existing account or register a new account using the my account functionlity. Also users can add,remove and view items in their favorite list. The bag contains the added items to purchase.

      ![](/README_DOC/user_fav_bag.jpg)

    - Present on the homepage body is the carousel functionality of image slider which serves as Hero image   but with a dynamic functionality with a SHOP NOW button to navigate to the product display area.

      ![](/README_DOC/hero.jpg)

    - The footer area is located at the bottom-most part of the homepage made up of Newsletter, Shipping, Payment, customer support, Social media and Copy right.

      ![](/README_DOC/footer.jpg)
 

    - The homepage footer also includes a newsletter signup  and customer support.

      ![](/README_DOC/newsletter.jpg)

      ![](/README_DOC/contact_us.jpg)


 ## Products

 - The user is presented with a list of products from the products page, each of which includes an image, the product name, category, price, brand, and rating. The top left corner also shows the overall number of goods. Using the filter bar in the upper right corner, the user can also continue to filter the products. The user can choose the headline choice and the level of filtering specificity from the dropdown menus to filter for particular categories.

      ![](/README_DOC/products.jpg)


 - By clicking on add item to bag, a pop up notification shows on bag that an item as been added to the bag, which the User could access by clicking on the bag to check the added item to update the bag by increasing or decreasing the quantity of items or by removing the item.

      ![](/README_DOC/add_to_bag.jpg)


 ## Checkout 

 - The user will be asked to provide the delivery details along with the complete list of the purchase's items. The "Adjust Bag" button allows the user to return to the shopping bag and make additional changes. Otherwise, the user may choose to pay by clicking the "Complete Order" button. Through Stripe, which uses a secure way, the payment is handled.

      ![](/README_DOC/checkout.jpg)
    

      ![](/README_DOC/check_out_details.jpg)

 - The user is redirected to the confirmation page, where the order confirmation is displayed, after the order has been submitted.

      ![](/README_DOC/purchasedetails.jpg)

      ![](/README_DOC/order_successful.jpg)

 - E-mail confirmation will be sent to the supplied emailaddress


### Register

  - Here is a detailed registration form which will allow users to create a personalized account.

  ![](/README_DOC/user%20register.jpg)

### Login and Logout

  There were several attempts to log in and out. It performed as intended.

  ![](/README_DOC/singin.jpg)

### E-Commerce App Testing 

- Functional Testing
  - Checking a web application’s requested functionality in the area of basic usability, its mainline functions, and accessibility is known as functional testing. BVA, decision table testing, and equivalence class testing among many other methods, may be used to create functional test cases for online applications.

The following test cases are a few of many test cases that can be considered for checking the functional testing:

- User Interference testing
  - Navigation Testing:
    - All internal and external links are tested for functionality during the navigation process. Websites must be tested for their ability to deliver reliable, well-organized links, as well as other navigational choices like site maps and search engines. The following checklist can be considered for navigation testing of an e-commerce site:
        - 1.	Check every link on the site.	An appropriate page should open.
        - 2.	Click on the back button 	An appropriate page should open.
        - 3.	Click on every link to see how the material appears on each web page.	The website’s contents    can effectively be read since appropriate horizontal and vertical scroll bars are available.

  - Form-Based Testing:
    - Forms on websites must be tested to ensure that all fields function properly. These types of forms on e-commerce sites can be seen while the user is registering or when the user is filling in billing and shipping details. Form-based testing checks the following concerns: 

      - Correct use of the tab key to go from one form field to another.
      - Verifies that the data submitted in the form is in the correct format. 
      - Verifies that all necessary fields are filled out on the form.

- Security Testing
  - Security is the process of protecting data from numerous attacks. When interacting across a network, it is necessary to secure sensitive and critical information and data. The user wishes to have a safeguard in place to protect personal, sensitive, and financial information. We want data that is accurate, dependable, and secure against illegal access.
    - Authentication: Is the data sent by an authorized user?
    - Access Control: Is data secure against unauthorized users? 
    - Transparency: Does the user receive exactly what is sent? 
    - Delivery: Is the information reaching the intended recipient? 
    - Reliability: How frequently does a failure occur? How long does it take for the network to recover after a failure?

- Browser compatibility Testing:
  - There are several browsers available, and each of them behaves differently. Although testing the web application with all browsers is impracticable, it is vital to validate the web application with defined and prioritized platforms to assure proper operation. A browser compatibility matrix may be developed to test the web application on multiple browsers.

- Load and stress Testing
  - Stress testing is running a web application under more than maximum and changing loads for extended periods of time. Unlike performance and load testing, stress testing assesses the system’s response when it is subjected to a load that exceeds its defined limitations. It is also used to monitor and test the dependability of a web application when available resources are being exploited beyond their maximum capacity. The system’s behavior is observed to identify when the system under stress test fails and how it recovers from the failure.

  - Load testing comprises simulating several users accessing the web application at the same time to test the web application under real-world conditions. It puts the web application through its paces by overloading it. Load testing plans should be developed as early as practicable in the software life cycle. Load testing includes the following measures to guarantee adequate performance during peak hours.

- Database Testing
  - E-commerce is database-driven, it is critical that these apps function effectively and protect the user’s sensitive data, such as personal information and credit card information. Data-centric web applications must be tested to ensure error-free functioning and greater client satisfaction. Consider the following scenario: you want to buy something from an online retailer. When a user does a search using keywords and pricing preferences, the database server generates a database query. If the query does not take into account the customer’s price choices owing to a programming error, the results will be incorrect. During database testing, several types of defects must be verified and eliminated.

### Features tested in this web application

  - Home page: The links to important pages should be visible and functional, correct images and text are visible on the main page.

  - Payment function: At this step, security testing comes into the picture. A number of variables need to be tested here like Debit/ Credit card details, can the customer pay in installments, the generation of order confirmation and receipt, etc.

  - Order processing mechanism: At the time of placing the order, the users should be able to select the preferred shipping method, the address should be correctly mapped to the order, etc.

  - Product Catalog: All the products should be clearly listed on the site with all the explanatory images, clear product descriptions, images should be of good quality, Add To Card option should be easily visible, etc.
  
  - Search engine: Users should be able to search the desired product seamlessly and should be directed to the exact product page, should be able to navigate to important sections like product categories, cart, etc with few clicks. 

- [W3C HTML Validator](https://validator.w3.org) 
  - 400.html
  - 403.html
  - 404.html
  - 500.html
  - add_product.html
  - bag-total.html
  - bag.html
  - base.html
  - checkout-buttons.html
  - checkout.html
  - checkout_success.html
  - contact.html
  - edit_product.html
  - email.html
  - email_confirmed.html
  - footer.html
  - index.html
  - login.html
  - logout.html
  - main-nav.html
  - message.html
  - mobile-top-header-one.html
  - product-image.html
  - product-info.html
  - product_detail.html
  - products.html
  - profile.html
  - quantity-form.html
  - shipping.html
  - signup.html
  - subscribe.html
  - unsubscribe.html
  - wishlist.html


- [W3C CSS Validator](http://jigsaw.w3.org/css-validator/)
  - base.css
  - responsiveness.css
  - profile.css
  - footer.css

    ![](/README_DOC/W3C_testing.jpg)
### Other testing 
- This application was tested to meet with the requirements of all modern devices, it is responsive.

    ![](/README_DOC/google_mobile_test.jpg)



### Bugs fixed

- There was a checkout issue when making the final payment, and was fixed

### Un-fixed Bug 

- There was a layout gap on both sides the navigation bar


[Back to contents](#table-of-contents)

## Deployment

### Deployment to Heroku

This project was deployed to [Heroku](https://www.heroku.com/). Below is a step by step deployment process:

1. Go to Heroku website and register as user
2. Create a new app
3. Navigate to the "Resources" tab and search for Heroku Postgres.
4. In order to use PostgreSQL, both packages `dj_database_url` and `psycopg2` have to be installed on Gitpod.
5. Import `dj_database_url` into the project's [`settings.py`](/gem_master/settings.py) to setup new database.
6. Disable the default database(SQLite) in the project's [`settings.py`](/gem_master/settings.py) and add the PostgreSQL database URL stored in the variable `DATABASE_URL`(can be found by clicking on the "settings" tab followed by clicking on "reveal config vars") in order to connect to PostgreSQL.
7. Run migrations (due to the use of PostreSQL) on Gitpod.

    ```
    $ python3 manage.py migrate
    ```

8. Load data (Categories and Products JSON files in the [`fixtures`](/products/fixtures) folder).
- Load categories first 

    ```
    $ python3 manage.py loaddata categories
    ```

- Then load products

    ```
    $ python3 manage.py loaddata products
    ```

9. Create superuser:

    ```
    $ python3 manage.py createsuperuser 
    ```

10. In the project's [`settings.py`](/gem_master/settings.py), re-enable the projec's default database(disabled in step number 5) and with an if statment make sure that when the app is running on Heroku the connection is made to PostgreSQL or otherwise to default database (SQLite).
11. Install `gunicorn` package on Gitpod
12. Create Procfile
13. Set `DISABLE_COLLECTSTATIC` to `1` on Heroku (so heroku does not collect static files during deployment).

    ```
    $ heroku config:set DISABLE_COLLECTSTATIC=1 --app gem-master
    ```

14. Add `ALLOWED_HOSTS` variable(containing host name of the premiumbody app and the localhost) to project's [`settings.py`](/gem_master/settings.py) file.
15. Commit and Push to Github
16. Since the app was created via the Heroku webpage, initializing heroku git remote is necessary before pushing to Heroku

    ```
    $ heroku git:remote -a gem-master
    ```

17. Push to Heroku

    ```
    $ git push heroku master
    ```

18. Finally, enable automatic deployment to Heroku when pushing to Github by going to Heroku webpage, clicking on the "Deploy" tab and then on "Connect to Github" button. Search for the gem-master repo and click on "Connect". Scroll down to the "Automatic deploys" section and click on "Enable Automatic Deploys".

[Back to contents](#table-of-contents)


 ### Amazon Services (S3)
 
Amazon Web Services(AWS) - S3 was deployed to handle  media and static files storage in gem-master app after being deployed by Heroku.

 ## Web Marketing & Business

 - A web marketing facebook page was created  [Facebook](https://www.facebook.com/profile.php?id=100086998397922&sk=photos/)

 ![](/README_DOC/facebook_marketing_page.jpg)

## Credits

### Media

-   The product images was taken from Kaggle [Kaggle](https://Kaggle.com/).
-   The Carousel and Hero images were taken from Pexels [Pexels](https://pexels.com/).

**Django Documentation**
- Django has an amazing documentation with a tutorial project and in depth explanations on core components.
- [Django Documentation ](https://docs.djangoproject.com/en/3.2/)

## **Aknowledgements**

*  Codeinstitute , the slack community, and Codeinstitue mentor support team

**Harry Leepz**
- [Github](https://github.com/Harry-Leepz/Nourish-and-Lift)
    - The favorite app code used was taken from Harry Leepz Github page.

**Dennis Chmielewski**
- [Github](https://github.com/dennisdevio)
    - The code for the contact app was taken from this Dennis Devio


**Master Code Online**
- [Youtube](https://www.youtube.com/watch?v=yZPgBThZT04&list=PL_557Q1uZ7gKYcVQtDYFvYONKtwtguF03&index=7)

    - A youtube learning platform was used for the functionality of the Newsletter app.

**Kenbrotech**
- [KenbroTech](https://www.youtube.com/watch?v=hWtlskOaFNI)


* The github link is  [Gemsofparis](https://github.com/gullah26/Gem-master "Gem Master").

* Admin details will be attached to the submission form.

## Thank you.
-   A major part of the logic and web application structure used in the Gemsofparis project was taken from code institute walk through project [GitHub repository](https://github.com/ckz8780/boutique_ado_v1). 


[Back to contents](#table-of-contents)
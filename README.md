# Newbury 40K League 2.0

This web app is an updated version of my original project [Newbury 40K League](https://github.com/P1G30N17/newbury-40k-league), however it is a complete redesign and new build from the ground up. The intention of my app is to allow players to register themselves as a user and then sign up to play in the Newbury Warhammer 40K League, playing against other 40K players in and around Newbury. The app aims to generate player matchups, take in player scores from their matchups, and keep track of their scores, games played, and league points. This structured environment will make it easier for players to find opponents for games, along with incentivizing the user to play a better and more thoughtful as the stakes are higher with this new competitive layer of gameplay. 

![Launch Screen](https://github.com/P1G30N17/dnd-text-adventure/blob/main/media/launch-screen.png?raw=true)

## User Stories
- Having a game of 40K with local gamers has never been more fun!
- I love being able to see how i'm doing competitively against my fellow Newbury 40K players.
- Having opponents generated for me, means I don't have to find or ask awkwardly on various 40K FB pages or forums, as my opponents have also opted in for a gamealready.
- I like how I'm able to register to play in the league, but also update my faction if I feel like changing things up.

## Features 

The Newbury 40K League 2.0, holds a very simple premise, arrange and maintain a league based database and allow user game score submissions. However the backend allows for a great deal of user customisability. The user cans register an account and then sign up for the league, giving the name and their desired faction for their army, which they then play with in the league. Their opponents are generated from other willing players that have also done the same, giving players fair matchups, to which each player will submit their score and have the league database updated in realtime to reflect the wins and losses of each player, and give their position for all to see. The app was designed with the CRUD development cycle in mind and each user can create, update, and delete their account if they so wish it, this would then be seen as a withdrawal from the league, and this can only be done by each individual user as secured via user login credentials. 

### Existing Features

- __The Home Page__

  - Here any user of the app can see the current league standings, and all current players and their factions who are registered for the league.
  - It offers easy navigation around the site to the various pages through the navbar element.
  - Users will also be given a Login or Register request on the right hand side of the navbar if they are not currently logged in.
  - If the user is already logged in this Navbar element will display their user name and allow them to logout if they so wish it.

![The Hompage](https://github.com/P1G30N17/newbury-40K-league-2.0/blob/main/static/media/homepage.png?raw=true)

- __The Navbar__

  - Here the user can navigate to the various pages of the site.

![The Navbar](https://github.com/P1G30N17/newbury-40K-league-2.0/blob/main/static/media/navbar.png?raw=true)

- __The League Table__

  - The League Table reflects all the information of registered players, this is not to be confused with registered users, as a user must first sign up to join the league before they will be refelcted in the table.
  - The table tracks and reflects players results from games they have played and submitted via the Submit Results page.
  - This gives players an easy to use and view update on their standind within the current league.
  - This table is updated in real time with each player's results updating as soon as they are submitted, allowing for a more accurate representation of information to all players.

![League Table](https://github.com/P1G30N17/newbury-40K-league-2.0/blob/main/static/media/homepage.png?raw=true)

- __The About page__ 

- Here the user can find all the relevant information regarding the league, such as rules for each game that all players must adhere to for a game to be considered legimate.
  - A note must be taken into consideration however, that as humans may not be bound by strict rules in reality there is still the possibility that results submissions could be fake, or incorrect. (This could be adjusted by players submitting a request to the admin, or a two player validation system where both players need to submit the correct results of their opponents - A potential implementation in future updates.)
- Updates to the league can also be posted here by the site admin, allowing users easy access to any future league updates or rules changes.

![About Page](https://github.com/P1G30N17/newbury-40K-league-2.0/blob/main/static/media/about.png?raw=true)

- __League__

- This navbar element contains a few drop down elements relevant to a registered player, and as such have login requirements(If the user is not logged in they will be taken to the relevant user login page)

![Navbar](https://github.com/P1G30N17/newbury-40K-league-2.0/blob/main/static/media/navbar.png?raw=true)

- If the user is logged in, they will be able to access:
  - My Profile:
    - This will show the user their player profile once they have registered for the league, these fields are their selected name, faction of choice, games played, league points and a running tally of their submitted victory points. Player's can also opt to update their player profile or delete it if they so wish it, taking them to the relevant pages.

    ![My Profile](https://github.com/P1G30N17/newbury-40K-league-2.0/blob/main/static/media/player-profile.png?raw=true)

  - My Matchups:
    - This is a feature that is still to be implemented, but in the future it will display two random opponents who the user must play within the month for their official league games.

    ![My Matchups](https://github.com/P1G30N17/newbury-40K-league-2.0/blob/main/static/media/matchups.png?raw=true)

  - Submit Results:
    - Here the user, once registered for the league can submit their results from a game, as victory points in Warhammer 40K have a maximum of 100 that can be scored the user can only enter a score between 0 - 100. The user must also select if they won their game or not via the toggle button, yes being 2 league points and no being only 1 league point.

    ![Submit Results](https://github.com/P1G30N17/newbury-40K-league-2.0/blob/main/static/media/submit-results.png?raw=true)

    - A successful results submission will redirect the player to the homepage with their now updated score visible on the home page.

    ![Submit Results Success](https://github.com/P1G30N17/newbury-40K-league-2.0/blob/main/static/media/results-success.png?raw=true)

  - Register for League:
    - Once a user has created a user account, they can then register for the league through this link, giving them the option to enter their name and faction that they wish to play with in the league.

    ![Register for League](https://github.com/P1G30N17/newbury-40K-league-2.0/blob/main/static/media/league-registration.png?raw=true)

  - Player Update

  - The player can update their name and faction from this page and it will then be reflected on the league table on the home page.

    ![Player Update](https://github.com/P1G30N17/newbury-40K-league-2.0/blob/main/static/media/player-update.png?raw=true)

- __Player Delete__

  - The Player can opt to delete their player account which will remove their current name, faction and all results from the league. However this does not delete their user account and the player can then reregister for the league if they wish to start on a new slate with a new name and faction.

![Player Delete](https://github.com/P1G30N17/newbury-40K-league-2.0/blob/main/static/media/player-deletion.png?raw=true)

- __User Portal__

- On the far right hand side of the navbar element the user will see their profile portal if they are logged in, if they are not logged in the will be presented with a login or register option. This duel option allows for quick user access to either create an account, or log in to an existing one.

![User Portal](https://github.com/P1G30N17/newbury-40K-league-2.0/blob/main/static/media/user-login-register.png?raw=true)

![User Login](https://github.com/P1G30N17/newbury-40K-league-2.0/blob/main/static/media/user-login.png?raw=true)

![User Register](https://github.com/P1G30N17/newbury-40K-league-2.0/blob/main/static/media/account-registration.png?raw=true)

- Once logged in the Login or Register option will be replaced with the user's chosen user name and the option to logout.

![User Portal](https://github.com/P1G30N17/newbury-40K-league-2.0/blob/main/static/media/logged-in-user.png?raw=true)

- __Footer__
  - The footer just gives users url links to the various clubs running in Newbury where players could play their games if they so wish, these links are to their respective clubs's Facebook group pages.

![Footer](https://github.com/P1G30N17/newbury-40K-league-2.0/blob/main/static/media/footer.png?raw=true)


### Features Left to Implement

- Auto generated matchups, to allow the database to generate random opponents from registered league players and present these to the user.
- The ability for the league to run into pre definded seasons, ie 3 months at a time, at which time the current league will end, results will be saved (perhaps a hall of fame page to view past league results) and a new league will start with the users being able to decided if they wish to register for the new league via the register for league page.
- Email automation, as users can link an email to their user accounts I would like to be able to give the user the option to be emailed about their generated opponents, and then give them the option to send an email asking their opponent for a time, date and place that they would like to have their game of Warhammer 40K. 

## Testing 

- __Automated Testing__
  
  - I made a few automated tests to the best of my knowledge of which almost all passed. The last two tests were with regards to the player delete and player update views. 
  ![URL Tests](https://github.com/P1G30N17/newbury-40K-league-2.0/blob/main/static/media/Url%20tests.png?raw=true)
  ![Views Test P1](https://github.com/P1G30N17/newbury-40K-league-2.0/blob/main/static/media/Views%20tests%20p1.png?raw=true)
  ![Views Test p2](https://github.com/P1G30N17/newbury-40K-league-2.0/blob/main/static/media/Views%20tests%20p2.png?raw=true)

- __Manual Testing__

  - As stated some of my automated tests were insufficient and so I manually tested the other views and functions that I could not run automated tests on.
    - The delete view was proven to work correctly, once the player opted to delete their player profile, their player record was correctly deleted from the league model and no longer reflected on the league table on the homepage.

    ![Delete Player](https://github.com/P1G30N17/newbury-40K-league-2.0/blob/main/static/media/show-delete-proof.png?raw=true)
    ![Delete Player Warning](https://github.com/P1G30N17/newbury-40K-league-2.0/blob/main/static/media/player-deletion.png?raw=true)
    ![Player Deleted Successfully](https://github.com/P1G30N17/newbury-40K-league-2.0/blob/main/static/media/player-deletion-success.png?raw=true)

    - The update view was proven to work correctly, once the player opted to update their player profile, their player record was correctly updated in the league model and the league table on the home page correctly reflected this update.
    
    ![Update Player Before](https://github.com/P1G30N17/newbury-40K-league-2.0/blob/main/static/media/player-update-proof.png?raw=true)
    ![Player Update Form](https://github.com/P1G30N17/newbury-40K-league-2.0/blob/main/static/media/player-update.png?raw=true)
    ![Player Update After](https://github.com/P1G30N17/newbury-40K-league-2.0/blob/main/static/media/player-update-success.png?raw=true)

    - The submit results function and update function worked in tandem and successfully did what they were intended, firstly taking the user to the correct submitresults.html page and then processing the player's input and POSTing it correctly to the database. This was then reflected correctly on the league table on the home page. 

    ![Unsubmitted Results](https://github.com/P1G30N17/newbury-40K-league-2.0/blob/main/static/media/homepage.png?raw=true)
    ![Results Submission Form](https://github.com/P1G30N17/newbury-40K-league-2.0/blob/main/static/media/submit-results.png?raw=true)
    ![Results Submitted Successfully](https://github.com/P1G30N17/newbury-40K-league-2.0/blob/main/static/media/results-success.png?raw=true)


### Bugs

- Currently if a user deletes their profile and then reregisters for the league, the player detail view is incorrectly linking to their old url. If the player was player 10 in the registered players and then deletes and reregisters for the league, their player profile is now still */player/10 but if you manual increment their player id to */player/11 you will be taken correctly to their profile. Upon which all the user functinality remains the same. Currently I am trying to address this issue as it is most serious, and I think it pertains to either an incorrect delete cascade method in the model or the user pk being incorrectly found and passed into the URL.

### Validator Testing 

- Python
  - All my python files were passed through [CI Python Linter](https://pep8ci.herokuapp.com/) and all errors and warnings were adressed.
- HTML 
  - The page source codes were all passed into [HTML Validator](https://validator.w3.org/nu/) and no errors or warnings were given.
- CSS
  - The CSS for this project was rather small due to Bootstrap being used, nonetheless the CSS from the project was passed into [CSS Validator](https://jigsaw.w3.org/css-validator/) and no errors or warnings were given.

### Web Browser Testing

- The project obtained a great lighthouse rating with the Google Lighthouse Dev Tool.

![Lighthouse Score](https://github.com/P1G30N17/newbury-40K-league-2.0/blob/main/static/media/lighthouse.png?raw=true)

- The various web browsers the project was tested on had mostly optimal results, with little to no errors between all 3.

### Unfixed Bugs

- Currently their is still the user delete bug as previously described in the bugs section. 

## Deployment

1. **Sign Up/Login to Heroku**
      - If you haven't already, sign up for a Heroku account at [Heroku's website](https://www.heroku.com/) or log in if you already have an account.

  2. **Create a New App on Heroku**
       - Once logged in, navigate to your Heroku dashboard and click on the **New** button, then select **Create new app**.
       - Choose a unique name for your app and select your region.

  3. **Connect GitHub Repository**
       - After creating your app, go to the **Deploy** tab within your app's dashboard.
       - Under the **Deployment method** section, select **GitHub** as the deployment method.
       - Search for your GitHub repository in the **Connect to GitHub** section and click **Connect**.

  4. **Configure Deployment Options**
       - Once connected, choose the branch you want to deploy (e.g. *main*) and optionally enable automatic deploys for future commits.

  5. **Deploy Branch**
       - After configuring the deployment options, manually deploy your application by clicking the **Deploy Branch** button.

  6. **Monitor Deployment Progress**
       - Heroku will start deploying your application from the selected GitHub branch. You can monitor the deployment progress from the activity log on the same page.

  7. **View Application**
      - Once the deployment is complete, Heroku will provide you with a URL to access your deployed application. Click on **View** button to open your application in a new tab.

## Credits 

- All work is my own original code and models, with the exception of the following:
  - Boostrap has been used to quickly and easily build the frontend of my app, credit goes to [Get Bootstrap](https://getbootstrap.com).
  - Crispyforms to easily display any form view, credit goes to [CrispyForms](https://django-crispy-forms.readthedocs.io/en/latest/#).
  - Tutor support from CodeInstitute with regards to deploying my project on Heroku and with an error was having with the submit results function not updating the database correctly.
  - Favicon generated using [FavIcon](https://favicon.io/).
  - Gameplay image was taken by myself, James King.


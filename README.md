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

![The Game](https://github.com/P1G30N17/dnd-text-adventure/blob/main/media/the-game.png?raw=true)

- __The Navbar__

  - Here the user can navigate to the various pages of the site.

![Using Commands](https://github.com/P1G30N17/dnd-text-adventure/blob/main/media/using-commands.png?raw=true)

- __The League Table__

  - The League Table reflects all the information of registered players, this is not to be confused with registered users, as a user must first sign up to join the league before they will be refelcted in the table.
  - The table tracks and reflects players results from games they have played and submitted via the Submit Results page.
  - This gives players an easy to use and view update on their standind within the current league.
  - This table is updated in real time with each player's results updating as soon as they are submitted, allowing for a more accurate representation of information to all players.

![HUD Display](https://github.com/P1G30N17/dnd-text-adventure/blob/main/media/hud.png?raw=true)

- __The About page__ 

- Here the user can find all the relevant information regarding the league, such as rules for each game that all players must adhere to for a game to be considered legimate.
  - A note must be taken into consideration however, that as humans may not be bound by strict rules in reality there is still the possibility that results submissions could be fake, or incorrect. (This could be adjusted by players submitting a request to the admin, or a two player validation system where both players need to submit the correct results of their opponents - A potential implementation in future updates.)
- Updates to the league can also be posted here by the site admin, allowing users easy access to any future league updates or rules changes.

![Player message](https://github.com/P1G30N17/dnd-text-adventure/blob/main/media/player-message.png?raw=true)

- __League__

- This navbar element contains a few drop down elements relevant to a registered player, and as such have login requirements(If the user is not logged in they will be taken to the relevant user login page)
- If the user is logged in, they will be able to access:
  - My Profile:
    - 
  - My Matchups:
    - 
  - Submit Results:
    - 
  - Register for League:
    - 

- __User Portal__

- On the far right hand side of the navbar element the user will see their profile portal if they are logged in, if they are not logged in the will be presented with a login or register option. This duel option allows for quick user access to either create an account, or log in to an existing one.
- Once logged in the Login or Register option will be replaced with the user's chosen user name.

![Victory and Game Over state](https://github.com/P1G30N17/dnd-text-adventure/blob/main/media/game-over.png?raw=true)

### Features Left to Implement

- Auto generated matchups, to allow the database to generate random opponents from registered league players and present these to the user.
- League points being implemented from a victory or a loss, this option will be submitted through the results submission page and will be relfected in the league table.
- The ability for the league to run into pre definded seasons, ie 3 months at a time, at which time the current league will end, results will be saved (perhaps a hall of fame page to view past league results) and a new league will start with the users being able to decided if they wish to register for the new league via the register for league page.
- Email automation, as users can link an email to their user accounts I would like to be able to give the user the option to be emailed about their generated opponents, and then give them the option to send an email asking their opponent for a time, date and place that they would like to have their game of Warhammer 40K. 

## Walkthrough

## Testing 

- 

### Bugs

- 

### Validator Testing 

- Python
  - A few errors were found and some warnings were noted when passing through the official [(CI Python Linter](https://pep8ci.herokuapp.com/)
    - 

### Unfixed Bugs

- 

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

  5. **Select Framework**
      - Since the DnD Text Adventure Game includes both Python and Node.js components, you need to specify the correct buildpacks for deployment. 
       - Under the *Settings* tab of your Heroku app, navigate to the **Buildpacks** section and add the appropriate buildpacks for Python and Node.js. (Make sure that they are in this correct order, Python above Node.js)
       - Also, add the following environment variables:
       - **PORT** set to **8000** to specify the port on which your app will run.

  6. **Deploy Branch**
       - After configuring the deployment options, manually deploy your application by clicking the **Deploy Branch** button.

  7. **Monitor Deployment Progress**
       - Heroku will start deploying your application from the selected GitHub branch. You can monitor the deployment progress from the activity log on the same page.

  8. **View Application**
      - Once the deployment is complete, Heroku will provide you with a URL to access your deployed application. Click on **View** button to open your application in a new tab.

## Credits 

### Code

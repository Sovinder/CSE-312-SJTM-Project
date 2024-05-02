# CSE-312-SJTM-Project

https://csesjtm.com/

**Project Part 3 Objective 3 Description**

The feature that we have implemented for our website is the functionality of both creating teams and joining teams.
Each logged in member will have the chance to create a single team. During the process of creating a team, the user
will be able to choose their respective sport, number of desired teamates and their team name. After creating the 
team, the "Join a Team" page will now display all of the teams that are joinable. Other users will be able to 
navigate to this page and join a team that fits their needs. If there is already too many players on the team,
the user will not be able to join. This objective worked heavily with the relationships between several SQL tables. 
We created primary keys to identify each user and their respective team. Additionally, the objective involved 
the creation of more complex forms and Jinja2 to correctly format and display the teams.

**Testing Procedure**

    1. Navigate to https://csesjtm.com/
        a. If the deployed website is not working, work locally by using docker compose up.
        b. Navigate the localhost:8080 if locally.
    2. Stay signed out.
        a. Navigate the "Create a Team"
        b. Assert that a page with a form is displayed.
        c. Fill in the form and submit.
    3. Verify that you are now redirected to the homepage.
    4. Navigate to the "Join a Team" page.
        a. Assert that the team you had just created is not displayed.
    5. Register and account and login
    6. Repeat steps 2-3 with a logged in account.
    7. Navigate back to the "Join a Team" page.
        a. Assert that the created team is now displayed.
    8. Logout and register/login to a different account
    9. Navigate to the "Join a Team"' page again.
        a. Verify that the team is still displayed.
    10. With this new user, join the team.
        a. Verify that the team name is now displayed on the homepage.
        b. Navigate to the chat page
        c. Type a chat
        d. Verify that your new team name is shown in the chat.
    11. Restart docker if you have run it locally.
        a. Verify that the "Join a Team" page is still displayed through the restart.
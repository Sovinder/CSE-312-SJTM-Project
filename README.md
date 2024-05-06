# CSE-312-SJTM-Project

https://csesjtm.com/

**Project Part 3 Objective 3 Description**

The feature that we have implemented for our website is the functionality of both creating teams and joining teams.
Each logged in member will have the chance to create a single team. During the process of creating a team, the user
will be able to choose their respective sport, number of desired teamates and their team name. After creating the
team, the "Join a Team" page will now display all of the teams that are joinable. Other users will be able to
navigate to this page and join a team that fits their needs. If there is already too many players on the team,
the user will not be able to join. Also, when an user is already joined a team, they won't be able to join other team or create a new team. This objective worked heavily with the relationships between several SQL tables.
We created primary keys to identify each user and their respective team. Additionally, the objective involved
the creation of more complex forms and Jinja2 to correctly format and display the teams.

**Testing Procedure**

    1. Navigate to https://csesjtm.com/
        a. If the deployed website is not working, work locally by using docker compose up.
        b. Navigate the localhost:8080 if locally.
    2. Register and Log in.
    3. Navigate the "Create a Team".
        b. Assert that a page with a form is displayed.
        c. Fill in the form and submit.
    3. Click "Back" to return to homepage.
    4. Navigate to the "Join a Team" page.
        a. Assert that the created team is now displayed.
        b. Send a chat message in chat room and verify that the team name appears next to username.
    5. Logout and register/login to a different account
    6. Navigate to the "Join a Team"' page again.
        a. Verify that the team is still displayed.
    7. With this new user, join the team.
        a. Verify that the team name is now displayed on the homepage.
        b. Navigate to the chat page
        c. Type a chat
        d. Verify that your new team name is shown in the chat.
    8. Restart docker if you have run it locally.
        a. Verify that the "Join a Team" page is still displayed through the restart.

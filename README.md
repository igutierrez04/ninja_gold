Ninja Gold Assignment

Create a simple game to test your understanding of FLask,
and implement the functionally below.

For this assignment, you're going to create a mini game that
helps a ninja make some money! When you start the game your
ninja should have 0 gold. The ninja can go to different places
(farm, cave, house, casino) and earn different amounts of gold.
In the case of a casino, your ninja can earm or lose up to 50 gold.
Your jon is to create a web app that allows this ninja to ear gold
and to display their past activities.

The root route should display 4 different forms on the HTML page, 
there should be a method that handles the POST request, determing
how much user should now have depending on their visit.

Note: You should only have 2 routes for this assignment -- '/' and
'/process_money'

Assignment check list

    - Create a new Flask project called ninja_gold
    - Create the template as shown in the wirefram above, with 4
        separate forms
    - Have the root route render this page
    - Have the "/process_money" POST route increase/decrease the
        user's gold by an appropriate amount and redirect to the
        root route
    - NINJA BONUS: Display all the activities performed by the user 
        in a log on the HTML
    - NINJA BONUS: Have the activities be color-coded (+ money is green,
        - money is red)
    -NINJA BONUS: Add a reset button to restart the game
    -SENSEI BONUS: HAve the activities display in decending ordeer, with
        the most recent activity first
    - SENSEI BONUS: Provide winning parameters to the game -- for example,
        a user must obtain 500 gold in less than 15 moves. Only display the
        reset button once the user has lost or won.
    -SENSEI BONUS: Complete the "/process_money" route without 4 conditional
        statemeents (i.e. without doing if farm... elif cave... etc.)
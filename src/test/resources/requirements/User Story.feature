Feature: 
    User Authentication of Viewpoint Voting Platform

@REQ-001 @ID-001 @LOGIN	
Scenario Outline:Validation of Invalid User Authentication 
Given the user clicks on the "LOGIN" element on the "home" page of GlassLewis site
When the user clicks "LOGIN" button underneath "Viewpoint Voting Platform" label of the dialog window
Then the user lands onto the "GlassLewis Viewpoint" page
And "GLASS LEWIS VIEWPOINT" should appear in the top banner
When the user enters "<USERNAME>","<PASSWORD>"
And the user clicks on "Sign in" button
Then the user should see the "<MESSAGE>" message on screen
And user should still be in the same login page
 
Examples:
|USERNAME     | PASSWORD    | MESSAGE                                       |
|Leave Blank  | Leave Blank | The fields USERNAME and PASSWORD are required |
|Testuser1    | Leave Blank | The fields USERNAME and PASSWORD are required |
|Leave Blank  | Password2   | The fields USERNAME and PASSWORD are required |
|Testuser1    | Password2   | Invalid username or password                  |

	
Background:
    Given the user is already registered in the system
	
@REQ-001 @ID-002 @LOGIN		
Scenario:Validation of valid User Authentication 
Given the user is already in "GlassLewis Viewpoint" page
When the user has input the correct username and password combination
And the user clicks on "Sign in" button
Then the user should land onto "Viewpoint Voting" page
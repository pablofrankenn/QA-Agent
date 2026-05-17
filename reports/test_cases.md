# Test Cases for https://www.saucedemo.com

# QA Test Cases for Swag Labs Login Page

## Test Case 1: Successful Login with Standard User

**Test Case Name:** Verify successful login with standard_user credentials

**Description:** 
Validate that a user can successfully log in to Swag Labs using the standard_user username and correct password, and is redirected to the products/inventory page.

**Steps to Reproduce:**
1. Navigate to the Swag Labs login page
2. Enter "standard_user" in the username field
3. Enter "secret_sauce" in the password field
4. Click the "Login" button
5. Observe the page redirect and content

**Expected Result:**
- Login is successful
- User is redirected to the inventory/products page
- No error messages are displayed
- User dashboard or product listing is visible

---

## Test Case 2: Login Attempt with Locked Out User

**Test Case Name:** Verify locked_out_user cannot access the application

**Description:**
Validate that the locked_out_user account is unable to log in and receives an appropriate error message indicating the account is locked.

**Steps to Reproduce:**
1. Navigate to the Swag Labs login page
2. Enter "locked_out_user" in the username field
3. Enter "secret_sauce" in the password field
4. Click the "Login" button
5. Observe error message displayed

**Expected Result:**
- Login fails
- An error message is displayed stating the user is locked out (e.g., "Sorry, this user has been locked out")
- User remains on the login page
- No redirect to the inventory page occurs

---

## Test Case 3: Login with Problem User Account

**Test Case Name:** Verify login functionality with problem_user account

**Description:**
Validate that the problem_user account can log in successfully, but may experience UI/functional issues on subsequent pages as per the test user designation.

**Steps to Reproduce:**
1. Navigate to the Swag Labs login page
2. Enter "problem_user" in the username field
3. Enter "secret_sauce" in the password field
4. Click the "Login" button
5. Verify page loads and check for any UI anomalies

**Expected Result:**
- Login is successful
- User is redirected to the inventory page
- User may observe visual or functional issues on the page (intentional for testing purposes)
- No error message is displayed during login

---

## Test Case 4: Login Attempt with Incorrect Password

**Test Case Name:** Verify login fails with correct username but incorrect password

**Description:**
Validate that login fails when a valid username is entered with an incorrect password, and an appropriate error message is displayed.

**Steps to Reproduce:**
1. Navigate to the Swag Labs login page
2. Enter "standard_user" in the username field
3. Enter an incorrect password (e.g., "wrong_password")
4. Click the "Login" button
5. Observe error message

**Expected Result:**
- Login fails
- Error message is displayed (e.g., "Username and password do not match any user in this service")
- User remains on the login page
- No redirect occurs

---

## Test Case 5: Login with Performance Glitch User

**Test Case Name:** Verify login with performance_glitch_user and assess page load performance

**Description:**
Validate that the performance_glitch_user account can successfully log in, but the application may exhibit slow load times or performance issues on subsequent pages.

**Steps to Reproduce:**
1. Navigate to the Swag Labs login page
2. Enter "performance_glitch_user" in the username field
3. Enter "secret_sauce" in the password field
4. Click the "Login" button
5. Monitor page load time and responsiveness
6. Navigate through inventory page

**Expected Result:**
- Login is successful
- User is redirected to the inventory page
- Page may load slower than expected (intentional for testing)
- Application remains functional despite potential performance delays
- No login error messages are displayed
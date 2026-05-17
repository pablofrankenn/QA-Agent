# Test Cases for https://www.saucedemo.com

# Test Cases for Swag Labs Login Page

## Test Case 1: Successful Login with Standard User

**Test Case Name:** Verify successful login with standard_user credentials

**Description:** Validate that a standard user can successfully log in to the Swag Labs application using valid credentials.

**Steps to Reproduce:**
1. Navigate to the Swag Labs login page
2. Enter username: "standard_user"
3. Enter password: "secret_sauce"
4. Click the "Login" button

**Expected Result:**
- User is successfully authenticated
- User is redirected to the inventory/dashboard page
- No error messages are displayed
- User session is established

---

## Test Case 2: Login with Locked Out User

**Test Case Name:** Verify locked_out_user receives appropriate error message

**Description:** Validate that the locked_out_user account displays an appropriate error message preventing login.

**Steps to Reproduce:**
1. Navigate to the Swag Labs login page
2. Enter username: "locked_out_user"
3. Enter password: "secret_sauce"
4. Click the "Login" button

**Expected Result:**
- Login is rejected
- An error message is displayed stating the user is locked out (e.g., "Sorry, this user has been locked out")
- User remains on the login page
- No session is created

---

## Test Case 3: Login with Problem User

**Test Case Name:** Verify login functionality with problem_user account

**Description:** Validate that problem_user can log in successfully and identify any UI rendering issues specific to this account.

**Steps to Reproduce:**
1. Navigate to the Swag Labs login page
2. Enter username: "problem_user"
3. Enter password: "secret_sauce"
4. Click the "Login" button
5. Observe the inventory page for any visual or functional anomalies

**Expected Result:**
- User successfully logs in and is redirected to the inventory page
- Login functionality works as expected
- Note any visual rendering issues or UI anomalies that appear on the inventory page
- All interactive elements are functional

---

## Test Case 4: Login Attempt with Incorrect Password

**Test Case Name:** Verify login fails with valid username but incorrect password

**Description:** Validate that login is rejected when correct username is paired with an incorrect password.

**Steps to Reproduce:**
1. Navigate to the Swag Labs login page
2. Enter username: "standard_user"
3. Enter password: "incorrect_password"
4. Click the "Login" button

**Expected Result:**
- Login attempt fails
- An error message is displayed (e.g., "Username and password do not match any user in this service")
- User remains on the login page
- No session is created
- Password field is cleared or masked

---

## Test Case 5: Login with Performance Glitch User

**Test Case Name:** Verify login with performance_glitch_user and assess page load performance

**Description:** Validate that performance_glitch_user can log in and monitor for performance issues or slow page loads specific to this account.

**Steps to Reproduce:**
1. Navigate to the Swag Labs login page
2. Enter username: "performance_glitch_user"
3. Enter password: "secret_sauce"
4. Click the "Login" button
5. Monitor page load time and responsiveness
6. Interact with page elements (clicking, scrolling)

**Expected Result:**
- User successfully authenticates and is redirected to the inventory page
- Login completes successfully despite potential performance delays
- Page eventually loads completely (may take longer than standard_user)
- All page elements are functional, though response time may be slower
- No functionality is broken due to performance issues
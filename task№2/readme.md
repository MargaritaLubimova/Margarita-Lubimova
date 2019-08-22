## Task №2 Bullet points for GnuCash app

### Bullet points for main functional:
1. Check install app and opening ( pass all steps to main screen) 
2. Check to add a new income (choose any sub-account)
3. Check to add a new expense (choose any sub-account)
4. Check to add a new equity (choose any sub-account)
5. Check to add a new liabilities (choose any sub-account)
6. Check edit any transaction
7. Check delete any transaction
8. Check cancel any transaction during creating
9. Check calculation after add expense/income/equity/liabilities in assets
10. Check to add a new sub-account in any category (assets/11. expense/income/equity/liabilities)
11. Check that after adding expense/income/equity/liabilities recent have information about it
12. Check add new account to favorites (it doesn’t work correctly)
13. Check Export with any export to (Save As/Dropbox/ownCloud/Send to) in any format (CSV/QIF/XML)
14. Check on each step the layout of visual display presentations (also with changing orientation) 
presentations

### Each point should check on other devices (this set depends on which devices are used by your users, it shows only approximately set and this exampel only iOS devices):
| Device            | OS Version    |
--------------------|---------------
Alcatel Pixi 4      |6.0 (API 23)
Asus ZenFone 3 Max  |6.0 (API 23)
Asus ZenFone GO     |5.1.1 (API 22)
BQ Aquaris X5       |7.1.1 (API 25)
Fly Champ	        |7.0 (API 24)
Google Pixel        |9.0.0 (API 28)
Huawei honor 7A	    |8.1 (API 27)
Huawei honor 9 Lite	|8.0 (API 26)
Lenovo Tab 4 Plus 8 |7.1.1 (API 25)
Nexus 5X LG	        |8.1 (API 27)   

## Bug report
### Bug №1
**Description:** New created a category in Favorites account doesn't appear on a Favorites screen.

**Steps:**
1. Open the main screen
2. Switch to Favorites account
3. Click on add sub-account (image plus)
4. Fill out account name
5. Click on save

**Actual result:** On the Favorites screen the sub-account doesn't exist.

**Expected result:** On the Favorites screen the sub-account exist.

### Bug №2
**Description:** Crash after export to "Send to".

**Steps:**
1. Open the main screen
2. Click on Menu
3. Click on export
4. Fill out fields such as:
5. Export to: Send to
    * Format: CSV
    * Separator: any
    * Since: any
    * Delite transaction after export: any
6. Click on EXPORT

**Actual result:** Happened a crash.

**Expected result:** Appeared alert with a message (e.g. Export has been a success)


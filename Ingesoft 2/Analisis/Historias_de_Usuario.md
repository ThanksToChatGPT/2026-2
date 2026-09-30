# Historias de usuario

## Epic 1. Account and Profile

### US-1: Create an account [MUST]
- **As a**: New user
- **I want**: To create an account with my email and password
- **So that**: My preferences and outfits are saved.

**Acceptance Criteria**
1. Given the user is on the sign-up form, when they enter an invalid email or password, then the form shows a validation error.
2. Given the user entered a valid email and password, when they submit the form, then the account is created and the user can log in.

---

### US-2: Log in and log out [MUST]
- **As a**: User
- **I want**: To log in and log out
- **So that**: My information stays private.

**Acceptance Criteria**
1. Given the user has an account, when they enter correct credentials, then the session opens.
2. Given the user is logged in, when they click log out, then the session closes.
3. Given the user is on the login page, when they enter wrong credentials, then an error message is shown.

---

### US-3: Sign in with Google [COULD]
- **As a**: User
- **I want**: To sign in with my Google account
- **So that**: I do not have to remember another password.

**Acceptance Criteria**
1. Given the user is on the login page, when the page loads, then a "Continue with Google" button is shown.
2. Given the user chooses to sign in with Google, when Google confirms their identity, then the account is created or linked automatically.

---

### US-4: Recover password by email [SHOULD]
- **As a**: User
- **I want**: To recover my password by email
- **So that**: I can get back into my account if I forget it.

**Acceptance Criteria**
1. Given the user forgot their password, when they ask for a reset with their email, then a reset link is sent to that email.
2. Given the user received a reset link, when the link stays unused for too long, then the link expires.

---

### US-5: Edit my profile [SHOULD]
- **As a**: User
- **I want**: To edit my profile (name, email, country,sizes)
- **So that**: My account shows my real information.

**Acceptance Criteria**
1. Given the user is on their profile page, when they edit their information and save, then the changes are saved and shown right away.

---

### US-6: Delete my account and data [SHOULD]
- **As a**: User
- **I want**: To delete my account and my data
- **So that**: I control my personal information.

**Acceptance Criteria**
1. Given the user is in their account settings, when they choose to delete the account, then the app asks them to confirm.
2. Given the user confirmed the deletion, when the process finishes, then all their personal data is removed.

---

### US-7: Search without an account [SHOULD]
- **As a**: Visitor
- **I want**: To use the search without an account
- **So that**: I can try the app before registering.

**Acceptance Criteria**
1. Given a visitor has no account, when they use the search and filters, then the results are shown without login.
2. Given a visitor has no account, when they try to save an outfit, then the app asks them to register.

---

## Epic 2. User Preferences

### US-8: Setup guide for new users [SHOULD]
- **As a**: New user
- **I want**: A short setup guide when I first enter
- **So that**: I can set my preferences quickly.

**Acceptance Criteria**
1. Given a user logs in for the first time, when the home page loads, then a step-by-step setup form appears.
2. Given the setup form is shown, when the user chooses to skip it, then they go into the app without saving preferences.

---

### US-9: Select liked brands [SHOULD]
- **As a**: User
- **I want**: To select the brands I like
- **So that**: I see them first in the results.

**Acceptance Criteria**
1. Given the user is choosing preferences, when they open the brand list, then they can pick many brands.
2. Given the user saved liked brands, when they see the search results, then items from those brands get higher priority.

---

### US-10: Choose favorite colors [SHOULD]
- **As a**: User
- **I want**: To choose my favorite colors
- **So that**: The results match my palette.

**Acceptance Criteria**
1. Given the user is choosing preferences, when they open the color section, then a color picker or color list is available.
2. Given the user selected favorite colors, when they save, then the selected colors are saved.

---

### US-11: Set price range [MUST]
- **As a**: User
- **I want**: To set my price range
- **So that**: I only see items I can afford.

**Acceptance Criteria**
1. Given the user is on the preferences page, when they set a minimum and a maximum price, then the price range is saved.
2. Given a price range is saved, when the user looks at the results, then only items inside the range are shown.

---

### US-12: Save my sizes [SHOULD]
- **As a**: User
- **I want**: To save my sizes (tops, bottoms, shoes)
- **So that**: I only see items available in my size.

**Acceptance Criteria**
1. Given the user is on the preferences page, when they enter sizes for tops, bottoms and shoes, then the sizes are saved per category.
2. Given sizes are saved, when the user searches, then the search can filter by the saved size.

---

### US-13: Choose fit preference [SHOULD]
- **As a**: User
- **I want**: To choose my fit preference (oversized, slim, regular)
- **So that**: The items match how I like to dress.

**Acceptance Criteria**
1. Given the user is on the preferences page, when they select one or more fits, then the fits are saved.
2. Given fits are saved, when the user searches or gets suggestions, then the fit is used in filters and suggestions.

---

### US-14: Set maximum budget [MUST]
- **As a**: User
- **I want**: To set a maximum budget
- **So that**: The app warns me if my outfit is too expensive.

**Acceptance Criteria**
1. Given the user is on the preferences page, when they type a maximum budget, then the budget is saved.
2. Given a budget is saved, when the outfit total goes over it, then a warning appears.

---

### US-15: Edit preferences anytime [MUST]
- **As a**: User
- **I want**: To edit my preferences at any time
- **So that**: The app changes when my taste changes.

**Acceptance Criteria**
1. Given the user is on the settings page, when they edit their preferences and save, then the changes are stored.
2. Given preferences were updated, when the user looks at the recommendations, then the recommendations are updated.

---

### US-16: Reset preferences [COULD]
- **As a**: User
- **I want**: To reset my preferences to default
- **So that**: I can start again.

**Acceptance Criteria**
1. Given the user is on the preferences page, when they press the reset button, then the app asks for confirmation.
2. Given the user confirmed the reset, when the action finishes, then all preferences are cleared.

---

### US-17: View preferences summary [MUST]
- **As a**: User
- **I want**: To see a summary of my preferences
- **So that**: I can check if they are correct.

**Acceptance Criteria**
1. Given the user has saved preferences, when they open their profile page, then all saved preferences are shown in one place.

---

## Epic 3. Product Search and Filtering

### US-18: Search clothing by text [MUST]
- **As a**: User
- **I want**: To search for clothing by text (for example "black cargo pants")
- **So that**: I quickly find what I need.

**Acceptance Criteria**
1. Given the user is on the search page, when they type words like "black cargo pants" and search, then the search returns items that match the words typed.

---

### US-19: See results from many stores [MUST]
- **As a**: User
- **I want**: To see results from many stores in one page
- **So that**: I do not have to visit each website.

**Acceptance Criteria**
1. Given the user searches for an item, when the results load, then items from at least two different stores are shown.
2. Given results are shown, when the user looks at an item, then the store name is displayed on it.

---

### US-20: Filter by price [MUST]
- **As a**: User
- **I want**: To filter by price
- **So that**: I only see items in my range.

**Acceptance Criteria**
1. Given the user is on the results page, when they use the price slider or price inputs, then the results update to that price.

---

### US-21: Filter by brand [MUST]
- **As a**: User
- **I want**: To filter by brand
- **So that**: I can look at only the brands I want.

**Acceptance Criteria**
1. Given the user is on the results page, when they select one or more brands in the brand filter, then only items from those brands are shown.

---

### US-22: Filter by color [MUST]
- **As a**: User
- **I want**: To filter by color
- **So that**: I find items in the color I need.

**Acceptance Criteria**
1. Given the user is on the results page, when they select a color in the color filter, then the results update to that color.

---

### US-23: Filter by size [MUST]
- **As a**: User
- **I want**: To filter by size
- **So that**: I only see available sizes.

**Acceptance Criteria**
1. Given the user is on the results page, when they select a size, then only items with stock in that size are shown.

---

### US-24: Filter by clothing type [MUST]
- **As a**: User
- **I want**: To filter by clothing type (top, bottom, shoes, accessories)
- **So that**: I can focus my search.

**Acceptance Criteria**
1. Given the user is on the results page, when they select a category or subcategory (for example hoodie or jacket), then only items of that category are shown.

---

### US-25: Filter by material [COULD]
- **As a**: User
- **I want**: To filter by material (cotton, denim, polyester, etc.)
- **So that**: I choose comfortable or quality clothes.

**Acceptance Criteria**
1. Given the store provides material data, when the user selects a material, then only items made of that material are shown.

---

### US-26: Filter by store [MUST]
- **As a**: User
- **I want**: To filter by store
- **So that**: I can include or exclude specific shops.

**Acceptance Criteria**
1. Given the user is on the results page, when they select or unselect stores, then the results include or exclude items from those stores.

---

### US-27: Sort results by price [MUST]
- **As a**: User
- **I want**: To sort results by price
- **So that**: I can organize what I see.

**Acceptance Criteria**
1. Given the user is on the results page, when they choose to sort by price, then the order of the results changes.

---

### US-28: Clear all filters [SHOULD]
- **As a**: User
- **I want**: To clear all filters with one click
- **So that**: I can start a new search fast.

**Acceptance Criteria**
1. Given the user has applied filters, when they press "Clear filters", then all filters are reset.

---

### US-29: Personalize results [SHOULD]
- **As a**: User
- **I want**: The results to be personalized with my preferences
- **So that**: The first items match my taste.

**Acceptance Criteria**
1. Given the user has saved preferences, when they search, then the results consider saved brands, colors, sizes and price range.
2. Given personalization is on, when the user turns it off, then the results are shown without using preferences.

---

### US-30: View recent searches [COULD]
- **As a**: User
- **I want**: To see my recent searches
- **So that**: I can repeat them easily.

**Acceptance Criteria**
1. Given the user has searched before, when they open the search bar, then the last searches are listed.
2. Given recent searches are listed, when the user deletes one, then it is removed from the list.

---

### US-31: No-results message [SHOULD]
- **As a**: User
- **I want**: A clear message when there are no results
- **So that**: I know what to do next.

**Acceptance Criteria**
1. Given a search has no matches, when the results page loads, then a "no results" message is shown with tips (remove filters, try other words).

---

### US-32: Pagination or infinite scroll [MUST]
- **As a**: User
- **I want**: Pagination or infinite scroll
- **So that**: The page loads fast even with many products.

**Acceptance Criteria**
1. Given a search has many products, when the results load, then they load in small groups and the page does not freeze.

---

## Epic 4. Product Details and Similar Products

### US-33: Open product page [MUST]
- **As a**: User
- **I want**: To open a product page
- **So that**: I can see all its information.

**Acceptance Criteria**
1. Given the user sees an item in the results, when they open it, then the product page shows name, images, price, brand, material, color, sizes and store.

---

### US-34: See product photos [MUST]
- **As a**: User
- **I want**: To see photos of a product
- **So that**: I can check how it looks.

**Acceptance Criteria**
1. Given the user is on a product page, when the page loads, then a gallery with at least one image is shown.

---

### US-35: See available sizes [MUST]
- **As a**: User
- **I want**: To see which sizes are available
- **So that**: I know if the item fits me.

**Acceptance Criteria**
1. Given the user is on a product page, when they look at the sizes, then available and unavailable sizes are marked differently.

---

### US-36: Group similar products [WOULD]
- **As a**: User
- **I want**: To see similar products grouped together
- **So that**: I can compare options easily.

**Acceptance Criteria**
1. Given there are similar items in the results, when the user views them, then similar items are grouped by type, color and style.

---

### US-37: "You may also like" section [WOULD]
- **As a**: User
- **I want**: To see a "You may also like" section
- **So that**: I discover more items.

**Acceptance Criteria**
1. Given the user is on a product page, when the page loads, then a "You may also like" section shows suggestions based on the viewed item and the user preferences.

---

### US-38: Link to store page [MUST]
- **As a**: User
- **I want**: A direct link to the store page
- **So that**: I can buy the item there.

**Acceptance Criteria**
1. Given the user is on a product page, when they click the store link, then the original product page opens in a new tab.

---

### US-39: See last price update [COULD]
- **As a**: User
- **I want**: To see the last time the price was updated
- **So that**: I know if the information is recent.

**Acceptance Criteria**
1. Given the user is on a product page, when the page loads, then an "Updated on" date is shown.

---

### US-40: Report a wrong product [WOULD]
- **As a**: User
- **I want**: To report a wrong product (bad price, wrong image, broken link)
- **So that**: The information gets fixed.

**Acceptance Criteria**
1. Given the user finds a wrong product, when they press "Report problem", then the report is sent to the admins.

---

## Epic 5. Price Comparison

### US-41: Highlight cheapest option [COULD]
- **As a**: User
- **I want**: The cheapest option to be highlighted
- **So that**: I notice it quickly.

**Acceptance Criteria**
1. Given the same item is sold in different stores, when the prices are shown, then the lowest price has a badge or a different color.

---

### US-42: Compare products side by side [MUST]
- **As a**: User
- **I want**: To compare two or more products side by side
- **So that**: I can decide between them.

**Acceptance Criteria**
1. Given the user selected two or more products, when they open the comparison, then a table shows price, brand, material, color, sizes and rating.

---

### US-43: Show prices in COP [MUST]
- **As a**: User
- **I want**: The price to include a clear currency (COP)
- **So that**: There is no confusion.

**Acceptance Criteria**
1. Given prices are shown anywhere in the app, when the user looks at them, then all prices show the same currency format (COP).

---

## Epic 6. Outfit Builder

### US-44: Start a new outfit [MUST]
- **As a**: User
- **I want**: To start a new outfit from scratch
- **So that**: I can create my own look.

**Acceptance Criteria**
1. Given the user is on the outfit page, when they press "New outfit", then an empty builder opens.

---

### US-45: Add a top to the outfit [MUST]
- **As a**: User
- **I want**: To add a top (t-shirt, shirt, hoodie, jacket) to my outfit
- **So that**: I build the upper part.

**Acceptance Criteria**
1. Given the user is in the outfit builder, when they select a t-shirt, shirt, hoodie or jacket, then the item is placed in the top slot.

---

### US-46: Add a bottom to the outfit [MUST]
- **As a**: User
- **I want**: To add a bottom (jeans, cargo, pants, shorts) to my outfit
- **So that**: I build the lower part.

**Acceptance Criteria**
1. Given the user is in the outfit builder, when they select jeans, cargo pants, pants or shorts, then the item is placed in the bottom slot.

---

### US-47: Add shoes to the outfit [MUST]
- **As a**: User
- **I want**: To add shoes (sneakers, boots, shoes) to my outfit
- **So that**: My look is complete.

**Acceptance Criteria**
1. Given the user is in the outfit builder, when they select sneakers, boots or shoes, then the item is placed in the shoes slot.

---

### US-48: Add accessories [COULD]
- **As a**: User
- **I want**: To add optional accessories (cap, glasses, bag, watch)
- **So that**: I can complete my look.

**Acceptance Criteria**
1. Given the user is in the outfit builder, when they add an accessory, then it is added to the outfit.
2. Given the user is in the outfit builder, when they skip the accessories, then the outfit stays complete without them.

---

### US-49: Replace a piece [MUST]
- **As a**: User
- **I want**: To replace any piece of the outfit
- **So that**: I can try different combinations.

**Acceptance Criteria**
1. Given the outfit has pieces, when the user presses "Change" on a piece, then a list of alternatives opens.

---

### US-50: Live outfit update [MUST]
- **As a**: User
- **I want**: To see the outfit update immediately after changing a piece
- **So that**: I can judge the new combination.

**Acceptance Criteria**
1. Given the user is in the outfit builder, when they change a piece, then the visual display updates without reloading the page.

---

### US-51: Remove a piece [SHOULD]
- **As a**: User
- **I want**: To remove a piece from the outfit
- **So that**: I can simplify my look.

**Acceptance Criteria**
1. Given the outfit has a piece, when the user presses "Remove" on it, then the piece is deleted from the outfit.

---

### US-52: Add products from search results [MUST]
- **As a**: User
- **I want**: To add products to the outfit directly from the search results
- **So that**: I do not lose time.

**Acceptance Criteria**
1. Given the user is on the results page, when they look at a product card, then an "Add to outfit" button appears on it.

---

### US-53: See outfit total price [MUST]
- **As a**: User
- **I want**: To see the total price of my outfit
- **So that**: I control my spending.

**Acceptance Criteria**
1. Given the outfit has pieces, when a piece is added, changed or removed, then the total price updates.

---

### US-54: Over-budget warning [MUST]
- **As a**: User
- **I want**: To see a warning when my outfit is over my budget
- **So that**: I can adjust it.

**Acceptance Criteria**
1. Given the user has a budget, when the outfit total is higher than the budget, then a warning message appears.

---

### US-55: See the store of each piece [MUST]
- **As a**: User
- **I want**: To see which store each piece comes from
- **So that**: I know where to buy it.

**Acceptance Criteria**
1. Given the outfit has pieces, when the user looks at a piece, then its store name and price are shown.

---

### US-56: Undo and redo changes [WOULD]
- **As a**: User
- **I want**: To undo and redo my last changes
- **So that**: I can go back if I do not like a change.

**Acceptance Criteria**
1. Given the user made changes to the outfit, when they press undo or redo, then the latest action is reversed or restored.

---

### US-57: Lock a piece [WOULD]
- **As a**: User
- **I want**: To lock a piece
- **So that**: It stays the same while I change the other ones.

**Acceptance Criteria**
1. Given the outfit has pieces, when the user locks a piece with the lock icon, then the piece stays fixed while the other pieces change.

---

### US-58: Style mismatch tips [WOULD]
- **As a**: User
- **I want**: The app to tell me if two pieces do not match well (color or style)
- **So that**: I get better combinations.

**Acceptance Criteria**
1. Given two pieces do not match well in color or style, when they are in the same outfit, then a soft warning with a short reason appears.
2. Given the warning is shown, when the user ignores it, then they can keep the outfit, because it is a tip and not a block.

---

## Epic 7. Outfit Visualization

### US-59: Visual outfit composition [MUST]
- **As a**: User
- **I want**: To see my outfit as a visual composition of the clothes
- **So that**: I can check how the pieces look together.

**Acceptance Criteria**
1. Given the outfit has pieces, when the user opens the display, then the pieces are shown together in one display.

---

### US-60: Virtual mannequin view [WOULD]
- **As a**: User
- **I want**: To see my outfit on a virtual mannequin
- **So that**: It feels closer to real clothes.

**Acceptance Criteria**
1. Given the outfit has pieces, when the user opens the mannequin view, then the pieces are placed on a mannequin.

---

### US-61: Zoom in on the outfit [WOULD]
- **As a**: User
- **I want**: To zoom in on my outfit
- **So that**: I can see the details.

**Acceptance Criteria**
1. Given the outfit is on the display, when the user uses the zoom controls, then the display zooms in and out.

---

### US-62: Switch visualization modes [WOULD]
- **As a**: User
- **I want**: To switch between visualization modes (composition, mannequin, avatar)
- **So that**: I choose what I like most.

**Acceptance Criteria**
1. Given the outfit is on the display, when the user picks another visualization mode, then the mode changes without losing the outfit.

---

## Epic 8. Saved Items, Wishlist and Sharing

### US-63: Save favorite products [SHOULD]
- **As a**: User
- **I want**: To save products to a favorites list
- **So that**: I can find them later.

**Acceptance Criteria**
1. Given the user is looking at a product, when they click the heart icon, then the product is added to or removed from favorites.

---

### US-64: Save outfits with a name [MUST]
- **As a**: User
- **I want**: To save my outfits with a name
- **So that**: I can come back to them.

**Acceptance Criteria**
1. Given the user has an outfit, when they save it with a name, then it is stored in "My outfits" with that name.

---

### US-65: Edit or delete saved outfits [SHOULD]
- **As a**: User
- **I want**: To edit or delete my saved outfits
- **So that**: I keep them organized.

**Acceptance Criteria**
1. Given the user has saved outfits, when they look at a saved outfit, then edit and delete options are available.

---

### US-66: Outfit collections [WOULD]
- **As a**: User
- **I want**: To organize my saved outfits in collections (for example "University", "Party")
- **So that**: I find them faster.

**Acceptance Criteria**
1. Given the user has saved outfits, when they create a collection and add outfits to it, then the outfits appear inside that collection.

---

### US-67: Duplicate a saved outfit [WOULD]
- **As a**: User
- **I want**: To duplicate a saved outfit
- **So that**: I can make a new version without losing the original.

**Acceptance Criteria**
1. Given the user has a saved outfit, when they press "Duplicate", then a copy is created and the original stays the same.

---

### US-68: Buy each piece in its store [MUST]
- **As a**: User
- **I want**: To open the store page of each piece of my outfit
- **So that**: I can buy them one by one.

**Acceptance Criteria**
1. Given the outfit has pieces, when the user presses "Buy" on a piece, then they go to the correct store.

---

### US-69: Export shopping list [SHOULD]
- **As a**: User
- **I want**: To export my shopping list (pieces, stores, prices and links)
- **So that**: I can buy them later.

**Acceptance Criteria**
1. Given the user has an outfit, when they export the shopping list, then the list can be copied or downloaded as PDF or text.

---

## Epic 9. Admin and Data Management

### US-70: Manage stores [MUST]
- **As a**: Admin
- **I want**: To add and manage the stores we collect data from
- **So that**: The catalog stays organized.

**Acceptance Criteria**
1. Given the admin is in the store panel, when they create, edit, activate or deactivate a store, then the change is saved.

---

### US-71: Collect products automatically [MUST]
- **As a**: Admin
- **I want**: The system to collect products automatically from the stores
- **So that**: The catalog is always full.

**Acceptance Criteria**
1. Given a store is active, when the scraping process runs, then the products are saved in the database.

---

### US-72: Schedule data collection [COULD]
- **As a**: Admin
- **I want**: The data collection to run on a schedule (for example every day)
- **So that**: Prices are up to date.

**Acceptance Criteria**
1. Given a schedule is set, when the set time arrives, then the scheduler runs the data collection.

---

### US-73: View collection logs [WOULD]
- **As a**: Admin
- **I want**: To see logs and errors of each data collection
- **So that**: I can fix problems.

**Acceptance Criteria**
1. Given data collection has run, when the admin opens the log page, then the date, store, status and errors are shown.

---

### US-74: Standardize product data [MUST]
- **As a**: Admin
- **I want**: The system to clean and standardize product data (names, colors, sizes, categories)
- **So that**: Filters work well.

**Acceptance Criteria**
1. Given products come from different stores, when the data is processed, then different names for the same color or size are turned into one standard value.

---

### US-75: Review user reports [WOULD]
- **As a**: Admin
- **I want**: To review the reports sent by users
- **So that**: I can correct wrong data.

**Acceptance Criteria**
1. Given users sent reports, when the admin opens the reports page, then a list of reports with status (open, solved) is shown.

---

### US-76: Edit or hide a product [SHOULD]
- **As a**: Admin
- **I want**: To manually edit or hide a product
- **So that**: I can remove bad data.

**Acceptance Criteria**
1. Given the admin is viewing a product, when they edit or hide it, then the change is applied to the product.

---

### US-77: View basic statistics [WOULD]
- **As a**: Admin
- **I want**: To see basic statistics (users, searches, most viewed items)
- **So that**: I understand how the app is used.

**Acceptance Criteria**
1. Given the app has activity, when the admin opens the dashboard, then simple numbers and charts (users, searches, most viewed items) are shown.

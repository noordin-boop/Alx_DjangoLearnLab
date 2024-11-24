# Django Admin Configuration for Book Model

### Registering the Book Model
1. Import the `Book` model in `admin.py` and register it using `@admin.register`.

2. Customize the `Book` model display with `BookAdmin`:
   - **list_display**: Shows `title`, `author`, and `publication_year` in the admin list view.
   - **search_fields**: Enables search functionality by `title` and `author`.
   - **list_filter**: Adds a filter for `publication_year`.

### Expected Outcome
Once configured, the Django admin will display the `Book` model with enhanced management features:
- Search by title and author.
- Filter by publication year.

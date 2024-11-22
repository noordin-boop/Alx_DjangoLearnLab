Here’s a detailed README file documenting how permissions and groups are configured and used in the project:

---

## **Permissions and Groups Setup in Django**

### **Overview**
This project demonstrates the use of **permissions** and **groups** in Django to restrict access to certain actions and views. Permissions are assigned to specific groups, and users in those groups can perform only the actions allowed by their assigned permissions.

---

### **Permissions Configuration**

#### **Custom Permissions**
The following custom permissions are defined in the `Book` model:

- **`can_view`**: Allows users to view a list of books.
- **`can_create`**: Allows users to create a new book entry.
- **`can_edit`**: Allows users to edit an existing book entry.
- **`can_delete`**: Allows users to delete a book entry.

These permissions are added in the `Book` model using the `Meta` class:

```python
class Meta:
    permissions = [
        ('can_view', 'Can view books'),
        ('can_create', 'Can create books'),
        ('can_edit', 'Can edit books'),
        ('can_delete', 'Can delete books'),
    ]
```

---

### **Groups Configuration**

The following groups are set up in the Django admin:

1. **Viewers**
   - Permissions: `can_view`
   - Users in this group can only view the list of books.

2. **Editors**
   - Permissions: `can_view`, `can_create`, `can_edit`
   - Users in this group can view, create, and edit books.

3. **Admins**
   - Permissions: All (`can_view`, `can_create`, `can_edit`, `can_delete`)
   - Users in this group have full access to manage books.

To manage groups:
1. Log in to the Django admin site.
2. Navigate to the **Groups** section.
3. Add or edit groups and assign the relevant permissions.

---

### **Enforcing Permissions in Views**

Permissions are enforced in views using Django’s `@permission_required` decorator. For example:

```python
@permission_required('yourapp.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'yourapp/book_list.html', {'books': books})
```

If a user does not have the required permission, they will receive a **403 Forbidden** response.

---

### **Testing the Permissions**

1. **Create Users and Assign Groups**
   - Create test users in the Django admin.
   - Assign them to the `Viewers`, `Editors`, or `Admins` groups.

2. **Test User Access**
   - Log in as different users and attempt to access the following endpoints:
     - `/books/`: View all books (requires `can_view`).
     - `/books/create/`: Create a new book (requires `can_create`).
     - `/books/<id>/edit/`: Edit a book (requires `can_edit`).
     - `/books/<id>/delete/`: Delete a book (requires `can_delete`).

3. **Expected Results**
   - Users should only be able to access views permitted by their group’s permissions.
   - Unauthorized users should receive a **403 Forbidden** error.

---

### **How to Set Up Permissions and Groups**

1. **Add Custom Permissions to Models**
   - Use the `Meta` class in the model to define custom permissions.

2. **Create Groups in Admin**
   - Navigate to the **Groups** section in the Django admin.
   - Create groups and assign permissions using the checkboxes.

3. **Assign Users to Groups**
   - Navigate to the **Users** section in the Django admin.
   - Assign users to groups via the **Groups** field in the user form.

4. **Use Permissions in Views**
   - Protect views using the `@permission_required` decorator.
   - Pass the permission string (e.g., `yourapp.can_view`) as an argument.

---

### **Project File Overview**

1. **`models.py`**
   - Defines the `Book` model and custom permissions.

2. **`admin.py`**
   - Configures admin interfaces for managing books and users.

3. **`views.py`**
   - Implements views with permissions enforced.

4. **`urls.py`**
   - Maps URLs to permission-protected views.

5. **Templates**
   - `book_list.html`: Displays all books.
   - `book_form.html`: Used for creating and editing books.
   - `book_confirm_delete.html`: Confirms deletion of a book.

---

### **Notes**

- Permissions are granular and linked to specific actions in the model.
- Groups simplify user management by assigning a set of permissions to multiple users at once.
- Ensure that `AUTH_USER_MODEL` is correctly set to a custom user model if you’re using one.

---

Let me know if you need this in a downloadable file format!
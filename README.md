# Prototype
# Author Raymond T. Niemczura
# Creation Date: 2/1/2022
# Last Modification Date: 3/4/22
#
# 3/4/22 - Added Python-app.yaml to build, test, and run changes to python code
# 
# Mongo DB Module Additions
# 1) pymongo_create_insert_emp.py - Creates, and populates an employee collection in employee_db.
# 2) pymongo_query_emp.py - display the entire employee collection, and then displays a new collection by selecting a field value.
# 3) pymongo_change_emp.py - displays the employee collection before and after changing one value.
# 4) pymongo_delete_emp.py - displays the employee collection before and after deleting on element.

# Two distinct paths were used to create, modify, and delete entries from a sqlite databases
# 1) Object oriented modules
# 2) Rest API using Flask modules
#
# Object oriented modules - The following describes how to run this approach as well as a description of the modules:
#    1) oo_run_crud_test.cmd - executes the following python modules:
#       a) oo_create_sqlite_db.py - creates sqlite database oo_datebase.db
#       b) oo_create_widget_table.py - creates widget table in the sqlite database
#       c) oo_crud_widget_commands.py - populates the widget table in the sqlite database
#    2) These files can be downloaded into any windows directory. My testing occurred in the c:\sqlite directory
#
# Rest API modules - The following describes how to run this approach as well as description of the module. This method uses the flask framework.
#    1) The following files were created in the parent directory in my case c:\sqlite\flask_app:
#       a) app.py - this file handles the setup, and execution of the html files(base, create, edit, and delete) in the template directory
#       b) init_db.py - create sqlite database named database.db using schema.sql which creates the widget table with 2 test widgets
#       c) schema.sql - creates the widget table
#       d) flask_setup.cmd - this file sets up the flask environment to run for the windows environment. SET is for windows. EXPORT would be used for linux
#    2) The following files were created in the template directory in my case c:\sqlite\flask_app\template directory
#       a) base.html - displays the contents of the sqlite database
#       b) create.html - create new widget rows
#       c) edit.html - edits existing widget rows
#       d) delete.html - deletes existing widget rows
#    3) Execution instructions
#       a) execute flask_setup.cmd from a command line in the parent directory in my case c:\sqlite\flask_app.  This will log entries as widget are processed
#       b) Launch a browser window and enter address http://127.0.0.1:5000/
#          . The window displays all of the rows in the widget table
#          . Click the Create link to add new widget rows
#          . Click the Edit button to change a widget.  This option also has an option to delete a widget. Click the Submit button when done
#          . The rows in the database are displayed again when the operation is complete.
#       c) Close the browser window, and enter Control C in the command window

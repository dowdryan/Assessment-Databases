### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
  - PSQL/PostgreSQL is an open-source database management system that uses it SQL extensions to help write queries, store data, and many other functions.

- What is the difference between SQL and PostgreSQL?
  - SQL: The language used to manipulate the relational databases.
  - PostgreSQL: A relational database management system.

- In `psql`, how do you connect to a database?
  - Connecting to a database requires you to enter a specific command: ```psql -h hostname -p port -U username -d database_name```. The hostname, port, username, and database_name values should be swapped for the neccessary values.

- What is the difference between `HAVING` and `WHERE`?
  - HAVING: Used to filter rows once they have been grouped.
  - WHERE: Used to filter rows before they are grouped.

- What is the difference between an `INNER` and `OUTER` join?
  - INNER: Joins specific rows where there are matching conditions in the specified tables.
  - OUTER: Joins matching rows from the specified tables and includes unmatched rows from the tables.

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
  - LEFT OUTER: Join all of the rows from the left table, alongside the matching rows from the right table.
  - RIGHT OUTER: Join all of the rows from the right table, alongside the matching rows from the left table. 

- What is an ORM? What do they do?
  - ORM/Object-Relational Mapping is a programming technique that helps connect object-oriented programming languages and relational databases, making it easy to move and work with data between them.

- What are some differences between making HTTP requests using AJAX and from the server side using a library like `requests`?
  - AJAX:
    - Executed on client side.
    - Uses JavaScript.
    - Can make asynchronous requests from the client to the server.
  - Requests: 
    - Executed on server side.
    - Uses whatever language the server uses.
    - Used on the server to interact with other servers, APIs, or web services.

- What is CSRF? What is the purpose of the CSRF token?
  - CSRF/Cross-Site Request Forgery refers to a type of cyberattack where an attacker manipulates another user's browser into making harmful requests to a web application.
  - A CSRF Token is a unique token added to each request, reducing the risk of forge requests from attackers. In doing so, they ensure that each request originates from a trustworthy source.

- What is the purpose of `form.hidden_tag()`?
  - form.hidden_tag() is a function used to incorporate a hidden HTML input field with a CSRF token, offering a convenient means to enhance security against potential attackers by including the CSRF token within a Flask-WTF form.

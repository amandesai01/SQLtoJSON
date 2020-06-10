<h1 align="center">SQLtoJSON</h1>
<div align="center">
<br>
[![](https://img.shields.io/badge/Made_with-Python-red?style=for-the-badge&logo=python)](https://www.python.org/ "Python")
[![](https://img.shields.io/badge/IDE-Visual_Studio_Code-red?style=for-the-badge&logo=visual-studio-code)](https://code.visualstudio.com/  "Visual Studio Code")
<br>
</div>
<h3> Meet your an amazing middleware for your MySQL operations. </h3>

<b>Just a Single line to connect and single line to execute, and boom! You have your response in JSON.</b><br>
<strong> Say Good Bye to Cursors, Connections, MySQL Drivers. This package has everything covered. And that is not the best part.</strong><br>

Best part is you get an easy to use web interface where you can see your "in-code" query history and try new queries.
Wanna change DB connection? Again, this package has got you covered. 

## Usage
```Python
from pypackage import s2j

db = s2j.s2j("localhost", "root", "password", "database") # Connected.

# Now oneliners for your queries!!!!!!
response = db.execQuery("SELECT * FROM users;")
print(response['data'])
```
## Output:
```
[
  {
    "fullname" : "Aman Desai",
    "email" : "aman.desai@somaiya.edu",
    "website" : "https://amandesai01.github.io"
  },
  {
  ...
  ...
  },
  ...
]
```

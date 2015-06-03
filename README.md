# pshitt-parser
A Parsing / Output tool for pshitt json logs and displaying them on your website.
https://github.com/regit/pshitt


# Usage:

- Modify the parser.py script to point to the path for your pshitt output

```
f = open('/path/to/passwords.json')
```

Set a cronjob to run at a set interval to update the page

```
*/5 * * * * python /path/to/pshitt-master/parser.py > /usr/share/nginx/html/index.html
```

You're all done!

Using Skeleton framework for css/tables - http://getskeleton.com/


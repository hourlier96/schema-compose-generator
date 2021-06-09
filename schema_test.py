from diagrams import Cluster, Diagram
from diagrams.onprem.database import *
from diagrams.onprem.compute import *

body = {
    "mysql": {
        "langage": "SQL",
        "ports": [
            "3306"
        ]
    },
    "phpmyadmin": {
        "langage": "Php",
        "ports": [
            "8080:80"
        ]
    },
    "vue-js": {
        "langage": "Js",
        "framework": "Vue",
        "ports": [
            "5050:8080"
        ]
    },
    "php": {
        "langage": "Php",
        "ports": [
            "9000:9001"
        ]
    },
    "nginx": {
        "depends_on": [
            "php"
        ]
    },
    "mercure": {},
    "traefik": {}
}

str = """ with Diagram("test stuf"):
    \t test = Mariadb("test")
    with Cluster("cluster stuff"):
        grp = Server("test server")
        test << grp" """

with open("test.py", "a+") as f:
    f.write(
        "from diagrams import Cluster, Diagram \nfrom diagrams.onprem.database import * \nfrom diagrams.onprem.compute import *")
    f.write(str)

# with Diagram("test stuf"):
#     test = Mariadb("test")
#     with Cluster("cluster stuff"):
#         grp = Server("test server")
#         test << grp

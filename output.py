
from diagrams import Cluster, Diagram
from diagrams.aws.compute import *
from diagrams.aws.database import *
from diagrams.onprem.database import *
from diagrams.onprem.compute import *
from diagrams.onprem.network import *
from diagrams.programming.framework import *
from diagrams.programming.language import *


with Diagram("Docker-compose diagram", show=False):
	# Create Diagrams: Docker-compose diagram
	with Cluster("Network"):
		elem_mysql = Mysql("Mysql")

		elem_php = Php("Php")

		elem_vue = Vue("Vue")

		elem_php = Php("Php")

		elem_nginx = Nginx("Nginx")

		elem_traefik = Traefik("Traefik")

	elem_php >> elem_mysql
	elem_php >> elem_mysql


from diagrams import Cluster, Diagram
from diagrams.aws.compute import *
from diagrams.aws.database import *
from diagrams.onprem.database import *
from diagrams.onprem.compute import *
from diagrams.onprem.network import *
from diagrams.aws.database import *
from diagrams.aws.integration import *
from diagrams.aws.storage import *
from diagrams.aws.security import *
from diagrams.programming.framework import *
from diagrams.programming.flowchart import *
from diagrams.custom import *
from diagrams.onprem.storage import *
from diagrams.gcp.api import *
from diagrams.gcp.compute import *
from diagrams.gcp.database import *
from diagrams.aws.compute import *
from diagrams.k8s.controlplane import *
from diagrams.programming.language import *


with Diagram("Docker-compose diagram", show=False):
	# Create Diagrams: Docker-compose diagram
	with Cluster("Entrypoint"):
		elem_traefik = Traefik("traefik")

		with Cluster("Traefik network"):
			elem_mysql = Mysql("mysql")

			elem_phpmyadmin = Php("phpmyadmin")

			elem_vue_js = Vue("vue-js")

			elem_api = API("api")

			elem_nginx = Nginx("nginx")

			elem_mercure = SecurityHub("mercure")

	elem_phpmyadmin >> elem_mysql
	elem_vue_js >> elem_api
	elem_vue_js >> elem_mercure
	elem_api >> elem_mercure
	elem_api >> elem_mysql
	elem_nginx >> elem_vue_js
	elem_nginx >> elem_api
	elem_nginx >> elem_phpmyadmin
	elem_nginx >> elem_mysql
	elem_mercure >> elem_vue_js
	elem_mercure >> elem_api
	elem_traefik >> elem_nginx

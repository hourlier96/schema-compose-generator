
from diagrams import Cluster, Diagram
from diagrams.aws.compute import *
from diagrams.onprem.database import *
from diagrams.onprem.compute import *


with Diagram("mon diag", show=False):
	# Create Diagrams: mon diag
	with Cluster("my cluster"):
		elem_server = Server("Server")

		elem_lambda = Lambda("Lambda")

	elem_server >> elem_lambda

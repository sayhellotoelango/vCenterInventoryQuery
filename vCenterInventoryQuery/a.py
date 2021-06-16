import requests
import urllib3
from vmware.vapi.vsphere.client import create_vsphere_client
from com.vmware.vcenter_client import (Folder,Host,Cluster)

session = requests.session()

# Disable cert verification for demo purpose. 
# This is not recommended in a production environment.
session.verify = False

# Disable the secure connection warning for demo purpose.
# This is not recommended in a production environment.
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Connect to a vCenter Server using username and password
vsphere_client = create_vsphere_client(server='10.27.47.88', username='administrator@vsphere.local', password='VMware123!', session=session)


datacenters=vsphere_client.vcenter.Datacenter.list()

for dc in datacenters:
	print(dc.name)
	clusters=vsphere_client.vcenter.Cluster.list(Cluster.FilterSpec(datacenters=set([dc.datacenter])))
	# print(clusters)
	for c in clusters:
		print("\t"+c.name)
		hosts=vsphere_client.vcenter.Host.list(Host.FilterSpec(clusters=set([c.cluster])))
		# print(hosts)
		for host in hosts:
			print("\t\t"+host.name)
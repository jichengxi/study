import requests

baseurl = "https://127.0.0.1:8443"
headers = {"Content-type": "application/json"}
data = {"operationType": "relocate",
        "sourceSite": "old-vc",
        "targetSite": "new-vc",
        "sourceDatacenter": "vccs02",
        "vmList": ["test-move-04"],
        "targetDatacenter": "PRO-DC",
        "targetHost": "172.24.39.101",
        "targetDatastore": "172.24.39.101-2",
        "targetCluster": None,
        "targetPool": None,
        "targetFolder": "test",
        "networkMap":
            {"Manage-1215-128 (DistributedVirtualPortgroup)": "Manage-1215-128 (DistributedVirtualPortgroup)",
             "OTC-NJ|APP_ANP|APP-053-PAY-2_EPG (DistributedVirtualPortgroup)": "OTC-NJ|APP_ANP|APP-053-PAY-2_EPG (DistributedVirtualPortgroup)"}
        }

url = baseurl + "/api/tasks"
res = requests.post(url, json=data, headers=headers, verify=False)



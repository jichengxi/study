from kubernetes import client, watch
import socket
from prometheus_client import Gauge
from prometheus_client.core import CollectorRegistry

# namespace = '1--94327399'
namespace = '1--14610456'
ApiToken = 'eyJhbGciOiJSUzI1NiIsImtpZCI6IiJ9.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJpbmZyYSIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VjcmV0Lm5hbWUiOiJjcm8tcmVhZG9ubHktdG9rZW4tNXdzcWgiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC5uYW1lIjoiY3JvLXJlYWRvbmx5Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQudWlkIjoiNjcxMGU1N2UtYmEzZi0xMWViLThjMmUtMDA1MDU2OTM5ZWNiIiwic3ViIjoic3lzdGVtOnNlcnZpY2VhY2NvdW50OmluZnJhOmNyby1yZWFkb25seSJ9.A7cCf2Z78aMpxwd-31DBD9ZAXF0JqykKapYaJ03YbPG3h6-F3Bvan2xd7HO1NjXtram62q021YkOCkQgA_kP1rDupkbMV_I1hnK8m0KCOla802pgOc33P3Y8om0xEuxuKw2FYMkA5yno9QpndIiLBkMbLEgtn86AZZmhWJKgYvLIKecPngMYOTZEK-H9nzrXi4bWrO84IfYfNQ9_QOuHdvTdIooDMXvr7gMSMCxd7y21T6_qqr2GoatF3WjLEaB5BZsEtWcZ_VKlxPO8hmt1TGYxt30KQ-DsTYgHpdhdJBBcb1J8ReiVK2PU4iyOX1FlvpswR_3iaIAqxB4A-hEkOg'
configuration = client.Configuration()
configuration.host = "https://172.29.32.173:7443"
configuration.verify_ssl = False
configuration.debug = True
configuration.api_key = {"authorization": "Bearer " + ApiToken}
api_client_config = client.ApiClient(configuration)
api_obj = client.CoreV1Api(api_client_config)

register = CollectorRegistry()
KafkaEndpointStatus = Gauge(name='kafka_broker_status',
                            documentation='kafka broker status in kubernetes cluster',
                            labelnames=['service_name',
                                        'pod_name',
                                        'pod_ip'])


# 端口检测
def check_port(ip_address, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((str(ip_address), int(port)))
    return result


ret = api_obj.list_namespaced_endpoints(namespace).items
service_dict_last = {}
service_dict_latest = {}
for a in ret:
    service_name = a.metadata.name
    service_dict_latest[service_name] = []
    for b in a.subsets[0].addresses:
        pod_name = b.hostname
        pod_ip = b.ip
        service_dict_latest[service_name].append(pod_ip)
        KafkaEndpointStatus.labels(service_name, pod_name, pod_ip).set(0)
        service_dict_last = service_dict_latest



# w = watch.Watch()
# for event in w.stream(api_obj.list_endpoints_for_all_namespaces):
#     if (event['object'].metadata.name != 'kube-controller-manager' )









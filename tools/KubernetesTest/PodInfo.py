from kubernetes import client, config, watch
from KubernetesTest.Tools import EventHandle

config.kube_config.load_kube_config(config_file="kubeconfig.yaml")

# 获取API的CoreV1Api版本对象
v1 = client.CoreV1Api()

w = watch.Watch()
for event in w.stream(v1.list_pod_for_all_namespaces):
    if event['object'].metadata.namespace == 'app01':
        EventHandle(event)

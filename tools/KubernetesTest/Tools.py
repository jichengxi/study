import logging

logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    # filename='new.log',
                    # filemode='w',
                    level=logging.DEBUG)


def EventHandle(event):
    """
    'event_type': 事件类型,
    'pod_name': pod名称,
    'controller_type': 控制器类型,
    'controller_name': 控制器名称,
    'namespace': pod所在命名空间,
    'pod_create_time': pod创建时间,
    'pod_delete_time': pod删除时间,
    'host_ip': pod所在主机IP,
    'pod_i_ps': pod所有IP,
    'pod_ip': pod默认路由IP,
    'pod_status': pod状态,
    'pod_start_time': pod启动时间,
    'container_id': 容器ID,
    'container_name': 容器名称,
    'container_image': 容器镜像,
    'container_ready': 容器是否就绪,
    'container_started': 容器是否启动,
    'container_restart_count': 容器重启次数,
    'container_last_state_running': 上一次容器running时状态 // 不确定需不需要的字段
    'container_last_state_terminated': 上一次容器terminated时状态 // 不确定需不需要的字段
    'container_last_state_waiting': 上一次容器waiting时状态 // 不确定需不需要的字段
    'container_started_at': 容器启动时间,
    'container_exit_code': 容器退出状态码,
    'container_finished_at': 容器停止时间,
    'container_finished_message': 容器停止的信息,
    'container_finished_reason': 容器停止的原因,
    'container_waiting_message': 容器等待的信息,
    'container_waiting_reason': 容器等待的原因,
    'init_container_statuses': 初始化容器状态  // 待定
    """
    event_type = event['type']
    pod_name = event['object'].metadata.name
    controller_type = event['object'].metadata.owner_references[0].kind if event['object'].metadata.owner_references else 'Pod'
    controller_name = event['object'].metadata.owner_references[0].name if event['object'].metadata.owner_references else None
    namespace = event['object'].metadata.namespace
    pod_create_time = event['object'].metadata.creation_timestamp
    pod_delete_time = event['object'].metadata.deletion_timestamp
    init_container_statuses = None
    host_ip = event['object'].status.host_ip
    pod_i_ps = event['object'].status.pod_i_ps
    pod_ip = event['object'].status.pod_ip
    pod_status = event['object'].status.phase
    pod_start_time = event['object'].status.start_time
    container_id = None
    container_name = None
    container_image = None
    container_ready = None
    container_started = None
    container_restart_count = None
    container_last_state_running = None
    container_last_state_terminated = None
    container_last_state_waiting = None
    container_started_at = None
    container_exit_code = None
    container_finished_at = None
    container_finished_message = None
    container_finished_reason = None
    container_waiting_message = None
    container_waiting_reason = None

    if event['object'].status.container_statuses:
        for i in event['object'].status.container_statuses:
            container_id = i.container_id
            container_name = i.name
            container_image = i.image
            container_ready = i.ready
            container_started = i.started
            container_restart_count = i.restart_count
            container_last_state_running = i.last_state.running
            container_last_state_terminated = i.last_state.terminated
            container_last_state_waiting = i.last_state.waiting
            if i.state.running:
                container_started_at = i.state.running.started_at
            if i.state.terminated:
                container_exit_code = i.state.terminated.exit_code
                container_started_at = i.state.terminated.started_at
                container_finished_at = i.state.terminated.finished_at
                container_finished_message = i.state.terminated.message
                container_finished_reason = i.state.terminated.reason
            if i.state.waiting:
                container_waiting_message = i.state.waiting.message
                container_waiting_reason = i.state.waiting.reason

    # 新建pod逻辑
    if event_type == 'MODIFIED' and pod_delete_time is None and pod_status == 'Running':
        apiVersion = event['object'].api_version
        Kind = event['object'].kind
        spec = str(event['object'].spec)
        metadata = {'annotations': event['object'].metadata.annotations,
                    'generateName': event['object'].metadata.generate_name,
                    'labels': event['object'].metadata.labels,
                    'name': event['object'].metadata.name,
                    'namespace': event['object'].metadata.namespace,
                    'ownerReferences': str(event['object'].metadata.owner_references)}
        workload = {
            'apiVersion': apiVersion,
            'Kind': Kind,
            'metadata': metadata,
            'spec': spec
        }
        logging.info(workload)

    # 删除pod逻辑
    if event['type'] == 'DELETED' and event['object'].metadata.deletion_timestamp:
        name = event['object'].metadata.name
        logging.info(name)

    event_data = {
        'event_type': event_type,
        'pod_name': pod_name,
        'controller_type': controller_type,
        'controller_name': controller_name,
        'namespace': namespace,
        'pod_create_time': pod_create_time,
        'pod_delete_time': pod_delete_time,
        'host_ip': host_ip,
        'pod_i_ps': pod_i_ps,
        'pod_ip': pod_ip,
        'pod_status': pod_status,
        'pod_start_time': pod_start_time,
        'container_id': container_id,
        'container_name': container_name,
        'container_image': container_image,
        'container_ready': container_ready,
        'container_started': container_started,
        'container_restart_count': container_restart_count,
        'container_last_state_running': container_last_state_running,
        'container_last_state_terminated': container_last_state_terminated,
        'container_last_state_waiting': container_last_state_waiting,
        'container_started_at': container_started_at,
        'container_exit_code': container_exit_code,
        'container_finished_at': container_finished_at,
        'container_finished_message': container_finished_message,
        'container_finished_reason': container_finished_reason,
        'container_waiting_message': container_waiting_message,
        'container_waiting_reason': container_waiting_reason,
        'init_container_statuses': init_container_statuses,
    }
    logging.debug(event_data)





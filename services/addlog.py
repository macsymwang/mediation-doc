import re
import json

def parse_markdown(config_path):
    # Read the configuration file
    with open(config_path, 'r') as config_file:
        config = json.load(config_file)
        namespace = config.get('namespace')
        input_file = config.get('input_file')
        output_file = config.get('output_file')

    with open(input_file, 'r') as file:
        lines = file.readlines()

    new_lines = []
    url_template_st = ("https://console.cloud.google.com/logs/query;duration=PT1H;query=resource.type%3D%22k8s_container%22%0Aresource.labels.project_id%3D%22cdo-gke-private-np-1a8686%22%0Aresource.labels.location%3D%22northamerica-northeast1%22%0Aresource.labels.cluster_name%3D%22private-na-ne1-001%22%0Aresource.labels.namespace_name%3D%22{namespace}%22%0Aresource.labels.container_name%3D%22{service_name}%22;storageScope=storage,projects%2Fcio-logging-storage-1b866dc7%2Flocations%2Fnorthamerica-northeast1%2Fbuckets%2Flogsink_bucket_kitchen_sink%2Fviews%2F_AllLogs?project=cio-logging-storage-1b866dc7")
    url_template_pr = ("https://console.cloud.google.com/logs/query;duration=PT1H;query=resource.type%3D%22k8s_container%22%0Aresource.labels.project_id%3D%22cdo-gke-private-pr-7712d7%22%0Aresource.labels.location%3D%22northamerica-northeast1%22%0Aresource.labels.cluster_name%3D%22private-na-ne1-001%22%0Aresource.labels.namespace_name%3D%22{namespace}%22%0Aresource.labels.container_name%3D%22{service_name}%22;storageScope=storage,projects%2Fcio-logging-storage-1b866dc7")

    for line in lines:
        new_lines.append(line)
        if line.startswith('*'):
            match = re.search(r'\[(.*?)\]', line)
            if match:
                service_name = match.group(1)
                if service_name.endswith('-st'):
                    log_url = url_template_st.format(service_name=service_name, namespace=namespace)
                elif service_name.endswith('-pr'):
                    log_url = url_template_pr.format(service_name=service_name, namespace=namespace)
                else:
                    continue
                new_lines.append(f"[log]({log_url})\n")

    with open(output_file, 'w') as file:
        file.writelines(new_lines)

# Call the function with the path to your configuration file
parse_markdown('./services/config.json')
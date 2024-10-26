import re

def parse_markdown(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    new_lines = []
    log_url_template = ("https://console.cloud.google.com/logs/query;duration=PT1H;query=resource.type%3D%22k8s_container%22%0Aresource.labels.project_id%3D%22cdo-gke-private-np-1a8686%22%0Aresource.labels.location%3D%22northamerica-northeast1%22%0Aresource.labels.cluster_name%3D%22private-na-ne1-001%22%0Aresource.labels.namespace_name%3D%22mediation-data%22%0Aresource.labels.container_name%3D%22{service_name}%22;storageScope=storage,projects%2Fcio-logging-storage-1b866dc7%2Flocations%2Fnorthamerica-northeast1%2Fbuckets%2Flogsink_bucket_kitchen_sink%2Fviews%2F_AllLogs?project=cio-logging-storage-1b866dc7")

    for line in lines:
        new_lines.append(line)
        if line.startswith('*'):
            match = re.search(r'\[(.*?)\]', line)
            if match:
                service_name = match.group(1)
                log_url = log_url_template.format(service_name=service_name)
                new_lines.append(f"[log]({log_url})\n")

    with open('np_modified.md', 'w') as file:
        file.writelines(new_lines)

# Call the function with the path to your markdown file
parse_markdown('./services/np.md')
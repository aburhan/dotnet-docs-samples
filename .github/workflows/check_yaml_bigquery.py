import os
import yaml
import google.cloud.bigquery
from github import Github

def load_yaml(filepath):
    with open(filepath, 'r') as f:
        return yaml.safe_load(f)

def update_yaml(filepath, data):
    with open(filepath, 'w') as f:
        yaml.safe_dump(data, f)

def query_bigquery(name, container, namespace):
    client = google.cloud.bigquery.Client()
    query = f"SELECT cpu, memory FROM `github-action-393418.test.test` where name = '{name}' and container_name= '{container}' and namespace = '{namespace}'"
    query_job = client.query(query)
    result = query_job.result()
    return result.to_dataframe()

def main():
    with open('multi_doc.yml', 'r') as file:
    docs = yaml.safe_load_all(file)

    for doc in docs:
        print(doc)
    yaml_files = os.listdir('../../manifests')
    print(yaml_files)
    yaml_files = [f for f in yaml_files if f.endswith('.yaml')]
    print(yaml_files)
    quit()
    for file in yaml_files:
        yaml_data = load_yaml(file)
        print(yaml_data)
        
        kind = yaml_data.get('kind', '')
        if kind in ['Deployment', 'StatefulSet', 'Pod', 'Job', 'CronJob', 'DaemonSet']:
            metadata = yaml_data.get('metadata', {})
            spec = yaml_data.get('spec', {}).get('containers', [{}])[0]
            name = metadata.get('name')
            namespace = metadata.get('namespace')
            container = spec.get('name')
            if name and namespace and container:
                df = query_bigquery(name, container, namespace)
                if not df.empty:
                    resources = spec.get('resources', {})
                    resources['requests'] = {'cpu': df['cpu'][0], 'memory': df['memory'][0]}
                    spec['resources'] = resources
                    yaml_data['spec']['containers'][0] = spec
                    update_yaml(file, yaml_data)
    return

if __name__ == "__main__":
    main()

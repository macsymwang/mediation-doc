- [CCS WHSIA Dashboard](#ccs-whsia-dashboard)
  - [CCS WHSIA TDR Stream](#ccs-whsia-tdr-stream)
  - [CCS WHSIA BLOCK EDR Stream](#ccs-whsia-block-edr-stream)
  - [CCS WHSIA MAINT EDR Stream](#ccs-whsia-maint-edr-stream)
  - [CCS WHSIA Firestore Stream](#ccs-whsia-firestore-stream)
- [SGSN  Dashboard](#sgsn--dashboard)
- [CCS Prepaid](#ccs-prepaid)
  - [CCS Prepaid EDR Stream](#ccs-prepaid-edr-stream)
  - [CCS Prepaid Voice TDR Stream](#ccs-prepaid-voice-tdr-stream)
  - [CCS Prepaid SMS/MMS TDR Stream](#ccs-prepaid-smsmms-tdr-stream)
  - [CCS Prepaid Traffic Control Stream](#ccs-prepaid-traffic-control-stream)
  - [CCS Prepaid Firestore Stream](#ccs-prepaid-firestore-stream)
- [Ericson DMC PGW(EDMC)](#ericson-dmc-pgwedmc)
- [Common Service](#common-service)

## CCS WHSIA [Dashboard](https://console.cloud.google.com/monitoring/dashboards/builder/1d377a4b-e402-4ae4-8e1e-82282b9ce200;duration=PT1H?inv=1&invt=AbfjKg&project=cio-stackdriver-np-b75434&pageState=(%22eventTypes%22:(%22selected%22:%5B%22CLOUD_ALERTING_ALERT%22,%22GKE_WORKLOAD_DEPLOYMENT%22,%22CLOUD_SQL_STORAGE%22%5D)))

### CCS WHSIA TDR Stream
* [ccs-pbsstr-data-tdr-collection-st](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-pbsstr-data-tdr-collection-st/overview?project=cdo-gke-private-np-1a8686)
* [ccs-pbs-mb-tier-tdr-collection-st](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-pbs-mb-tier-tdr-collection-st/overview?project=cdo-gke-private-np-1a8686)
* [ccs-pbsstr-data-tdr-processing-st](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-pbsstr-data-tdr-processing-st/overview?project=cdo-gke-private-np-1a8686)
* [ccs-pbs-mb-tdr-matrixx-storage-st](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-pbs-mb-tdr-matrixx-storage-st/overview?project=cdo-gke-private-np-1a8686)
* [ccs-pbs-mb-filtered-tdr-storage-st](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-pbs-mb-filtered-tdr-storage-st/overview?authuser=0&project=cdo-gke-private-np-1a8686)
* [ccs-pbs-mb-tdr-tostream-st](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-pbs-mb-tdr-tostream-st/overview?authuser=0&project=cdo-gke-private-np-1a8686)

### CCS WHSIA BLOCK EDR Stream
* [ccs-pbs-mb-block-edr-collection-st](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-pbs-mb-block-edr-collection-st/overview?authuser=0&project=cdo-gke-private-np-1a8686)
* [ccs-pbsstr-data-block-edr-processing-st](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-pbsstr-data-block-edr-processing-st/overview?authuser=0&project=cdo-gke-private-np-1a8686)
* [ccs-pbs-mb-edr-block-storage-st](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-pbs-mb-edr-block-storage-st/overview?authuser=0&project=cdo-gke-private-np-1a8686)

### CCS WHSIA MAINT EDR Stream
* [ccs-stream-pubsub-edr-maint-collection-st](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-stream-pubsub-edr-maint-collection-st/overview?authuser=0&project=cdo-gke-private-np-1a8686)
* [ccs-pbsstr-data-maint-edr-processing-st](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-pbsstr-data-maint-edr-processing-st/overview?authuser=0&project=cdo-gke-private-np-1a8686)
* [ccs-pbs-mb-edr-maint-storage-st](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-pbs-mb-edr-maint-storage-st/overview?authuser=0&project=cdo-gke-private-np-1a8686)
* [ccs-pbs-mb-edr-maint-tostream-st](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-pbs-mb-edr-maint-tostream-st/overview?authuser=0&project=cdo-gke-private-np-1a8686)

### CCS WHSIA Firestore Stream
* [ccs-stream-pubsub-firestore-tdr-collection-st](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-stream-pubsub-firestore-tdr-collection-st/overview?authuser=0&project=cdo-gke-private-np-1a8686)
* [ccs-stream-pubsub-firestore-tier-tdr-collection-st](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-stream-pubsub-firestore-tier-tdr-collection-st/overview?authuser=0&project=cdo-gke-private-np-1a8686)
* [ccs-stream-pubsub-firestore-edr-block-collection-st](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-stream-pubsub-firestore-edr-block-collection-st/overview?authuser=0&project=cdo-gke-private-np-1a8686)
* [ccs-stream-pubsub-firestore-edr-maint-collection-st](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-stream-pubsub-firestore-edr-maint-collection-st/overview?authuser=0&project=cdo-gke-private-np-1a8686)
* [ccs-pubsub-microbatch-tdr-firestore-storage-st](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-pubsub-microbatch-tdr-firestore-storage-st/overview?authuser=0&project=cdo-gke-private-np-1a8686)
* [ccs-pubsub-microbatch-edr-maint-firestore-storage-st](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-pubsub-microbatch-edr-maint-firestore-storage-st/overview?authuser=0&project=cdo-gke-private-np-1a8686)  
  [log](https://console.cloud.google.com/logs/query;duration=PT1H;query=resource.type%3D%22k8s_container%22%0Aresource.labels.project_id%3D%22cdo-gke-private-np-1a8686%22%0Aresource.labels.location%3D%22northamerica-northeast1%22%0Aresource.labels.cluster_name%3D%22private-na-ne1-001%22%0Aresource.labels.namespace_name%3D%22mediation-data%22%0Aresource.labels.container_name%3D%22ccs-pubsub-microbatch-edr-maint-firestore-storage-st%22;storageScope=storage,projects%2Fcio-logging-storage-1b866dc7%2Flocations%2Fnorthamerica-northeast1%2Fbuckets%2Flogsink_bucket_kitchen_sink%2Fviews%2F_AllLogs?project=cio-logging-storage-1b866dc7)
* [ccs-pubsub-microbatch-edr-block-firestore-storage-st](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-pubsub-microbatch-edr-block-firestore-storage-st/overview?authuser=0&project=cdo-gke-private-np-1a8686)


## SGSN  [Dashboard](https://console.cloud.google.com/monitoring/dashboards/builder/d5d20af4-3016-424b-acc9-8bb34cbbeb7b;duration=PT1H?project=cio-stackdriver-np-b75434&pageState=(%22events%22:(%22active%22:%5B%22CLOUD_ALERTING_ALERT%22,%22GKE_WORKLOAD_DEPLOYMENT%22,%22CLOUD_SQL_STORAGE%22%5D,%22inactive%22:%5B%5D)))
* [netops-sgw-sgsn-sftp-collection-st](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/netops-lab-01/mediation-control/netops-sgw-sgsn-sftp-collection-st/overview?project=tu-nfv-cio-mediation-01-pr)
* [sgw-sgsn-ext-pubsub-raw-collection-st](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/sgw-sgsn-ext-pubsub-raw-collection-st/overview?project=cdo-gke-private-np-1a8686)
* [sgw-sgsn-pubsub-mb-raw-data-load-st](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/sgw-sgsn-pubsub-mb-raw-data-load-st/overview?project=cdo-gke-private-np-1a8686)
* [sgw-sgsn-pubsub-mb-raw-bq-load-st](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/sgw-sgsn-pubsub-mb-raw-bq-load-st/overview?project=cdo-gke-private-np-1a8686)

## CCS Prepaid

### CCS Prepaid EDR Stream
* [ccs-prepaid-stream-pubsub-edr-collection-st](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-prepaid-stream-pubsub-edr-collection-st/overview?project=cdo-gke-private-np-1a8686)
* [ccs-prepaid-pubsub-microbatch-edr-process-st](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-prepaid-pubsub-microbatch-edr-process-st/overview?project=cdo-gke-private-np-1a8686)
* [ccs-prepaid-pubsub-microbatch-edr-storage-st](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-prepaid-pubsub-microbatch-edr-storage-st/overview?project=cdo-gke-private-np-1a8686)
* [ ccs-prepaid-pubsub-microbatch-edr-post-process-st](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-prepaid-pubsub-microbatch-edr-post-process-st/overview?project=cdo-gke-private-np-1a8686)
* [ccs-prepaid-pubsub-microbatch-edr-sms-rating-process](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-prepaid-pubsub-microbatch-edr-sms-rating-process-st/overview?project=cdo-gke-private-np-1a8686)
* [netops-prepaid-edr-sftp-push-lab](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/netops-lab-01/mediation-control/netops-prepaid-edr-sftp-push-lab/overview?hl=en&project=tu-nfv-cio-mediation-01-np)

### CCS Prepaid Voice TDR Stream
* [ccs-prepaid-stream-pubsub-voice-tdr-collection-st](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-prepaid-stream-pubsub-voice-tdr-collection-st/overview?project=cdo-gke-private-np-1a8686)
* [ccs-prepaid-ps-mb-data-voice-tdr-processing-st](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-prepaid-ps-mb-data-voice-tdr-processing-st/overview?project=cdo-gke-private-np-1a8686)
* [ccs-prepaid-ps-mb-data-voice-tdr-storage-st](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-prepaid-ps-mb-data-voice-tdr-storage-st/overview?project=cdo-gke-private-np-1a8686)
* [ccs-prepaid-ps-mb-post-voice-tdr-processing-st](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-prepaid-ps-mb-post-voice-tdr-processing-st/overview?project=cdo-gke-private-np-1a8686)
* [netops-voice-prepaid-tdr-sftp-push-lab](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/netops-lab-01/mediation-control/netops-voice-prepaid-tdr-sftp-push-lab/overview?hl=en&project=tu-nfv-cio-mediation-01-np)

### CCS Prepaid SMS/MMS TDR Stream
* [ccs-prepaid-stream-pubsub-sms-tdr-collection-st](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-prepaid-stream-pubsub-sms-tdr-collection-st/overview?project=cdo-gke-private-np-1a8686)
* [ccs-prepaid-pubsub-mb-sms-tdr-processing-st](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-prepaid-pubsub-mb-sms-tdr-processing-st/overview?project=cdo-gke-private-np-1a8686)
* [ccs-prepaid-ps-mb-data-sms-tdr-storage-st](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-prepaid-ps-mb-data-sms-tdr-storage-st/overview?project=cdo-gke-private-np-1a8686)
* [ccs-prepaid-pubsub-mb-sms-tdr-post-processing-st](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-prepaid-pubsub-mb-sms-tdr-post-processing-st/overview?project=cdo-gke-private-np-1a8686)
* [netops-sms-prepaid-tdr-sftp-push-lab](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/netops-lab-01/mediation-control/netops-sms-prepaid-tdr-sftp-push-lab/overview?hl=en&project=tu-nfv-cio-mediation-01-np)

### CCS Prepaid Traffic Control Stream
* [ccs-prepaid-pubsub-data-tdr-stream-controller-st](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-prepaid-pubsub-data-tdr-stream-controller-st/overview?project=cdo-gke-private-np-1a8686)
* [ccs-prepaid-pubsub-voice-tdr-stream-controller](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-prepaid-pubsub-voice-tdr-stream-controller-st/overview?project=cdo-gke-private-np-1a8686)
* [ccs-prepaid-pubsub-sms-tdr-stream-controller](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-prepaid-pubsub-sms-tdr-stream-controller-st/overview?project=cdo-gke-private-np-1a8686)
* [ccs-prepaid-pubsub-maint-edr-stream-controller](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-prepaid-pubsub-maint-edr-stream-controller-st/overview?project=cdo-gke-private-np-1a8686)
* [ccs-prepaid-pubsub-threshold-edr-stream-controller-st](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-prepaid-pubsub-threshold-edr-stream-controller-st/overview?project=cdo-gke-private-np-1a8686)

### CCS Prepaid Firestore Stream
* [ccs-prepaid-pubsub-firestore-data-tdr-collection-st](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-prepaid-pubsub-firestore-data-tdr-collection-st/overview?project=cdo-gke-private-np-1a8686)
* [ccs-prepaid-pubsub-firestore-sms-tdr-collection-st](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-prepaid-pubsub-firestore-sms-tdr-collection-st/overview?project=cdo-gke-private-np-1a8686)
* [ccs-prepaid-pubsub-firestore-voice-tdr-collection-st](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-prepaid-pubsub-firestore-voice-tdr-collection-st/overview?project=cdo-gke-private-np-1a8686)
* [ccs-prepaid-pubsub-firestore-maint-edr-collection-st](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-prepaid-pubsub-firestore-maint-edr-collection-st/overview?project=cdo-gke-private-np-1a8686) 
* [ccs-prepaid-pubsub-firestore-threshold-edr-collection-st](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-prepaid-pubsub-firestore-threshold-edr-collection-st/overview?project=cdo-gke-private-np-1a8686)
* [ccs-prepaid-microbatch-tdr-firestore-storage-st](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-prepaid-microbatch-tdr-firestore-storage-st/overview?project=cdo-gke-private-np-1a8686)
* [ccs-prepaid-microbatch-edr-firestore-storage-st](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-prepaid-microbatch-edr-firestore-storage-st/overview?project=cdo-gke-private-np-1a8686)

## Ericson DMC PGW(EDMC)
* [pgw-edmc-data-raw-microbatch-dedupprocessor-st](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/pgw-edmc-data-raw-microbatch-dedupprocessor-st/overview?project=cdo-gke-private-np-1a8686)

## Common Service
* [mediation-cloud-peh-service-pubsub-st](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-control/mediation-cloud-peh-service-pubsub-st/overview?project=cdo-gke-private-np-1a8686)
* [mediation-cloud-db-controller-service-st](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-control/mediation-cloud-db-controller-service-st/overview?project=cdo-gke-private-np-1a8686)
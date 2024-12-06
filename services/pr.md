- [Common Services](#common-services)
  - [PEH and BEH](#peh-and-beh)
  - [DB Extraction](#db-extraction)
- [SGW](#sgw)
  - [SGW Stream](#sgw-stream)
- [CCS WHSIA Dashboard](#ccs-whsia-dashboard)
  - [CCS WHSIA Data TDR](#ccs-whsia-data-tdr)
  - [CCS WHSIA Maint EDR](#ccs-whsia-maint-edr)
  - [CCS WHSIA Firestore Stream](#ccs-whsia-firestore-stream)
- [CCS Prepaid](#ccs-prepaid)
  - [CCS Prepaid Firestore Stream](#ccs-prepaid-firestore-stream)
- [SGSN Dashboard](#sgsn-dashboard)
  - [SGSN](#sgsn)

## Common Services

### PEH and BEH
* [mediation-cloud-peh-service-pubsub-pr](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-control/mediation-cloud-peh-service-pubsub-pr/overview?inv=1&invt=AbeY9A&project=cdo-gke-private-pr-7712d7)
* [mediatedfilesum-pubsub-storage-pr](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-control/mediatedfilesum-pubsub-storage-pr/overview?inv=1&invt=AbeY9A&project=cdo-gke-private-pr-7712d7)
* [business-error-handler-pubsub-pr](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-control/business-error-handler-pubsub-pr/overview?inv=1&invt=AbeY9A&project=cdo-gke-private-pr-7712d7)

### DB Extraction
* [mediation-cloud-db-controller-service-pr](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-control/mediation-cloud-db-controller-service-pr/overview?inv=1&invt=AbeY9A&project=cdo-gke-private-pr-7712d7)

## SGW

### SGW Stream
* [netops-edmc-sft-collection-pr](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast2/netops-lab-01/mediation-control/netops-edmc-sft-collection-pr/overview?hl=en&project=tu-nfv-cio-mediation-02-pr)
* [ericsson-sgw-pubsub-mb-raw-ext-load-pr](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ericsson-sgw-pubsub-mb-raw-ext-load-pr/overview?project=cdo-gke-private-pr-7712d7)

## CCS WHSIA [Dashboard](https://console.cloud.google.com/monitoring/dashboards/builder/caacbbab-f795-4d96-bb43-d35991817fcc;duration=PT1H?project=cio-stackdriver-pr-7f46b3&pageState=(%22events%22:(%22active%22:%5B%22CLOUD_ALERTING_ALERT%22,%22GKE_WORKLOAD_DEPLOYMENT%22,%22CLOUD_SQL_STORAGE%22%5D,%22inactive%22:%5B%5D)))

### CCS WHSIA Data TDR 
* [ccs-pbsstr-data-tdr-collection-pr](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-pbsstr-data-tdr-collection-pr/overview?project=cdo-gke-private-pr-7712d7)
* [ccs-pbs-mb-tier-tdr-collection-pr](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-pbs-mb-tier-tdr-collection-pr/overview?project=cdo-gke-private-pr-7712d7)
* [ccs-pbsstr-data-tdr-processing-pr](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-pbsstr-data-tdr-processing-pr/overview?project=cdo-gke-private-pr-7712d7)
* [ccs-pbs-mb-tdr-matrixx-storage-pr](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-pbs-mb-tdr-matrixx-storage-pr/overview?project=cdo-gke-private-pr-7712d7)
* [ccs-pbs-mb-filtered-tdr-storage-pr](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-pbs-mb-filtered-tdr-storage-pr/overview?project=cdo-gke-private-pr-7712d7)
* [ccs-pbs-mb-tdr-tostream-pr](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-pbs-mb-tdr-tostream-pr/overview?project=cdo-gke-private-pr-7712d7)

### CCS WHSIA Maint EDR
* [ccs-pbsstr-data-maint-edr-processing-pr](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-pbsstr-data-maint-edr-processing-pr/overview?project=cdo-gke-private-pr-7712d7)
* [ccs-pbs-mb-edr-maint-storage-pr](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-pbs-mb-edr-maint-storage-pr/overview?project=cdo-gke-private-pr-7712d7)

### CCS WHSIA Firestore Stream
* [ccs-stream-pubsub-firestore-tdr-collection-pr](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-stream-pubsub-firestore-tdr-collection-pr/overview?project=cdo-gke-private-pr-7712d7)
* [ccs-stream-pubsub-firestore-tier-tdr-collection-pr](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-stream-pubsub-firestore-tier-tdr-collection-pr/overview?project=cdo-gke-private-pr-7712d7)
* [ccs-stream-pubsub-firestore-edr-block-collection-pr](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-stream-pubsub-firestore-edr-block-collection-pr/overview?project=cdo-gke-private-pr-7712d7)
* [ccs-stream-pubsub-firestore-edr-maint-collection-pr](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-stream-pubsub-firestore-edr-maint-collection-pr/overview?project=cdo-gke-private-pr-7712d7)
* [ccs-pubsub-microbatch-tdr-firestore-storage-pr](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-pubsub-microbatch-tdr-firestore-storage-pr/overview?project=cdo-gke-private-pr-7712d7)
* [ccs-pubsub-microbatch-edr-maint-firestore-storage-pr](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-pubsub-microbatch-edr-maint-firestore-storage-pr/overview?project=cdo-gke-private-pr-7712d7)
* [ccs-pubsub-microbatch-edr-block-firestore-storage-pr](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-pubsub-microbatch-edr-block-firestore-storage-pr/overview?project=cdo-gke-private-pr-7712d7)

## CCS Prepaid

### CCS Prepaid Firestore Stream
* [ccs-prepaid-microbatch-edr-firestore-storage-pr](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-prepaid-microbatch-edr-firestore-storage-pr/overview?project=cdo-gke-private-pr-7712d7)
* [ccs-prepaid-microbatch-tdr-firestore-storage-pr](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-prepaid-microbatch-tdr-firestore-storage-pr/overview?project=cdo-gke-private-pr-7712d7)
* [ccs-prepaid-pubsub-firestore-maint-edr-collection-pr](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-prepaid-pubsub-firestore-maint-edr-collection-pr/overview?project=cdo-gke-private-pr-7712d7)
* [ccs-prepaid-pubsub-firestore-data-tdr-collection-pr](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-prepaid-pubsub-firestore-data-tdr-collection-pr/overview?project=cdo-gke-private-pr-7712d7)
* [ccs-prepaid-pubsub-firestore-sms-tdr-collection-pr](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-prepaid-pubsub-firestore-sms-tdr-collection-pr/overview?project=cdo-gke-private-pr-7712d7)
* [ccs-prepaid-pubsub-firestore-failure-edr-collection-pr](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-prepaid-pubsub-firestore-failure-edr-collection-pr/overview?project=cdo-gke-private-pr-7712d7)
* [ccs-prepaid-pubsub-firestore-threshold-edr-collection-pr](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-prepaid-pubsub-firestore-threshold-edr-collection-pr/overview?project=cdo-gke-private-pr-7712d7)
* [ccs-prepaid-pubsub-firestore-voice-tdr-collection-pr](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/ccs-prepaid-pubsub-firestore-voice-tdr-collection-pr/overview?project=cdo-gke-private-pr-7712d7)

## SGSN [Dashboard](https://console.cloud.google.com/monitoring/dashboards/builder/f6584a67-6028-4c66-9f81-f2437d8d3a85;duration=PT1H?project=cio-stackdriver-pr-7f46b3&pageState=(%22events%22:(%22active%22:%5B%22CLOUD_ALERTING_ALERT%22%5D,%22inactive%22:%5B%5D)))

### SGSN 
* [sgw-sgsn-pubsub-mb-raw-bq-load-pr](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/sgw-sgsn-pubsub-mb-raw-bq-load-pr/overview?project=cdo-gke-private-pr-7712d7)
* [sgw-sgsn-pubsub-mb-raw-data-load-pr](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/sgw-sgsn-pubsub-mb-raw-data-load-pr/overview?project=cdo-gke-private-pr-7712d7)
* [sgw-sgsn-ext-pubsub-raw-collection-pr](https://console.cloud.google.com/kubernetes/deployment/northamerica-northeast1/private-na-ne1-001/mediation-data/sgw-sgsn-ext-pubsub-raw-collection-pr/overview?project=cdo-gke-private-pr-7712d7)
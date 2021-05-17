

[CAMP Agent documentation](#camp-agent-documentation)

- [Source Agent](#source-agent)s
  - [1. Overview](#Xc8951b796c7b61cbdd4998c72efbdeed0056e13)
  - [2. Data Input Source](#Xa5c2c9a08f1a161f2a4b6f878aad55594468ca9)
  - [3. Source Agent details](#X914313715c775d98213c776e191d7923bccede3)
    - [GCS Source Stream Mode Agent](#gcs-source-stream-mode-agent)
    - [GCS Source Microbatch Mode Agent](#gcs-source-microbatch-mode-agent)
  - [4. How to create Application micro service](#X79acab923d4823f82df4083049a94c625b95b0a)
  - [5. Maven dependencies](#X59aa7b69700c12326376d2fd0ea5515ec7693e9)
- [Processor Agent](#processor-agent)s
  - [1. Overview](#Xf4d734d644efe11d5f0b5b6850821e6173395fa)
  - [2. Processor Agent Details](#X860b5db2de945ebe9f16c976281de142990511c)
    - [Processor Stream Mode Agent](#gcs-processor-stream-mode-agent)
    - [GCS Processor Microbatch Mode Agent](#gcs-processor-microbatch-mode-agent)
  - [4. How to create Application micro service](#X0f4441adfe1a56aab6b304c12f977b82e1ebbf3)
  - [5. Maven dependencies](#X217b9b41bd6fb65818bb1ccf0d78c56027022b4)
- [Sink Storage Agent](h#processor-agent)s
  - [1. Overview](#Xf4d734d644efe11d5f0b5b6850821e6173395fa)
  - [2. Sink Agent Details](#X860b5db2de945ebe9f16c976281de142990511c)
    - [Stream Mode Agent](#gcs-processor-stream-mode-agent)
    - [GCS Microbatch Mode Agent](#gcs-processor-microbatch-mode-agent)
  - [4. How to create Application micro service](#X0f4441adfe1a56aab6b304c12f977b82e1ebbf3)
  - [5. Maven dependencies](#X217b9b41bd6fb65818bb1ccf0d78c56027022b4)
##
## **CAMP Agent documentation V.0.1**

CAMP agents: camp is build using the Spring Cloud Stream framework (V3.0.6 as of this writing, check https://spring.io/projects/spring-cloud-stream for details), reader should be familiar with this framework. 

CAMP agents currently supports two binder implementations: RabbitMQ and Google PubSub. CAMP also use several other spring libraries, including spring cloud gcp.

CAMP agents will do most of the work required for each spring cloud stream service as they operate on generic messages. Microservices implemented using CAMP agents usually only need to provide the business logic part as a spring bean and middleware configuration as detailed on each agent below.

CAMP agents are currently offered for two main flow modes:
1. ### **Microbatch**
Microbatch means all services operate on files, source agent will collect and split the file in micro batches, then it produces one message into middleware for each of these files. Each subsequent service will act upon the received a message that contains (among other information) the location in GCS of the batch to be processed.

1. ### **Streaming**
STREAMING means that all agents (except source) operate on content extracted/published directly from middleware messages. Source agents are the entry points that read files from storage or sftp and publishes each record to the middleware.

`	`Then, following 
## **I. Source Agent**
#### *1. Overview*
Source is a agent to collect data from input sources and sends messages to a destination. Right now we can handle input data as gzip files from Google Cloud Storage, and also GZIP files from SFTP servers(Not full finished).
#### *2. Data Input Source*
This is input system to upload gzip files. The input files content is JSON array and should be gzipped. Right now only supports Google Storage bucket as input source.

- Here is bucket folder structure

| Folder Name | Type                                        |
|-------------|---------------------------------------------|
| inbox       | The folder for input system to upload files |
| process     | The folder for processing                   |
| error       | The folder to keep error messages files     |
| archive     | The folder to keep archive                  |
- Google Storage bucket properties

| Name           | Description                          |
|----------------|--------------------------------------|
| gcs.projectid  | The project id                       |
| gcs.bucket     | The bucket id                        |
| gcs.inbox      | The inbox folder name e.g. inbox     |
| gcs.archive    | The archive folder name e.g. archive |
| gcs.filefilter | The gzipped file suffix e.g. gz      |
#### *3. Source Agent details*
There are 2 mode for processing. Stream mode and Microbatch mode. each mode will have there own agent and based different message channel (Pubsub or RabbitMQ).

- Common configuration properties

| Name                                                            | Description                                                                      |
|-----------------------------------------------------------------|----------------------------------------------------------------------------------|
| spring.cloud.function.definition                                | The cloud function name for streaming. sendMessageFromFile                       |
| spring.cloud.stream.function.bindings.sendMessageFromFile-out-0 | output                                                                           |
| spring.cloud.stream.poller.fixedDelay                           | The time interval to check input file by millisecond                             |
| file.after.process                                              | What to do after processed the input file{move, delete, rename}, default is move |
| file.after.process.rename.ext                                   | If rename file after process, what’s the extention name                          |
| file.process.limit                                              | 1 , right now only support process 1 file at time                                |
| mediation.processor.batch.name                                  | The source business bean name for streaming. e.g. senderBatchProcessor           |
##### GCS Source Stream Mode Agent
For GCS source Stream agent: It will scan the input google cloud storage bucket inbox folder by schedule. If there are files, the agent will load files content into JSON array. Then the agent will split JSON array into individual message and send them to target topic.

- **Pubsub GCS Source Stream Mode Agent**: use Pubsub as message channel
  - Module: **stream-processor-general-pubsub-agent**
  - Config properties:

| Pubsub Properties                  | Description                                 |
|------------------------------------|---------------------------------------------|
| spring.cloud.gcp.project-id        | The GCP project id                          |
| mediation.cloud.pubsub.data.topic  | The target topic name for data send message |
| mediation.cloud.pubsub.audit.topic | The target topic name for audit message     |
- **RabbitMQ GCS Source Stream Agent**: use RabbitMQ as message channel
  - Module: **stream-processor-general-rabbit-agent**
  - Config properties:

| RabbitMQ Properties      | Description                            |
|--------------------------|----------------------------------------|
| spring.rabbitmq.host     | RabbitMQ server connection information |
| spring.rabbitmq.port     |                                        |
| spring.rabbitmq.username |                                        |
| spring.rabbitmq.password |                                        |
##### GCS Source Microbatch Mode Agent
For GCS source Microbatch agent: It will scan the input google cloud storage bucket inbox folder by schedule. If there are files, the agent will load files content into JSON array. Then based on file partion size the agent will split JSON array into multi small files and send files information to target topic.

- **Pubsub GCS Microbatch Mode Agent**: use Pubsub as message channel
  - Module: **batch-source-pubsub-microbatch-agent**
  - Config properties:

| Pubsub Properties                  | Description                                 |
|------------------------------------|---------------------------------------------|
| spring.cloud.gcp.project-id        | The GCP project id                          |
| mediation.cloud.pubsub.data.topic  | The target topic name for data send message |
| mediation.cloud.pubsub.audit.topic | The target topic name for audit message     |
| file.process.partition.size        | The size of the each small file             |
#### *4. How to create Application micro service*
Source agents are start points on a spring cloud stream flow. CAMP libraries provide a bean to act as an spring cloud stream source, Application service needs to provide the business logic getPayload bean for basic validation on input file then send data records messages (stream mode) or spliited files messages (microbatch mode) to downstream topic. And also send file audit message to audit topic. Then archive the processed file.

Step to create source micro service

- [1] Based on project decide which mode to use : stream or microbatch
- [2] Based on mode create maven project and add dependencies
- [3] Create Spring stream bean class to implements getPayload
- [4] Based on business project and GCP project information set configuration in application.properties
- **Pubsub GCS Source Stream Mode Agent** and **RabbitMQ GCS Source Stream Agent** Here is bean interface to implements Stream Mode Source service:

@Component("senderBatchProcessor")
**public** **class** GcsListSourceGenerator **implements** BusinessBatchProcessor {
`    `**public** List<FileSummaryFileRecord> getPayload(List<FileSummaryFileRecord> fileRecords) {    
`        `**...**

Example service maven project: [Pubsub Source Service](https://github.com/telus/cio-mediation/tree/nonprod/mediation-cloud-usage-demo/cmi-batch2stream-gcs-pubsub-source) | [RabbitMQ Source Service](https://github.com/telus/cio-mediation/tree/nonprod/mediation-cloud-usage-demo/cmi-batch2stream-gcs-rabbit-source)

- **Pubsub GCS Source Microbatch Mode Agent** Here is bean interface to implements Microbatch Mode Source service:

@Component("senderBatchProcessor")
**public** **class** GcsListSourceGenerator **implements** BusinessBatchProcessor {
`    `**public** List<FileSummaryFileRecord> getPayload(List<FileSummaryFileRecord> fileRecords) {  
`        `**...**

Example service maven project: [Pubsub Microbatch Source Service](https://github.com/telus/cio-mediation/tree/nonprod/mediation-cloud-usage-demo/cmi-batch2stream-gcs-pubsub-microbatch-source) #### 5. Maven dependencies In order to produce a spring cloud stream microservice, in addition to the spring dependencies, the following CAMP dependencies must be added to the service pom file:

`        `<dependency**>**
`            `**<groupId>com.telus.mediationCloud</groupId>**
`            `**<artifactId>common-api</artifactId>**
`        `**</dependency>**
`        `**<dependency>**
`            `**<groupId>com.telus.mediationCloud</groupId>**
`            `**<artifactId>common-cache</artifactId>**
`        `**</dependency>**
`        `**<dependency>**
`            `**<groupId>com.telus.mediationCloud</groupId>**
`            `**<artifactId>common-gcs-file-producers</artifactId>**
`        `**</dependency>**
`        `**<dependency>**
`            `**<groupId>com.telus.mediationCloudUsage</groupId>**
`            `**<artifactId>cmi-business-models</artifactId>**
`        `**</dependency>**

- Based on the mode and message channel

`        `RabbitMQ Stream mode 
`        `<dependency**>**
`            `**<groupId>com.telus.mediationCloud</groupId>**
`            `**<artifactId>batch-source-rabbit-stream-agent</artifactId>**
`        `**</dependency>**

`        `Pubsub Stream mode 
`        `<dependency**>**
`            `**<groupId>com.telus.mediationCloud</groupId>**
`            `**<artifactId>batch-source-pubsub-stream-agent</artifactId>**
`        `**</dependency>**

`        `Pubsub Microbatch mode 
`        `<dependency**>**
`            `**<groupId>com.telus.mediationCloud</groupId>**
`            `**<artifactId>batch-source-pubsub-microbatch-agent</artifactId>**
`        `**</dependency>**

-----
## **II. Processor Agent**
### **1. Overview**
Processor is a agent to consumes message from a destination and produces messages to send to another destination. Processor will implements business logic like data validation , data transformation and data lookup. Then pass the messages to downstream.
### **2. Processor Agent Details**

There are 2 mode for processing. Stream mode and Microbatch mode. each mode will have there own agent and based different message channel (Pubsub or RabbitMQ).

- Common configuration properties

| Name                                                       | Description                                                                                              |
|------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| spring.cloud.function.definition                           | The cloud function name for streaming. messageProcess                                                    |
| spring.cloud.stream.function.bindings.messageProcess-in-0  | input                                                                                                    |
| spring.cloud.stream.function.bindings.messageProcess-out-0 | output                                                                                                   |
| mediation.cloud.project                                    | The business project name, e.g. CMI                                                                      |
| mediation.cloud.businessprocessorfactory.ProcessorName     | The business processor bean name, e.g. GeneralMessageProcessor                                           |
| file.after.process                                         | Used by GCS library, what to do with input file after its processed. Can be “delete”, “rename” or “move” |
| file.after.process.rename.ext                              | File extension to be used if configuration above is “rename”                                             |
1. #### *GCS Processor Stream Mode Agents*
For GCS Processor Stream agent: It will subscribe the incoming message from Source Agent. Then implements business logic then sends processed message to downstream topic.
##### Available agents:
- **Pubsub GCS Processor Stream Mode Agent**: use Pubsub as message channel
  - Module: **stream-processor-general-pubsub-agent**
  - Config properties:

| Pubsub Properties                              | Description                                            |
|------------------------------------------------|--------------------------------------------------------|
| spring.cloud.gcp.project-id                    | The GCP project id                                     |
| mediation.cloud.pubsub.data.topic              | The target topic name for data send message            |
| mediation.cloud.pubsub.audit.topic             | The target topic name for audit message                |
| spring.cloud.stream.bindings.input.destination | The input topic name for incoming message              |
| spring.cloud.stream.bindings.input.group       | The input topic subscription name for incoming message |
- **RabbitMQ GCS Processor Stream Agent**: use RabbitMQ as message channel
  - Module: **stream-processor-general-rabbit-agent**
  - Config properties:

| RabbitMQ Properties      | Description                            |
|--------------------------|----------------------------------------|
| spring.rabbitmq.host     | RabbitMQ server connection information |
| spring.rabbitmq.port     |                                        |
| spring.rabbitmq.username |                                        |
| spring.rabbitmq.password |                                        |
1. #### *GCS Processor Microbatch Mode Agents*
For GCS Processor Pub/Sub agent: every input message should contain a reference to an input file stored in a GCP storage bucket. It has the following high level logic:

Retrieve message from middleware

`	`Retrieve the file in the middleware message, load all records into memory.

`	`For every record in the file, call the getPayload method from the provided bussinessProcessor implementation.

`	`Create two output files depending on the output for getPayload method: one for records in error (records where getPayload returned null) and another for successfully processed records to be published to the middleware.

`	`Publish message to pub/sub with information about the successfully processed records file.

`	`Create and publish audit entry 

`	`Remove/rename/move input file

##### Available agents:
- **Pubsub GCS Processor Microbatch Mode Agent**: use Pubsub as message channel

- Module: **stream-processor-general-pubsub-microbatch-agent**
- Config properties:

| Pubsub Properties                              | Description                                                                   |
|------------------------------------------------|-------------------------------------------------------------------------------|
| spring.cloud.gcp.project-id                    | The GCP project id                                                            |
| spring.cloud.stream.bindings.input.destination | The input topic name for incoming message                                     |
| spring.cloud.stream.bindings.input.group       | The input topic subscription name for incoming message                        |
| mediation.cloud.pubsub.data.topic              | The target topic name from where receive data                                 |
| mediation.cloud.pubsub.audit.topic             | The target topic name for audit message                                       |
| gcs.projectid                                  | Used by GCS library, GCP project where GCS bucket resides                     |
| gcs.bucket                                     | Used by GCS library, GCS bucket where input files are stored                  |
| gcs.processed                                  | Used by GCS library, GCS folder where input file will be moved if not deleted |

#### *4. How to create Application micro service*
Processor agents are middle components on a spring cloud stream flow. CAMP libraries provide a bean to act as a spring cloud stream processor, Application service needs to provide the business logic getPayload bean for validation, transformation and lookup on input message then send data records messages (stream mode) or splited files messages (microbatch mode) to downstream topic. And also send file audit message to audit topic. Then delete the processed temp file(if microbatch mode).

Step to create processor micro service

- [1] Based on project decide which mode to use : stream or microbatch
- [2] Based on mode create maven project and add dependencies
- [3] Create Spring stream bean class to implement getPayload method on BusinessProcessor interface.
- ` `[4] Based on business project and GCP project information set configuration in application.properties
- **Pubsub GCS Processor Stream Mode Agent** and **RabbitMQ GCS Processor Stream Agent** Here is bean interface to implements Stream Mode processor service:

@Component("GeneralMessageProcessor")
**public** **class** GeneralMessageProcessor **implements** BusinessProcessor {
`    `**public** Object getPayload(BaseMessage baseMessage) {  
`        `**...**

Example service maven project: [Pubsub Processor Service](https://github.com/telus/cio-mediation/tree/nonprod/mediation-cloud-usage-demo/cmi-message-pubsub-processor) | [RabbitMQ Processor Service](https://github.com/telus/cio-mediation/tree/nonprod/mediation-cloud-usage-demo/cmi-message-rabbit-processor)

- **Pubsub GCS Source Microbatch Mode Agent** Here is bean interface to implements Microbatch Mode processor service:

@Component("GeneralMessageProcessor")
**public** **class** GeneralMessageProcessor **implements** BusinessProcessor {
`    `**public** Object getPayload(BaseMessage baseMessage) {  
`        `**...**

Example service maven project: [Pubsub Microbatch Processor Service](https://github.com/telus/cio-mediation/tree/nonprod/mediation-cloud-usage-demo/cmi-message-pubsub-microbatch-processor) #### 5. Maven dependencies In order to produce a spring cloud stream microservice, in addition to the spring dependencies, the following CAMP dependencies must be added to the service pom file:

`        `<dependency**>**
`            `**<groupId>com.telus.mediationCloud</groupId>**
`            `**<artifactId>common-api</artifactId>**
`        `**</dependency>**
`        `**<dependency>**
`            `**<groupId>com.telus.mediationCloud</groupId>**
`            `**<artifactId>common-cache</artifactId>**
`        `**</dependency>**
`        `**<dependency>**
`            `**<groupId>com.telus.mediationCloud</groupId>**
`            `**<artifactId>common-gcs-file-producers</artifactId>**
`        `**</dependency>**
`        `**<dependency>**
`            `**<groupId>com.telus.mediationCloudUsage</groupId>**
`            `**<artifactId>cmi-business-models</artifactId>**
`        `**</dependency>**

- Based on the mode and message channel

`        `RabbitMQ Stream mode 
`        `<dependency**>**
`            `**<groupId>com.telus.mediationCloud</groupId>**
`            `**<artifactId>stream-processor-general-rabbit-agent</artifactId>**
`        `**</dependency>**

`        `Pubsub Stream mode 
`        `<dependency**>**
`            `**<groupId>com.telus.mediationCloud</groupId>**
`            `**<artifactId>stream-processor-general-pubsub-agent</artifactId>**
`        `**</dependency>**

`        `Pubsub Microbatch mode 
`        `<dependency**>**
`            `**<groupId>com.telus.mediationCloud</groupId>**
`            `**<artifactId>stream-processor-general-pubsub-microbatch-agent</artifactId>**
`        `**</dependency>**

## **III. Sink Storage Agents**
### **1. Overview**
### Sink agents are termination points on a spring cloud stream flow. CAMP sink agents perform data insert into GCP Data Store or Cloud SQL databases. CAMP libraries provide a bean to act as a spring cloud stream sink.
### Note that CAMP guarantees no data is lost during operation, but in some scenarios it is possible that a message is duplicated. Then to avoid Database duplicates, it is important that the insert operation remains idempotent. To achieve this, every record should have an unique ID field and the application service must be able to provide an unique value for the field if the same record is processed again (i.e use a hash in key fields that are unique between records). 
### **2. Sink Storage Agent Details**
There are 2 modes for processing. Stream mode and Microbatch mode. each mode will have their own agent and based different message channel (Pubsub or RabbitMQ).
### For Microbatch, CAMP assumes every received middleware message will contain a reference to a file containing multiple records to be inserted. 
### CAMP will try to insert all records in a single transaction, then it’s expected that each file has at most records as the MAX transaction size for the chosen storage option.

- Common configuration properties

| Name                                                    | Description                                                    |
|---------------------------------------------------------|----------------------------------------------------------------|
| spring.cloud.function.definition                        | The cloud function name for receiving input data. storeMessage |
| spring.cloud.stream.function.bindings.storeMessage-in-0 | input                                                          |
| mediation.cloud.project                                 | The business project name, e.g. CMI                            |
| mediation.cloud.businessprocessorfactory.ProcessorName  | The business processor bean name, e.g. cmiProcessor            |
| mediation.cloud.storagemapper.MapperName                | Name for bean implementing getObjectMap, i.e: cmiMapper        |
| mediation.cloud.error.bucket                            | GCS bucket to store error records                              |
| mediation.cloud.error.folder                            | GCS folder where to store error files                          |
| spring.cloud.gcp.datastore.namespace                    | Only for DATA STORE agents. Namespace for inserted data.       |
1. #### *Storage Sink Stream Mode Agents*
For Storage Sink Stream agent: It will subscribe the incoming message from Source or Processor Agent. Then implements business logic to convert the record to an object that can be inserted into storage. This agent has the high level logic:

`	`Retrieve message from middleware

`	`If message is one of the accepted types call the business processor to map received data to internal java object. 

`	`Locates mapper bean based on configuration entries.

`	`Inserts single record into storage.

##### Available agents:
- **Pubsub Data Store Stream Agent**: use Pubsub as message channel
  - Module: **stream-sink-DBstorage-pubsub-agent**
  - Agent Config properties:

| Pubsub Properties                              | Description                                            |
|------------------------------------------------|--------------------------------------------------------|
| spring.cloud.gcp.project-id                    | The GCP project id                                     |
| spring.cloud.stream.bindings.input.destination | The input topic name for incoming message              |
| spring.cloud.stream.bindings.input.group       | The input topic subscription name for incoming message |
- **RabbitMQ Data Store Stream Agent**: use RabbitMQ as message channel and GCP datastore as storage.
  - Module: **stream-sink-DBstorage-rabbit-agent**
  - Config properties:

| RabbitMQ Properties                                                      | Description                            |
|--------------------------------------------------------------------------|----------------------------------------|
| spring.rabbitmq.host                                                     | RabbitMQ server connection information |
| spring.rabbitmq.port                                                     |                                        |
| spring.rabbitmq.username                                                 |                                        |
| spring.rabbitmq.password                                                 |                                        |
| spring.cloud.stream.rabbit.bindings.input.consumer.auto-bind-dlq         | Activate use of DLQ for failures       |
| <p>spring.cloud.stream.rabbit.bindings.input.consumer.dlq-ttl</p><p></p> | Should be empty                        |
1. #### *Storage Sink Microbatch Mode Agents*
For GCS Sink agent: every input message should contain a reference to an input file stored in a GCP storage bucket. It has the following high level logic:

AGENT high level logic:

`	`Retrieve message from middleware

`	`If message is one of the accepted types:

Open the file referenced in the middleware message, load all records in memory.

For each record, call the business processor to map record data to internal java object. Store converted records in a list

Locates mapper bean based on configuration entries.

Call CAMP storage libraries to insert all records into data store in a single transaction If transaction fails, CAMP will attempt to insert one record at a time, and will return a list of records that could not be inserted.

Records in error will be classified then into retryable and non-retryable error records. CAMP will create output files for each of the categories.

Generate audit entry for the file just processed and send it via middleware to the audit service.

`	`Remove the input file
##### Available agents:
- **Pubsub GCS Data Store Sink Microbatch Mode Agent**: use Pubsub as message channel

- Module: **stream-sink-DBstorage-pubsub-microbatch-agent**
- Config properties:

| Pubsub Properties                                          | Description                                                                                              |
|------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| mediation.cloud.pubsub.data.topic                          | The target topic name from where receive data                                                            |
| mediation.cloud.pubsub.audit.topic                         | The target topic name for audit message                                                                  |
| mediation.cloud.pubsub.dlq.topic                           | Name of the DLQ topic                                                                                    |
| mediation.cloud.audit.file.category                        | File category for audit entry. i.e: CMIMicroBatchSink                                                    |
| spring.cloud.gcp.project-id                                | The GCP project id                                                                                       |
| spring.cloud.function.definition                           | Name Of bean implementing the spring stream processor method, must be: **messageProcess**                |
| spring.cloud.stream.function.bindings.messageProcess-in-0  | Spring cloud stream binding, has to be “**input**”                                                       |
| spring.cloud.stream.function.bindings.messageProcess-out-0 | Spring cloud stream binding, has to be “**output**”                                                      |
| spring.cloud.stream.bindings.input.destination             | The input topic name for incoming message                                                                |
| spring.cloud.stream.bindings.input.group                   | The input topic subscription name for incoming message                                                   |
| gcs.projectid                                              | Used by GCS library, GCP project where GCS bucket resides                                                |
| gcs.bucket                                                 | Used by GCS library, GCS bucket where input files are stored                                             |
| gcs.processed                                              | Used by GCS library, GCS folder where input file will be moved if not deleted                            |
| file.after.process                                         | Used by GCS library, what to do with input file after its processed. Can be “delete”, “rename” or “move” |
| file.after.process.rename.ext                              | File extension to be used if configuration above is “rename”                                             |
| mediation.cloud.error.bucket                               | GCS bucket name where to store error records                                                             |
| mediation.cloud.error.folder                               | GCS storage folder for error records                                                                     |

#### *4. How to create Application micro service*
Sink agents are final components on a spring cloud stream flow. CAMP libraries provide a bean to act as a spring cloud stream sink, Application service needs to provide the business logic getPayload bean for transformation of the incoming data into a Spring Storage annotated object (Data Store or Cloud SQL).  It is also expected that an “ID” field exists annotated with “@Id” and has a unique value (if not one MUST be generated).

Application service also has to provide a bean that implements the getObjectMap method that returns a StorageMap object, note that is currently for future use, so an empty object can be returned.

Step to create sink micro service

- [1] Based on project decide which mode to use : stream or microbatch
- [2] Based on mode create maven project and add dependencies
- [3] Create Spring stream bean class to implement getPayload method on BusinessProcessor interface:

**public** **interface** BusinessProcessor {

`    `Object getPayload(BaseMessage baseMessage);

}

- [4] Create Spring stream bean class to implement the getObjectMap method on Storagemapper interface:

**public** **interface** StorageMapper {	

`		`StorageMap getObjectMap(Object baseObject);	

}

- ` `[4] Based on business project and GCP project information set configuration in application.properties

Example service maven project: [Pubsub Microbatch Data Store Sink Service](https://github.com/telus/cio-mediation/tree/nonprod/mediation-cloud-usage-demo/cmi-storage-pubsub-microbatch-sink). Maven dependencies in order to produce a spring cloud stream microservice, in addition to the spring dependencies, the following CAMP dependencies must be added to the service pom file:

`        `<dependency**>**
`            `**<groupId>com.telus.mediationCloud</groupId>**
`            `**<artifactId>common-api</artifactId>**
`        `**</dependency>**
`        `**<dependency>**
`            `**<groupId>com.telus.mediationCloud</groupId>**
`            `**<artifactId>common-cache</artifactId>**
`        `**</dependency>**
`        `**<dependency>**
`            `**<groupId>com.telus.mediationCloudUsage</groupId>**
`            `**<artifactId>cmi-business-models</artifactId>**
`        `**</dependency>**

- Based on the mode and message channel

`        `RabbitMQ Stream mode 
`        `<dependency**>**
`            `**<groupId>com.telus.mediationCloud</groupId>**
`            `**<artifactId>stream-sink-DBstorage-rabbit-agent</artifactId>**
`        `**</dependency>**

`        `Pubsub Stream mode 
`        `<dependency**>**
`            `**<groupId>com.telus.mediationCloud</groupId>**
`            `**<artifactId>stream-sink-DBstorage-pubsub-agent</artifactId>**
`        `**</dependency>**

`        `Pubsub Microbatch mode 
`        `<dependency**>**
`            `**<groupId>com.telus.mediationCloud</groupId>**
`            `**<artifactId>stream-sink-DBstorage-pubsub-microbatch-agent</artifactId>**
`        `**</dependency>**

- Based on the storage service 

**<dependency>**

`   `**<groupId>com.telus.mediationCloud</groupId>**

`   `**<artifactId>common-store-firestore-ds</artifactId>**

**</dependency>**        


-----

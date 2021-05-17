
- [CAMP Agent documentation](#camp-agent-documentation)
  - [Source Agent](#source-agent)
    - [1. Overview](#1-overview)
    - [2. Data Input Source](#2-data-input-source)
    - [3. Source Agent details](#3-source-agent-details)
      - [GCS Source Stream Mode Agent](#gcs-source-stream-mode-agent)
      - [GCS Source Microbatch Mode Agent](#gcs-source-microbatch-mode-agent)
    - [4. How to create Application micro service](#4-how-to-create-application-micro-service)
    - [5. Maven dependencies](#5-maven-dependencies)
    - [Processor Agent](#processor-agent)
      - [1. Overview](#1-overview-1)
      - [2. Processor Agent Details](#2-processor-agent-details)
        - [Processor Stream Mode Agent](#processor-stream-mode-agent)
        - [GCS Processor Microbatch Mode Agent](#gcs-processor-microbatch-mode-agent)
      - [4. How to create Application micro service](#4-how-to-create-application-micro-service-1)
      - [5. Maven dependencies](#5-maven-dependencies-1)

# CAMP Agent documentation

## Source Agent
### 1. Overview
Source is a agent to collect data from input sources and sends messages to a destination. Right now we can handle input data as gzip files from Google Cloud Storage, and also GZIP files from SFTP servers(Not full finished). 

### 2. Data Input Source 
This is input system to upload gzip files. The input files content is JSON array and should be gzipped. Right now only supports Google Storage bucket as input source.

* Here is bucket folder structure

    | Folder Name | Type                                        |
    |-------------|---------------------------------------------|
    | inbox       | The folder for input system to upload files |
    | process     | The folder for processing                   |
    | error       | The folder to keep error messages files     |
    | archive     | The folder to keep archive                  |

* Google Storage bucket properties
  
    | Name           | Description                            |
    |----------------|----------------------------------------|
    | gcs.projectid  | The project id                         |
    | gcs.bucket     | The bucket id                          |
    | gcs.inbox      | The inbox folder name e.g. `inbox`     |
    | gcs.archive    | The archive folder name e.g. `archive` |
    | gcs.filefilter | The gzipped file suffix e.g. `gz`      |

###  3. Source Agent details     
There are 2 mode for processing. Stream mode and Microbatch mode. each mode will have there own agent and based different message channel (Pubsub or RabbitMQ).

* Common configuration properties

    | Name                                                            | Description                                                                          |
    |-----------------------------------------------------------------|--------------------------------------------------------------------------------------|
    | spring.cloud.function.definition                                | The cloud function name for streaming. `sendMessageFromFile`                         |
    | spring.cloud.stream.function.bindings.sendMessageFromFile-out-0 | `output`                                                                             |
    | spring.cloud.stream.poller.fixedDelay                           | The time interval to check input file by millisecond                                 |
    | file.after.process                                              | What to do after processed the input file{`move, delete, rename`}, default is `move` |
    | file.after.process.rename.ext                                   | If rename file after process, what's the extention name                              |
    | file.process.limit                                              | `1` , right now only support process 1 file at time                                  |
    | mediation.processor.batch.name                                  | The source business bean name for streaming. e.g. `senderBatchProcessor`             |
    
#### GCS Source Stream Mode Agent 
For GCS source Stream agent: It will scan the input google cloud storage bucket inbox folder by schedule. If there are files, the agent will load files content into JSON array. Then the agent will split JSON array into individual message and send them to target topic.

* **Pubsub GCS Source Stream Mode Agent**: use Pubsub as message channel 
    * Module:  **stream-processor-general-pubsub-agent**
    * Config properties: 
 
        | Pubsub Properties                  | Description                                 |
        |------------------------------------|---------------------------------------------|
        | spring.cloud.gcp.project-id        | The GCP project id                          |
        | mediation.cloud.pubsub.data.topic  | The target topic name for data send message |
        | mediation.cloud.pubsub.audit.topic | The target topic name for audit message     |

* **RabbitMQ GCS Source Stream Agent**:  use RabbitMQ as message channel
    * Module:  **stream-processor-general-rabbit-agent**
    * Config properties: 
 
        | RabbitMQ Properties      | Description                            |
        |--------------------------|----------------------------------------|
        | spring.rabbitmq.host     | RabbitMQ server connection information |
        | spring.rabbitmq.port     |                                        |
        | spring.rabbitmq.username |                                        |
        | spring.rabbitmq.password |                                        |

#### GCS Source Microbatch Mode Agent 
For GCS source Microbatch agent: It will scan the input google cloud storage bucket inbox folder by schedule. If there are files, the agent will load files content into JSON array. Then based on file partion size the agent will split JSON array into multi small files and send files information to target topic.

* **Pubsub GCS Microbatch Stream Mode Agent**: use Pubsub as message channel 
    * Module:  **batch-source-pubsub-microbatch-agent**
    * Config properties: 
 
        | Pubsub Properties                  | Description                                 |
        |------------------------------------|---------------------------------------------|
        | spring.cloud.gcp.project-id        | The GCP project id                          |
        | mediation.cloud.pubsub.data.topic  | The target topic name for data send message |
        | mediation.cloud.pubsub.audit.topic | The target topic name for audit message     |
        | file.process.partition.size        | The size of the each small file             |

###  4. How to create Application micro service
Source agents are start points on a spring cloud stream flow. CAMP libraries provide a bean to act as an spring cloud stream source, Application service needs to provide the business logic getPayload bean for basic validation on input file then send data records messages (stream mode) or spliited files messages (microbatch mode) to downstream topic.  And also send file audit message to audit topic. Then archive the processed file.

Step to create source micro service

   - [1] Based on project decide which mode to use : stream or microbatch
   - [2] Based on mode create maven project and add dependencies
   - [3] Create Spring stream bean class to implements ```getPayload```
   - [4] Based on business project and GCP project information set configuration in application.properties

* **Pubsub GCS Source Stream Mode Agent** and **RabbitMQ GCS Source Stream Agent**
Here is bean interface to implements Stream Mode Source service:

```java
@Component("senderBatchProcessor")
public class GcsListSourceGenerator implements BusinessBatchProcessor {
    public List<FileSummaryFileRecord> getPayload(List<FileSummaryFileRecord> fileRecords) {    
        ...
```
Example service maven project: [Pubsub Source Service](https://github.com/telus/cio-mediation/tree/nonprod/mediation-cloud-usage-demo/cmi-batch2stream-gcs-pubsub-source) | [RabbitMQ Source Service](https://github.com/telus/cio-mediation/tree/nonprod/mediation-cloud-usage-demo/cmi-batch2stream-gcs-rabbit-source)

* **Pubsub GCS Source Microbatch Mode Agent** 
Here is bean interface to implements Microbatch Mode Source service:

```java
@Component("senderBatchProcessor")
public class GcsListSourceGenerator implements BusinessBatchProcessor {
    public List<FileSummaryFileRecord> getPayload(List<FileSummaryFileRecord> fileRecords) {  
        ...
```
Example service maven project: [Pubsub Microbatch Source Service](https://github.com/telus/cio-mediation/tree/nonprod/mediation-cloud-usage-demo/cmi-batch2stream-gcs-pubsub-microbatch-source) 
### 5. Maven dependencies
In order to produce a spring cloud stream microservice, in addition to the spring dependencies, the following CAMP dependencies must be added to the service pom file:

```xml
        <dependency>
            <groupId>com.telus.mediationCloud</groupId>
            <artifactId>common-api</artifactId>
        </dependency>
        <dependency>
            <groupId>com.telus.mediationCloud</groupId>
            <artifactId>common-cache</artifactId>
        </dependency>
        <dependency>
            <groupId>com.telus.mediationCloud</groupId>
            <artifactId>common-gcs-file-producers</artifactId>
        </dependency>
        <dependency>
            <groupId>com.telus.mediationCloudUsage</groupId>
            <artifactId>cmi-business-models</artifactId>
        </dependency>
```

* Based on the mode and message channel 
  
```xml
        RabbitMQ Stream mode 
        <dependency>
            <groupId>com.telus.mediationCloud</groupId>
            <artifactId>batch-source-rabbit-stream-agent</artifactId>
        </dependency>
```

```xml
        Pubsub Stream mode 
        <dependency>
            <groupId>com.telus.mediationCloud</groupId>
            <artifactId>batch-source-pubsub-stream-agent</artifactId>
        </dependency>
```
 
```xml
        Pubsub Microbatch mode 
        <dependency>
            <groupId>com.telus.mediationCloud</groupId>
            <artifactId>batch-source-pubsub-microbatch-agent</artifactId>
        </dependency>
```
----------------------

### Processor Agent
#### 1. Overview
Processor is a agent to consumes message from a destination and produces messages to send to another destination. Processor will implements business logic like data validation , data transformation and data lookup.
Then pass the messages to downstream.

#### 2. Processor Agent Details
There are 2 mode for processing. Stream mode and Microbatch mode. each mode will have there own agent and based different message channel (Pubsub or RabbitMQ).

* Common configuration properties

    | Name                                                       | Description                                                      |
    |------------------------------------------------------------|------------------------------------------------------------------|
    | spring.cloud.function.definition                           | The cloud function name for streaming. `messageProcess`          |
    | spring.cloud.stream.function.bindings.messageProcess-in-0  | `input`                                                          |
    | spring.cloud.stream.function.bindings.messageProcess-out-0 | `output`                                                         |
    | mediation.cloud.project                                    | The business project name, e.g. `CMI`                            |
    | mediation.cloud.businessprocessorfactory.ProcessorName     | The business processor bean name, e.g. `GeneralMessageProcessor` |
    | file.after.process                                         | `delete` since this is in middle of data stream                  |

##### Processor Stream Mode Agent 
For GCS Processor Stream agent: It will subscribe the incoming message from Source Agent. Then implements business logic then sends processed message to downstream topic.

* **Pubsub Processor Stream Mode Agent**: use Pubsub as message channel 
    * Module:  **stream-processor-general-pubsub-agent**
    * Config properties: 
 
        | Pubsub Properties                              | Description                                            |
        |------------------------------------------------|--------------------------------------------------------|
        | spring.cloud.gcp.project-id                    | The GCP project id                                     |
        | mediation.cloud.pubsub.data.topic              | The target topic name for data send message            |
        | mediation.cloud.pubsub.audit.topic             | The target topic name for audit message                |
        | spring.cloud.stream.bindings.input.destination | The input topic name for incoming message              |
        | spring.cloud.stream.bindings.input.group       | The input topic subscription name for incoming message |

* **RabbitMQ Processor Stream Agent**:  use RabbitMQ as message channel
    * Module:  **stream-processor-general-rabbit-agent**
    * Config properties: 
 
        | RabbitMQ Properties      | Description                            |
        |--------------------------|----------------------------------------|
        | spring.rabbitmq.host     | RabbitMQ server connection information |
        | spring.rabbitmq.port     |                                        |
        | spring.rabbitmq.username |                                        |
        | spring.rabbitmq.password |                                        |

##### GCS Processor Microbatch Mode Agent 
####  4. How to create Application micro service
Processor agents are middle components on a spring cloud stream flow. CAMP libraries provide a bean to act as an spring cloud stream processor, Application service needs to provide the business logic getPayload bean for validation, transformation and lookup on input message then send data records messages (stream mode) or spliited files messages (microbatch mode) to downstream topic.  And also send file audit message to audit topic. Then delete the processed temp file(if microbatch mode).

Step to create processor micro service

   - [1] Based on project decide which mode to use : stream or microbatch
   - [2] Based on mode create maven project and add dependencies
   - [3] Create Spring stream bean class to implements ```getPayload```
   - [4] Based on business project and GCP project information set configuration in application.properties

* **Pubsub GCS Processor Stream Mode Agent** and **RabbitMQ GCS Processor Stream Agent**
Here is bean interface to implements Stream Mode processor service:

```java
@Component("GeneralMessageProcessor")
public class GeneralMessageProcessor implements BusinessProcessor {
    public Object getPayload(BaseMessage baseMessage) {  
        ...
```
Example service maven project: [Pubsub Processor Service](https://github.com/telus/cio-mediation/tree/nonprod/mediation-cloud-usage-demo/cmi-message-pubsub-processor) | [RabbitMQ Processor Service](https://github.com/telus/cio-mediation/tree/nonprod/mediation-cloud-usage-demo/cmi-message-rabbit-processor)

* **Pubsub GCS Source Microbatch Mode Agent** 
Here is bean interface to implements Microbatch Mode processor service:

```java
@Component("GeneralMessageProcessor")
public class GeneralMessageProcessor implements BusinessProcessor {
    public Object getPayload(BaseMessage baseMessage) {  
        ...
```

Example service maven project: [Pubsub Microbatch Processor Service](https://github.com/telus/cio-mediation/tree/nonprod/mediation-cloud-usage-demo/cmi-message-pubsub-microbatch-processor) 
#### 5. Maven dependencies
In order to produce a spring cloud stream microservice, in addition to the spring dependencies, the following CAMP dependencies must be added to the service pom file:

```xml
        <dependency>
            <groupId>com.telus.mediationCloud</groupId>
            <artifactId>common-api</artifactId>
        </dependency>
        <dependency>
            <groupId>com.telus.mediationCloud</groupId>
            <artifactId>common-cache</artifactId>
        </dependency>
        <dependency>
            <groupId>com.telus.mediationCloud</groupId>
            <artifactId>common-gcs-file-producers</artifactId>
        </dependency>
        <dependency>
            <groupId>com.telus.mediationCloudUsage</groupId>
            <artifactId>cmi-business-models</artifactId>
        </dependency>
```

* Based on the mode and message channel 
  
```xml
        RabbitMQ Stream mode 
        <dependency>
            <groupId>com.telus.mediationCloud</groupId>
            <artifactId>stream-processor-general-rabbit-agent</artifactId>
        </dependency>
```

```xml
        Pubsub Stream mode 
        <dependency>
            <groupId>com.telus.mediationCloud</groupId>
            <artifactId>stream-processor-general-pubsub-agent</artifactId>
        </dependency>
```
 
```xml
        Pubsub Microbatch mode 
        <dependency>
            <groupId>com.telus.mediationCloud</groupId>
            <artifactId>stream-processor-general-pubsub-microbatch-agent</artifactId>
        </dependency>
```
----------------------
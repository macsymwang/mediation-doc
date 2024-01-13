
- [Introduction](#introduction)
  - [1. Create schema **camp**, and all roles for database control](#1-create-schema-camp-and-all-roles-for-database-control)
  - [2. Create DB user postgreops](#2-create-db-user-postgreops)
  - [3. Create common components](#3-create-common-components)
  - [4. Create Project Schema, Roles and Tables](#4-create-project-schema-roles-and-tables)
  - [6. Cloud Scheduler](#6-cloud-scheduler)
  - [7. Cloud Function](#7-cloud-function)
  - [8. Create new DB user account](#8-create-new-db-user-account)

# Introduction 
This is document about Mediation CloudSQL postgre Database maintenance jobs like create common schema , tables and store procedure for table partition.
This is assumed already created CloudSQL database by terraform for the projects. if the database common components already created you can skip to step 4.


## 1. Create schema **camp**, and all roles for database control
**camp** schema is common schema for all mediation common components, like transaction_outbox table, all store functions and procedures.
- login the database as **postgre**
- create **camp** schema and camp_all, camp_read roles
> execute the SQL: [create schema and roles](https://github.com/telus/cio-mediation-db-ddl/blob/master/mediation-common/camp/Roles_And_Schemas.sql)

## 2. Create DB user postgreops
   **postgreops** is user for all DB maintenance jobs, like create table , partition creation and drop.  
   - reuse same  password with super user **postgre**
   - login the database as **postgre**
```
CREATE USER postgresops WITH PASSWORD '<password>';
GRANT postgres TO postgresops;
```
  
## 3. Create common components
- ### login the database as ***postgresops***

- ### Create common tables
  create common tables like transaction_outbox which share by many CAMP agents

  > execute the SQL: [create transaction_outbox](https://github.com/telus/cio-mediation-db-ddl/blob/master/mediation-common/camp/camp.transaction_outbox.sql)

- ### Create common store functions and store procedures
  - camp.create_daily_partition : the function to create daily partition based on TIMESTAMP(0) column , most for EDR tables. example **sap_event_detail_ts** on [sap_event_detail](https://github.com/telus/cio-mediation-db-ddl/blob/master/mediation-b2b/cloud_ipdrm/edradm/edramd.sap_event_detail_Postgres_PR.sql) table.
  > execute create sql: [create_daily_partition](https://github.com/telus/cio-mediation-db-ddl/blob/master/mediation-common/camp/create_daily_partition.sql)

  - camp.create_daily_sub_partition : the function to create daily partition on TIMESTAMP(0) column and sub partition on bill cycle code column. most for TDR tables. example **med_data_srvc_event_ts** and **billing_cycle_cd** on [rated_data_srvc_event](https://github.com/telus/cio-mediation-db-ddl/blob/master/mediation-b2b/cloud_ipdrm/ipadm/ipdadm.rated_data_srvc_event_Postgres.sql) table.
  > execute create sql: [create_daily_sub_partition](https://github.com/telus/cio-mediation-db-ddl/blob/master/mediation-common/camp/create_daily_sub_partition.sql)
  
  - camp.drop_daily_partition :  the function to drop  daily partition
  > execute create sql: [drop_daily_partition](https://github.com/telus/cio-mediation-db-ddl/blob/master/mediation-common/camp/drop_daily_partition.sql)
  
---
> All below as for your project specific change, here use b2b database as example. 
> you should change the names based on projects.
---

## 4. Create Project Schema, Roles and Tables
- ### login the database as ***postgresops***

- ### create project schema
  
- ### create project role
- ### create project table

## 6. Cloud Scheduler

## 7. Cloud Function

## 8. Create new DB user account
- [Steps to create WIF accounts for CAMP services to passwordless access to GCP resources and CLOUD sql
](https://docs.google.com/document/d/1xRPOuXNuonoZhSUP1vpN4VmiEkZyGtQGcB_jQIf4nGM/edit)
create user Milica identified by ftn
    default tablespace USERS temporary tablespace TEMP;
    grant connect, resource to Milica;
    grant create table to Milica;
    grant create view to Milica;
    grant create procedure to Milica;
    grant create synonym to Milica;
    grant create sequence to Milica;
    grant select on dba_rollback_segs to Milica;
    grant select on dba_segments to Milica;
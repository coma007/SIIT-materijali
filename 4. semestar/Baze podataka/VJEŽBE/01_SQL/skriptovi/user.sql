create user Exxxxx identified by ftn
	default tablespace USERS temporary tablespace TEMP;


	grant connect, resource to Exxxxx;

	grant create table to Exxxxx;

	grant create view to Exxxxx;

	grant create procedure to Exxxxx;

	grant create synonym to Exxxxx;

	grant create sequence to Exxxxx;

	grant select on dba_rollback_segs to Exxxxx;

	grant select on dba_segments to Exxxxx;

	grant unlimited tablespace to Exxxxx;
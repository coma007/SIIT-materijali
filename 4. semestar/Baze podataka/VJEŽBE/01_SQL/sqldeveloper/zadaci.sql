select * from radnik;

select * from projekat;

select * from radproj;

select ime, prz from radnik;

select DISTINCT * from radnik;

select ime, prz, mbr
from radnik
where plt > 25000;

select ime, prz 
from radnik
where sef is null;

select r2.ime, r2.prz
from radnik r1, radnik r2
where r1.sef = r2.mbr
group by (r2.ime, r2.prz) ;

select mbr, ime, prz
from radnik
where plt between 20000 and 24000;

select mbr, ime, prz
from radnik
where plt > 20000 and plt < 24000;

select mbr, ime, prz, god
from radnik
where god between '01-JAN-1953' and '31-DEC-1975';

select mbr, ime, prz, god
from radnik
where god not between '01-JAN-1953' and '31-DEC-1975';

select mbr, ime, prz
from radnik
where ime like 'M%';

select mbr, ime, prz
from radnik
where ime not like 'A%';

select mbr, ime, prz
from radnik
where ime like '__r%';


select mbr, ime, prz
from radnik
where prz like 'R%';

select distinct ime 
from radnik
where ime like 'E%';

select * 
from radnik r
where r.ime like '%E%' or ime like;

select distinct mbr 
from radproj
where spr in (10, 20, 30);

select distinct mbr 
from radproj
where spr = 10 or brc in (2,4,6);

select distinct mbr
from radnik
where ime not in ('Ana', 'Sanja');

select ime, prz
from radnik
where sef is not null
order by 1, 2 asc;

select mbr, ime, prz, plt 
from radnik
order by plt desc;

select mbr, ime || ' ' || prz "ime i prezime", plt * 117 
from radnik;

select *
from radnik
where lower(prz) like ('%' || lower(ime) || '%');

select mbr, ime, prz, plt
from radnik
where ime = any ('Pera', 'Moma');

select mbr, ime, prz, plt
from radnik
where ime != all ('Pera', 'Moma');

select mbr,  plt + null
from radnik;

select mbr, nvl(plt + pre, plt)
from radnik;

select count(distinct sef)
from radnik;

select count(*)
from radnik;

select max(sef)
from radnik;

select sum(distinct sef)
from radnik;

select count(sef)
from radnik;


select min(plt), max(plt)
from radnik;

select count(*), round(avg(plt),2), sum(plt*12)
from radnik;

select plt, (select avg(plt) from radnik), abs((select(avg(plt)) from radnik) - plt)
from radnik;

select sum(pre)
from radnik
where mbr > 100;

select * from 
(select mbr, ime from radnik);

select mbr, plt, rownum
from radnik where rownum <= 10
order by plt desc;

select mbr, plt, rownum
from 
(select *
from radnik
order by plt desc)
where rownum <= 10;

select plt as plata, 
(select round(avg(plt),2) from radnik) as prosjek,
abs((select round(avg(plt),2) from radnik) - plt) as razlika
from radnik;

select mbr, count(spr)
from radproj
where mbr < 40
group by mbr, spr;

select spr, count(mbr), sum(brc)
from radproj
group by spr;

select mbr, count(spr)
from radproj
group by mbr
having count(spr) > 2;

select mbr, ime, prz, plt
from radnik
where plt > (select avg(plt) from radnik)
order by plt asc;

select ime, prz
from radnik
where mbr = any (select mbr 
from radproj
where spr = 30);

select mbr, ime, prz
from radnik
where mbr in 
(select mbr from radproj where spr = 10 and spr != 30);

select mbr, spr from radproj where spr = 10 and spr != 30;
select mbr, spr from radproj where spr = 10;

select mbr, ime, prz
from radnik
where mbr in 
(select mbr from radproj where spr = 10)
and mbr not in
(select mbr from radproj where spr = 30);

select mbr, ime, prz
from radnik
where mbr in 
(select mbr from radproj where spr=10)
and mbr not in 
(select mbr from radproj where spr=30);

select ime, prz, god
from radnik
where god = (select max(god) from radnik);

select ime, prz, god
from radnik
where god >= all(select god from radnik);

select r.mbr, prz, ime, plt, brc
from radnik r, radproj rp
where spr = 10 and r.mbr = rp.mbr;

select r.mbr, ime, prz, plt
from radnik r, projekat p
where r.mbr = p.ruk
group by r.mbr, ime, prz, plt;

select distinct mbr, ime, prz, plt
from radnik, projekat
where ruk=mbr;

select distinct ime, prz
from radnik r, projekat p
where p.spr = 10 and r.mbr != p.ruk;

select ime, prz 
from radnik
where mbr != (select ruk from projekat where spr = 10);

select distinct nap
from projekat p, radproj rp
where p.spr = rp.spr 
and rp.mbr in (select mbr from radproj where spr = 60);

select nap
from projekat
where spr in 
(select spr from radproj where mbr in
(select mbr from radproj where spr = 60));

select ime, prz, count(nap)
from radnik, projekat
where mbr = ruk
group by ime, prz;

select r.mbr, prz, ime, count(spr), sum(brc)
from radnik r, radproj rp
where r.mbr = rp.mbr
group by r.mbr, prz, ime;

select ime, prz, sum(distinct rp.spr)
from radnik r, projekat p, radproj rp
where r.mbr = rp.mbr and r.mbr = p. ruk
group by r.mbr, ime, prz;

select nap, sum(brc)
from projekat p, radproj rp
where p.spr = rp.spr
group by nap
having sum(brc) > 15;

select p.spr, p.nap, sum(mbr)
from projekat p, radproj rp
where p.spr = rp.spr
group by p.spr, p.nap
having sum(mbr) > 2;

select p.spr, p.nap
from projekat p, radproj rp
where p.spr = rp.spr
group by p.spr, p.nap
having avg(brc) > (select avg(brc) from radproj);

select p.spr, p.nap
from projekat p, radproj rp
where p.spr = rp.spr
group by p.spr, p.nap
having avg(brc) >= 
all (select avg(brc)
from radproj
group by spr);

select mbr, ime, prz, plt
from radnik r
where plt > (select plt from radnik where mbr = 40);

select r.mbr, r.ime, r.prz, r.plt
from radnik r, radnik rc
where r.plt > rc.plt and rc.mbr = 40
order by plt;

select mbr, ime, prz, plt
from radnik
where plt > all (select plt from radnik where mbr = 40)
order by plt;

select distinct r.ime, r.prz, r.plt
from radnik r, radnik rc, projekat p, radproj rp
where rc.mbr = p.ruk and r.mbr = rp.mbr and rp.spr = p.spr
and r.plt <= rc.plt - 1000;

select distinct r1.ime, r1.prz, r1.plt from 
radnik r1, radnik r2, projekat p, radproj rp
where r1.mbr=rp.mbr and rp.spr=p.spr and 
p.ruk=r2.mbr and r1.plt+1000<r2.plt;

select r.mbr, ime, prz, plt
from radnik r, radproj rp1
where r.mbr = rp1.mbr and 
rp1.brc > (select avg(brc) from radproj rp2 where rp2.spr = rp1.spr);

select *
from radnik r
where not exists (select * from radnik r1 where r1.god < r.god);

select * 
from radnik r
where not exists (select * from radproj rp where rp.mbr = r.mbr);

select mbr, ime, prz
from radnik r
where not exists 
(select * from radproj rp where rp.mbr = r.mbr and rp.spr = 10);

select *
from radnik
where not exists
(select ruk from projekat where ruk=mbr);

select distinct r.* 
from radnik r, projekat p
where r.mbr = p.ruk and not exists
(select god from radnik r1, projekat p1
where r1.mbr = p1.ruk and r1.god > r.god);

select r.mbr, ime, prz
from radnik r, radproj rp
where r.mbr = rp.mbr and (rp.spr = 20 or plt > (select avg(plt) from radnik))
group by r.mbr, ime, prz;

select r.mbr, ime, prz
from radnik r, radproj rp
where r.mbr = rp.mbr and rp.spr = 20
union 
select r.mbr, ime, prz
from radnik r, radproj rp
where r.mbr = rp.mbr and plt > (select avg(plt) from radnik);

select mbr, ime, prz
from radnik
where prz like 'M%' or prz like 'R%'
intersect
select mbr, ime, prz
from radnik
where prz like 'M%' or prz like 'P%';

select mbr, ime, prz
from radnik
where prz like 'M%';

select r.*
from radnik r, radproj rp
where r.mbr = rp.mbr and rp.spr = 30;

select ime, prz
from radnik natural join radproj
where spr=30;

select ime, prz
from radnik r inner join radproj rp
on r.mbr = rp.mbr
where spr=30;

select r.mbr, ime, prz, spr
from radnik r left outer join radproj rp
on r.mbr = rp.mbr;

select mbr, ime, prz, nvl(nap, 'ne rukovodi')
from radnik r left outer join projekat p
on mbr = ruk;

select nap, nvl(mbr, 0)
from radproj rp right outer join projekat p
on p.spr = rp.spr;

select r.mbr, ime, prz, spr
from radnik r left outer join radproj rp
on r.mbr = rp.mbr;

select r.mbr, prz, ime, nvl(p.spr, 0), nvl(nap, 'ne postoji')
from radnik r left outer join radproj rp
on r.mbr = rp.mbr 
left outer join projekat p
on rp.spr = p.spr
order by r.mbr;

select r.ime, r.prz, nvl(s.prz, 'nema sefa') sef
from radnik r left outer join radnik s
on r.sef = s.mbr;

select *
from radnik, projekat;

select *
from radnik cross join projekat;

select *
from radnik natural join radproj;

select brc, nap, count(mbr)
from projekat cross join radproj
group by brc, nap
order by brc desc;

SELECT brc, COUNT(mbr) 
FROM radproj GROUP BY brc 
ORDER BY brc DESC;

select mbr, ime, prz, count(spr)
from radnik left outer join projekat
on mbr = ruk
group by mbr, ime, prz
having count(spr) <
(select avg(count(spr)) 
from radnik r left outer join radproj rp
on r.mbr = rp.mbr
where prz not like '%ic'
group by r.mbr);

select avg(count(spr)) 
from radnik r left outer join radproj rp
on r.mbr = rp.mbr
where prz not like '%ic'
group by r.mbr;

SELECT mbr, ime, COUNT(spr) br_pr_rukovodi
FROM radnik r LEFT OUTER JOIN projekat p on r.mbr=p.ruk
GROUP BY mbr, ime HAVING COUNT(spr) < (SELECT 
AVG(COUNT(spr)) FROM radproj rp, radnik r 
WHERE rp.mbr = r.mbr
AND prz NOT LIKE '%ic'
GROUP BY r.mbr);

select mbr, ime, prz, plt,
case
when plt < 10000 then 'mala primanja'
when plt >= 10000 and plt < 20000 then 'srednje visoka primanja'
when plt >= 20000 and plt < 30000 then 'visoka primanja'
else 'izuzetno visoka primanja'
end as primanja
from radnik
order by
case primanja
when 'mala primanja' then 4
when 'srednje visoka primanja' then 3
when 'visoka primanja' then 2
else 1
end, plt asc;

select mbr, ime, prz, plt, sef
from radnik
order by
case
when sef is null then 1
else 2
end, plt desc;

insert into radnik (mbr, ime, prz, sef, plt, pre, god)
values (101, 'Marinko', 'Rokvic', 10, 12000, 0, '28-may-1999');

select * from radnik where mbr = 101;

delete radnik where mbr = 101;

delete radnik;

update radnik
set plt = plt * 1.2;

rollback;

create table faze_projekta (
    spr integer not null, 
    sfp integer not null,
    rukfp integer,
    nafp varchar(20),
    datp date,
    constraint fp_pk primary key (spr, sfp),
    constraint fp_fk1 foreign key (spr) references projekat (spr),
    constraint fp_fk2 foreign key (rukfp) references radnik (mbr),
    constraint fp_nap unique (nafp));
    
insert into faze_projekta (spr, sfp, rukfp, nafp, datp)
values (10, 1, 101, 'Fazica', '01-JAN-2022');

select * from faze_projekta
where sfp = 1;

alter table faze_projekta
add datz date;

alter table faze_projekta
add constraint fp_dates check (datp < datz);

select * from faze_projekta;

update faze_projekta
set datz = '02-JAN-2022'
where spr = 10;

select *
from radnik
where prz like substr(ime, 1, 3) || '%';

select trim(trailing 'a' from ime), prz
from radnik
where ime like '%a';

create or replace view radnik_plata (ime, prezime, plata)
as (select ime, prz, plt 
from radnik);

create or replace view radnik_angazovanje (mbr, uk_brc) as 
(select radnik.mbr, nvl(sum(brc), 0)
from radnik left outer join radproj
on radnik.mbr = radproj.mbr
group by radnik.mbr);

create or replace view sefovi (mbr, prz, ime, radnici, uk_brc) as 
(select s.mbr, s.prz, s.ime, count(r.mbr), uk_brc
from radnik r, radnik s, radnik_angazovanje ra
where s.mbr = r.sef and s.mbr = ra.mbr
group by s.mbr, s.prz, s.ime, uk_brc);

select sum(uk_brc)
from sefovi;

with proj_angaz as (
select spr, count (mbr) as tot
from radproj
group by spr
)
select r.mbr, prz, ime, rp.spr, pa.tot-1
from radnik r, radproj rp, proj_angaz pa
where r.mbr = rp.mbr and rp.spr = pa.spr;

with angazman as (
select spr, sum(brc) ang
from radproj
group by spr
)
select r.mbr, prz, ime, rp.spr, brc/a.ang
from radnik r, radproj rp, angazman a
where r.mbr = rp.mbr and rp.spr = a.spr;

with pr_angazman as (
select spr, avg(brc) pr_ang
from radproj
group by spr
)
select r.mbr, prz, ime, plt
from radnik r, radproj rp, pr_angazman a
where r.mbr = rp.mbr and rp.spr = a.spr and rp.brc > a.pr_ang
group by r.mbr, prz, ime, plt
order by r.mbr;

with angazman_radnika as (
select mbr, sum(brc) ang
from radproj
group by mbr),
sefovi as (
select s.mbr 
from radnik r, radnik s
where r.sef = s.mbr)
select s.mbr, ar.ang
from sefovi s, angazman_radnika ar
where s.mbr = ar.mbr
group by s.mbr, ar.ang;

with angazman_radnika as (
select mbr, sum(brc) ang
from radproj
group by mbr),
sefovi as (
select s.mbr 
from radnik r, radnik s
where r.sef = s.mbr)
select sum(ar.ang)
from sefovi s, angazman_radnika ar
where s.mbr = ar.mbr;

with angaz_po_radnicima (mbr, sbrc) as (
select r.mbr, nvl(sum(rp.brc), 0)
from radnik r, radproj rp
where r.mbr = rp.mbr (+)
group by r.mbr),
angaz_sefova (mbr, prz, ime, brrad, brsat) as (
select distinct r.sef, r1.prz, r1.ime, count(*), a.sbrc
from radnik r, radnik r1, angaz_po_radnicima a
where r.Sef = r1.Mbr and r.Sef = a.Mbr
group by r.Sef, r1.Prz, r1.Ime, a.SBrc)
select sum(brsat) as ukangsef
from angaz_sefova;
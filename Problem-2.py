emp = (('ID','LAST_NAME', 'FIRST_NAME', 'USERID', 'START_DATE', 'COMMENTS', 'TITLE', 'SALARY', 'COMMISSION', 'DEPT_ID','MANAGER_ID'),
       (1, 'MARTIN', 'CARMEN', 'MARTINCU', '1990-03-03', '', 'PRESIDENT', 4500.0, '', 50, ''),
       (10, 'JACKSON', 'MARTA', 'JACKSOMT', '1991-02-27', '', 'WAREHOUSE MANAGER', 1507.0, '', 45, 2),
       (11, 'HENDERSON', 'COLIN', 'HENDERCS', '1990-05-14', '', 'SALES REPRESENTATIVE', 1400.0, 10 , 31, 3),       
       (12, 'GILSON', 'SAM', 'MARTINCU', '1992-01-18', '', 'SALES REPRESENTATIVE', 1490.0, 12.5, 32, 3),
       (13, 'SANDERS', 'JASON', 'GILSONSJ', '1991-02-18', '', 'SALES REPRESENTATIVE', 1515.0, 10, 33, 3),
       (14, 'DAMERSON', 'ANDRE', 'SANDERJK', '1991-10-09', '', 'SALES REPRESENTATIVE', 1450.0, 17.5, 35, 3),
       (15, 'HARDWICK', 'ELAINE', 'HARDWIEM', '1992-02-07', '', 'STOCK CLERK', 1400.0,'' , 41, 6),
       (16, 'BROWN', 'GEORGE', 'BROWNGW', '1990-03-08', '', 'STOCK CLERK', 940.0, '', 41, 6),
       (17, 'WASHINGTON', 'THOMAS', 'WASHINTL', '1991-02-09', '', 'STOCK CLERK', 1200.0, '', 42, 7),
       (18, 'PATTERSON', 'DONALD', 'PATTERDV', '1991-08-06', '', 'STOCK CLERK', 795.0, '', 42, 7),
       (19, 'BELL', 'ALEXANDER', 'BELLAG', '1991-05-26', '', 'STOCK CLERK', 850.0,'', 43, 8),
       (2, 'SMITH', 'DORIS', 'SMITHDJ', '1990-03-08', '', 'VP, OPERATIONS', 2450.0, '', 41, 1),
       (20, 'GANTOS', 'EDDIE', 'GANTOSEJ', '1990-11-30', '', 'STOCK CLERK', 800.0, '', 44, 9),
       (21, 'STEPHENSON', 'BLAINE', 'STEPHEBS', '1991-03-17', '', 'STOCK CLERK', 860.0, '', 45, 10),
       (22, 'CHESTER', 'EDDIE', 'CHESTEEK', '1990-11-30', '', 'STOCK CLERK', 80.0, '', 44, 9),
       (23, 'PEARL', 'ROGER', 'PEARLRG', '1990-10-17', '', 'STOCK CLERK', 795.0, '', 34, 9),
       (24, 'DANCER', 'BONNIE', 'DANCERBW', '1991-03-17', '', 'STOCK CLERK', 860.0, '', 45, 7),
       (25, 'SCHMITT', 'SANDRA', 'SCHMITTS', '1991-05-09', '', 'STOCK CLERK', 1100.0, '', 45, 8),
       (3, 'NORTON', 'MICHAEL', 'NORTONMA', '1990-06-17', '', 'VP, Sales', 2400.0, '', 31, 1),
       (4, 'QUENTIN', 'MARK', 'QUENTIML', '1990-04-07', '', 'Vp, Finance', 2450.0, '', 10, 1),
       (5, 'ROPER', 'JOSEPH', 'ROPERJM', '1990-03-04', '', 'VP, Administration', 2550.0, '', 50, 1),
       (6, 'BROWN', 'MOLLY', 'BROWNMR', '1991-01-18', '', 'WAREHOUSE MANAGER', 1600.0, '', 41, 2),
       (7, 'HAWKINS', 'ROBERTA', 'HAWKINRT', '1990-05-14', '', 'WAREHOUSE MANAGER', 1650.0, '', 42, 2),
       (8, 'BURNS', 'BEN', 'BURNSBA', '1990-04-07', '', 'WAREHOUSE MANAGER', 1500.0, '', 43, 2),
       (9, 'CATSKILL', 'CATSKIAW', 'MARTINCU', '1992-02-09', '', 'WAREHOUSE MANAGER', 1700.0, '', 44, 2))


dept = (('ID', 'NAME', 'REGION_ID'),
        (10, 'FINANCE', 1),
        (31, 'SALES', 1),
        (32, 'SALES', 2),
        (33, 'SALES', 3),
        (34, 'SALES', 4),
        (35, 'SALES', 5),
        (41, 'OPERATIONS', 1),
        (42, 'OPERATIONS', 2),
        (43, 'OPERATIONS', 3),
        (44, 'OPERATIONS', 4),
        (45, 'OPERATIONS', 5),
        (50, 'ADMINISTRATION', 1))



# select * from s_dept;

print "\nselect * from s_dept:", emp[1::] 

# select last_name, first_name, title, salary from s_emp;

print "\nselect last_name, first_name, title, salary from s_emp:", \
[  [  i[1], i[2], i[6], i[7]  ] for i in emp[1::]  ]


# select last_name, first_name, title, salary from s_emp where salary > 1500 and dept_id > 40;

print "\nselect last_name, first_name, title, salary from s_emp where salary > 1500 and dept_id > 40:", \
[  [  i[1], i[2], i[6], i[7]  ] for i in emp[1::] if i[7] > 1500 and i[9] > 40 ]



# select last_name, first_name, title, salary from s_emp where salary > 1500 and dept_id > 40 order by last_name;

print "\nselect last_name, first_name, title, salary from s_emp where salary > 1500 and dept_id > 40 order by last_name:", \
sorted ( [  [  i[1], i[2], i[6], i[7]  ] for i in emp[1::] if i[7] > 1500 and i[9] > 40], key = lambda x: x[0])



# select last_name, first_name, title, salary from s_emp where salary > 1500 and dept_id > 40 order by salary desc;

print "\nselect last_name, first_name, title, salary from s_emp where salary > 1500 and dept_id > 40 order by salary desc:", \
sorted ( [  [  i[1], i[2], i[6], i[7]  ] for i in emp[1::] if i[7] > 1500 and i[9] > 40], key = lambda x: x[3])


# select last_name, first_name, title, salary, name from s_emp e join s_dept d on(e.dept_id = d.id);

print "\nselect last_name, first_name, title, salary, name from s_emp e join s_dept d on(e.dept_id = d.id):",

[ [ i[1], i[2], i[6], i[7], j[1] ] for i in emp[1::] for j in dept[1::] ]


# select dept_id, avg(salary) from s_emp group by dept_id order by dept_id;

for department in { d[9] for d in emp[1::] }: print (lambda deptID, avgSal: (deptID, avgSal))(department, (lambda l: round(sum(l) / len(l), 2))(map(float,[ e[7] for e in emp[1::] if e[9] == department ])))

# select dept_id, avg(salary) from s_emp group by dept_id having avg(salary) < 1500;
      
print "\nselect dept_id, avg(salary) from s_emp group by dept_id having avg(salary) < 1500:", 

for department in { d[9] for d in emp[1::] }: print (lambda deptID, avgSal: (deptID, avgSal) if avgSal > 1500 else '')(department, (lambda l: round(sum(l) / len(l), 2))(map(float,[ e[7] for e in emp[1::] if e[9] == department ])))

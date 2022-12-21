/* PFFAFFMANN EXAMPLE
create table movies (
      id         INT NOT NULL UNIQUE,
      title      CHAR NOT NULL,
      year       INT NOT NULL,
      length     INT NOT NULL,
      studioId    INT NOT NULL,
      cost       INT NOT NULL         );
*/

/* Internet Example
CREATE TABLE Orders (
    OrderID int NOT NULL,
    OrderNumber int NOT NULL,
    PersonID int,
    PRIMARY KEY (OrderID),
    FOREIGN KEY (PersonID) REFERENCES Persons(PersonID)
);
*/

create table residencehall (
    hallid              INT NOT NULL UNIQUE,
    hallname            VARCHAR(250) NOT NULL,
    location            VARCHAR(250) NOT NULL,
    floors              INT NOT NULL,
    tier                INT NOT NULL,
    capacity            INT NOT NULL,
    oncampus            BOOLEAN NOT NULL,
    PRIMARY KEY (hallid)
);

create table student (
    lnumber             INT NOT NULL UNIQUE,
    hallid              INT NOT NULL,
    firstname           VARCHAR(250) NOT NULL,
    middlename          VARCHAR(250),
    lastname            VARCHAR(250) NOT NULL,
    classyear           INT NOT NULL,
    email               VARCHAR(50) NOT NULL,
    phonenumber         VARCHAR(20) NOT NULL,
    adress              VARCHAR(120) NOT NULL,
    dob                 DATE NOT NULL,
    pobox               VARCHAR(4) NOT NULL,
    emergencycontact    VARCHAR(15) NOT NULL,
    mealplan            INT NOT NULL,
    graduated           INT,
    notes               VARCHAR(250),
    PRIMARY KEY (lnumber),
    FOREIGN KEY (hallid) REFERENCES residencehall(hallid)
);

create table course (
    courseid             INT NOT NULL UNIQUE, /* Arbitrary unique identifier */
    coursenumber         INT NOT NULL,   /* This represents the 320 in "CS320" */       
    department          VARCHAR(250) NOT NULL,  /* This represents the "CS" in "CS320" */
    name                VARCHAR(250) NOT NULL,
    description         VARCHAR(250),
    PRIMARY KEY (courseid)
);

create table major (
    majorid INT NOT NULL UNIQUE,
    majorname VARCHAR(250) NOT NULL,
    majordegree VARCHAR(250) NOT NULL,
    PRIMARY KEY(majorid) 
);

create table majorcoursereqs (
    majorid INT NOT NULL, 
    courseid INT NOT NULL,
    FOREIGN KEY (majorid) REFERENCES major(majorid),
    FOREIGN KEY (courseid) REFERENCES course(courseid)
);

create table studentmajor (
    studentid INT NOT NULL,
    majorid INT NOT NULL,
    FOREIGN KEY (studentid) REFERENCES student(lnumber),
    FOREIGN KEY (majorid) REFERENCES major(majorid)
);

create table jobtype (
    jobid               INT NOT NULL UNIQUE,
    jobname             CHAR(250) NOT NULL UNIQUE,
    hours               INT NOT NULL,
    PRIMARY KEY (jobid)
);

create table staff (
    staffid             INT NOT NULL UNIQUE,
    jobid               INT NOT NULL,
    firstname           VARCHAR(250) NOT NULL,
    middlename          VARCHAR(250),
    lastname            VARCHAR(250) NOT NULL,
    yearsworked         INT NOT NULL,
    tenure              BOOLEAN NOT NULL,
    department          VARCHAR(250) NOT NULL,
    location            VARCHAR(250) NOT NULL,
    salary              INT NOT NULL,
    PRIMARY KEY (staffid),
    FOREIGN KEY (jobid) REFERENCES jobtype(jobid)
);

create table classinstance (
    crn                 INT NOT NULL UNIQUE,
    courseid            INT NOT NULL,
    professorid         INT NOT NULL,
    section             INT NOT NULL,
    semester            VARCHAR(10) NOT NULL,   /* Either Fall, Winter, Spring, or Summer (I know Winter and Summer are not technically semesters) */
    year                INT NOT NULL,
    location            VARCHAR(250) NOT NULL,
    starttime           VARCHAR(10) NOT NULL,   /* this will be 0800 - 1600 format*/ 
    duration            INT NOT NULL,           /* Duration in minutes */
    weekdays            VARCHAR(10) NOT NULL,
    enrollmentlimit     INT NOT NULL,           /* We don't need current enrollment number since we can just run a COUNT query for that to check for it */
    PRIMARY KEY (crn),
    FOREIGN KEY (courseid) REFERENCES course(courseid),
    FOREIGN KEY (professorid) REFERENCES staff(staffid)
);

create table outcome (
    courseid        INT NOT NULL,
    outcometype         VARCHAR(5) NOT NULL, /* Outcomes can be GM1, GM2, H, V, W, SS, NS, FYS */
    FOREIGN KEY (courseid) REFERENCES course(courseid)
);

create table prerequisite (
    courseid             INT NOT NULL,
    prerequisite        INT NOT NULL,
    FOREIGN KEY (courseid) REFERENCES course(courseid),
    FOREIGN KEY (prerequisite) REFERENCES course(courseid)
);

/*Links student to their respective class instance*/
create table studenttoclassinstance (
    lnumber             INT NOT NULL,
    crn                 INT NOT NULL,
    status              VARCHAR(12) NOT NULL, /*Number representing if withdrawn, in-progress, or if taken already*/
    grade               VARCHAR(3), /*Can be null if still in progress or withdrawn*/
    FOREIGN KEY (lnumber) REFERENCES student(lnumber),
    FOREIGN KEY (crn) REFERENCES classinstance(crn)
);

create table librarybooks (
    bookid              INT NOT NULL UNIQUE,
    bookname            VARCHAR(50) NOT NULL,
    author              VARCHAR(50) NOT NULL,
    PRIMARY KEY (bookid)
);



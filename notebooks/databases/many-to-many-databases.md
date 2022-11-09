Assignment Specifications: Many-to-Many Databases

Tables for the Assignment
Create the following tables in a database named "roster". Make sure that your database and tables are named exactly as follows including matching case.



    DROP TABLE IF EXISTS Member;
    DROP TABLE IF EXISTS `User`;
    DROP TABLE IF EXISTS Course;

    CREATE TABLE `User` (
        user_id     INTEGER NOT NULL AUTO_INCREMENT,
        name        VARCHAR(128) UNIQUE,
        PRIMARY KEY(user_id)
    ) ENGINE=InnoDB CHARACTER SET=utf8;

    CREATE TABLE Course (
        course_id     INTEGER NOT NULL AUTO_INCREMENT,
        title         VARCHAR(128) UNIQUE,
        PRIMARY KEY(course_id)
    ) ENGINE=InnoDB CHARACTER SET=utf8;

    CREATE TABLE Member (
        user_id       INTEGER,
        course_id     INTEGER,
        role          INTEGER,

        CONSTRAINT FOREIGN KEY (user_id) REFERENCES `User` (user_id)
          ON DELETE CASCADE ON UPDATE CASCADE,
        CONSTRAINT FOREIGN KEY (course_id) REFERENCES Course (course_id)
           ON DELETE CASCADE ON UPDATE CASCADE,

        PRIMARY KEY (user_id, course_id)
    ) ENGINE=InnoDB CHARACTER SET=utf8;


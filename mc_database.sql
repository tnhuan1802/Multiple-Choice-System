CREATE TABLE if not exists account (
    username VARCHAR(15) NOT NULL,
    `password` VARCHAR(15) NOT NULL,
    `role` VARCHAR(13) NOT NULL ,
    userId INT NOT NULL AUTO_INCREMENT,
    PRIMARY KEY (userId)
);
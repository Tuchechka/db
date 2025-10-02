SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

CREATE SCHEMA IF NOT EXISTS `mydb3` DEFAULT CHARACTER SET utf8 ;
USE `mydb3` ;

DROP TABLE IF EXISTS `mydb3`.`Answers`;
CREATE TABLE IF NOT EXISTS `mydb3`.`Answers` (
  `answer_id` INT NOT NULL AUTO_INCREMENT,
  `question_id` INT NOT NULL,
  `text` TEXT NOT NULL,
  `is_correct` TINYINT(1) NOT NULL,
  PRIMARY KEY (`answer_id`),
  UNIQUE INDEX `id_UNIQUE` (`answer_id` ASC) VISIBLE,
  CONSTRAINT `answer_to_question`
    FOREIGN KEY (`question_id`)
    REFERENCES `mydb3`.`Questions` (`question_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;

DROP TABLE IF EXISTS `mydb3`.`Courses`;
CREATE TABLE IF NOT EXISTS `mydb3`.`Courses` (
  `course_id` INT NOT NULL AUTO_INCREMENT,
  `titel_course` VARCHAR(255) NOT NULL,
  `description_course` TEXT NOT NULL,
  `duration_course` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`course_id`),
  UNIQUE INDEX `id_UNIQUE` (`course_id` ASC) VISIBLE,
  FULLTEXT INDEX `titel_course FULLTEXT` (`titel_course`) INVISIBLE,
  FULLTEXT INDEX `description_course FULLTEXT` (`description_course`) VISIBLE,
  INDEX `duration_course B-TREE` (`duration_course` ASC) VISIBLE)
ENGINE = InnoDB;

DROP TABLE IF EXISTS `mydb3`.`Enrollments`;
CREATE TABLE IF NOT EXISTS `mydb3`.`Enrollments` (
  `enrollment_id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `course_id` INT NOT NULL,
  `enrollment_date` DATE NOT NULL,
  PRIMARY KEY (`enrollment_id`),
  UNIQUE INDEX `id_UNIQUE` (`enrollment_id` ASC) VISIBLE,
  INDEX `enrollment_date B-TREE` (`enrollment_date` ASC) VISIBLE,
  CONSTRAINT `enrollments_to_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `mydb3`.`Users` (`user_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `enrollments_to_courses`
    FOREIGN KEY (`course_id`)
    REFERENCES `mydb3`.`Courses` (`course_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;

DROP TABLE IF EXISTS `mydb3`.`Modules`;
CREATE TABLE IF NOT EXISTS `mydb3`.`Modules` (
  `module_id` INT NOT NULL AUTO_INCREMENT,
  `course_id` INT NOT NULL,
  `titel_module` VARCHAR(255) NOT NULL,
  `description_module` TEXT NOT NULL,
  PRIMARY KEY (`module_id`),
  UNIQUE INDEX `id_UNIQUE` (`module_id` ASC) VISIBLE,
  FULLTEXT INDEX `titel_module FULLTEXT` (`titel_module`) INVISIBLE,
  FULLTEXT INDEX `description_module FULLTEXT` (`description_module`) VISIBLE,
  CONSTRAINT `modules_to_courses`
    FOREIGN KEY (`course_id`)
    REFERENCES `mydb3`.`Courses` (`course_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;

DROP TABLE IF EXISTS `mydb3`.`Notifications`;
CREATE TABLE IF NOT EXISTS `mydb3`.`Notifications` (
  `notification_id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `course_id` INT NOT NULL,
  `message` TEXT NOT NULL,
  `sent_date` DATE NOT NULL,
  `is_read` TINYINT(1) NOT NULL,
  PRIMARY KEY (`notification_id`),
  UNIQUE INDEX `id_UNIQUE` (`notification_id` ASC) VISIBLE,
  FULLTEXT INDEX `message FULLTEXT` (`message`) INVISIBLE,
  INDEX `send_date B-TREE` (`sent_date` ASC) INVISIBLE,
  INDEX `is_read B-TREE` (`is_read` ASC) VISIBLE,
  CONSTRAINT `notifications_to_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `mydb3`.`Users` (`user_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `notifications_to_courses`
    FOREIGN KEY (`course_id`)
    REFERENCES `mydb3`.`Courses` (`course_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;

DROP TABLE IF EXISTS `mydb3`.`Progress`;
CREATE TABLE IF NOT EXISTS `mydb3`.`Progress` (
  `progress_id` INT NOT NULL AUTO_INCREMENT,
  `enrollment_id` INT NOT NULL,
  `module_id` INT NOT NULL,
  `completed_date` DATE NOT NULL,
  `is_completed` TINYINT(1) NOT NULL,
  `progress_percentage` DECIMAL(5,2) UNSIGNED NOT NULL,
  PRIMARY KEY (`progress_id`),
  UNIQUE INDEX `id_UNIQUE` (`progress_id` ASC) VISIBLE,
  INDEX `completed_date B-TREE` (`completed_date` ASC) INVISIBLE,
  INDEX `is_completed B-TREE` (`is_completed` ASC) INVISIBLE,
  INDEX `progress_percentage B-TREE` (`progress_percentage` ASC) VISIBLE,
  CONSTRAINT `progress_to_enrollments`
    FOREIGN KEY (`enrollment_id`)
    REFERENCES `mydb3`.`Enrollments` (`enrollment_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `progress_to_modules`
    FOREIGN KEY (`module_id`)
    REFERENCES `mydb3`.`Modules` (`module_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;

DROP TABLE IF EXISTS `mydb3`.`Questions`;
CREATE TABLE IF NOT EXISTS `mydb3`.`Questions` (
  `question_id` INT NOT NULL AUTO_INCREMENT,
  `test_id` INT NOT NULL,
  `text` TEXT NOT NULL,
  `number_points` INT NOT NULL,
  PRIMARY KEY (`question_id`),
  UNIQUE INDEX `id_UNIQUE` (`question_id` ASC) VISIBLE,
  FULLTEXT INDEX `text FULLTEXT` (`text`) INVISIBLE,
  INDEX `number_points B-TREE` (`number_points` ASC) VISIBLE,
  CONSTRAINT `question_to_tests`
    FOREIGN KEY (`test_id`)
    REFERENCES `mydb3`.`Tests` (`test_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;

DROP TABLE IF EXISTS `mydb3`.`Test_Attempts`;
CREATE TABLE IF NOT EXISTS `mydb3`.`Test_Attempts` (
  `attempt_id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `test_id` INT NOT NULL,
  `attempt_date` DATE NOT NULL,
  `score` DECIMAL(5,2) UNSIGNED NOT NULL,
  PRIMARY KEY (`attempt_id`),
  UNIQUE INDEX `id_UNIQUE` (`attempt_id` ASC) VISIBLE,
  INDEX `score B-TREE` (`score` ASC) INVISIBLE,
  INDEX `attempt_date B-TREE` (`attempt_date` ASC) VISIBLE,
  CONSTRAINT `test_attempts_to_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `mydb3`.`Users` (`user_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `test_attempts_to_tests`
    FOREIGN KEY (`test_id`)
    REFERENCES `mydb3`.`Tests` (`test_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;

DROP TABLE IF EXISTS `mydb3`.`Tests`;
CREATE TABLE IF NOT EXISTS `mydb3`.`Tests` (
  `test_id` INT NOT NULL AUTO_INCREMENT,
  `module_id` INT NOT NULL,
  `titel_test` VARCHAR(255) NOT NULL,
  `description_test` TEXT NOT NULL,
  `created_date` DATE NOT NULL,
  PRIMARY KEY (`test_id`),
  UNIQUE INDEX `id_UNIQUE` (`test_id` ASC) VISIBLE,
  FULLTEXT INDEX `titel_test FULLTEXT` (`titel_test`) INVISIBLE,
  FULLTEXT INDEX `description_test FULLTEXT` (`description_test`) VISIBLE,
  INDEX `created_date B-TREE` (`created_date` ASC) VISIBLE,
  CONSTRAINT `tests_to_modules`
    FOREIGN KEY (`module_id`)
    REFERENCES `mydb3`.`Modules` (`module_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;

DROP TABLE IF EXISTS `mydb3`.`Users`;
CREATE TABLE IF NOT EXISTS `mydb3`.`Users` (
  `user_id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `phone_number` VARCHAR(255) NULL,
  `registration_date` DATE NOT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE INDEX `idUsers_UNIQUE` (`user_id` ASC) VISIBLE,
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE,
  UNIQUE INDEX `phone_number_UNIQUE` (`phone_number` ASC) VISIBLE,
  INDEX `registration_date B-TREE` (`registration_date` ASC) INVISIBLE)
ENGINE = InnoDB;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

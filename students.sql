-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 08, 2024 at 03:56 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `studentmgt_system`
--

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `Roll No` varchar(225) NOT NULL,
  `Name` varchar(225) NOT NULL,
  `Class` varchar(225) NOT NULL,
  `Section` varchar(225) NOT NULL,
  `Contact` int(225) NOT NULL,
  `City` varchar(225) NOT NULL,
  `Gender` varchar(225) NOT NULL,
  `DOB` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`Roll No`, `Name`, `Class`, `Section`, `Contact`, `City`, `Gender`, `DOB`) VALUES
('1', 'David', '12', 'Mathematics', 222222222, 'Hayward', 'Male', '2005-01-03'),
('2', 'Anne', '12', 'Arts', 333333333, 'Downyard', 'Female', '2004-02-08'),
('3', 'Sam', '11', 'Tec', 555555555, 'Paris', 'Male', '2000-01-02'),
('4', 'Peter', '12', 'Bio', 666666666, 'Bronx', 'Female', '2001-07-08'),
('5', 'Johny', '11', 'Tec', 888888888, 'Albany', 'Female', '2002-06-02'),
('6', 'Kate', '12', 'Bio', 111111111, 'Hayward', 'Female', '2002-08-08');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`Roll No`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

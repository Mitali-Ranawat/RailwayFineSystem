-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 15, 2019 at 03:22 PM
-- Server version: 10.1.38-MariaDB
-- PHP Version: 7.1.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `railway_fine_system`
--

-- --------------------------------------------------------

--
-- Table structure for table `fine`
--

CREATE TABLE `fine` (
  `fine_id` int(11) NOT NULL,
  `type_of_fine` varchar(50) NOT NULL,
  `amount` double DEFAULT NULL,
  `Punishment` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `fine`
--

INSERT INTO `fine` (`fine_id`, `type_of_fine`, `amount`, `Punishment`) VALUES
(1, 'Travelling without ticket', 250, ''),
(2, 'Travelling Fraudulently', 1000, 'Jail for 6 months'),
(3, 'Alarm chain pulling', 1000, 'Jail for 12 months'),
(4, 'Travelling in coach reserved for handicapped', 500, 'Jail for 3 months'),
(5, 'Travelling on roof top', 500, 'Jail for 3 months'),
(6, 'Trespassing', 1000, 'Jail for 6 months'),
(7, 'Nuisance and littering', 250, 'Jail for 1 month'),
(8, 'Bill pasting', 1000, 'Jail for 6 months'),
(9, 'Touting', 10000, 'Jail for 3 years'),
(10, 'Unauthorised Hawking', 1000, 'Jail for 1 year');

-- --------------------------------------------------------

--
-- Table structure for table `finee`
--

CREATE TABLE `finee` (
  `finee_name` varchar(40) NOT NULL,
  `finee_username` varchar(40) NOT NULL,
  `finee_password` varchar(15) NOT NULL,
  `email` varchar(50) DEFAULT NULL,
  `aadhar_card` varchar(12) NOT NULL,
  `gender` varchar(6) DEFAULT NULL,
  `age` varchar(3) DEFAULT NULL,
  `contact_no` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `finee`
--

INSERT INTO `finee` (`finee_name`, `finee_username`, `finee_password`, `email`, `aadhar_card`, `gender`, `age`, `contact_no`) VALUES
('Mitali', 'mitali', '123123', 'mitalir@gmail.com', '556677889944', 'Female', '19', '9087655432'),
('Ninad', 'nindy', '2345', 'ninad@gmail.com', '123465780921', 'Male', '21', '7588247409'),
('sparsh', 'psparsh', '0987', 'as', '345678901234', 'Male', '19', '9876765544'),
('sayali', 'sayali', '12345', 'adf', '123456789012', 'Female', '19', '987654321'),
('shubham', 'shubhu', 'narayani', 'shubhu@mail.co.in', '829718184149', 'Male', '20', '8282828282');

-- --------------------------------------------------------

--
-- Table structure for table `finer`
--

CREATE TABLE `finer` (
  `finer_name` varchar(40) DEFAULT NULL,
  `finer_username` varchar(30) NOT NULL,
  `finer_password` varchar(15) NOT NULL,
  `aadhar_card` varchar(12) NOT NULL,
  `email` varchar(50) DEFAULT NULL,
  `age` varchar(3) NOT NULL,
  `contact_no` varchar(10) DEFAULT NULL,
  `gender` varchar(6) DEFAULT NULL,
  `post` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `finer`
--

INSERT INTO `finer` (`finer_name`, `finer_username`, `finer_password`, `aadhar_card`, `email`, `age`, `contact_no`, `gender`, `post`) VALUES
('aryan', 'aryan', '9999', '345678765432', 'aryan@gmail.com', '14', '9806573241', 'Male', 'Ticket Collector'),
('narayani', 'gundi', '0000', '2147483647', 'nana', '19', '9876567890', 'F', 'Ticket Collector');

-- --------------------------------------------------------

--
-- Table structure for table `fine_generated`
--

CREATE TABLE `fine_generated` (
  `id` int(11) NOT NULL,
  `finee_username` varchar(15) NOT NULL,
  `finer_username` varchar(15) NOT NULL,
  `type_of_fine` varchar(100) NOT NULL,
  `fine_amt` double DEFAULT NULL,
  `fine_collected_at` varchar(30) DEFAULT NULL,
  `fine_submitted_at` varchar(30) DEFAULT NULL,
  `date` date NOT NULL,
  `date_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `fine_generated`
--

INSERT INTO `fine_generated` (`id`, `finee_username`, `finer_username`, `type_of_fine`, `fine_amt`, `fine_collected_at`, `fine_submitted_at`, `date`, `date_time`) VALUES
(1, 'sayali', 'gundi', 'Travelling without ticket', 279, 'Matunga', NULL, '0000-00-00', '2019-04-15 09:31:37'),
(2, 'sayali', 'gundi', 'Travelling Fraudulently', 1000, 'Vidyavihar', NULL, '0000-00-00', '2019-04-15 09:42:23');

-- --------------------------------------------------------

--
-- Table structure for table `station_coordinates`
--

CREATE TABLE `station_coordinates` (
  `station_id` varchar(20) NOT NULL,
  `station_name` varchar(50) DEFAULT NULL,
  `relative_distance` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `station_coordinates`
--

INSERT INTO `station_coordinates` (`station_id`, `station_name`, `relative_distance`) VALUES
('A', 'Ambernath', 60),
('BL', 'Badlapur', 67),
('BND', 'Bhandup', 26),
('BY', 'Byculla', 4),
('C', 'Kurla', 15),
('CR', 'Currey road', 6.5),
('CSMT', 'Chhatrapati Shivaji Maharaj Terminus', 0),
('D', 'Dadar', 9),
('DI', 'Dombivali', 48),
('DV', 'Diva', 43),
('G', 'Ghatkopar', 21),
('K', 'Kalyan', 54),
('KJ', 'Kanjurmarg', 25),
('KL', 'Kalwa', 36),
('KO', 'Kopar', 47),
('KP', 'Khopoli', 114),
('KR', 'Karjat', 100),
('MM', 'Mumbra', 40),
('MT', 'Matunga', 11),
('MU', 'Mulund', 32),
('N', 'Neral', 86),
('NA', 'Nahur', 28),
('S', 'Sion', 13),
('SD', 'Sandhurst road', 2),
('T', 'Thane', 34),
('UL', 'Ulhasnagar', 57),
('VG', 'Vangani', 78),
('VI', 'Vidyavihar', 18),
('VK', 'Vikroli', 23),
('VT', 'Vithalwadi', 56);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `fine`
--
ALTER TABLE `fine`
  ADD PRIMARY KEY (`fine_id`);

--
-- Indexes for table `finee`
--
ALTER TABLE `finee`
  ADD PRIMARY KEY (`finee_username`);

--
-- Indexes for table `finer`
--
ALTER TABLE `finer`
  ADD PRIMARY KEY (`finer_username`);

--
-- Indexes for table `fine_generated`
--
ALTER TABLE `fine_generated`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_3` (`finee_username`),
  ADD KEY `fk_4` (`finer_username`);

--
-- Indexes for table `station_coordinates`
--
ALTER TABLE `station_coordinates`
  ADD PRIMARY KEY (`station_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `fine_generated`
--
ALTER TABLE `fine_generated`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `fine_generated`
--
ALTER TABLE `fine_generated`
  ADD CONSTRAINT `fk_3` FOREIGN KEY (`finee_username`) REFERENCES `finee` (`finee_username`),
  ADD CONSTRAINT `fk_4` FOREIGN KEY (`finer_username`) REFERENCES `finer` (`finer_username`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

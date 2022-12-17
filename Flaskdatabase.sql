-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Dec 17, 2022 at 09:55 PM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 7.4.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `Flaskdatabase`
--

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `s.no` int(11) NOT NULL,
  `name` text NOT NULL,
  `email` varchar(50) NOT NULL,
  `mob` varchar(10) NOT NULL,
  `msg` text NOT NULL,
  `date` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`s.no`, `name`, `email`, `mob`, `msg`, `date`) VALUES
(1, 'Amit', 'amit@gmail.com', '7065265407', 'Hi', '2022-06-09 00:00:00'),
(2, 'frtegdv', 'amit@gmail.com', 'fdsaf', 'fdsfds', '2022-06-09 00:00:00'),
(3, 'Ashu', 'ashu@gmail.com', '7658769870', 'ddd', '2022-06-09 00:00:00'),
(4, 'Aman', 'Aman@gmail.com', '1234567894', 'fdd', '2022-06-11 00:00:00'),
(5, 'Amandeep', 'Amand@gmail.com', '', 'kjj', '2022-06-11 01:56:13'),
(6, 'Aman', 'amit@gmail.com', 'fdsaf', 'jj', '2022-06-11 02:02:58'),
(9, 'Krishna', 'k@gmail.com', '879878098', 'hihi', '2022-06-12 03:35:50'),
(10, 'Anshi', 'Anshi@gmail.com', '9870808', 'jjjlkj', '2022-06-12 03:40:21'),
(11, 'Tukku', 'Tuk@gamd.co', '9809080', 'io', '2022-06-12 03:41:34'),
(12, 'Preeti', 'P@gmail.com', '878898889', 'kjhkj', '2022-06-12 18:34:02'),
(13, 'AmitM', 'amitM@gmail.com', '889999', 'fd', '2022-06-12 21:56:53'),
(14, 'AmitM', 'amitM@gmail.com', '889999', 'fd', '2022-06-14 01:25:12'),
(15, 'AmitM', 'amitM@gmail.com', '889999', 'fd', '2022-06-14 01:27:54'),
(16, 'AmitM', 'amitM@gmail.com', '889999', 'fd', '2022-06-14 01:38:43'),
(17, 'AmitM', 'amitM@gmail.com', '889999', 'fd', '2022-06-14 01:42:00'),
(18, 'AmitM', 'amitM@gmail.com', '889999', 'fr', '2022-06-14 01:45:46'),
(19, 'AmitM', 'amit@gmail.com', '889999', 'hj', '2022-06-14 02:04:48');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `sno` int(11) NOT NULL,
  `title` text NOT NULL,
  `slug` varchar(25) NOT NULL,
  `content` text NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`sno`, `title`, `slug`, `content`, `date`) VALUES
(1, 'First Post1', 'first-post', 'Hi , This is my first post', '2022-06-25 01:37:45'),
(2, 'Second Post', 'sec-post', 'Hi, this is my second post', '2022-06-16 21:54:06');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`s.no`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `s.no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

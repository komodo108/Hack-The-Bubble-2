-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8889
-- Generation Time: Nov 03, 2018 at 12:34 PM
-- Server version: 5.7.23
-- PHP Version: 7.1.20

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
-- Database: `Hacking`
--

-- --------------------------------------------------------

--
-- Table structure for table `Booking`
--

CREATE TABLE `Booking` (
  `id` int(11) UNSIGNED NOT NULL,
  `client` int(11) UNSIGNED NOT NULL,
  `lounger` int(11) UNSIGNED NOT NULL,
  `start_time` datetime NOT NULL,
  `finish_time` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Booking`
--

INSERT INTO `Booking` (`id`, `client`, `lounger`, `start_time`, `finish_time`) VALUES
(1, 1, 1, '2018-11-03 13:00:00', '2018-11-03 14:00:00'),
(2, 2, 2, '2018-11-03 13:00:00', '2018-11-04 13:00:00'),
(3, 3, 1, '2018-11-03 14:00:00', '2018-11-03 15:00:00'),
(4, 4, 1, '2018-11-03 15:00:00', '2018-11-04 13:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `Client`
--

CREATE TABLE `Client` (
  `id` int(11) UNSIGNED NOT NULL,
  `username` text NOT NULL,
  `password` text NOT NULL,
  `spend` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Client`
--

INSERT INTO `Client` (`id`, `username`, `password`, `spend`) VALUES
(1, 'user1', 'password', 0),
(2, 'user2', 'password', 0),
(3, 'user3', 'password', 0),
(4, 'user4', 'password', 0);

-- --------------------------------------------------------

--
-- Table structure for table `Item`
--

CREATE TABLE `Item` (
  `id` int(11) UNSIGNED NOT NULL,
  `price` double NOT NULL,
  `name` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Item`
--

INSERT INTO `Item` (`id`, `price`, `name`) VALUES
(1, 2.3, 'Pina Colada'),
(2, 10, 'Whiskey (200ml)'),
(3, 4.5, 'Steak'),
(4, 0, 'Water');

-- --------------------------------------------------------

--
-- Table structure for table `Lounger`
--

CREATE TABLE `Lounger` (
  `id` int(11) UNSIGNED NOT NULL,
  `name` text NOT NULL,
  `desc` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Lounger`
--

INSERT INTO `Lounger` (`id`, `name`, `desc`) VALUES
(1, 'Cool', 'This lounger is awesome'),
(2, 'Sunny', 'This lounger is slightly closer to the sun!');

-- --------------------------------------------------------

--
-- Table structure for table `Order`
--

CREATE TABLE `Order` (
  `id` int(11) UNSIGNED NOT NULL,
  `item` int(11) UNSIGNED NOT NULL,
  `quantity` int(11) NOT NULL,
  `booking` int(11) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Order`
--

INSERT INTO `Order` (`id`, `item`, `quantity`, `booking`) VALUES
(1, 4, 1, 1),
(2, 2, 10, 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Booking`
--
ALTER TABLE `Booking`
  ADD PRIMARY KEY (`id`),
  ADD KEY `client` (`client`),
  ADD KEY `lounger` (`lounger`);

--
-- Indexes for table `Client`
--
ALTER TABLE `Client`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Item`
--
ALTER TABLE `Item`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Lounger`
--
ALTER TABLE `Lounger`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Order`
--
ALTER TABLE `Order`
  ADD PRIMARY KEY (`id`),
  ADD KEY `booking` (`booking`),
  ADD KEY `item` (`item`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Booking`
--
ALTER TABLE `Booking`
  MODIFY `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `Client`
--
ALTER TABLE `Client`
  MODIFY `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `Item`
--
ALTER TABLE `Item`
  MODIFY `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `Lounger`
--
ALTER TABLE `Lounger`
  MODIFY `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `Order`
--
ALTER TABLE `Order`
  MODIFY `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Booking`
--
ALTER TABLE `Booking`
  ADD CONSTRAINT `booking_ibfk_1` FOREIGN KEY (`client`) REFERENCES `Client` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `booking_ibfk_2` FOREIGN KEY (`lounger`) REFERENCES `Lounger` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `Order`
--
ALTER TABLE `Order`
  ADD CONSTRAINT `order_ibfk_1` FOREIGN KEY (`booking`) REFERENCES `Booking` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `order_ibfk_2` FOREIGN KEY (`item`) REFERENCES `Item` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

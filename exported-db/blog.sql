-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 15, 2021 at 08:05 PM
-- Server version: 10.4.18-MariaDB
-- PHP Version: 7.3.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `blog`
--

-- --------------------------------------------------------

--
-- Table structure for table `Blog`
--

CREATE TABLE `Blog` (
  `SrNo` int(11) NOT NULL,
  `Title` varchar(500) DEFAULT NULL,
  `Subtitle` text DEFAULT NULL,
  `Slug` varchar(500) DEFAULT NULL,
  `Info` varchar(50) DEFAULT NULL,
  `Intro` text DEFAULT NULL,
  `FeaturedImgLink` varchar(100) DEFAULT NULL,
  `Tag1` varchar(50) DEFAULT NULL,
  `Tag2` varchar(50) DEFAULT NULL,
  `Tag3` varchar(50) DEFAULT NULL,
  `Content1` text DEFAULT NULL,
  `ImgLink1` varchar(100) DEFAULT NULL,
  `Content2` text DEFAULT NULL,
  `ImgLink2` varchar(100) DEFAULT NULL,
  `ExtLink` varchar(100) DEFAULT NULL,
  `Content3` text DEFAULT NULL,
  `ImgLink3` varchar(100) DEFAULT NULL,
  `Content4` text DEFAULT NULL,
  `ImgLink4` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Blog`
--

INSERT INTO `Blog` (`SrNo`, `Title`, `Subtitle`, `Slug`, `Info`, `Intro`, `FeaturedImgLink`, `Tag1`, `Tag2`, `Tag3`, `Content1`, `ImgLink1`, `Content2`, `ImgLink2`, `ExtLink`, `Content3`, `ImgLink3`, `Content4`, `ImgLink4`) VALUES
(1, 'How Auroras Are Formed', 'The northern lights, or aurora borealis, offer an entrancing, dramatic, magical display that fascinates all who see it — but just what causes this dazzling natural phenomenon?', 'how-auroras-are-formed', '29 Jan 2021 15:40', 'At the center of our solar system lies the sun, the yellow star that sustains life on our planet. The sun\'s many magnetic fields distort and twist as our parent star rotates on its axis. When these fields become knotted together, they burst and create so-called sunspots. Usually, these sunspots occur in pairs; the largest can be several times the size of Earth\'s diameter', 'https://drive.google.com/uc?export=view&id=1KAsEkdZiY_27BPQcwZvquCdq6HImczqE', 'Astronomy', 'Aurora', 'Space', 'At the center of the sun, the temperature is 27 million degrees Fahrenheit (15 million degrees Celsius). As the temperature on its surface rises and falls, the sun boils and bubbles. Particles escape from the star from the sunspot regions on the surface, hurtling particles of plasma, known as solar wind, into space. It takes these winds around 40 hours to reach Earth. When they do, they can cause the dramatic displays known as the aurora borealis.', '', 'Auroras occur not only on Earth, but also on other worlds in our solar system (and perhaps exoplanets as well). The gas giants in our solar system (Jupiter, Saturn, Uranus and Neptune) each have thick atmospheres and strong magnetic fields, and each have auroras — although these auroras are a little different from Earth\'s, given they are formed under different conditions.', '', '', 'Venus has an aurora generated by its stretched-out magnetic field (a \"magnetotail\"). Mars, which has too thin an atmosphere for global auroras, experiences local auroras due to magnetic fields in the crust. NASA\'s MAVEN (Mars Atmosphere and Volatile Evolution) spacecraft also found widespread northern hemisphere auroras generated by energetic particles striking the Martian atmosphere.', '', '', '');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Blog`
--
ALTER TABLE `Blog`
  ADD PRIMARY KEY (`SrNo`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

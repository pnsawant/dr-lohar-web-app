-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 09, 2021 at 05:46 PM
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
-- Database: `mydb`
--

-- --------------------------------------------------------

--
-- Table structure for table `awards`
--

CREATE TABLE `awards` (
  `SrNo` int(11) NOT NULL,
  `Title` varchar(500) DEFAULT NULL,
  `Subtitle` varchar(500) DEFAULT NULL,
  `ImageLink` varchar(500) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `awards`
--

INSERT INTO `awards` (`SrNo`, `Title`, `Subtitle`, `ImageLink`) VALUES
(1, 'National Graduate Physics Examination', 'Indian Association of Physics Teachers (IAPT)', 'None'),
(2, 'UGC-Meritorious Fellow', 'University grant commission (UGC)', 'None'),
(3, 'Early Career Research Award', 'Department of Science and Technology-Science and Engineering Research Board (DST-SERB) government of India', 'https://drive.google.com/uc?export=view&id=1AlfoypS-S783e1Rg30dKoqPa7bFByTvG'),
(4, 'Young Achiever award 2019', 'InSe unit of SDPL', 'https://drive.google.com/uc?export=view&id=1UMg7ToChUdGek0Xpc7IYlJPSuOJZ46x5'),
(5, 'Young Scientist award', 'Indian Science Congress (ISC)', 'https://drive.google.com/uc?export=view&id=1kd2Zr9dC9NutWnNAmW5TIUc5-7Sjxzls');

-- --------------------------------------------------------

--
-- Table structure for table `collaborations`
--

CREATE TABLE `collaborations` (
  `SrNo` int(11) NOT NULL,
  `FirstName` varchar(500) DEFAULT NULL,
  `Surname` varchar(500) DEFAULT NULL,
  `Place` varchar(500) DEFAULT NULL,
  `AboutLink` varchar(500) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `collaborations`
--

INSERT INTO `collaborations` (`SrNo`, `FirstName`, `Surname`, `Place`, `AboutLink`) VALUES
(1, 'Prof V.J.', 'Fulari', 'Department of Physics, Shivaji University, Kolhapur', 'https'),
(2, 'Dr. M. C.', 'Rath', 'Bhaba Atomic Research Centre, Mumbai', 'https'),
(3, 'Dr. Ranjeet Patil and  ', 'Prof. Y. R. Ma', 'Nantional Dong Wa University, Taiwan', 'dgdf'),
(4, 'Dr. Vinayak Parale,', 'Prof. H. H. Park  and Prof. V. J. Fulari', 'Yonsai University, South Korea', 'bfhh'),
(5, 'Dr. G. S. Ghodake and ', 'D. Y. Kim', 'Dongguk University, South Korea', 'gdfghdh');

-- --------------------------------------------------------

--
-- Table structure for table `conferences`
--

CREATE TABLE `conferences` (
  `SrNo` int(11) NOT NULL,
  `Name` varchar(500) DEFAULT NULL,
  `Place` varchar(500) DEFAULT NULL,
  `Year` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `conferences`
--

INSERT INTO `conferences` (`SrNo`, `Name`, `Place`, `Year`) VALUES
(1, 'International Conference on Multifunctional Materials (ICMM 2010)', 'Banaras Hindu University, Varanasi', 2010),
(2, 'National seminar on Physics of materials and Materials Based device fabrication (NSPM-MDF-2011)', 'Department of Physics, Shivaji University, Kolhapur', 2011),
(3, '1st international conference on Physics of Materials and Materials based device fabrication, (ICPM-MDF 2012)', 'Department of Physics, Shivaji University, Kolhapur', 2012),
(4, 'International Conference on Energy Efficient technologies for Sustainability ', 'St. Xavier’s Catholic College of Engineering Nagercoil, Tamilnadu', 2013),
(5, '2nd National seminar on Physics of materials and Materials Based device fabrication (NSPM-MDF-2013)', 'Department of Physics, Shivaji University, Kolhapur', 2013),
(6, '2nd international conference on Physics of Materials and Materials based device fabrication, (ICPM-MDF 2012)', 'Department of Physics, Shivaji University, Kolhapur', 2014),
(7, 'Recent trends and Issues in renewable Energy (NCRTIRE-2014)', 'Rajashi Chhatrapati Shahu College, Kolhapur', 2014),
(8, '3nd international conference on Physics of Materials and Materials based device fabrication, (ICPM-MDF 2014)', 'Department of Physics, Shivaji University, Kolhapur', 2014),
(9, 'National Conference on Environmental Radiation and functional Materials (NCERFM 2015)', 'Department of Physics, Osmania University, Hyderabad', 2015),
(10, 'Silver Jubilee Conference on Study of Matter Using Intense Radiation Sources and Under Extreme Conditions  ', 'UGC-DAE Consortium for Scientific research University campus, Khandwa Road, Indore (M. P.)', 2016),
(11, 'National conference on Recent trends in Physical, Chemical and Nanosciences- 2017 (NCRT-PCNano-2017)', 'Department of Physics, Lal Bahadur Shastri College of Arts, Science and Commerce, Satara', 2017),
(12, 'National Conference on Recent Advances in Materials science and spectroscopy (NCRAMSS-2017)', 'Department of Physics, Shri Mata Vaisno Devi University, Katra, J&K, India', 2017),
(13, 'Two-day National Conference on water conservation for agriculture Drought prone area', 'Department of Geography, Lal Bahadur Shastri College of Arts, Science and Commerce, Satara', 2017),
(14, '	\r\nNational symposium on Multidisciplinary aspects of Spectroscopy', 'Department of Physics, Deen Dayal Upadhyaya Gorakhpur University, Gorakhpur', 2017),
(15, 'India International Science Festival 2019', 'Lucknow', 2018),
(16, '106th Indian Science Congress', 'Lovely Professinal University, Phagwara, Jalandhar.', 2019),
(17, 'India International Science Festival 2019 (Young Scientists’ Conference)', 'Biswa Bangla Convention centre Kolkata.', 2019);

-- --------------------------------------------------------

--
-- Table structure for table `conforgsec`
--

CREATE TABLE `conforgsec` (
  `SrNo` int(11) NOT NULL,
  `Name` varchar(500) DEFAULT NULL,
  `Role` varchar(500) DEFAULT NULL,
  `Place` varchar(500) DEFAULT NULL,
  `Year` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `conforgsec`
--

INSERT INTO `conforgsec` (`SrNo`, `Name`, `Role`, `Place`, `Year`) VALUES
(1, 'National conference on Recent trends in Physical, Chemical and Nanosciences- 2017 (NCRT-PCNano-2017)', 'Organizing Secretory', 'Department of Physics, Lal Bahadur Shastri College of Arts, Science and Commerce, Satara', 2017);

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `Name` varchar(500) NOT NULL,
  `Email` varchar(500) NOT NULL,
  `Subject` varchar(500) NOT NULL,
  `Message` varchar(2000) NOT NULL,
  `Info` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`Name`, `Email`, `Subject`, `Message`, `Info`) VALUES
('MyName', 'name@gmail.com', 'My Subject', 'Hello There!', '08 Feb 2021 | 14:45');

-- --------------------------------------------------------

--
-- Table structure for table `groupmembers`
--

CREATE TABLE `groupmembers` (
  `SrNo` int(11) NOT NULL,
  `FirstName` varchar(500) DEFAULT NULL,
  `Surname` varchar(500) DEFAULT NULL,
  `ImageLink` varchar(500) DEFAULT NULL,
  `Role` varchar(500) DEFAULT NULL,
  `Info` varchar(2000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `groupmembers`
--

INSERT INTO `groupmembers` (`SrNo`, `FirstName`, `Surname`, `ImageLink`, `Role`, `Info`) VALUES
(1, 'Mr Onkar', 'Pore', 'https://drive.google.com/uc?export=view&id=1Id-Fh-i60s-QnrnxbRDVWYL_56y_OlYS', 'PhD Student', 'I am working under the guidance of Dr. Gaurav Lohar on the subject of supercapacitors'),
(2, 'Mr Rohit', 'Kamble', 'https://drive.google.com/uc?export=view&id=1I2kJoU4LnuDCB2KTGmFCimtx0N_vTQN8', 'PhD Student', 'I am working under the guidance of Dr Lohar on the subject of perovskite'),
(3, 'Mr Digambar', 'Sawant', 'https://drive.google.com/uc?export=view&id=114okVmXs11sglh02hsL24en1m4lMTwmE', 'Research Student', 'I am working on the issue of supercapacitors under the guidance of Dr Gaurav Lohar'),
(4, 'Mr Abhijit', 'Shelke', 'https://drive.google.com/uc?export=view&id=1g-IiGSOnyg70BsiTT0LZ7OY2Dqg-kxcW', 'PhD Student', 'I am working on the subject of metal organic framework under the guidance of Dr Gaurav lohar'),
(5, 'Mr Vishal', 'Arjugade', 'https://drive.google.com/uc?export=view&id=1WXFTIX7cs3isnVu-jcbyiyv-YCV08irq', 'MPhil Student', 'I am working on the issue of supercapacitors under the guidance of Dr Lohar');

-- --------------------------------------------------------

--
-- Table structure for table `inductionprogram`
--

CREATE TABLE `inductionprogram` (
  `SrNo` int(11) NOT NULL,
  `Name` varchar(500) DEFAULT NULL,
  `Place` varchar(500) DEFAULT NULL,
  `Year` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `inductionprogram`
--

INSERT INTO `inductionprogram` (`SrNo`, `Name`, `Place`, `Year`) VALUES
(1, 'Induction program on various aspects of Teaching-learning such as pedagogical tools, Assessment & evaluation methods, ICT and at familiarizing them with the framework of higher education in India.', 'Indian institute of Science Education and Research, Pune', 2018),
(2, '73rd Refresher Course in Physics', 'UGC- Human Resource development Centre, Punjabi University, Patiyala', 2019);

-- --------------------------------------------------------

--
-- Table structure for table `memberships`
--

CREATE TABLE `memberships` (
  `SrNo` int(11) NOT NULL,
  `Title` varchar(500) DEFAULT NULL,
  `Subtitle` varchar(500) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `memberships`
--

INSERT INTO `memberships` (`SrNo`, `Title`, `Subtitle`) VALUES
(1, 'Laser & Spectroscopy Society of India', 'Life Member'),
(2, 'Indian Science Congress', 'Life Member'),
(3, 'Institute of Scholar (InSc unit of SDPL)', 'Life Member');

-- --------------------------------------------------------

--
-- Table structure for table `patents`
--

CREATE TABLE `patents` (
  `SrNo` int(11) NOT NULL,
  `Title` varchar(500) DEFAULT NULL,
  `Subtitle` varchar(500) DEFAULT NULL,
  `ImageLink` varchar(500) DEFAULT NULL,
  `para1` varchar(1000) DEFAULT NULL,
  `line1` varchar(500) DEFAULT NULL,
  `line2` varchar(500) DEFAULT NULL,
  `line3` varchar(500) DEFAULT NULL,
  `line4` varchar(500) DEFAULT NULL,
  `para2` varchar(1000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `patents`
--

INSERT INTO `patents` (`SrNo`, `Title`, `Subtitle`, `ImageLink`, `para1`, `line1`, `line2`, `line3`, `line4`, `para2`) VALUES
(1, 'PATENT: 1', 'Effect of high energy electron irradiation on gold substitute electrochemically reduced graphene oxide: modified photoluminescence properties', 'https://drive.google.com/uc?export=view&id=11rlPvsf52noenP4EBVF4tFDszN2HyLzc', '', 'AGENCY/COUNTRY: INDIAN', 'CBR NO: 2072', 'CBR Date - 30/01/2017', 'Ordinary application', '');

-- --------------------------------------------------------

--
-- Table structure for table `projects`
--

CREATE TABLE `projects` (
  `SrNo` int(11) NOT NULL,
  `Title` varchar(500) DEFAULT NULL,
  `Subtitle` varchar(500) DEFAULT NULL,
  `ImageLink` varchar(500) DEFAULT NULL,
  `para1` varchar(1000) DEFAULT NULL,
  `line1` varchar(500) DEFAULT NULL,
  `line2` varchar(500) DEFAULT NULL,
  `line3` varchar(500) DEFAULT NULL,
  `line4` varchar(500) DEFAULT NULL,
  `para2` varchar(1000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `projects`
--

INSERT INTO `projects` (`SrNo`, `Title`, `Subtitle`, `ImageLink`, `para1`, `line1`, `line2`, `line3`, `line4`, `para2`) VALUES
(1, 'PROJECT: 1', 'Performance and evaluation of high energy electron irradiation on metal oxide reduced graphene oxide composite for supercapacitor and biosensor applications', 'https://drive.google.com/uc?export=view&id=1Yb1I2S1koaZBGHJwstkHilG_snwV18UR', 'Related to Early Career research award', 'Funding : Department od Science and Technology - Science Engineering Research Board (DST-SERB)', 'Cost in Rs. 21.77 Lakh', 'Approved equipment : 5  ', 'Period of availability : 3 years', ''),
(2, 'PROJECT: 2', 'Performance and evaluation of copper oxide reduced graphene oxide composite for supercapacitor and biosensor applications', 'https://drive.google.com/uc?export=view&id=1FpcvirVIJzOoOaD9HqWMFFT4V2Ik91Bw', 'Grant under Research Initiation Scheme 2017-18', 'Funding : Shivaji University, Kolhapur', 'Total Cost in Rs. 70000/-', 'First Installment : Rs. 55,000/-', 'Total period of project : 2 years', '');

-- --------------------------------------------------------

--
-- Table structure for table `publications`
--

CREATE TABLE `publications` (
  `SrNo` int(11) NOT NULL,
  `Reference` varchar(500) DEFAULT NULL,
  `DOI` varchar(500) DEFAULT NULL,
  `Year` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `publications`
--

INSERT INTO `publications` (`SrNo`, `Reference`, `DOI`, `Year`) VALUES
(1, 'J.V. Thombare, V.T. Kambale, V.K. Bansode, G.M. Lohar, S.H. Han, V.J. Fulari, Chemical Synthesis of Polypyrrole Thin Films using Ferric nitrate as an Oxidant, Journal of Shivaji University (Science & Technology) 41 2014-2015.', 'http://www.unishivaji.ac.in/uploads/journal/JOURNAL-42(2)/PE%2035%20.pdf', 2012),
(2, 'S.K. Shinde, J.V. Thombare, G.M. Lohar, U.M. Chougale, V.J. Fulari. Preparation and characterization of CdSe 0.6 Te 0.4 thin films by electrodeposition method', 'https://inis.iaea.org/search/search.aspx?orig_q=RN:44033887', 2012),
(3, 'G.M. Lohar, J.V. Thombare, S.K. Shinde, S.S. Fulari, V.J. More, Photoelectrochemical cell performance of electrodeposited iron doped zinc selenide thin film, Energy Efficient Technologies for Sustainability (ICEETS), 2013 (2013) 411-413', '10.1109/ICEETS.2013.6533417', 2013),
(4, 'J.V. Thombare, G.M. Lohar, S.K. Shinde, U.M. Chougale, V.J. Fulari, A.B. Kadam, S.S. Dhasade, M.C. Rath, S.H. Han, Studies on electrochemically synthesized polypyrrole (Ppy) thin films for supercapacitor application, Energy Efficient Technologies for Sustainability (ICEETS), 2013 (2013) 1064 – 1067', '10.1109/ICEETS.2013.6533534', 2013),
(5, 'S.K. Shinde, J.V. Thombare, G.M. Lohar, D.J. Barad, V.J. Fulari, S.S. Shinde, Galvanostatically deposited Cd0.7Fe0.3Se electrode for solar cell application, Energy Efficient Technologies for Sustainability (ICEETS), 2013 (2013) 420 – 423', '10.1109/ICEETS.2013.6533419', 2013),
(6, 'V.J. Fulari. G.M. Lohar, J.V. Thombare, S.K. Shinde, S.H. Han, Structural, photoluminescence and photoelectrochemical properties of electrosynthesized ZnSe spheres, Journal of Materials Science: Materials in Electronics 25 (2014) 1597–1604', 'https://doi.org/10.1007/s10854-014-1750-4', 2014),
(7, 'V.J. Fulari, U.M. Chougale, A.S. Powar, S.V. Tikone, S.K. Shinde, G.M. Lohar, J.V. Thombare, Synthesis and Characterization of Copper doped Cadmium Sulphide Thin Films by Electrodeposition Method, Journal of Shivaji University (Science & Technology) 41 (2014)', 'http://www.unishivaji.ac.in/uploads/journal/JOURNAL-42(2)/PG%203.pdf', 2014),
(8, 'V.J. Fulari G.M. Lohar, J.V. Thombare, S.K. Shinde, B.P. Relekar, M.C. Rath, Optical properties of galvanostatically synthesized hydrophilic Fe doped ZnSe thin films, ASIAN JOURNAL OF PHYSICS 23 (2014) 909-913', 'http://demo050307.hostgator.co.in/content2/vol-23-2014/vol-23-no-6', 2014),
(9, 'J.V. Thombare, S.K. Shinde, G.M. Lohar, U.M. Chougale, S.S. Dhasade, H.D. Dhaygude, B.P. Relekar, V.J. Fulari, Optical properties of electrochemically synthesized polypyrrole thin films: the electrolyte effect, Journal of Semiconductors 35 (2014) 063001', 'https://doi.org/10.1088/1674-4926/35/6/063001.', 2014),
(10, 'S.K. Shinde, G.S. Ghodake, D.P. Dubal, G.M. Lohar, D.S. Lee, V.J. Fulari, Structural, optical, and photo-electrochemical properties of marygold-like CdSe0.6Te0.4synthesized by electrochemical route, Ceramics International 40 (2014) 11519-11524', 'https://doi.org/10.1016/j.ceramint.2014.03.063', 2014),
(11, 'G.M. Lohar, S.K. Shinde, M.C. Rath, V.J. Fulari, Structural, optical, photoluminescence, electrochemical, and photoelectrochemical properties of Fe doped ZnSe hexagonal nanorods, Materials Science in Semiconductor Processing 26 (2014) 548-554', 'https://doi.org/10.1016/j.mssp.2014.05.047', 2014),
(12, 'S.K. Shinde, D.P. Dubal, G.S. Ghodake, D.S. Lee, G.M. Lohar, M.C. Rath, V.J. Fulari, Baking impact of Fe composition on CdSe films for solar cell application, Materials Letters 132 (2014) 243-246', 'https://doi.org/10.1016/j.matlet.2014.06.099', 2014),
(13, 'G.M. Lohar, S.K. Shinde, V.J. Fulari, Structural, morphological, optical and photoluminescent properties of spray-deposited ZnSe thin film, Journal of Semiconductors 35 (2014) 113001', 'https://iopscience.iop.org/article/10.1088/1674-4926/35/11/113001/meta', 2014),
(14, 'V.J. Fulari G.M. Lohar, TEMPERATURE DEPENDENT PHOTOLUMINESCENCE OF GALVANOSTATICALLY ELECTROSYNTHESIZED ZNSE THIN FILMS, International Journal of Engineering Research 3 (2015) 171-175', '', 2015),
(15, 'G.M. Lohar, J.V. Thombare, S.K. Shinde, U.M. Chougale, V.J. Fulari, Preparation and Characterization Iron doped Zinc Selenide Thin Film by Electrodeposition, Journal of Shivaji University (Science and Technology) 41 (2015) 1-3', 'https://pdfs.semanticscholar.org/3962/cd28f197d903e030a2852ee2a0ee23c1a7b7.pdf', 2015),
(16, 'G.M. Lohar, Photoelectrochemical Cell Performance of Electron Beam Irradiated Iron Doped Zinc Selenide Thin Films, Journal of Shivaji University (Science & Technology) 41 (2015) 1-3', 'http://ir.inflibnet.ac.in:8080/jspui/bitstream/10603/143542/9/10%20summary%20and%20conclusions.pdf', 2015),
(17, 'G.M. Lohar, J.V. Thombare, S.K. Shinde, B.P. Relekar, H.D. Dhaygude, V.J. Fulari, Hydrophilic semconducting micro-chip like Cu doped ZnS thin films grown at room temperature, material science an Indian journal 12 (2015) 057-062', 'https://pdfs.semanticscholar.org/fa48/cecece1c328d7b50caa42a38d9488a118f93.pdf', 2015),
(18, 'J.V. Thombare, G.M. Lohar, S.K. Shinde, S.S. Dhasade, M.C. Rath, V.J. Fulari, Synthesis, characterization and surface wettability study of polypyrrole films: Effect of applied constant current density, Electronic Materials Letters 11 (2015) 266-270', 'https://doi.org/10.1007/s13391-014-4082-x', 2015),
(19, 'H.D. Dhaygude, B.P. Relekar, S.K. Shinde, G.M. Lohar, U.M. Chougale, V.J. Fulari, Electrochemical Synthesis of Nanorods-Like CdS Electrode for Solar Cell Application, Advanced Science Letters 21 (2015) 2641-2644', 'https://doi.org/10.1166/asl.2015.6399', 2015),
(20, 'S.S. Mali, S.K. Shinde, J.R. Mane, A.A. Mane, S.A. Swami, H.D. Dhaygude, G.M. Lohar, B.P. Relekar, V.J. Fulari, Surfactant-Assisted Morphological Modification of Hierarchical CuO Thin Films for Electrochemical Supercapacitors, Advanced Science Letters 21 (2015) 2594-2597', 'https://doi.org/10.1166/asl.2015.6402', 2015),
(21, 'S.K. Shinde, D.P. Dubal, G.S. Ghodake, H.D. Dhaygude, G.M. Lohar, B.P. Relekar, V.J. Fulari, Temperature Dependence of Cationic and Anionic Precursor on Morphological Improvement of CuO Electrodes and Its Consequent Effect on Electrochemical Supercapacitive Properties, Advanced Science Letters 21 (2015) 2653-2656', 'https://doi.org/10.1166/asl.2015.6400', 2015),
(22, 'S.R. Nikam, K. Shinde, D.P. Dubal, G.S. Ghodake, H.D. Dhaygude, B.P. Relekar, G.M. Lohar, V.J. Fulari, Effect of Mn:(CuO/Cu(OH)2) Electrodes for Supercapacitors Application, Advanced Science Letters 21 (2015) 2590-2593', 'https://doi.org/10.1166/193666115816678998', 2015),
(23, 'H.D. Dhaygude, S.K. Shinde, D.P. Dubal, G.M. Lohar, V.J. Fulari, Electrosynthesis of nanoflower like-ZnS thin films and its characterizations, Journal of Materials Science: Materials in Electronics 26 (2015) 8563-8567', 'https://doi.org/10.1007/s10854-015-3529-7.', 2015),
(24, 'G.M. Lohar, H.D. Dhaygude, R.A. Patil, Y. Ma, V.J. Fulari, Studies of properties of Fe2+ doped ZnSe nano-needles for photoelectrochemical cell application, Journal of Materials Science: Materials in Electronics 26 (2015) 8904-8914', 'https://doi.org/10.1007/s10854-015-3572-4', 2015),
(25, 'G.M. Lohar, S.T. Jadhav, M.V. Takale, R.A. Patil, Yuan-Ron Ma, M.C. Rath, V.J. Fulari, Photoelectrochemical cell studies of Fe2+ doped ZnSe nanorods using the potentiostatic mode of electrodeposition, Journal of colloid and interface science 458 (2015) 136-146', 'https://doi.org/10.1016/j.jcis.2015.07.046', 2015),
(26, 'G.M. Lohar, S.T. Jadhav, H.D. Dhaygude, M.V. Takale, R.A. Patil, Y.R. Ma, M.C. Rath, V.J. Fulari, Studies of properties of Fe3+ doped ZnSe nanoparticles and hollow spheres for photoelectrochemical cell application, Journal of Alloys and Compounds 653 (2015) 22-31', 'https://doi.org/10.1016/j.jallcom.2015.08.208', 2015),
(27, 'H.D. Dhaygude, S.K. Shinde, N.B. Velhal, G.M. Lohar, V.J. Fulari, Synthesis and characterization of ZnO thin film by low cost modified SILAR technique, AIMS Materials Science 3 (2018) 349-356', '10.3934/matersci. 2016.2. 349', 2016),
(28, 'H.D. Dhaygude, S.K. Shinde, M.V. Takale, D.P. Dubal, G.M. Lohar, V.J. Fulari, Electrodeposited nanosphere like CdxZn1−xS electrodes for photoelectrochemical cell, Journal of Materials Science: Materials in Electronics 27 (2016) 5145-5152', 'https://doi.org/10.1007/s10854-016-4406-8', 2016),
(29, 'S.A. Mahadik, F.D. Pedraza, B.P. Relekar, V.G. Parale, G.M. Lohar, S.S. Thorat, Synthesis and characterization of superhydrophobic–superoleophilic surface, Journal of Sol-Gel Science and Technology 78 (2016) 475-481', 'https://doi.org/10.1007/s10971-016-3974-7', 2016),
(30, 'H.D. Dhaygude, S.K. Shinde, M.V. Takale, G.M. Lohar, M.C. Rath, V.J. Fulari, Effect of electron irradiation on structural, morphological and photoluminescence properties of ZnS thin films, Ceramics International 42 (2016) 10159-10164', 'https://doi.org/10.1016/j.ceramint.2016.03.129', 2016),
(31, 'B.P. Relekar, G.M. Lohar, R.K. Kamble, A.B. Bansode, H.D. Dhygude, V.J. Fulari, Potentiostatically Deposited MnO2 Thin Film for Supercapacitor Application, Materials Focus 5 (2016) 258-260', 'https://doi.org/10.1166/mat.2016.1321', 2016),
(32, 'G.M. Lohar, H.D. Dhaygude, B.P. Relekar, M.C. Rath, V.J. Fulari, Effect of 10 MeV energy of electron irradiation on Fe2+ doped ZnSe nanorods and their modified properties, Ionics 22 (2016) 1451-1460', 'https://doi.org/10.1007/s11581-016-1650-0', 2016),
(33, 'B.P. Relekar, G.M. Lohar, R.K. Kamble, A.B. Bansode, H.D. Dhygude, V.J. Fulari, Potentiostatically Deposited MnO2 Thin Film for Supercapacitor Application, Materials Focus 5 (2016) 258-260', 'https://doi.org/10.1166/mat.2016.1321', 2016),
(34, 'G.M. Lohar, H.D. Dhaygude, B.P. Relekar, M.C. Rath, V.J. Fulari, Effect of 10 MeV energy of electron irradiation on Fe2+ doped ZnSe nanorods and their modified properties, Ionics 22 (2016) 1451-1460', 'https://doi.org/10.1007/s11581-016-1650-0', 2016),
(35, 'A.S. Patil, G.M. Lohar, V.J. Fulari, Structural, morphological, optical and photoelectrochemical cell properties of copper oxide using modified SILAR method, Journal of Materials Science: Materials in Electronics 27 (2016) 9550-9557', 'https://doi.org/10.1007/s10854-016-5007-2', 2016),
(36, 'G.M. Lohar, R.K. Kamble, S.T. Punde, S.T. Jadhav, A.S. Patil, H.D. Dhaygude, B.P. Relekar, V.J. Fulari, Electrochemical Synthesis of Ni Doped ZnSe Thin Film for Photoelectrochemical Cell Application, Materials Focus 5 (2016) 481-484\r\n\r\n', 'https://doi.org/10.1166/mat.2016.1349', 2016),
(37, 'B.P. Relekar, G.M. Lohar, P.S. Indapure, S.T. Punde, S.T. Jadhav, H.D. Dhygude, V.J. Fulari, Galvanostatically Deposited MnO2 Thin Film and Their Electrochemical Properties, Materials Focus 5 (2016) 577-579', 'https://doi.org/10.1166/mat.2016.1347', 2016),
(38, 'A.S. Patil, M.D. Patil, G.M. Lohar, S.T. Jadhav, V.J. Fulari, Supercapacitive properties of CuO thin films using modified SILAR method, Ionics 23 (2017) 1259-1266', 'https://doi.org/10.1007/s11581-016-1921-9', 2017),
(39, 'A.V. Fulari, M.V. Ramana Reddy, S.T. Jadhav, G.S. Ghodake, Dae-Young Kim, G.M. Lohar, TiO2/reduced graphene oxide composite based nano-petals for supercapacitor application: effect of substrate, Journal of Materials Science: Materials in Electronics 29 (2018) 10814–10824', 'https://doi.org/10.1007/s10854-018-9146-5', 2018),
(40, 'G.M. Lohar, S.T. Jadhav, B.P. Relekar, R.A. Patil, Y. Ma, V.J. Fulari, Electrochemically synthesized 1D and 3D hybrid Fe3+ doped ZnSe dandelions for photoelectrochemical cell application, Optik 158 (2018) 53-63', 'https://doi.org/10.1016/j.ijleo.2017.12.017', 2018),
(41, 'B.P. Relekar, S.A. Mahadik, S.T. Jadhav, A.S. Patil, R.R. Koli, G.M. Lohar, V.J. Fulari, Effect of Electrodeposition Potential on Surface Free Energy and Supercapacitance of MnO2 Thin Films, Journal of Electronic Materials 47 (2018) 2731-2738', 'https://doi.org/10.1007/s11664-018-6109-9', 2018),
(42, 'B.P. Relekar, A.V. Fulari, G.M. Lohar, V.J. Fulari, Development of Porous Manganese Oxide/Polyaniline Composite Using Electrochemical Route for Electrochemical Supercapacitor, Journal of Electronic Materials 24 (2019) 2449-2455', 'https://doi.org/10.1007/s11664-019-07039-3', 2019),
(43, 'J. Geng, J. Ma, S. Ma, F. Li, L. Zhang, X. Ning, G.M. Lohar, Energy band investigation and role of Fe content in Zn1-xFexSe based nanomaterials for photoelectrochemical cell application, Ceramics International 45 (2019) 14457-14463', 'https://doi.org/10.1016/j.ceramint.2019.04.167', 2019),
(44, 'R.V. Shejwal, G.M. Lohar, A.S. Shelke, O.C. Pore, D.V. Rupnavar, C.P. Mane, INVESTIGATION OF ELECTROCHEMICAL PROPERTIES OF CHEMICALLY SYNTHESIZED NICKEL DOPED ZINC OXIDE NANORODS, INTERNATIONAL JOURNAL FOR RESEARCHES IN BIOSCIENCES AGRICULTURE & TECHNOLOGY 2 (2019) 31-35', '', 2019),
(45, 'R.V. Shejwal, G.M. Lohar, A.S. Shelke, O.C. Pore, D.V. Rupnavar, C.P. Mane, SYNTHESIS AND CHARACTERIZATION OF NANOPOROUS NIO NANOFLAKES SYNTHESIZED USING CHEMICAL BATH DEPOSITION, INTERNATIONAL JOURNAL FOR RESEARCHES IN BIOSCIENCES AGRICULTURE & TECHNOLOGY 2 (2019) 27-30', '', 2019),
(46, 'B.P. Relekar, A.V. Fulari, M.C. Rath, V.J. Fulari, G.M. Lohar, Modification in porous MnO2/PANI composite using high-energy electron irradiation for electrochemical supercapacitor. J Mater Sci: Mater Electron 31, 11741–11747 (2020)', 'https://doi.org/10.1007/s10854-020-03725-9', 2020),
(47, 'Q. Li, Y. Li, A.V. Fulari, G.S. Ghodake· D‑Y Kim, G.M. Lohar, Performance of chemically synthesized Mn3O4/rGO nanocomposite for electrochemical supercapacitor: a cost-effective high-performance electrode, Nanotechnology (2020) ', 'https://doi.org/10.1088/1361-6528/ab9f77', 2020),
(48, 'G.M. Lohar, D. V. Rupnawar, R.V. Shejawal, A.V. Fulari, Preparation of natural dyes from salvia and spathodea for TiO2-based dye-sensitized solar cells (DSSCs) and their electrochemical impedance spectroscopic study under light and dark conditions, Bulletin of Materials Science 43 (2020) 236', 'https://doi.org/10.1007/s12034-020-02180-w', 2020);

-- --------------------------------------------------------

--
-- Table structure for table `workshop`
--

CREATE TABLE `workshop` (
  `SrNo` int(11) NOT NULL,
  `Name` varchar(500) DEFAULT NULL,
  `Place` varchar(500) DEFAULT NULL,
  `Year` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `workshop`
--

INSERT INTO `workshop` (`SrNo`, `Name`, `Place`, `Year`) VALUES
(1, 'Environmental problems and Biodiversity', 'Department of Zoology, Lal Bahadur Shastri College of Arts, Science and Commerce, Satara', 2017),
(2, 'Digital literacy Workshop', 'Shrinivas Patil Foundation Sunbeam Education Trust, Karad', 2017),
(3, 'One day Workshop on Avishkar', 'Sadguru Gadage Maharaj College, Karad', 2017),
(4, 'One day workshop on Choice based credit system (CBCS)', 'Lal Bahadur Shastri College of Arts, Science and Commerce, Satara', 2018),
(5, 'One day workshop on new changed syllabus (CBCS) of B. Sc. Part- 1 Physics', 'Yashwantrao Chavan College of Science, Karad', 2018),
(6, 'One day workshop on Choice based credit system', 'Yashwantrao Chavan Institute of Science, Satara', 2018),
(7, 'One day teacher workshop on new changed syllabus (CBCS) of B. Sc. Part- 1 Physics', 'D. P. Bhosale College, Koregaon', 2018),
(8, 'Trainers Training Programme of Avishkar 2018-2019', 'Kisan Veer Mahavidyalaya, Wai', 2018),
(9, 'Workshop on Beneficial effects of Radiation and Indian Nuclear energy programme', 'Yashwantrao Chavan College of Science, Karad', 2018),
(10, 'One day workshop on new changed syllabus (CBCS) of B. Sc. Part- 2 Physics practical', 'Yashwantrao Chavan College of Science, Karad', 2019),
(11, 'One day teacher workshop on new changed syllabus (CBCS) of B. Sc. Part- 2 Physics', 'Arts Science and commerce College Ramanandnagar (Burli)', 2019);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `awards`
--
ALTER TABLE `awards`
  ADD PRIMARY KEY (`SrNo`);

--
-- Indexes for table `collaborations`
--
ALTER TABLE `collaborations`
  ADD PRIMARY KEY (`SrNo`);

--
-- Indexes for table `conferences`
--
ALTER TABLE `conferences`
  ADD PRIMARY KEY (`SrNo`);

--
-- Indexes for table `conforgsec`
--
ALTER TABLE `conforgsec`
  ADD PRIMARY KEY (`SrNo`);

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`Info`);

--
-- Indexes for table `groupmembers`
--
ALTER TABLE `groupmembers`
  ADD PRIMARY KEY (`SrNo`);

--
-- Indexes for table `inductionprogram`
--
ALTER TABLE `inductionprogram`
  ADD PRIMARY KEY (`SrNo`);

--
-- Indexes for table `memberships`
--
ALTER TABLE `memberships`
  ADD PRIMARY KEY (`SrNo`);

--
-- Indexes for table `patents`
--
ALTER TABLE `patents`
  ADD PRIMARY KEY (`SrNo`);

--
-- Indexes for table `projects`
--
ALTER TABLE `projects`
  ADD PRIMARY KEY (`SrNo`);

--
-- Indexes for table `publications`
--
ALTER TABLE `publications`
  ADD PRIMARY KEY (`SrNo`);

--
-- Indexes for table `workshop`
--
ALTER TABLE `workshop`
  ADD PRIMARY KEY (`SrNo`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 19, 2025 at 07:20 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `makeup_tutorial`
--
CREATE DATABASE IF NOT EXISTS `makeup_tutorial` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE `makeup_tutorial`;

-- --------------------------------------------------------

--
-- Table structure for table `cart`
--

CREATE TABLE `cart` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  `added_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `cart`
--

INSERT INTO `cart` (`id`, `user_id`, `product_id`, `quantity`, `added_at`) VALUES
(14, 3, 3, 2, '2025-11-17 07:05:49'),
(15, 8, 3, 1, '2025-11-19 17:47:11');

-- --------------------------------------------------------

--
-- Table structure for table `history`
--

CREATE TABLE `history` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `action` varchar(200) NOT NULL,
  `tutorial_type` varchar(100) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `history`
--

INSERT INTO `history` (`id`, `user_id`, `action`, `tutorial_type`, `created_at`) VALUES
(1, 4, 'Purchased: Lipstick - Ruby Red (x1)', 'Purchase', '2025-11-13 07:02:08'),
(2, 4, 'Viewed tutorial: Test Tutorial', 'Tutorial', '2025-11-13 07:18:36'),
(3, 3, 'Purchased: Foundation Brush (x1)', 'Purchase', '2025-11-13 09:14:31'),
(4, 3, 'Viewed tutorial: Test Tutorial', 'Tutorial', '2025-11-13 09:17:30'),
(5, 3, 'Viewed tutorial: Test Tutorial', 'Tutorial', '2025-11-14 13:51:12'),
(6, 3, 'Purchased: Lipstick - Ruby Red (x1)', 'Purchase', '2025-11-14 15:00:50'),
(7, 3, 'Purchased: Lipstick - Ruby Red (x1)', 'Purchase', '2025-11-16 21:09:49'),
(8, 3, 'Purchased: Foundation Brush (x1)', 'Purchase', '2025-11-16 21:10:22'),
(9, 3, 'Purchased: Foundation Brush (x1)', 'Purchase', '2025-11-16 21:23:04'),
(10, 3, 'Purchased: Lipstick - Ruby Red (x1)', 'Purchase', '2025-11-16 22:23:52'),
(11, 3, 'Purchased: Lipstick - Ruby Red (x1)', 'Purchase', '2025-11-16 22:33:50'),
(12, 3, 'Viewed tutorial: Test Tutorial', 'Tutorial', '2025-11-18 09:36:56'),
(13, 3, 'Viewed tutorial: Latina Makeup Tutorial', 'Tutorial', '2025-11-18 09:44:15'),
(14, 3, 'Viewed tutorial: No Makeup Look Tutorial', 'Tutorial', '2025-11-18 09:45:20'),
(15, 3, 'Viewed tutorial: No Makeup Look Tutorial', 'Tutorial', '2025-11-18 09:50:24'),
(16, 3, 'Viewed tutorial: No Makeup Look Tutorial', 'Tutorial', '2025-11-18 09:52:20'),
(17, 3, 'Viewed tutorial: No Makeup Look Tutorial', 'Tutorial', '2025-11-18 10:00:20'),
(18, 3, 'Viewed tutorial: No Makeup Look Tutorial', 'Tutorial', '2025-11-18 10:00:50'),
(19, 3, 'Viewed tutorial: No Makeup Look Tutorial', 'Tutorial', '2025-11-18 10:01:36'),
(20, 3, 'Viewed tutorial: No Makeup Look Tutorial', 'Tutorial', '2025-11-18 10:27:55'),
(21, 3, 'Viewed tutorial: No Makeup Look Tutorial', 'Tutorial', '2025-11-18 10:28:00'),
(22, 3, 'Viewed tutorial: No Makeup Look Tutorial', 'Tutorial', '2025-11-18 10:36:26'),
(23, 3, 'Viewed tutorial: No Makeup Look Tutorial', 'Tutorial', '2025-11-18 10:36:32'),
(24, 3, 'Viewed tutorial: No Makeup Look Tutorial', 'Tutorial', '2025-11-18 10:36:38'),
(25, 3, 'Viewed tutorial: Glam Makeup Tutorial', 'Tutorial', '2025-11-18 10:37:06'),
(26, 3, 'Viewed tutorial: No Makeup Look Tutorial', 'Tutorial', '2025-11-18 10:48:51'),
(27, 3, 'Viewed tutorial: No Makeup Look Tutorial', 'Tutorial', '2025-11-18 10:48:55'),
(28, 3, 'Viewed tutorial: No Makeup Look Tutorial', 'Tutorial', '2025-11-18 10:48:56'),
(29, 3, 'Viewed tutorial: No Makeup Look Tutorial', 'Tutorial', '2025-11-18 10:48:56'),
(30, 3, 'Viewed tutorial: No Makeup Look Tutorial', 'Tutorial', '2025-11-18 10:48:56'),
(31, 3, 'Viewed tutorial: No Makeup Look Tutorial', 'Tutorial', '2025-11-18 10:48:57'),
(32, 3, 'Viewed tutorial: No Makeup Look Tutorial', 'Tutorial', '2025-11-18 10:48:57'),
(33, 3, 'Viewed tutorial: No Makeup Look Tutorial', 'Tutorial', '2025-11-18 10:48:57'),
(34, 3, 'Viewed tutorial: No Makeup Look Tutorial', 'Tutorial', '2025-11-18 10:48:57'),
(35, 3, 'Viewed tutorial: Glam Makeup Tutorial', 'Tutorial', '2025-11-18 10:49:02'),
(36, 3, 'Viewed tutorial: No Makeup Look Tutorial', 'Tutorial', '2025-11-18 10:49:10'),
(37, 3, 'Viewed tutorial: Glam Makeup Tutorial', 'Tutorial', '2025-11-18 10:50:06'),
(38, 3, 'Viewed tutorial: Glam Makeup Tutorial', 'Tutorial', '2025-11-18 10:50:14'),
(39, 3, 'Viewed tutorial: No Makeup Look Tutorial', 'Tutorial', '2025-11-18 12:12:58'),
(40, 3, 'Viewed tutorial: Glam Makeup Tutorial', 'Tutorial', '2025-11-18 12:13:05'),
(41, 3, 'Viewed tutorial: No Makeup Look Tutorial', 'Tutorial', '2025-11-18 12:16:40'),
(42, 3, 'Viewed tutorial: Latina Makeup Tutorial', 'Tutorial', '2025-11-18 12:16:48'),
(43, 3, 'Viewed tutorial: No Makeup Look Tutorial', 'Tutorial', '2025-11-18 12:17:01'),
(44, 3, 'Viewed tutorial: No Makeup Look Tutorial', 'Tutorial', '2025-11-18 12:22:11'),
(45, 3, 'Viewed tutorial: No Makeup Look Tutorial', 'Tutorial', '2025-11-18 12:22:19'),
(46, 3, 'Viewed tutorial: No Makeup Look Tutorial', 'Tutorial', '2025-11-18 12:22:22'),
(47, 3, 'Viewed tutorial: No Makeup Look Tutorial', 'Tutorial', '2025-11-18 12:27:48'),
(48, 3, 'Viewed tutorial: Latina Makeup Tutorial', 'Tutorial', '2025-11-18 12:28:17'),
(49, 3, 'Viewed tutorial: No Makeup Look Tutorial', 'Tutorial', '2025-11-18 12:51:15'),
(50, 3, 'Viewed tutorial: Latina Makeup Tutorial', 'Tutorial', '2025-11-18 12:51:23'),
(51, 3, 'Viewed tutorial: Douyin Makeup Tutorial', 'Tutorial', '2025-11-18 12:51:30'),
(52, 3, 'Viewed tutorial: Glam Makeup Tutorial', 'Tutorial', '2025-11-18 12:54:02'),
(53, 3, 'Viewed tutorial: No Makeup Look Tutorial', 'Tutorial', '2025-11-18 12:54:07'),
(54, 3, 'Viewed tutorial: No Makeup Look Tutorial', 'Tutorial', '2025-11-18 13:08:00'),
(55, 3, 'Viewed tutorial: No Makeup Look Tutorial', 'Tutorial', '2025-11-18 13:11:34'),
(56, 3, 'Viewed tutorial: Glam Makeup Tutorial', 'Tutorial', '2025-11-18 13:50:13'),
(57, 3, 'Viewed tutorial: Glam Makeup Tutorial', 'Tutorial', '2025-11-18 13:50:13'),
(58, 3, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-18 18:50:11'),
(59, 3, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-18 18:56:41'),
(60, 3, 'Viewed tutorial: Glam Makeup Tutorial - Red Carpet Glam', 'Tutorial', '2025-11-18 18:56:47'),
(61, 3, 'Viewed tutorial: No Makeup Look - Natural Glow', 'Tutorial', '2025-11-18 18:57:15'),
(62, 3, 'Viewed tutorial: No Makeup Look - Natural Glow', 'Tutorial', '2025-11-18 18:57:24'),
(63, 3, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-18 19:08:44'),
(64, 3, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-18 19:14:54'),
(65, 3, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-18 19:26:56'),
(66, 3, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-18 19:27:00'),
(67, 3, 'Viewed tutorial: Glam Makeup Tutorial - Red Carpet Glam', 'Tutorial', '2025-11-18 19:27:22'),
(68, 3, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-18 19:27:28'),
(69, 3, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-18 19:29:45'),
(70, 3, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-18 19:29:48'),
(71, 3, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-18 19:31:14'),
(72, 3, 'Viewed tutorial: Glam Makeup Tutorial - Red Carpet Glam', 'Tutorial', '2025-11-18 19:31:21'),
(73, 3, 'Viewed tutorial: No Makeup Look - Natural Glow', 'Tutorial', '2025-11-18 19:31:26'),
(74, 3, 'Viewed tutorial: Glam Makeup Tutorial - Red Carpet Glam', 'Tutorial', '2025-11-18 19:31:30'),
(75, 3, 'Viewed tutorial: No Makeup Look - Fresh and Dewy', 'Tutorial', '2025-11-18 19:31:37'),
(76, 3, 'Viewed tutorial: Latina Makeup Tutorial - Bold Eyes', 'Tutorial', '2025-11-18 19:31:43'),
(77, 3, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-18 19:31:50'),
(78, 3, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-18 19:31:54'),
(79, 3, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-18 19:44:08'),
(80, 3, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-18 19:47:51'),
(81, 3, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-18 19:48:11'),
(82, 3, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-18 19:49:22'),
(83, 3, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-18 20:12:20'),
(84, 3, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-18 20:12:44'),
(85, 3, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-18 20:12:48'),
(86, 3, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-18 20:12:53'),
(87, 3, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-18 20:13:01'),
(88, 3, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-18 20:16:26'),
(89, 3, 'Viewed tutorial: No Makeup Look - Natural Glow', 'Tutorial', '2025-11-18 20:18:36'),
(90, 3, 'Viewed tutorial: No Makeup Look - Natural Glow', 'Tutorial', '2025-11-18 20:18:41'),
(91, 3, 'Viewed tutorial: Glam Makeup Tutorial - Red Carpet Glam', 'Tutorial', '2025-11-18 20:20:06'),
(92, 3, 'Viewed tutorial: No Makeup Look - Natural Glow', 'Tutorial', '2025-11-18 20:20:18'),
(93, 3, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-18 20:20:55'),
(94, 3, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-18 20:22:57'),
(95, 3, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-18 20:28:17'),
(96, 3, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-18 20:28:26'),
(97, 3, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-18 20:28:30'),
(98, 3, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-18 20:28:35'),
(99, 3, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-18 20:28:39'),
(100, 3, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-18 20:36:23'),
(101, 3, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-18 20:38:27'),
(102, 3, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-18 20:41:12'),
(103, 3, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-18 20:41:19'),
(104, 3, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-18 20:41:22'),
(105, 3, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-18 20:41:27'),
(106, 3, 'Viewed tutorial: Latina Makeup Tutorial - Sultry Lips', 'Tutorial', '2025-11-18 20:42:47'),
(107, 3, 'Viewed tutorial: Latina Makeup Tutorial - Sultry Lips', 'Tutorial', '2025-11-18 20:42:52'),
(108, 3, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-18 20:47:47'),
(109, 3, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-19 05:39:51'),
(110, 3, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-19 05:39:56'),
(111, 3, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-19 05:40:12'),
(112, 3, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-19 05:49:52'),
(113, 3, 'Viewed tutorial: Douyin Makeup Tutorial - Trendy Eyes', 'Tutorial', '2025-11-19 05:50:26'),
(114, 3, 'Viewed tutorial: Douyin Makeup Tutorial - Trendy Eyes', 'Tutorial', '2025-11-19 05:50:34'),
(115, 3, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-19 11:22:16'),
(116, 3, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-19 11:22:47'),
(117, 3, 'Viewed tutorial: Glam Makeup Tutorial - Red Carpet Glam', 'Tutorial', '2025-11-19 11:28:16'),
(118, 3, 'Viewed tutorial: Glam Makeup Tutorial - Red Carpet Glam', 'Tutorial', '2025-11-19 11:28:16'),
(119, 3, 'Viewed tutorial: Glam Makeup Tutorial - Red Carpet Glam', 'Tutorial', '2025-11-19 11:29:09'),
(120, 3, 'Viewed tutorial: No Makeup Look - Natural Glow', 'Tutorial', '2025-11-19 12:05:20'),
(121, 8, 'Viewed tutorial: Latina Makeup Tutorial - Sultry Lips', 'Tutorial', '2025-11-19 16:18:05'),
(122, 8, 'Viewed tutorial: Latina Makeup Tutorial - Sultry Lips', 'Tutorial', '2025-11-19 16:24:08'),
(123, 8, 'Viewed tutorial: Latina Makeup Tutorial - Sultry Lips', 'Tutorial', '2025-11-19 16:24:08'),
(124, 8, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-19 16:24:08'),
(125, 8, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-19 16:24:08'),
(126, 8, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-19 16:24:08'),
(127, 8, 'Viewed tutorial: Latina Makeup Tutorial - Sultry Lips', 'Tutorial', '2025-11-19 16:24:08'),
(128, 8, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-19 16:24:08'),
(129, 8, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-19 16:24:08'),
(130, 8, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-19 16:24:08'),
(131, 8, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-19 16:24:08'),
(132, 8, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-19 16:24:09'),
(133, 8, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-19 16:24:09'),
(134, 8, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-19 16:24:09'),
(135, 8, 'Viewed tutorial: Glam Makeup Tutorial - Red Carpet Glam', 'Tutorial', '2025-11-19 16:24:09'),
(136, 8, 'Viewed tutorial: No Makeup Look - Fresh and Dewy', 'Tutorial', '2025-11-19 16:24:09'),
(137, 8, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-19 16:24:10'),
(138, 8, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-19 16:24:10'),
(139, 8, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-19 16:24:11'),
(140, 8, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-19 16:24:11'),
(141, 8, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-19 16:24:11'),
(142, 8, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-19 16:24:11'),
(143, 8, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-19 16:24:11'),
(144, 8, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-19 16:24:45'),
(145, 8, 'Viewed tutorial: Glam Makeup Tutorial - Red Carpet Glam', 'Tutorial', '2025-11-19 16:25:44'),
(146, 8, 'Viewed tutorial: Latina Makeup Tutorial - Bold Eyes', 'Tutorial', '2025-11-19 16:25:53'),
(147, 8, 'Viewed tutorial: Glam Makeup Tutorial - Red Carpet Glam', 'Tutorial', '2025-11-19 16:26:01'),
(148, 8, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-19 16:27:33'),
(149, 8, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-19 16:31:25'),
(150, 8, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-19 16:55:12'),
(151, 8, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-19 16:55:19'),
(152, 8, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-19 16:55:26'),
(153, 8, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-19 16:56:15'),
(154, 8, 'Viewed tutorial: Glam Makeup Tutorial - Evening Glam', 'Tutorial', '2025-11-19 16:59:56'),
(155, 8, 'Viewed tutorial: Glam Makeup Tutorial - Red Carpet Glam', 'Tutorial', '2025-11-19 17:01:30'),
(156, 8, 'Viewed tutorial: Glam Makeup Tutorial - Red Carpet Glam', 'Tutorial', '2025-11-19 17:01:36'),
(157, 8, 'Viewed tutorial: Glam Makeup Tutorial - Red Carpet Glam', 'Tutorial', '2025-11-19 17:01:40');

-- --------------------------------------------------------

--
-- Table structure for table `otp`
--

CREATE TABLE `otp` (
  `id` int(11) NOT NULL,
  `email` varchar(100) NOT NULL,
  `otp_code` varchar(6) NOT NULL,
  `timestamp` datetime DEFAULT NULL,
  `used` tinyint(1) DEFAULT NULL,
  `expires_at` datetime NOT NULL DEFAULT (current_timestamp() + interval 10 minute)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `otp`
--

INSERT INTO `otp` (`id`, `email`, `otp_code`, `timestamp`, `used`, `expires_at`) VALUES
(1, 'roseanntolentino0608@gmail.com', '442057', '2025-11-19 13:26:26', 0, '2025-11-19 13:36:26'),
(2, 'roseanntolentino0608@gmail.com', '743724', '2025-11-19 13:26:43', 0, '2025-11-19 13:36:43'),
(3, 'roseanntolentino0608@gmail.com', '576052', '2025-11-19 13:27:00', 0, '2025-11-19 13:37:00'),
(4, 'roseanntolentino0608@gmail.com', '124210', '2025-11-19 13:39:31', 0, '2025-11-19 13:49:31');

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `description` text NOT NULL,
  `price` float NOT NULL,
  `category` varchar(100) NOT NULL,
  `image_url` varchar(500) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`id`, `name`, `description`, `price`, `category`, `image_url`, `created_at`) VALUES
(1, 'Foundation Brush', 'Professional foundation brush for flawless application', 299, 'Tools', NULL, '2025-11-13 06:38:58'),
(2, 'Lipstick - Ruby Red', 'Long-lasting matte lipstick in classic red shade', 395, 'Lip Products', NULL, '2025-11-13 06:38:58'),
(3, 'Eyeshadow Palette', '12-color eyeshadow palette with matte and shimmer shades', 857, 'Eye Products', NULL, '2025-11-13 06:38:58'),
(4, 'Mascara', 'Volumizing and lengthening mascara for dramatic lashes', 299, 'Eye Products', NULL, '2025-11-13 06:38:58'),
(5, 'Blush - Peachy Pink', 'Cream blush for natural-looking rosy cheeks', 325, 'Face Products', NULL, '2025-11-13 06:38:58'),
(6, 'Highlighter', 'Champagne highlighter for glowing skin', 499, 'Face Products', NULL, '2025-11-13 06:38:58'),
(7, 'Eyeliner Pencil', 'Precise eyeliner pencil for defined eyes', 299, 'Eye Products', NULL, '2025-11-13 06:38:58'),
(8, 'Setting Powder', 'Translucent setting powder to set makeup all day', 399, 'Face Products', NULL, '2025-11-13 06:38:58'),
(9, 'Bronzer', 'Natural bronzer for sun-kissed glow', 249, 'Face Products', NULL, '2025-11-13 06:38:58'),
(10, 'Lip Gloss', 'Hydrating lip gloss with subtle shimmer', 299, 'Lip Products', NULL, '2025-11-13 06:38:58'),
(11, 'Lipliner', 'Outline the lips', 299, 'Lip Product', '', '2025-11-19 09:00:19');

-- --------------------------------------------------------

--
-- Table structure for table `purchase`
--

CREATE TABLE `purchase` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  `total_price` float NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `rating` int(11) DEFAULT NULL,
  `received` tinyint(1) DEFAULT 0,
  `payment_method` varchar(50) NOT NULL DEFAULT 'Cash on Delivery',
  `payment_status` varchar(50) DEFAULT 'pending',
  `order_id` varchar(50) DEFAULT NULL,
  `shipping_name` varchar(100) DEFAULT NULL,
  `shipping_address` text DEFAULT NULL,
  `shipping_contact` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `purchase`
--

INSERT INTO `purchase` (`id`, `user_id`, `product_id`, `quantity`, `total_price`, `created_at`, `rating`, `received`, `payment_method`, `payment_status`, `order_id`, `shipping_name`, `shipping_address`, `shipping_contact`) VALUES
(1, 4, 2, 1, 650, '2025-11-13 07:02:08', NULL, 0, 'Cash on Delivery', 'pending', NULL, NULL, NULL, NULL),
(2, 3, 1, 1, 1800, '2025-11-13 09:14:31', 1, 1, 'Cash on Delivery', 'pending', NULL, NULL, NULL, NULL),
(3, 3, 2, 1, 650, '2025-11-14 15:00:51', 0, 0, 'Cash on Delivery', 'pending', NULL, NULL, NULL, NULL),
(4, 3, 2, 1, 650, '2025-11-16 21:09:49', NULL, 0, 'Cash on Delivery', 'pending', 'ORD-1763327177', NULL, NULL, NULL),
(5, 3, 1, 1, 1800, '2025-11-16 21:10:22', NULL, 0, 'Cash on Delivery', 'pending', 'ORD-1763327418', NULL, NULL, NULL),
(6, 3, 1, 1, 1800, '2025-11-16 21:23:04', 0, 1, 'Cash on Delivery', 'pending', 'ORD-1763328177', 'shane', 'pagkakaisa st', '09123456789'),
(7, 3, 2, 1, 650, '2025-11-16 22:23:52', NULL, 0, 'Cash on Delivery', 'pending', 'ORD-1763331801', 'shane', '1359 Pagkakaisa ', '09930072700'),
(8, 3, 2, 1, 650, '2025-11-16 22:33:50', 0, 0, 'Cash on Delivery', 'pending', 'ORD-1763332405', 'shane', '1359 Pagkakaisa ', '09930072700');

-- --------------------------------------------------------

--
-- Table structure for table `tutorial`
--

CREATE TABLE `tutorial` (
  `id` int(11) NOT NULL,
  `title` varchar(200) NOT NULL,
  `description` text NOT NULL,
  `category` varchar(100) NOT NULL,
  `difficulty` varchar(50) NOT NULL,
  `duration` int(11) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `steps` text NOT NULL,
  `step_images` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `tutorial`
--

INSERT INTO `tutorial` (`id`, `title`, `description`, `category`, `difficulty`, `duration`, `created_at`, `updated_at`, `user_id`, `steps`, `step_images`) VALUES
(41, 'Glam Makeup Tutorial - Evening Glam', 'A glamorous makeup tutorial for special evening occasions', 'Glam Makeup', '', 0, NULL, NULL, 1, '[\"Moisturizer\", \"Primer\", \"Foundation\", \"Concealer\", \"Brows\", \"Eyeshadow\", \"Glitter Primer\", \"Contour\", \"Highlighter\", \"Lashes\"]', '[\"https://example.com/glam1-step1.jpg\", \"https://example.com/glam1-step2.jpg\", \"https://example.com/glam1-step3.jpg\", \"https://example.com/glam1-step4.jpg\", \"https://example.com/glam1-step5.jpg\", \"https://example.com/glam1-step6.jpg\", \"https://example.com/glam1-step7.jpg\", \"https://example.com/glam1-step8.jpg\", \"https://example.com/glam1-step9.jpg\", \"https://example.com/glam1-step10.jpg\"]'),
(42, 'Glam Makeup Tutorial - Red Carpet Glam', 'A glamorous makeup tutorial for red carpet events', 'Glam Makeup', '', 0, NULL, NULL, 1, '[\"Moisturizer\", \"Primer\", \"Foundation\", \"Concealer\", \"Brows\", \"Eyeshadow\", \"Glitter\", \"Contour\", \"Highlighter\", \"Lashes\", \"Lipstick\"]', '[\"https://example.com/glam2-step1.jpg\", \"https://example.com/glam2-step2.jpg\", \"https://example.com/glam2-step3.jpg\", \"https://example.com/glam2-step4.jpg\", \"https://example.com/glam2-step5.jpg\", \"https://example.com/glam2-step6.jpg\", \"https://example.com/glam2-step7.jpg\", \"https://example.com/glam2-step8.jpg\", \"https://example.com/glam2-step9.jpg\", \"https://example.com/glam2-step10.jpg\", \"https://example.com/glam2-step11.jpg\"]'),
(43, 'No Makeup Look - Natural Glow', 'A simple no makeup look for everyday natural beauty', 'No Makeup Look', '', 0, NULL, NULL, 1, '[\"Moisturizer\", \"Sunscreen or Tinted Sunscreen\"]', '[\"https://example.com/nomakeup1-step1.jpg\", \"https://example.com/nomakeup1-step2.jpg\"]'),
(44, 'No Makeup Look - Fresh and Dewy', 'A fresh and dewy no makeup look for a youthful appearance', 'No Makeup Look', '', 0, NULL, NULL, 1, '[\"Moisturizer\", \"Sunscreen\", \"Blush\"]', '[\"https://example.com/nomakeup2-step1.jpg\", \"https://example.com/nomakeup2-step2.jpg\", \"https://example.com/nomakeup2-step3.jpg\"]'),
(45, 'Latina Makeup Tutorial - Bold Eyes', 'A bold eye makeup tutorial inspired by Latina beauty', 'Latina Makeup', '', 0, NULL, NULL, 1, '[\"Matte Primer\", \"Foundation\", \"Eyeshadow\", \"Eyeliner\", \"Mascara\"]', '[\"https://example.com/latina1-step1.jpg\", \"https://example.com/latina1-step2.jpg\", \"https://example.com/latina1-step3.jpg\", \"https://example.com/latina1-step4.jpg\", \"https://example.com/latina1-step5.jpg\"]'),
(46, 'Latina Makeup Tutorial - Sultry Lips', 'A sultry lip-focused makeup tutorial for Latina flair', 'Latina Makeup', '', 0, NULL, NULL, 1, '[\"Matte Primer\", \"Foundation\", \"Lip Liner\", \"Lipstick\", \"Gloss\"]', '[\"https://example.com/latina2-step1.jpg\", \"https://example.com/latina2-step2.jpg\", \"https://example.com/latina2-step3.jpg\", \"https://example.com/latina2-step4.jpg\", \"https://example.com/latina2-step5.jpg\"]'),
(47, 'Douyin Makeup Tutorial - Trendy Eyes', 'A trendy eye makeup tutorial popular on Douyin', 'Douyin Makeup', '', 0, NULL, NULL, 1, '[\"Sunscreen\", \"Contact Lens\", \"Eyeshadow\", \"Eyeliner\"]', '[\"https://example.com/douyin1-step1.jpg\", \"https://example.com/douyin1-step2.jpg\", \"https://example.com/douyin1-step3.jpg\", \"https://example.com/douyin1-step4.jpg\"]'),
(48, 'Douyin Makeup Tutorial - Cute and Playful', 'A cute and playful makeup tutorial inspired by Douyin trends', 'Douyin Makeup', '', 0, NULL, NULL, 1, '[\"Sunscreen\", \"Contact Lens\", \"Blush\", \"Highlighter\", \"Lip Tint\"]', '[\"https://example.com/douyin2-step1.jpg\", \"https://example.com/douyin2-step2.jpg\", \"https://example.com/douyin2-step3.jpg\", \"https://example.com/douyin2-step4.jpg\", \"https://example.com/douyin2-step5.jpg\"]'),
(49, 'Glam Makeup Tutorial - Evening Glam', 'A glamorous makeup tutorial for special evening occasions', 'Glam Makeup', '', 0, NULL, NULL, 1, '[\"Moisturizer\", \"Primer\", \"Foundation\", \"Concealer\", \"Brows\", \"Eyeshadow\", \"Glitter Primer\", \"Contour\", \"Highlighter\", \"Lashes\", Settings Spray]', '[\"https://example.com/glam1-step1.jpg\", \"https://example.com/glam1-step2.jpg\", \"https://example.com/glam1-step3.jpg\", \"https://example.com/glam1-step4.jpg\", \"https://example.com/glam1-step5.jpg\", \"https://example.com/glam1-step6.jpg\", \"https://example.com/glam1-step7.jpg\", \"https://example.com/glam1-step8.jpg\", \"https://example.com/glam1-step9.jpg\", \"https://example.com/glam1-step10.jpg\"]'),
(50, 'Glam Makeup Tutorial - Red Carpet Glam', 'A glamorous makeup tutorial for red carpet events', 'Glam Makeup', '', 0, NULL, NULL, 1, '[\"Moisturizer\", \"Primer\", \"Foundation\", \"Concealer\", \"Brows\", \"Eyeshadow\", \"Glitter\", \"Contour\", \"Highlighter\", \"Lashes\", \"Lipstick\", \"Settings Spray\"]', '[\"https://example.com/glam2-step1.jpg\", \"https://example.com/glam2-step2.jpg\", \"https://example.com/glam2-step3.jpg\", \"https://example.com/glam2-step4.jpg\", \"https://example.com/glam2-step5.jpg\", \"https://example.com/glam2-step6.jpg\", \"https://example.com/glam2-step7.jpg\", \"https://example.com/glam2-step8.jpg\", \"https://example.com/glam2-step9.jpg\", \"https://example.com/glam2-step10.jpg\", \"https://example.com/glam2-step11.jpg\"]'),
(51, 'No Makeup Look - Natural Glow', 'A simple no makeup look for everyday natural beauty', 'No Makeup Look', '', 0, NULL, NULL, 1, '[\"Moisturizer\", \"Sunscreen or Tinted Sunscreen\", \"Blush\", \"Lipstick\"]', '[\"https://example.com/nomakeup1-step1.jpg\", \"https://example.com/nomakeup1-step2.jpg\"]'),
(52, 'No Makeup Look - Fresh and Dewy', 'A fresh and dewy no makeup look for a youthful appearance', 'No Makeup Look', '', 0, NULL, NULL, 1, '[\"Moisturizer\", \"Sunscreen or Tinted Sunscreen\", \"Blush\", \"Lipstick\"]', '[\"https://example.com/nomakeup2-step1.jpg\", \"https://example.com/nomakeup2-step2.jpg\", \"https://example.com/nomakeup2-step3.jpg\"]'),
(53, 'Latina Makeup Tutorial - Bold Eyes', 'A bold eye makeup tutorial inspired by Latina beauty', 'Latina Makeup', '', 0, NULL, NULL, 1, '[\"Matte Primer\", \"Foundation\",\"Concealer\", \"Eyeshadow\", \"Eyeliner\", \"Mascara\"]', '[\"https://example.com/latina1-step1.jpg\", \"https://example.com/latina1-step2.jpg\", \"https://example.com/latina1-step3.jpg\", \"https://example.com/latina1-step4.jpg\", \"https://example.com/latina1-step5.jpg\"]'),
(54, 'Latina Makeup Tutorial - Sultry Lips', 'A sultry lip-focused makeup tutorial for Latina flair', 'Latina Makeup', '', 0, NULL, NULL, 1, '[\"Matte Primer\", \"Foundation\", \"Lip Liner\", \"Lipstick\", \"Gloss\"]', '[\"https://example.com/latina2-step1.jpg\", \"https://example.com/latina2-step2.jpg\", \"https://example.com/latina2-step3.jpg\", \"https://example.com/latina2-step4.jpg\", \"https://example.com/latina2-step5.jpg\"]'),
(55, 'Douyin Makeup Tutorial - Trendy Eyes', 'A trendy eye makeup tutorial popular on Douyin', 'Douyin Makeup', '', 0, NULL, NULL, 1, '[\"Contact Lens\", \"Eyeshadow\", \"Eyeliner\"]', '[\"https://example.com/douyin1-step1.jpg\", \"https://example.com/douyin1-step2.jpg\", \"https://example.com/douyin1-step3.jpg\"]'),
(56, 'Douyin Makeup Tutorial - Cute and Playful', 'A cute and playful makeup tutorial inspired by Douyin trends', 'Douyin Makeup', '', 0, NULL, NULL, 1, '[\"Sunscreen\", \"Foundation\", \"Blush\", \"Highlighter\", \"Lip Tint\"]', '[\"https://example.com/douyin2-step1.jpg\", \"https://example.com/douyin2-step2.jpg\", \"https://example.com/douyin2-step3.jpg\", \"https://example.com/douyin2-step4.jpg\", \"https://example.com/douyin2-step5.jpg\"]');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password_hash` varchar(200) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `is_admin` tinyint(1) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `name`, `email`, `password_hash`, `created_at`, `is_admin`) VALUES
(1, 'alria', 'alria@gmail.com', 'scrypt:32768:8:1$t9UWhckcN21EA6Pr$677d574bc87254e30c37bcabf6371ed950b980964dc50cab502ab1a1966d8dcbf86bfea34f0e6efa9f6bf4671fc55a3dd2449a194851eaa335a3a60d0454d097', '2025-11-06 07:51:04', 0),
(2, 'calia', 'calia@gmail.com', 'scrypt:32768:8:1$9F8R2EOku63nHUZd$ba327705b9104f0af1f4aa30649cd2a7851a7bedd1a5c0fd039aa83b6adc7b9e422c9b488c988fc1df46d12ac048b41cbdb448f928d96d520b8e9f3acad09180', '2025-11-06 09:53:33', 0),
(3, 'shane', 'shane@gmail.com', 'scrypt:32768:8:1$uPKHZNntE9amPvvy$fab32de253412a185531ba725266fc6cc5c6baf523441fa7a1967e4ff84ba77c25826246d1a7fbfd7a0b68fb0c2b2df3b53e9f36fbb6d26b95e1646a539e8ddd', '2025-11-06 09:58:20', 0),
(4, 'rose', 'roseann@gmail.com', 'scrypt:32768:8:1$aZqn42NbHqqwBhq7$fedbc56aa7b72fc1fa5981cdc76ac76ee164eaef61ca0b7f54880f3162438105d30d98ef8b45991793a7e6f638fdbba278e96ae80f86a90bdf20282cc7487705', '2025-11-13 06:11:02', 0),
(5, 'Admin', 'admin@makeuptutorial.com', 'scrypt:32768:8:1$8YkWVWF23oHWcz4C$588e4c224a3627f2a4861716978ce9753be479d751bb71a9e75859b47ebc8fc691763a2c82b7842dfb269ecced7d0c65958dd978a8b5ebc6cd169aa0f8c0ed79', '2025-11-13 09:59:30', 1),
(6, 'testuser', 'test@example.com', 'scrypt:32768:8:1$sYS3AdssR1GSNIE8$44c657c5cffadd93556b9c0c6e9fd8235f02f7d9b301bdd32b26cc9f5cc4958dc29faaffa6ae045e3759cdf6c77f18c67fcbd09947562b6a0200f94bc1122d0a', '2025-11-14 16:45:39', 1),
(7, 'prince harv', 'princeharv@gmail.com', 'scrypt:32768:8:1$vBdBMjhHS9pJSgzt$a35faffda74907cb26a4a2480589133f6f7c33fad65ae5e6a65de9c2c747bc31c61c4ef198a9cf381af1e1cd3d62e0aeab54fb090abe2594b469433267ac9d00', '2025-11-17 11:57:28', 0),
(8, 'rose', 'roseanntolentino0608@gmail.com', 'scrypt:32768:8:1$IpVWFBmA0yk8XKSs$81d101d4bdcad1694be9c3e2830ae66286061b5569595819155aa9fc0e62e484c1efa67f0eb90d7379e4ce153f31c2382a17ee465c7f8daf4090557d40a04c01', '2025-11-18 04:47:14', 0),
(9, 'testuser2', 'test2@example.com', 'scrypt:32768:8:1$ruwocu5XL5Uel9qO$3c201cb505cd64f52c77077df636368487c6dc6b0be8f78286f2014686512f2fb33c3adf49f1027e733f0bcc61159b20d177933bc920773fb3d9e8cb48dfe7e2', '2025-11-18 06:08:52', 0),
(10, 'finaltest', 'finaltest@example.com', 'scrypt:32768:8:1$u3sWAFEW2XrSuuh8$10d2eb182a4aa48f4d09db5216e14dc85f9a1bdcbd567086defb84d753540970218fab488ad2fd74ee71e3b390ee7d5aac7574cbbd543e11327b5378f75b0e7c', '2025-11-18 06:12:36', 0),
(11, 'finaltestuser', 'finaltestuser@example.com', 'scrypt:32768:8:1$NkgoO9lPPwL08U3k$e2623bf4657b7a91b09dbe29e7eb0f827986da935f7cbdd1178b2d3c80c955c7cefc82455edad9e82df68e796791b0aed84e5ea6060b63247331484691039d2b', '2025-11-18 06:15:09', 0);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password_hash` varchar(255) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `name`, `email`, `password_hash`, `created_at`) VALUES
(1, '', 'rose@gmail.com', 'scrypt:32768:8:1$qlkds8htVNb7tln3$a30f530324ff59b8bb4c1d9c6dc57779ad86482bc145b8aff7ece293856a89ed898f3fad25008ed12c4524008b465d13a2c3d056d72884772a3b69c341404a63', '2025-11-05 01:02:25'),
(2, 'rose', 'ann@gmail.com', 'scrypt:32768:8:1$QVy9WFB6Oe7ULE9Y$e7ef3f842078621371ea3d1d2fa2ab691ab877002f754e87c8c3b8df2444568d8dbcc2cc1f3e02f3bd2da896c6a1bae2741e70423ae063e9a8df6b1be0f7c61e', '2025-11-05 01:33:43'),
(3, 'shane', 'shane@gmail.com', 'scrypt:32768:8:1$ONGVHbGiVD3UUIOj$0bf04baa276509897119cc8fbe0334a91e5eb6acdf03a9f86201aaa8c2acd69596463fd34d9f0e765490d47faed720807002dfc0aebdb22df8e8798e52eb93eb', '2025-11-05 22:08:54'),
(4, 'troy', 'troy@gmail.com', 'scrypt:32768:8:1$BsJTtYHkto1CduE2$cff9d57d2522632210abfda4f82a4ae789564cc25dafd3840de8d72b381b0b5d7a6fff2b121e67e29fb68f69d7252b49838d5d5294f93635b8d48bc86c4e64d3', '2025-11-05 23:30:31');

-- --------------------------------------------------------

--
-- Table structure for table `user_history`
--

CREATE TABLE `user_history` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `action` varchar(200) NOT NULL,
  `tutorial_type` varchar(100) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `cart`
--
ALTER TABLE `cart`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `product_id` (`product_id`);

--
-- Indexes for table `history`
--
ALTER TABLE `history`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `otp`
--
ALTER TABLE `otp`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `purchase`
--
ALTER TABLE `purchase`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `product_id` (`product_id`);

--
-- Indexes for table `tutorial`
--
ALTER TABLE `tutorial`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `user_history`
--
ALTER TABLE `user_history`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `cart`
--
ALTER TABLE `cart`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `history`
--
ALTER TABLE `history`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=158;

--
-- AUTO_INCREMENT for table `otp`
--
ALTER TABLE `otp`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `product`
--
ALTER TABLE `product`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `purchase`
--
ALTER TABLE `purchase`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `tutorial`
--
ALTER TABLE `tutorial`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=57;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `user_history`
--
ALTER TABLE `user_history`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `cart`
--
ALTER TABLE `cart`
  ADD CONSTRAINT `cart_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  ADD CONSTRAINT `cart_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`);

--
-- Constraints for table `history`
--
ALTER TABLE `history`
  ADD CONSTRAINT `history_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

--
-- Constraints for table `purchase`
--
ALTER TABLE `purchase`
  ADD CONSTRAINT `purchase_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  ADD CONSTRAINT `purchase_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`);

--
-- Constraints for table `tutorial`
--
ALTER TABLE `tutorial`
  ADD CONSTRAINT `tutorial_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

--
-- Constraints for table `user_history`
--
ALTER TABLE `user_history`
  ADD CONSTRAINT `user_history_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);
--
-- Database: `phpmyadmin`
--
CREATE DATABASE IF NOT EXISTS `phpmyadmin` DEFAULT CHARACTER SET utf8 COLLATE utf8_bin;
USE `phpmyadmin`;

-- --------------------------------------------------------

--
-- Table structure for table `pma__bookmark`
--

CREATE TABLE `pma__bookmark` (
  `id` int(10) UNSIGNED NOT NULL,
  `dbase` varchar(255) NOT NULL DEFAULT '',
  `user` varchar(255) NOT NULL DEFAULT '',
  `label` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '',
  `query` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='Bookmarks';

-- --------------------------------------------------------

--
-- Table structure for table `pma__central_columns`
--

CREATE TABLE `pma__central_columns` (
  `db_name` varchar(64) NOT NULL,
  `col_name` varchar(64) NOT NULL,
  `col_type` varchar(64) NOT NULL,
  `col_length` text DEFAULT NULL,
  `col_collation` varchar(64) NOT NULL,
  `col_isNull` tinyint(1) NOT NULL,
  `col_extra` varchar(255) DEFAULT '',
  `col_default` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='Central list of columns';

-- --------------------------------------------------------

--
-- Table structure for table `pma__column_info`
--

CREATE TABLE `pma__column_info` (
  `id` int(5) UNSIGNED NOT NULL,
  `db_name` varchar(64) NOT NULL DEFAULT '',
  `table_name` varchar(64) NOT NULL DEFAULT '',
  `column_name` varchar(64) NOT NULL DEFAULT '',
  `comment` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '',
  `mimetype` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '',
  `transformation` varchar(255) NOT NULL DEFAULT '',
  `transformation_options` varchar(255) NOT NULL DEFAULT '',
  `input_transformation` varchar(255) NOT NULL DEFAULT '',
  `input_transformation_options` varchar(255) NOT NULL DEFAULT ''
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='Column information for phpMyAdmin';

-- --------------------------------------------------------

--
-- Table structure for table `pma__designer_settings`
--

CREATE TABLE `pma__designer_settings` (
  `username` varchar(64) NOT NULL,
  `settings_data` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='Settings related to Designer';

-- --------------------------------------------------------

--
-- Table structure for table `pma__export_templates`
--

CREATE TABLE `pma__export_templates` (
  `id` int(5) UNSIGNED NOT NULL,
  `username` varchar(64) NOT NULL,
  `export_type` varchar(10) NOT NULL,
  `template_name` varchar(64) NOT NULL,
  `template_data` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='Saved export templates';

-- --------------------------------------------------------

--
-- Table structure for table `pma__favorite`
--

CREATE TABLE `pma__favorite` (
  `username` varchar(64) NOT NULL,
  `tables` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='Favorite tables';

-- --------------------------------------------------------

--
-- Table structure for table `pma__history`
--

CREATE TABLE `pma__history` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `username` varchar(64) NOT NULL DEFAULT '',
  `db` varchar(64) NOT NULL DEFAULT '',
  `table` varchar(64) NOT NULL DEFAULT '',
  `timevalue` timestamp NOT NULL DEFAULT current_timestamp(),
  `sqlquery` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='SQL history for phpMyAdmin';

-- --------------------------------------------------------

--
-- Table structure for table `pma__navigationhiding`
--

CREATE TABLE `pma__navigationhiding` (
  `username` varchar(64) NOT NULL,
  `item_name` varchar(64) NOT NULL,
  `item_type` varchar(64) NOT NULL,
  `db_name` varchar(64) NOT NULL,
  `table_name` varchar(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='Hidden items of navigation tree';

-- --------------------------------------------------------

--
-- Table structure for table `pma__pdf_pages`
--

CREATE TABLE `pma__pdf_pages` (
  `db_name` varchar(64) NOT NULL DEFAULT '',
  `page_nr` int(10) UNSIGNED NOT NULL,
  `page_descr` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT ''
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='PDF relation pages for phpMyAdmin';

-- --------------------------------------------------------

--
-- Table structure for table `pma__recent`
--

CREATE TABLE `pma__recent` (
  `username` varchar(64) NOT NULL,
  `tables` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='Recently accessed tables';

--
-- Dumping data for table `pma__recent`
--

INSERT INTO `pma__recent` (`username`, `tables`) VALUES
('root', '[{\"db\":\"makeup_tutorial\",\"table\":\"purchase\"},{\"db\":\"makeup_tutorial\",\"table\":\"product\"},{\"db\":\"makeup_tutorial\",\"table\":\"users\"},{\"db\":\"makeup_tutorial\",\"table\":\"tutorial\"},{\"db\":\"makeup_tutorial\",\"table\":\"history\"},{\"db\":\"makeup_tutorial\",\"table\":\"user_history\"},{\"db\":\"makeup_tutorial\",\"table\":\"user\"},{\"db\":\"makeup_tutorial\",\"table\":\"otp\"},{\"db\":\"makeup_tutorial\",\"table\":\"otp_codes\"},{\"db\":\"makeup_tutorial\",\"table\":\"cart\"}]');

-- --------------------------------------------------------

--
-- Table structure for table `pma__relation`
--

CREATE TABLE `pma__relation` (
  `master_db` varchar(64) NOT NULL DEFAULT '',
  `master_table` varchar(64) NOT NULL DEFAULT '',
  `master_field` varchar(64) NOT NULL DEFAULT '',
  `foreign_db` varchar(64) NOT NULL DEFAULT '',
  `foreign_table` varchar(64) NOT NULL DEFAULT '',
  `foreign_field` varchar(64) NOT NULL DEFAULT ''
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='Relation table';

-- --------------------------------------------------------

--
-- Table structure for table `pma__savedsearches`
--

CREATE TABLE `pma__savedsearches` (
  `id` int(5) UNSIGNED NOT NULL,
  `username` varchar(64) NOT NULL DEFAULT '',
  `db_name` varchar(64) NOT NULL DEFAULT '',
  `search_name` varchar(64) NOT NULL DEFAULT '',
  `search_data` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='Saved searches';

-- --------------------------------------------------------

--
-- Table structure for table `pma__table_coords`
--

CREATE TABLE `pma__table_coords` (
  `db_name` varchar(64) NOT NULL DEFAULT '',
  `table_name` varchar(64) NOT NULL DEFAULT '',
  `pdf_page_number` int(11) NOT NULL DEFAULT 0,
  `x` float UNSIGNED NOT NULL DEFAULT 0,
  `y` float UNSIGNED NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='Table coordinates for phpMyAdmin PDF output';

-- --------------------------------------------------------

--
-- Table structure for table `pma__table_info`
--

CREATE TABLE `pma__table_info` (
  `db_name` varchar(64) NOT NULL DEFAULT '',
  `table_name` varchar(64) NOT NULL DEFAULT '',
  `display_field` varchar(64) NOT NULL DEFAULT ''
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='Table information for phpMyAdmin';

-- --------------------------------------------------------

--
-- Table structure for table `pma__table_uiprefs`
--

CREATE TABLE `pma__table_uiprefs` (
  `username` varchar(64) NOT NULL,
  `db_name` varchar(64) NOT NULL,
  `table_name` varchar(64) NOT NULL,
  `prefs` text NOT NULL,
  `last_update` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='Tables'' UI preferences';

-- --------------------------------------------------------

--
-- Table structure for table `pma__tracking`
--

CREATE TABLE `pma__tracking` (
  `db_name` varchar(64) NOT NULL,
  `table_name` varchar(64) NOT NULL,
  `version` int(10) UNSIGNED NOT NULL,
  `date_created` datetime NOT NULL,
  `date_updated` datetime NOT NULL,
  `schema_snapshot` text NOT NULL,
  `schema_sql` text DEFAULT NULL,
  `data_sql` longtext DEFAULT NULL,
  `tracking` set('UPDATE','REPLACE','INSERT','DELETE','TRUNCATE','CREATE DATABASE','ALTER DATABASE','DROP DATABASE','CREATE TABLE','ALTER TABLE','RENAME TABLE','DROP TABLE','CREATE INDEX','DROP INDEX','CREATE VIEW','ALTER VIEW','DROP VIEW') DEFAULT NULL,
  `tracking_active` int(1) UNSIGNED NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='Database changes tracking for phpMyAdmin';

-- --------------------------------------------------------

--
-- Table structure for table `pma__userconfig`
--

CREATE TABLE `pma__userconfig` (
  `username` varchar(64) NOT NULL,
  `timevalue` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `config_data` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='User preferences storage for phpMyAdmin';

--
-- Dumping data for table `pma__userconfig`
--

INSERT INTO `pma__userconfig` (`username`, `timevalue`, `config_data`) VALUES
('root', '2025-11-19 18:02:42', '{\"Console\\/Mode\":\"collapse\"}');

-- --------------------------------------------------------

--
-- Table structure for table `pma__usergroups`
--

CREATE TABLE `pma__usergroups` (
  `usergroup` varchar(64) NOT NULL,
  `tab` varchar(64) NOT NULL,
  `allowed` enum('Y','N') NOT NULL DEFAULT 'N'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='User groups with configured menu items';

-- --------------------------------------------------------

--
-- Table structure for table `pma__users`
--

CREATE TABLE `pma__users` (
  `username` varchar(64) NOT NULL,
  `usergroup` varchar(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='Users and their assignments to user groups';

--
-- Indexes for dumped tables
--

--
-- Indexes for table `pma__bookmark`
--
ALTER TABLE `pma__bookmark`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `pma__central_columns`
--
ALTER TABLE `pma__central_columns`
  ADD PRIMARY KEY (`db_name`,`col_name`);

--
-- Indexes for table `pma__column_info`
--
ALTER TABLE `pma__column_info`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `db_name` (`db_name`,`table_name`,`column_name`);

--
-- Indexes for table `pma__designer_settings`
--
ALTER TABLE `pma__designer_settings`
  ADD PRIMARY KEY (`username`);

--
-- Indexes for table `pma__export_templates`
--
ALTER TABLE `pma__export_templates`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `u_user_type_template` (`username`,`export_type`,`template_name`);

--
-- Indexes for table `pma__favorite`
--
ALTER TABLE `pma__favorite`
  ADD PRIMARY KEY (`username`);

--
-- Indexes for table `pma__history`
--
ALTER TABLE `pma__history`
  ADD PRIMARY KEY (`id`),
  ADD KEY `username` (`username`,`db`,`table`,`timevalue`);

--
-- Indexes for table `pma__navigationhiding`
--
ALTER TABLE `pma__navigationhiding`
  ADD PRIMARY KEY (`username`,`item_name`,`item_type`,`db_name`,`table_name`);

--
-- Indexes for table `pma__pdf_pages`
--
ALTER TABLE `pma__pdf_pages`
  ADD PRIMARY KEY (`page_nr`),
  ADD KEY `db_name` (`db_name`);

--
-- Indexes for table `pma__recent`
--
ALTER TABLE `pma__recent`
  ADD PRIMARY KEY (`username`);

--
-- Indexes for table `pma__relation`
--
ALTER TABLE `pma__relation`
  ADD PRIMARY KEY (`master_db`,`master_table`,`master_field`),
  ADD KEY `foreign_field` (`foreign_db`,`foreign_table`);

--
-- Indexes for table `pma__savedsearches`
--
ALTER TABLE `pma__savedsearches`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `u_savedsearches_username_dbname` (`username`,`db_name`,`search_name`);

--
-- Indexes for table `pma__table_coords`
--
ALTER TABLE `pma__table_coords`
  ADD PRIMARY KEY (`db_name`,`table_name`,`pdf_page_number`);

--
-- Indexes for table `pma__table_info`
--
ALTER TABLE `pma__table_info`
  ADD PRIMARY KEY (`db_name`,`table_name`);

--
-- Indexes for table `pma__table_uiprefs`
--
ALTER TABLE `pma__table_uiprefs`
  ADD PRIMARY KEY (`username`,`db_name`,`table_name`);

--
-- Indexes for table `pma__tracking`
--
ALTER TABLE `pma__tracking`
  ADD PRIMARY KEY (`db_name`,`table_name`,`version`);

--
-- Indexes for table `pma__userconfig`
--
ALTER TABLE `pma__userconfig`
  ADD PRIMARY KEY (`username`);

--
-- Indexes for table `pma__usergroups`
--
ALTER TABLE `pma__usergroups`
  ADD PRIMARY KEY (`usergroup`,`tab`,`allowed`);

--
-- Indexes for table `pma__users`
--
ALTER TABLE `pma__users`
  ADD PRIMARY KEY (`username`,`usergroup`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `pma__bookmark`
--
ALTER TABLE `pma__bookmark`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `pma__column_info`
--
ALTER TABLE `pma__column_info`
  MODIFY `id` int(5) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `pma__export_templates`
--
ALTER TABLE `pma__export_templates`
  MODIFY `id` int(5) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `pma__history`
--
ALTER TABLE `pma__history`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `pma__pdf_pages`
--
ALTER TABLE `pma__pdf_pages`
  MODIFY `page_nr` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `pma__savedsearches`
--
ALTER TABLE `pma__savedsearches`
  MODIFY `id` int(5) UNSIGNED NOT NULL AUTO_INCREMENT;
--
-- Database: `test`
--
CREATE DATABASE IF NOT EXISTS `test` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `test`;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

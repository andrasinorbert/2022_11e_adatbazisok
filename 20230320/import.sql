/*
CREATE TABLE `Csatak` (
  `Csatanév` varchar(50) NOT NULL,
  `Dátum` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_hungarian_ci;
*/

INSERT INTO `Csatak` (`Csatanév`, `Dátum`) VALUES
('Denmark Strait', '5/24-27/41'),
('Guadalcanal', '11/15/42'),
('North Cape', '12/26/43'),
('Suriago Strait', '10/25/44');

/*
CREATE TABLE `Hajok` (
  `Hajónév` varchar(50) NOT NULL,
  `Osztály` varchar(50) NOT NULL,
  `felavatva` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;
*/

INSERT INTO `Hajok` (`Hajónév`, `Osztály`, `felavatva`) VALUES
('California', 'Tennessee', 1921),
('Haruna', 'Kongo', 1915),
('Hiei', 'Kongo', 1914),
('Iowa', 'Iowa', 1943),
('Kirishima', 'Kongo', 1915),
('Kongo', 'Kongo', 1913),
('Missuri', 'Iowa', 1944),
('Musashi', 'Yamato', 1942),
('New Jersey', 'Iowa', 1943),
('North Carolina', 'North Carolina', 1941),
('Ramillies', 'Revenge', 1917),
('Renown', 'Renown', 1916),
('Repulse', 'Renown', 1916),
('Resolution', 'Revenge', 1916),
('Revenge', 'Revenge', 1916),
('Royal Oak', 'Revenge', 1916),
('Royal Sovereign', 'Revenge', 1916),
('Tennesse', 'Tenesse', 1920),
('Washington', 'North Carolina', 1941),
('Wisconsin', 'Iowa', 1944),
('Yamato', 'Yamato', 1941);

/*
CREATE TABLE `Kimenetelek` (
  `Hajónév` varchar(50) NOT NULL,
  `Csatanév` varchar(50) NOT NULL,
  `eredmény` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_hungarian_ci;
*/

INSERT INTO `Kimenetelek` (`Hajónév`, `Csatanév`, `eredmény`) VALUES
('Arizona', 'Denmark Strait', 'elsüllyedt'),
('Bismark', 'Pearl Harbour', 'elsüllyedt'),
('California', 'Surigao Strait', 'ok'),
('Duke of York', 'North Cape', 'ok'),
('Fuso', 'Surigao Strait', 'elsüllyedt'),
('Hood', 'Denmark Strait', 'elsüllyedt'),
('King George V', 'Denmark Strait', 'ok'),
('Kirishima', 'Guadalcanal', 'elsüllyedt'),
('Prince of Wales', 'Denmark Strait', 'sérült'),
('Rodney', 'Denmark Strait', 'ok'),
('Scharnhorst', 'North Cape', 'elsüllyedt'),
('South of Dakota', 'Guadalcanal', 'sérült'),
('Tennessee', 'Surigao Strait', 'ok'),
('Washington', 'Guadalcanal', 'ok'),
('West Wirginia', 'Surigao Strait', 'ok'),
('Yamashiro', 'Surigao Strait', 'elsüllyedt');
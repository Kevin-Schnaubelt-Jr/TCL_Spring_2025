CREATE TABLE Planets (
PlanetID INT AUTO_INCREMENT PRIMARY KEY,
Name VARCHAR(100) UNIQUE,
Biome VARCHAR(100) NOT NULL,
Weather VARCHAR(100) NOT NULL,
Flora VARCHAR(100) NOT NULL,
Fauna VARCHAR(100) NOT NULL,
CONSTRAINT chk_biome CHECK (Biome IN ('Scorched', 'Lush', 'Barren'))
);

INSERT INTO Planets (Name, Biome, Weather, flora, Fauna)
VALUES
('Owdenv Prime', 'Lush', 'Torrid Deluges', 'Ample', 'Sparse'),
('Azel', 'Scorched', 'Scalding Heat', 'Rich', 'Moderate'),
('Iuntar G35', 'Exotic', 'Invisible Mist', 'Between Worlds', 'Unusual'),
('Heydrunton Prime', 'Scorched', 'Scaling Heat', 'Abundant', 'High'),
('Wicas V', 'Barren', 'Planetwide Desiccation', 'Abundant', 'Full');

SELECT * FROM Planets
ORDER BY Name ASC;
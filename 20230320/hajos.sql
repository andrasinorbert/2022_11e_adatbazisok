-- Melyek azok a hajók, amelyeket 
--  1921 előtt avattak fel?

SELECT Hajónév
FROM Hajok
WHERE felavatva<1921;

-- Adjuk meg azokat a hajóosztályokat
-- a gyártó országok nevével együtt,
-- amelyeknek az ágyúi legalább 16-os kaliberűek!

SELECT Osztály, Ország
FROM Hajoosztalyok
WHERE kaliber >=16;

-- Adjuk meg az adatbázisban szereplő
-- összes hadihajó nevét!

SELECT Hajok.Hajónév As "Hajónév" from Hajok union select Kimenetelek.Hajónév As "Hajónév" from Kimenetelek order by Hajónév;

--Adjuk meg a Denmark Strait-csatában 
--elsüllyedt hajók nevét!

SELECT Hajónév
from Kimenetelek
where	Kimenetelek.eredmény= "elsüllyedt" AND
		Kimenetelek.Csatanév = "Denmark Strait";

-- Melyek azok az országok, amelyeknek
-- csatahajóik (bb) is és cirkálóhajóik (bc)
-- is voltak?

select ország
from Hajoosztalyok
where tipus="bb"
and ország IN
    (select ország
    from Hajoosztalyok
    where tipus = "bc");

-- Melyik hajó melyik országban készült?

select Hajónév, Hajoosztalyok.Ország
from Hajoosztalyok NATURAL JOIN Hajok

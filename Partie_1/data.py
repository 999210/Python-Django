data = """
Date;Region;Filère;consumption_twh
2014;Île-de-France;Consommation ;71,01
2015;Île-de-France;Consommation ;73,22
2016;Île-de-France;Consommation ;74
2017;Île-de-France;Consommation ;72,28
2018;Île-de-France;Consommation ;71,68
2019;Île-de-France;Consommation ;70,37
2020;Île-de-France;Consommation ;65,83
2021;Île-de-France;Consommation ;69,19
2022;Île-de-France;Consommation ;66,52
2023;Île-de-France;Consommation ;63,16
2024;Île-de-France;Consommation ;24,28
2014;Centre-Val de Loire;Consommation ;17,74
2015;Centre-Val de Loire;Consommation ;18,14
2016;Centre-Val de Loire;Consommation ;18,43
2017;Centre-Val de Loire;Consommation ;18,4
2018;Centre-Val de Loire;Consommation ;18,12
2019;Centre-Val de Loire;Consommation ;18,21
2020;Centre-Val de Loire;Consommation ;17,53
2021;Centre-Val de Loire;Consommation ;18,2
2022;Centre-Val de Loire;Consommation ;17,5
2023;Centre-Val de Loire;Consommation ;17,28
2024;Centre-Val de Loire;Consommation ;6,74
2014;Bourgogne-Franche-Comté;Consommation ;20,74
2015;Bourgogne-Franche-Comté;Consommation ;20,81
2016;Bourgogne-Franche-Comté;Consommation ;21,81
2017;Bourgogne-Franche-Comté;Consommation ;21,83
2018;Bourgogne-Franche-Comté;Consommation ;21,36
2019;Bourgogne-Franche-Comté;Consommation ;21,21
2020;Bourgogne-Franche-Comté;Consommation ;20,08
2021;Bourgogne-Franche-Comté;Consommation ;21,29
2022;Bourgogne-Franche-Comté;Consommation ;19,88
2023;Bourgogne-Franche-Comté;Consommation ;19,55
2024;Bourgogne-Franche-Comté;Consommation ;7,35
2014;Normandie;Consommation ;27,5
2015;Normandie;Consommation ;27,79
2016;Normandie;Consommation ;28,65
2017;Normandie;Consommation ;28,13
2018;Normandie;Consommation ;27,99
2019;Normandie;Consommation ;27,75
2020;Normandie;Consommation ;26,46
2021;Normandie;Consommation ;27,51
2022;Normandie;Consommation ;26,33
2023;Normandie;Consommation ;25,66
2024;Normandie;Consommation ;9,89
2014;Hauts-de-France;Consommation ;50,11
2015;Hauts-de-France;Consommation ;50,4
2016;Hauts-de-France;Consommation ;50,99
2017;Hauts-de-France;Consommation ;50,95
2018;Hauts-de-France;Consommation ;50,81
2019;Hauts-de-France;Consommation ;49,63
2020;Hauts-de-France;Consommation ;47,25
2021;Hauts-de-France;Consommation ;49,65
2022;Hauts-de-France;Consommation ;47,25
2023;Hauts-de-France;Consommation ;47,11
2024;Hauts-de-France;Consommation ;17,6
2014;Grand Est;Consommation ;45,32
2015;Grand Est;Consommation ;45,81
2016;Grand Est;Consommation ;47,15
2017;Grand Est;Consommation ;47,03
2018;Grand Est;Consommation ;46,09
2019;Grand Est;Consommation ;45,7
2020;Grand Est;Consommation ;42,92
2021;Grand Est;Consommation ;45,49
2022;Grand Est;Consommation ;43,61
2023;Grand Est;Consommation ;41,09
2024;Grand Est;Consommation ;15,1
2014;Pays de la Loire;Consommation ;26,12
2015;Pays de la Loire;Consommation ;26,56
2016;Pays de la Loire;Consommation ;27,43
2017;Pays de la Loire;Consommation ;27,31
2018;Pays de la Loire;Consommation ;27,4
2019;Pays de la Loire;Consommation ;27,15
2020;Pays de la Loire;Consommation ;26,01
2021;Pays de la Loire;Consommation ;27,36
2022;Pays de la Loire;Consommation ;26,35
2023;Pays de la Loire;Consommation ;25
2024;Pays de la Loire;Consommation ;9,59
2014;Bretagne;Consommation ;21,57
2015;Bretagne;Consommation ;21,86
2016;Bretagne;Consommation ;22,43
2017;Bretagne;Consommation ;22,27
2018;Bretagne;Consommation ;22,49
2019;Bretagne;Consommation ;22,57
2020;Bretagne;Consommation ;21,9
2021;Bretagne;Consommation ;22,74
2022;Bretagne;Consommation ;21,27
2023;Bretagne;Consommation ;21,37
2024;Bretagne;Consommation ;8,28
2014;Nouvelle-Aquitaine;Consommation ;41,65
2015;Nouvelle-Aquitaine;Consommation ;43,18
2016;Nouvelle-Aquitaine;Consommation ;44,03
2017;Nouvelle-Aquitaine;Consommation ;44,11
2018;Nouvelle-Aquitaine;Consommation ;43,86
2019;Nouvelle-Aquitaine;Consommation ;43,47
2020;Nouvelle-Aquitaine;Consommation ;41,89
2021;Nouvelle-Aquitaine;Consommation ;43,88
2022;Nouvelle-Aquitaine;Consommation ;41,48
2023;Nouvelle-Aquitaine;Consommation ;40,9
2024;Nouvelle-Aquitaine;Consommation ;15,09
2014;Occitanie;Consommation ;35,75
2015;Occitanie;Consommation ;37,11
2016;Occitanie;Consommation ;37,74
2017;Occitanie;Consommation ;38,47
2018;Occitanie;Consommation ;38,68
2019;Occitanie;Consommation ;38,29
2020;Occitanie;Consommation ;36,79
2021;Occitanie;Consommation ;38,18
2022;Occitanie;Consommation ;37,31
2023;Occitanie;Consommation ;35,76
2024;Occitanie;Consommation ;12,79
2014;Auvergne-Rhône-Alpes;Consommation ;63,56
2015;Auvergne-Rhône-Alpes;Consommation ;66,26
2016;Auvergne-Rhône-Alpes;Consommation ;66,6
2017;Auvergne-Rhône-Alpes;Consommation ;66,75
2018;Auvergne-Rhône-Alpes;Consommation ;66,03
2019;Auvergne-Rhône-Alpes;Consommation ;64,54
2020;Auvergne-Rhône-Alpes;Consommation ;60,84
2021;Auvergne-Rhône-Alpes;Consommation ;64,66
2022;Auvergne-Rhône-Alpes;Consommation ;63,73
2023;Auvergne-Rhône-Alpes;Consommation ;60,77
2024;Auvergne-Rhône-Alpes;Consommation ;22,75
2014;Provence-Alpes-Côte d'Azur;Consommation ;39,53
2015;Provence-Alpes-Côte d'Azur;Consommation ;40,76
2016;Provence-Alpes-Côte d'Azur;Consommation ;40,96
2017;Provence-Alpes-Côte d'Azur;Consommation ;41,25
2018;Provence-Alpes-Côte d'Azur;Consommation ;40,49
2019;Provence-Alpes-Côte d'Azur;Consommation ;40,84
2020;Provence-Alpes-Côte d'Azur;Consommation ;38,83
2021;Provence-Alpes-Côte d'Azur;Consommation ;41,05
2022;Provence-Alpes-Côte d'Azur;Consommation ;39,83
2023;Provence-Alpes-Côte d'Azur;Consommation ;38,74
2024;Provence-Alpes-Côte d'Azur;Consommation ;13,77
2014;Corse;Consommation ;2,09
2015;Corse;Consommation ;2,22
2016;Corse;Consommation ;2,19
2017;Corse;Consommation ;2,27
2018;Corse;Consommation ;2,28
2019;Corse;Consommation ;2,33
2020;Corse;Consommation ;2,22
2021;Corse;Consommation ;2,38
2022;Corse;Consommation ;2,34
2023;Corse;Consommation ;2,26
2024;Corse;Consommation ;0,77
"""

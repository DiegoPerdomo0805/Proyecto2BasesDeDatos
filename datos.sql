-- INSERT PARA titulos
INSERT INTO titulo (id, nombre, tipo) 
VALUES ('CNM123','Star Wars: Clone Wars','S');

INSERT INTO titulo (id, nombre, tipo) 
VALUES ('CNM321','Star Treck','P');

INSERT INTO titulo (id, nombre, tipo) 
VALUES ('CNM234','Spider Man','P');

INSERT INTO titulo (id, nombre, tipo) 
VALUES ('CNM345','RED','P');

INSERT INTO titulo (id, nombre, tipo) 
VALUES ('CNM456','The Mandalorian','S');

INSERT INTO titulo (id, nombre, tipo) 
VALUES ('CNM098','Squid Game','S');

-- INSERT PARA pelicula
INSERT INTO pelicula (id, duracion) 
VALUES ('CNM321',10800);

INSERT INTO pelicula (id, duracion) 
VALUES ('CNM234',7200);

INSERT INTO pelicula (id, duracion) 
VALUES ('CNM345',7330);

-- INSERT PARA series
INSERT INTO series (id, temporadas, episodios)
VALUES ('CNM123',7,6);

INSERT INTO series (id, temporadas, episodios) 
VALUES ('CNM456',2,12);

INSERT INTO series (id, temporadas, episodios) 
VALUES ('CNM098',1,10);

-- INSERT PARA titulo_director
INSERT INTO titulo_director (id, director) 
VALUES ('CNM123','0432');

INSERT INTO titulo_director (id, director) 
VALUES ('CNM321','0543');

INSERT INTO titulo_director (id, director) 
VALUES ('CNM234','0654');

INSERT INTO titulo_director (id, director) 
VALUES ('CNM345','0678');

INSERT INTO titulo_director (id, director) 
VALUES ('CNM456','0178');

INSERT INTO titulo_director  (id, director) 
VALUES ('CNM098','0067');

-- INSERT PARA director
INSERT INTO director (id_director, nombre) 
VALUES ('0432','Dave Filoni');

INSERT INTO director (id, director) 
VALUES ('0543','J. J. Abrams');

INSERT INTO director (id, director) 
VALUES ('0654','Jon Watts');

INSERT INTO director (id, director) 
VALUES ('0678','Domee Shi');

INSERT INTO director (id, director) 
VALUES ('0178','Jon Favreau');

INSERT INTO director  (id, directorO) 
VALUES ('0067','Hwang Dong-hyuk');

-- INSERT PARA titulo_actores
INSERT INTO titulo_actores (id, actor) 
VALUES ('CNM123','098');

INSERT INTO titulo_actores (id, actor) 
VALUES ('CNM123','987');

INSERT INTO titulo_actores (id, actor) 
VALUES ('CNM123','789');

INSERT INTO titulo_actores (id, actor) 
VALUES ('CNM321','890');

INSERT INTO titulo_actores (id, actor) 
VALUES ('CNM321','678');

INSERT INTO titulo_actores (id, actor) 
VALUES ('CNM234','876');

INSERT INTO titulo_actores (id, actor) 
VALUES ('CNM345','674');

INSERT INTO titulo_actores (id, actor) 
VALUES ('CNM456','178');

INSERT INTO titulo_actores (id, actor) 
VALUES ('CNM098','543');

INSERT INTO titulo_actores (id, actor) 
VALUES ('CNM098','432');

INSERT INTO titulo_actores (id, actor) 
VALUES ('CNM098','453');


-- INSERT PARA actor
INSERT INTO actor (id_actor, nombre) 
VALUES ('098','Ashley Eckstein');

INSERT INTO actor (id_actor, nombre) 
VALUES ('987','Dee Bradley');

INSERT INTO actor (id_actor, nombre) 
VALUES ('789','James Earl Jones');

INSERT INTO actor (id_actor, nombre) 
VALUES ('890','William Shatner');

INSERT INTO actor (id_actor, nombre) 
VALUES ('678','Leonard Nimoy');

INSERT INTO actor  (id_actor, nombre) 
VALUES ('876','Cum Holando');

INSERT INTO actor (id_actor, nombre) 
VALUES ('674','Rosalie Chiang');

INSERT INTO actor (id_actor, nombre) 
VALUES ('543','Lee Byung Hun');

INSERT INTO actor (id_actor, nombre) 
VALUES ('178','Pedro Pascal');

INSERT INTO actor (id_actor, nombre) 
VALUES ('432','Gong Yoo');

INSERT INTO actor (id_actor, nombre) 
VALUES ('453','Hoyeon Jung');

-- INSERT PARA titulos_details
INSERT INTO titulos_details (id, genero, release_date) 
VALUES ('CNM123','123','01-03-2015');

INSERT INTO titulos_details (id, genero, release_date) 
VALUES ('CNM321','321','03-01-2012');

INSERT INTO titulos_details (id, genero, release_date) 
VALUES ('CNM234','345','10-03-2011');

INSERT INTO titulos_details (id, genero, release_date) 
VALUES ('CNM345','432','09-09-2005');

INSERT INTO titulos_details (id, genero, release_date) 
VALUES ('CNM456','543','09-03-2009');

INSERT INTO titulos_details (id, genero, release_date) 
VALUES ('CNM098','123','09-05-2020');


-- INSERT PARA genero
INSERT INTO genero (id_genero, nombre) 
VALUES ('123','ACCION');

INSERT INTO genero (id_genero, nombre) 
VALUES ('321','FICCION');

INSERT INTO genero (id_genero, nombre) 
VALUES ('234','AVENTURAS');

INSERT INTO genero (id_genero, nombre) 
VALUES ('432','INFANTIL');

INSERT INTO genero (id_genero, nombre) 
VALUES ('345','HEORES');

INSERT INTO genero  (id_genero, nombre) 
VALUES ('543','ESPACIAL');

-- INSERT PARA premiados
INSERT INTO premiados (id_titulo, id_premio, estado) 
VALUES ('CNM123','PR004','P');

INSERT INTO premiados (id_titulo, id_premio, estado) 
VALUES ('CNM234','PR003','N');

INSERT INTO premiados (id_titulo, id_premio, estado) 
VALUES ('CNM345','PR006','P');

INSERT INTO premiados (id_titulo, id_premio, estado) 
VALUES ('CNM456','PR005','P');

-- INSERT PARA premio
INSERT INTO premio (id, nombre) 
VALUES ('PR001','Mejor Fotografia');

INSERT INTO premio (id, nombre) 
VALUES ('PR002','Mejor guion');

INSERT INTO premio (id, nombre) 
VALUES ('PR003','Mejor dirrecion');

INSERT INTO premio (id, nombre) 
VALUES ('PR004','Mejor ambientacion');

INSERT INTO premio (id, nombre) 
VALUES ('PR005','Mejor banda sonora');

INSERT INTO premio (id, nombre) 
VALUES ('PR006','Mejor animacion');

-- INSERT PARA anunciante
INSERT INTO anunciante (id, nombre) 
VALUES ('AN001','Woka Cola Espuma');

INSERT INTO anunciante (id, nombre) 
VALUES ('AN002','Lepsi');

INSERT INTO anunciante (id, nombre) 
VALUES ('AN003','Francesco Fuammm');

INSERT INTO anunciante (id, nombre) 
VALUES ('AN004','YouTube Naranja');

-- INSERT PARA anuncio
INSERT INTO anuncio (id, nombre, id_anunciante) 
VALUES ('ANES001','Woka Cola Espuma!');

INSERT INTO anuncio (id, nombre, id_anunciante)  
VALUES ('ANES002','No espuma, no maiden');

INSERT INTO anuncio (id, nombre, id_anunciante) 
VALUES ('ANES003','Velocidad Mcqueen');

INSERT INTO anuncio (id, nombre, id_anunciante) 
VALUES ('ANES004','Tas solo?');

-- INSERT PARA anuncio_contenido
INSERT INTO anuncio_contenido (id_anuncio, id_titulo) 
VALUES ('ANES001','CNM123');

INSERT INTO anuncio_contenido (id_anuncio, id_titulo) 
VALUES ('CNM321');

INSERT INTO anuncio_contenido (id_anuncio, id_titulo) 
VALUES ('ANES002','CNM234');

INSERT INTO anuncio_contenido (id_anuncio, id_titulo) 
VALUES ('ANES003','CNM345');

INSERT INTO anuncio_contenido (id_anuncio, id_titulo) 
VALUES ('ANES004','CNM456');

INSERT INTO anuncio_contenido (id_anuncio, id_titulo) 
VALUES ('ANES004','CNM098');

-- YA ESTA DE AQUI HACIA ARRIBA, HACIA ABAJO VAMOS A VER QUE TAL

-- INSERT PARA cuenta
INSERT INTO cuenta (cuenta_id, nivel_cuenta, PASSWORD, CORREO) 
VALUES ('0987654','1','Acetato123','Phineas1@ferb.com');

INSERT INTO cuenta (cuenta_id, nivel_cuenta, PASSWORD, CORREO) 
VALUES ('0123456','1','HelloThere@123','GeneralKenovi@grivius.net');

-- INSERT PARA perfiles
INSERT INTO perfiles (cuenta, perfil, active, perfil_id)
VALUES ('0987654','Ferb','False',"12122323");

INSERT INTO perfiles (cuenta, perfil, active, perfil_id) 
VALUES ('0987654','PERRY!','True','67875546');

INSERT INTO perfiles (cuenta, perfil, active, perfil_id) 
VALUES ('0123456','Satine','False','23455467');

INSERT INTO perfiles (cuenta, perfil, active, perfil_id) 
VALUES ('0123456','Anakin','False','09877865');

INSERT INTO perfiles (cuenta, perfil, active, perfil_id) 
VALUES ('0123456','ObiJuan','True','55785678');

-- INSERT PARA favoritos
INSERT INTO favoritos (perfil, id_titulo) 
VALUES ('PERRY','CNM123');

INSERT INTO favoritos (perfil, id_titulo) 
VALUES ('ObiJuan','GCNM456');

-- INSERT PARA viendo
INSERT INTO viendo (perfil, id_titulo) 
VALUES ('ObiJuan','GCNM456');

-- INSERT PARA WATCH_AGAIN
INSERT INTO favoritos (perfil, id_titulo, times_watched, date_watched) 
VALUES ('PERRY','CNM123', 360000, 03-05-2022);

INSERT INTO favoritos (perfil, id_titulo, times_watched, date_watched) 
VALUES ('ObiJuan','CNM123',3600, 01-06-2020);

-- INSERT PARA recomendados
INSERT INTO recomendados (perfil, id_titulo) 
VALUES ('PERRY','CNM234', 360000, 03-05-2022);

INSERT INTO recomendados (perfil, id_titulo) 
VALUES ('ObiJuan','CNM321',3600, 01-06-2020);

CREATE table TITULOS (
	ID varchar(6) primary key not null,
    NOMBRE varchar(40) not null,
    TIPO varchar(1) not null
);

CREATE table generos (
	id_genero varchar(3) primary key not null,
    NOMBRE varchar(12) not null
);

CREATE table actor (
	id_actor varchar(4) primary key not null,
    NOMBRE varchar(30) not null
);

CREATE table director (
	id_director varchar(4) primary key not null,
    NOMBRE varchar(30) not null
);

CREATE table peliculas (
	id varchar(6) not null,
    duracion int not null,
    foreign key (id) references titulos(id),
    primary key (id)
);

CREATE table series (
	id varchar(6) not null,
	temporadas int not null,
    episodios int not null,
    foreign key (id) references titulos(id),
    primary key (id)
);

create table titulo_actores (
	id varchar(6) not null,
	estelar1 varchar(4) not null,
	estelar2 varchar(4),
	estelar3 varchar(4),
    foreign key (id) references titulos(id),
    foreign key (estelar1) references actor(id_actor),
    foreign key (estelar2) references actor(id_actor),
    foreign key (estelar3) references actor(id_actor),
    primary key (id)
);

create table titulo_details (
	id varchar(6) not null,
	genero1 varchar(4) not null,
	genero2 varchar(4),
	genero3 varchar(4),
    foreign key (id) references titulos(id),
    foreign key (genero1) references generos(id_genero),
    foreign key (genero2) references generos(id_genero),
    foreign key (genero3) references generos(id_genero),
    primary key (id)
);

create table titulo_director (
	id varchar(6) not null,
	director varchar(4) not null,
    foreign key (id) references titulos(id),
    foreign key (director) references director(id_director),
    primary key (id)
);

alter table titulo_actores drop column estelar2;
alter table titulo_actores drop column estelar3;
alter table titulo_actores rename column estelar1 to actor;

alter table titulo_details drop column genero3;
alter table titulo_details drop column genero2;
alter table titulo_details rename column genero1 to genero;

alter table titulo_details add release_date date

CREATE table premios (
	id varchar(3) primary key not null,
    NOMBRE varchar(30) not null
);

create table premiados (
	id_titulo varchar(6) not null,
	id_premio varchar(3) not null,
    foreign key (id_titulo) references titulos(id),
    foreign key (id_premio) references premios(id),
    primary key (id_titulo)
);

CREATE table anunciantes (
	id varchar(5) primary key not null,
    NOMBRE varchar(20) not null
);

create table anuncio (
	id varchar(7) not null,
	nombre varchar(20) not null,
	id_anunciante varchar(5) not null,
    foreign key (id_anunciante) references anunciantes(id),
    primary key (id)
);

create table anuncio_contenido(
	id_anuncio varchar(7) not null,
	id_titulo varchar(6) not null,
	foreign key (id_anuncio) references anuncio(id),
	foreign key (id_titulo) references titulos(id),
    primary key (id_anuncio, id_titulo)
);


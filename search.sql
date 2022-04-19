
--Busquedas de contenido
select t.nombre from titulos t where t.id in( select ta.id from titulo_actores ta 
inner join actor a on ta.actor = a.id_actor where lower(a.nombre) like  lower('%%'))

select t.nombre from titulos t where t.id in(select td.id from titulo_director td 
inner join director d on td.director = d.id_director where lower(d.nombre) like  lower('%%'))

select t.nombre from titulos t where t.id in(select td.id from titulo_details td 
inner join generos g on td.genero = g.id_genero where lower(g.nombre) like  lower('%%'))

select t.nombre from titulos t where lower(t.nombre) like lower('%%')

--busquedas estadísticas de contenido administrativo

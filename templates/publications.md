Title: Publications test
Date: 7/19/2018, 4:29:08 PM
Category: About-me
Tags: info
Slug: publications-test
Lang: {{ lang }}
Authors: Pablo Rodríguez-Sánchez
Summary: Academic publications
Modified: 09/24/2024, 11:58:04

{% if lang == "es" %}

## Publicaciones científicas
He sido autor o coautor en {{ number }} publicaciones científicas:

{% elif lang == "nl" %}

## Wetenschappelijke artikels
Ik ben de auteur of coauteur van {{ number }} wetenschappelijke artikels geweest:

{% else %}

## Scientific articles
I’ve been author or coauthor in {{ number }} scientific articles:

{% endif %}

{{ publications_table }}
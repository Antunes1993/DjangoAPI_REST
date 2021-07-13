from rest_framework.pagination import PageNumberPagination


class PaginacaoCustomizada(PageNumberPagination):

    #minimo
    page_size = 2

    #valor escolhido pelo usuário (entre page_size e max_page_size)
    page_size_query_param = 'tamanho_pagina'

    #maximo
    max_page_size = 5
import api from '../../../../services/api/axios';

const endpoint =
    '/communications/news/';

export const getNews = () =>
    api.get(endpoint);

export const getNewsItem = (id) =>
    api.get(`${endpoint}${id}/`);

export const createNews = (
    data
) =>
    api.post(endpoint, data);

export const updateNews = (
    id,
    data
) =>
    api.put(
        `${endpoint}${id}/`,
        data
    );

export const deleteNews = (
    id
) =>
    api.delete(
        `${endpoint}${id}/`
    );